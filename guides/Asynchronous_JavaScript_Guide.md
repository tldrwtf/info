# Asynchronous JavaScript Guide

Build reliable, non-blocking JavaScript code with callbacks, Promises, and `async`/`await`.

## Quick Reference Card

| Concept | Syntax / Pattern | Why It Matters |
|---------|------------------|----------------|
| **Callback** | `runTask((err, result) => {})` | Legacy async pattern and event APIs |
| **Promise** | `new Promise((resolve, reject) => {})` | Standard async contract with chaining |
| **Async Function** | `async function load() {}` | Always returns a Promise |
| **Await** | `const data = await fetch(url)` | Write async logic in readable steps |
| **Parallel Work** | `await Promise.all([a(), b()])` | Run independent tasks concurrently |
| **Resilient Parallel** | `await Promise.allSettled([...])` | Collect success/failure without short-circuit |
| **Timeout + Cancel** | `AbortController` + `setTimeout` | Prevent hanging requests and stale updates |
| **Async Iteration** | `for await (const chunk of stream)` | Process streamed or chunked data |

---

## Table of Contents
1. [How JavaScript Concurrency Actually Works](#1-how-javascript-concurrency-actually-works)
2. [Callbacks](#2-callbacks)
3. [Promises](#3-promises)
4. [Async / Await](#4-async--await)
5. [Concurrency Patterns You Will Use Daily](#5-concurrency-patterns-you-will-use-daily)
6. [Cancellation, Timeouts, and Retries](#6-cancellation-timeouts-and-retries)
7. [UI Patterns for Async Work](#7-ui-patterns-for-async-work)
8. [Common Pitfalls and Debugging](#8-common-pitfalls-and-debugging)
9. [Practice Drills](#9-practice-drills)
10. [Production Checklist](#10-production-checklist)

---

## 1. How JavaScript Concurrency Actually Works

JavaScript runs your code on a single main thread, but the runtime (browser or Node.js) can handle I/O in the background.

Core pieces:
- **Call Stack**: where synchronous functions execute.
- **Web APIs / Runtime APIs**: timers, network, file and event handling.
- **Task Queue (Macrotasks)**: `setTimeout`, DOM events, I/O callbacks.
- **Microtask Queue**: Promise reactions (`.then`, `await` continuations), `queueMicrotask`.
- **Event Loop**: picks the next task once the call stack is empty, and drains microtasks before the next task.

### Execution order demo

```javascript
console.log("A");

setTimeout(() => console.log("B: timeout"), 0);

Promise.resolve().then(() => console.log("C: microtask"));

console.log("D");

// Output:
// A
// D
// C: microtask
// B: timeout
```

Why: microtasks run before moving to the next macrotask.

---

## 2. Callbacks

A callback is a function passed to be called later.

### Error-first callback pattern

```javascript
function readUser(id, callback) {
  setTimeout(() => {
    if (!id) {
      callback(new Error("Missing id"));
      return;
    }

    callback(null, { id, name: "Ari" });
  }, 300);
}

readUser("42", (err, user) => {
  if (err) {
    console.error(err.message);
    return;
  }

  console.log(user.name);
});
```

### Callback hell example

```javascript
getUser(userId, (err, user) => {
  if (err) return handleError(err);

  getOrders(user.id, (err2, orders) => {
    if (err2) return handleError(err2);

    getRecommendations(orders, (err3, recs) => {
      if (err3) return handleError(err3);
      render(recs);
    });
  });
});
```

Typical fix: wrap callback APIs in Promises and compose with `async`/`await`.

---

## 3. Promises

A Promise has three states:
- **pending**
- **fulfilled** (resolved)
- **rejected**

### Create and consume

```javascript
function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

wait(500)
  .then(() => "done")
  .then((message) => console.log(message))
  .catch((error) => console.error("Unexpected:", error))
  .finally(() => console.log("cleanup"));
```

### Promisify legacy callback code

```javascript
function readUserPromise(id) {
  return new Promise((resolve, reject) => {
    readUser(id, (err, user) => {
      if (err) reject(err);
      else resolve(user);
    });
  });
}
```

### `Promise` helpers

- `Promise.all(iterable)`: fail fast, best when all results are required.
- `Promise.allSettled(iterable)`: never throws due to individual failures.
- `Promise.race(iterable)`: first settled wins (success or failure).
- `Promise.any(iterable)`: first fulfilled wins; throws `AggregateError` if all fail.

---

## 4. Async / Await

`async`/`await` is Promise syntax sugar that improves readability.

### Robust fetch pattern

```javascript
async function fetchJson(url, options = {}) {
  const response = await fetch(url, options);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

async function loadProduct(productId) {
  try {
    const product = await fetchJson(`https://fakestoreapi.com/products/${productId}`);
    console.log(product.title);
  } catch (error) {
    console.error("Could not load product:", error.message);
  }
}
```

### Sequential vs parallel

```javascript
async function loadSequential() {
  const a = await fetchJson("/api/a");
  const b = await fetchJson("/api/b");
  return { a, b };
}

async function loadParallel() {
  const [a, b] = await Promise.all([
    fetchJson("/api/a"),
    fetchJson("/api/b")
  ]);

  return { a, b };
}
```

Use sequential only when `b` depends on `a`.

---

## 5. Concurrency Patterns You Will Use Daily

### Fan-out and aggregate

```javascript
async function fetchUsers(ids) {
  const results = await Promise.allSettled(
    ids.map((id) => fetchJson(`/api/users/${id}`))
  );

  return {
    success: results
      .filter((r) => r.status === "fulfilled")
      .map((r) => r.value),
    failed: results
      .filter((r) => r.status === "rejected")
      .map((r) => r.reason.message)
  };
}
```

### Concurrency limiting (avoid overloading API)

```javascript
async function mapWithLimit(items, limit, worker) {
  const queue = [...items];
  const output = [];

  async function runWorker() {
    while (queue.length) {
      const item = queue.shift();
      output.push(await worker(item));
    }
  }

  await Promise.all(Array.from({ length: limit }, runWorker));
  return output;
}
```

Use this for large batches (emails, imports, media operations).

### Async iteration

```javascript
async function* pages() {
  for (let page = 1; page <= 3; page += 1) {
    const data = await fetchJson(`/api/items?page=${page}`);
    yield data.items;
  }
}

async function consume() {
  for await (const items of pages()) {
    console.log("received page with", items.length, "items");
  }
}
```

---

## 6. Cancellation, Timeouts, and Retries

### Abort stale requests

```javascript
let currentController;

async function searchProducts(query) {
  if (currentController) currentController.abort();

  currentController = new AbortController();

  try {
    const data = await fetchJson(`/api/search?q=${encodeURIComponent(query)}`, {
      signal: currentController.signal
    });

    renderResults(data);
  } catch (error) {
    if (error.name === "AbortError") return; // expected during rapid typing
    showError(error.message);
  }
}
```

### Timeout wrapper

```javascript
async function fetchWithTimeout(url, ms = 5000) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), ms);

  try {
    return await fetchJson(url, { signal: controller.signal });
  } finally {
    clearTimeout(timeoutId);
  }
}
```

### Retry with exponential backoff

```javascript
async function retry(fn, { retries = 3, baseDelay = 300 } = {}) {
  let attempt = 0;

  while (true) {
    try {
      return await fn();
    } catch (error) {
      attempt += 1;
      if (attempt > retries) throw error;

      const delay = baseDelay * 2 ** (attempt - 1);
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}
```

Retry transient failures (timeouts, 502/503/504), not validation errors.

---

## 7. UI Patterns for Async Work

### Loading, success, error, empty states

```javascript
async function loadTodos() {
  setViewState("loading");

  try {
    const todos = await fetchJson("/api/todos");

    if (todos.length === 0) {
      setViewState("empty");
      return;
    }

    renderTodos(todos);
    setViewState("ready");
  } catch (error) {
    setErrorMessage(error.message);
    setViewState("error");
  }
}
```

### Prevent duplicate submissions

```javascript
let isSaving = false;

async function onSubmit(formData) {
  if (isSaving) return;

  isSaving = true;
  disableSubmitButton(true);

  try {
    await fetchJson("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData)
    });

    showToast("Saved");
  } catch (error) {
    showError(error.message);
  } finally {
    isSaving = false;
    disableSubmitButton(false);
  }
}
```

---

## 8. Common Pitfalls and Debugging

1. **Forgetting `await`**
   You pass a Promise where plain data was expected.
2. **Missing `return` in Promise chains**
   Breaks chaining and hides failures.
3. **Using `Array.forEach` with `async` callback**
   `forEach` does not await. Use `for...of` or `Promise.all(map(...))`.
4. **Not checking `response.ok`**
   `fetch` does not reject on HTTP 404/500 by default.
5. **Unhandled Promise rejections**
   Always terminate async flows with `catch` or `try/catch`.
6. **Race conditions in UI**
   Old request finishes after new request and overwrites fresh state.

### Debug tip

Use timestamped logs to observe async ordering:

```javascript
function logStep(step) {
  console.log(`${new Date().toISOString()} :: ${step}`);
}
```

---

## 9. Practice Drills

1. Refactor nested callbacks into `async`/`await`.
2. Build a "search as you type" input using `AbortController`.
3. Fetch 10 endpoints with concurrency limit `3`.
4. Implement `fetchWithTimeout` + retry wrapper.
5. Add loading/error/empty states to an API-driven list.

---

## 10. Production Checklist

- [ ] Every network call checks `response.ok`.
- [ ] Timeouts are defined for user-facing requests.
- [ ] Retries only for transient failures.
- [ ] Parallel requests used where dependencies allow.
- [ ] Aborted/stale requests do not update UI.
- [ ] Loading/error/empty states exist for all async screens.
- [ ] All Promise chains terminate with error handling.

---

## See Also
- [JavaScript Fetch API Guide](./JavaScript_Fetch_API_Guide.md) - HTTP requests, response parsing, and API patterns
- [DOM Manipulation Guide](./DOM_Manipulation_Guide.md) - Rendering async data safely in the UI
- [Frontend Fundamentals Workbook](./Frontend_Fundamentals_Workbook.md) - Integrated JS, DOM, and CSS practice track
- [JavaScript LocalStorage Guide](./JavaScript_LocalStorage_Guide.md) - Persisting async results and caching patterns
- [JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md) - Core language fundamentals
