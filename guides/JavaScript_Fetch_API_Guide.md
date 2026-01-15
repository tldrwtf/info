# JavaScript Fetch API Guide

## Quick Reference Card

| Concept | Syntax | Purpose |
|---------|--------|---------|
| **Basic Fetch** | `fetch(url)` | Make HTTP request, returns Promise |
| **Get JSON** | `response.json()` | Parse response body as JSON |
| **Async/Await** | `const res = await fetch(url)` | Wait for promise to resolve |
| **Error Handling** | `try { } catch (error) { }` | Handle network errors |
| **Check Status** | `if (response.ok) { }` | Verify HTTP 200-299 status |
| **POST Request** | `fetch(url, { method: 'POST' })` | Send data to server |
| **Set Headers** | `{ headers: { 'Content-Type': 'application/json' } }` | Configure request metadata |
| **Send JSON** | `body: JSON.stringify(data)` | Serialize data for POST/PUT |

---

## Table of Contents
1. [What is Fetch API?](#what-is-fetch-api)
2. [Basic GET Requests](#basic-get-requests)
3. [Understanding Responses](#understanding-responses)
4. [Error Handling](#error-handling)
5. [POST Requests](#post-requests)
6. [Headers and Configuration](#headers-and-configuration)
7. [Real-World Patterns](#real-world-patterns)
8. [Common Pitfalls](#common-pitfalls)

---

## What is Fetch API?

The **Fetch API** is the modern JavaScript standard for making HTTP requests. It replaces the older `XMLHttpRequest` and provides a cleaner, Promise-based interface for network communication.

### Key Characteristics

```javascript
// Fetch returns a Promise
fetch("https://api.example.com/data")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

**Why Use Fetch?**
- **Promise-based**: Works seamlessly with async/await
- **Cleaner syntax**: More readable than XMLHttpRequest
- **Built-in JSON support**: Easy response parsing
- **Modern standard**: Native to all modern browsers
- **Flexible**: Supports all HTTP methods (GET, POST, PUT, DELETE, etc.)

---

## Basic GET Requests

### Fetch with Promise Chain

```javascript
const button = document.getElementById("btn");

button.addEventListener("click", () => {
  fetch("https://fakestoreapi.com/products/1")
    .then((response) => {
      // Response is the HTTP response object
      return response.json(); // Parse JSON from response body
    })
    .then(data => {
      // data is now a JavaScript object
      console.log(data);

      // Display in DOM
      const body = document.querySelector("body");
      const h1 = document.createElement("h1");
      h1.textContent = data.title;
      body.appendChild(h1);
    })
    .catch(error => {
      console.error("Something went wrong:", error);
    });
});
```

### Fetch with Async/Await (Recommended)

```javascript
const fetchProductData = async () => {
  try {
    const response = await fetch("https://fakestoreapi.com/products/1");
    const data = await response.json();
    console.log(data);

    // Display in DOM
    const body = document.querySelector("body");
    const h1 = document.createElement("h1");
    const img = document.createElement('img');

    h1.textContent = data.title;
    img.setAttribute("src", data.image);

    body.appendChild(h1);
    body.appendChild(img);
  } catch (error) {
    console.error("Something went wrong:", error);
  }
};

fetchProductData();
```

**Key Points:**
- Fetch returns a Promise that resolves to a `Response` object
- You must call `.json()` to extract data from the response
- `.json()` also returns a Promise, so you need a second `await`
- Always use `try...catch` with async/await for error handling

---

## Understanding Responses

### The Response Object

When you call `fetch()`, you get a `Response` object that contains:

```javascript
const response = await fetch("https://api.example.com/data");

console.log(response.ok);        // true if status 200-299
console.log(response.status);    // HTTP status code (200, 404, 500, etc.)
console.log(response.statusText); // Status text ("OK", "Not Found", etc.)
console.log(response.headers);   // Response headers
console.log(response.url);       // Final URL after redirects
```

### Extracting Data from Response

The response body can be read in different formats:

```javascript
// Parse as JSON (most common)
const data = await response.json();

// Read as plain text
const text = await response.text();

// Read as Blob (for images, files)
const blob = await response.blob();

// Read as FormData
const formData = await response.formData();
```

**IMPORTANT: Double Await Pattern**

```javascript
// BAD: Only one await
const data = await fetch("https://api.com/data");
console.log(data); // Response object, NOT the actual data

// GOOD: Two awaits
const response = await fetch("https://api.com/data");
const data = await response.json(); // Now data is the actual JSON
console.log(data);
```

---

## Error Handling

### Two Types of Errors

Fetch API distinguishes between **network errors** and **HTTP errors**:

```javascript
const fetchData = async () => {
  try {
    const response = await fetch("https://api.example.com/data");

    // Check if response is OK (status 200-299)
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    // Catches both network errors AND thrown HTTP errors
    console.error("Fetch failed:", error);
  }
};
```

### Network Errors vs HTTP Errors

```javascript
// Network Error: No internet, DNS failure, CORS block
// fetch() Promise REJECTS → goes to catch block

// HTTP Error: Server responds with 404, 500, etc.
// fetch() Promise RESOLVES → check response.ok manually
```

### Comprehensive Error Handling Pattern

```javascript
const getPokemon = async (pokemonName) => {
  try {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);

    // Handle HTTP errors
    if (!response.ok) {
      if (response.status === 404) {
        throw new Error(`Pokemon "${pokemonName}" not found`);
      } else if (response.status === 500) {
        throw new Error("Server error - try again later");
      } else {
        throw new Error(`HTTP error: ${response.status}`);
      }
    }

    const data = await response.json();

    return {
      name: data.name,
      type: data.types[0].type.name,
      hp: data.stats[0].base_stat,
      sprite: data.sprites.other.dream_world.front_default
    };
  } catch (error) {
    // Network error OR thrown HTTP error
    console.error("Error fetching Pokemon:", error.message);
    return null;
  }
};

// Usage
const pokemon = await getPokemon("pikachu");
if (pokemon) {
  console.log(pokemon);
}
```

---

## POST Requests

### Sending JSON Data

```javascript
const createUser = async (userData) => {
  try {
    const response = await fetch("https://api.example.com/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(userData) // Convert JS object to JSON string
    });

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const newUser = await response.json();
    return newUser;
  } catch (error) {
    console.error("Failed to create user:", error);
  }
};

// Usage
const user = await createUser({
  name: "John Doe",
  email: "john@example.com",
  age: 30
});
```

### Request Configuration Options

```javascript
fetch(url, {
  method: "POST",           // HTTP method
  headers: {                // Request headers
    "Content-Type": "application/json",
    "Authorization": "Bearer token123"
  },
  body: JSON.stringify(data), // Request body (must be string)
  mode: "cors",             // CORS mode (cors, no-cors, same-origin)
  credentials: "include",   // Send cookies (include, same-origin, omit)
  cache: "no-cache",        // Cache mode
  redirect: "follow"        // Redirect behavior
});
```

### Form Data POST

```javascript
const uploadForm = async (formElement) => {
  const formData = new FormData(formElement);

  try {
    const response = await fetch("https://api.example.com/upload", {
      method: "POST",
      body: formData // FormData automatically sets correct Content-Type
    });

    if (!response.ok) {
      throw new Error("Upload failed");
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error("Error uploading form:", error);
  }
};
```

---

## Headers and Configuration

### Setting Request Headers

```javascript
const fetchWithAuth = async () => {
  const token = localStorage.getItem("authToken");

  const response = await fetch("https://api.example.com/protected", {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Content-Type": "application/json",
      "Accept": "application/json"
    }
  });

  return await response.json();
};
```

### Reading Response Headers

```javascript
const response = await fetch("https://api.example.com/data");

// Get specific header
const contentType = response.headers.get("Content-Type");
console.log(contentType); // "application/json"

// Check if header exists
if (response.headers.has("X-Custom-Header")) {
  console.log("Custom header present");
}

// Iterate all headers
for (const [key, value] of response.headers) {
  console.log(`${key}: ${value}`);
}
```

---

## Real-World Patterns

### Pattern 1: Pokemon Fetcher with Display

```javascript
const cardContainer = document.querySelector(".cardContainer");

const getPokemon = async (pokemon) => {
  try {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemon}`);

    if (!response.ok) {
      throw new Error(`Pokemon not found: ${pokemon}`);
    }

    const data = await response.json();

    const pokeData = {
      name: data.name,
      type: data.types[0].type.name,
      hp: data.stats[0].base_stat,
      height: data.height,
      weight: data.weight,
      attack: data.stats[1].base_stat,
      sprite: data.sprites.other.dream_world.front_default
    };

    return pokeData;
  } catch (error) {
    console.error("Error:", error.message);
    return null;
  }
};

const displayPokemon = (pokedata) => {
  if (!pokedata) return;

  cardContainer.innerHTML = '';
  const myCard = document.createElement('div');
  myCard.className = 'my-card';

  myCard.innerHTML = `
    <img class='pokePic' src='${pokedata.sprite}'>
    <div class="info">
      <h3>${pokedata.name}</h3>
      <p>Type: ${pokedata.type}</p>
      <h3>Stats:</h3>
      <p>HP: ${pokedata.hp} - ATK: ${pokedata.attack}</p>
      <p>Height: ${pokedata.height} - Weight: ${pokedata.weight}</p>
    </div>
  `;

  cardContainer.appendChild(myCard);
};

// Event handler
const myForm = document.querySelector("form");
const myInput = document.getElementById("searchBar");

myForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const pokemon = myInput.value.toLowerCase().trim();

  if (!pokemon) return;

  const pokeData = await getPokemon(pokemon);
  displayPokemon(pokeData);
  myInput.value = '';
});
```

### Pattern 2: LocalStorage Integration

```javascript
// Save fetched data to localStorage
const catchPokemon = (pokeData) => {
  const isCaught = Math.random() < 0.5; // 50% catch rate

  if (isCaught) {
    // Get existing team from localStorage
    const myTeam = JSON.parse(localStorage.getItem("myTeam")) || [];

    // Add new pokemon to team
    myTeam.push(pokeData);

    // Save back to localStorage
    localStorage.setItem("myTeam", JSON.stringify(myTeam));

    alert(`Success! You caught ${pokeData.name}`);
  } else {
    alert(`You failed to catch ${pokeData.name}. Try again!`);
  }
};

// Load from localStorage on page load
const loadMyTeam = () => {
  const myTeam = JSON.parse(localStorage.getItem("myTeam")) || [];

  if (myTeam.length === 0) {
    teamContainer.innerHTML = '<p class="empty-message">No Pokemon caught yet!</p>';
    return;
  }

  myTeam.forEach((pokemon) => {
    const pokemonCard = document.createElement('div');
    pokemonCard.className = 'pokemon-card';

    pokemonCard.innerHTML = `
      <img class="pokemon-pic" src="${pokemon.sprite}" alt="${pokemon.name}">
      <div class="pokemon-info">
        <h3>${pokemon.name}</h3>
        <p>${pokemon.type}</p>
        <p>Height: ${pokemon.height}</p>
        <p>Weight: ${pokemon.weight}</p>
      </div>
      <div class="pokemon-stats">
        <p>HP: ${pokemon.hp}</p>
        <p>Attack: ${pokemon.attack}</p>
      </div>
    `;

    teamContainer.appendChild(pokemonCard);
  });
};

window.addEventListener('load', loadMyTeam);
```

### Pattern 3: Loading States

```javascript
const fetchDataWithLoading = async () => {
  const statusElement = document.getElementById("status");

  try {
    // Show loading state
    statusElement.textContent = "Loading...";
    statusElement.className = "loading";

    const response = await fetch("https://api.example.com/data");

    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }

    const data = await response.json();

    // Show success state
    statusElement.textContent = "Data loaded successfully!";
    statusElement.className = "success";

    return data;
  } catch (error) {
    // Show error state
    statusElement.textContent = `Error: ${error.message}`;
    statusElement.className = "error";
    return null;
  }
};
```

### Pattern 4: Retry Logic

```javascript
const fetchWithRetry = async (url, maxRetries = 3) => {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      return await response.json();
    } catch (error) {
      console.warn(`Attempt ${attempt} failed:`, error.message);

      if (attempt === maxRetries) {
        throw new Error(`Failed after ${maxRetries} attempts`);
      }

      // Wait before retry (exponential backoff)
      await new Promise(resolve => setTimeout(resolve, 1000 * attempt));
    }
  }
};

// Usage
try {
  const data = await fetchWithRetry("https://api.example.com/data");
  console.log(data);
} catch (error) {
  console.error("All retry attempts failed:", error);
}
```

---

## Common Pitfalls

### Pitfall 1: Forgetting to Check response.ok

```javascript
// BAD: Doesn't handle HTTP errors
const data = await fetch(url).then(res => res.json());

// GOOD: Always check response.ok
const response = await fetch(url);
if (!response.ok) {
  throw new Error(`HTTP error: ${response.status}`);
}
const data = await response.json();
```

### Pitfall 2: Missing Second Await

```javascript
// BAD: Only awaits fetch, not .json()
const data = await fetch(url).then(res => res.json());
// If .json() fails, the promise rejection is unhandled

// GOOD: Await both operations
const response = await fetch(url);
const data = await response.json();
```

### Pitfall 3: Not Handling Network Errors

```javascript
// BAD: No error handling
const data = await fetch(url).then(res => res.json());

// GOOD: Wrap in try-catch
try {
  const response = await fetch(url);
  const data = await response.json();
} catch (error) {
  console.error("Network or parse error:", error);
}
```

### Pitfall 4: Forgetting JSON.stringify for POST

```javascript
// BAD: Sending object directly
fetch(url, {
  method: "POST",
  body: { name: "John" } // Won't work!
});

// GOOD: Stringify the object
fetch(url, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "John" })
});
```

### Pitfall 5: CORS Issues

```javascript
// If you get CORS errors:
// - Server must send proper Access-Control-Allow-Origin headers
// - You cannot fix CORS from the client side
// - Use mode: 'no-cors' only if you don't need the response

// Limited access (no response body)
fetch(url, { mode: 'no-cors' });

// Proper solution: Configure server CORS headers
// Express example:
// app.use(cors({ origin: 'https://your-site.com' }));
```

---

## HTTP Status Codes Reference

| Status Code | Meaning | Action |
|-------------|---------|--------|
| **200** | OK | Success - process data |
| **201** | Created | Resource created successfully |
| **204** | No Content | Success - no response body |
| **400** | Bad Request | Invalid request data |
| **401** | Unauthorized | Authentication required |
| **403** | Forbidden | Access denied |
| **404** | Not Found | Resource doesn't exist |
| **500** | Internal Server Error | Server-side error |
| **503** | Service Unavailable | Server temporarily down |

---

## Summary

**Key Takeaways:**
1. **Fetch returns a Promise** - use async/await or .then()
2. **Two awaits needed** - one for fetch, one for .json()
3. **Check response.ok** - fetch doesn't reject on HTTP errors
4. **Use try...catch** - handle both network and parse errors
5. **JSON.stringify for POST** - convert objects to JSON strings
6. **Set Content-Type header** - tell server what you're sending

**Best Practice Pattern:**

```javascript
const fetchData = async (url) => {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Fetch failed:", error);
    return null;
  }
};
```

---

## See Also

- [JavaScript Async Programming Guide](./JavaScript_Async_Programming_Guide.md) - Async/await fundamentals and Promise patterns
- [JavaScript LocalStorage Guide](./JavaScript_LocalStorage_Guide.md) - Persisting fetched data across sessions
- [React Basics Guide](./React_Basics_Guide.md) - Using Fetch in React components with useEffect
- [DOM Manipulation Guide](./DOM_Manipulation_Guide.md) - Displaying fetched data in the DOM
- [JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md) - Core JavaScript syntax and concepts
- [APIs and Requests Cheat Sheet](../cheatsheets/APIs_and_Requests_Cheat_Sheet.md) - HTTP methods and API fundamentals

---

