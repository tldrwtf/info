# JavaScript LocalStorage Guide

## Quick Reference Card

| Method | Syntax | Purpose |
|--------|--------|---------|
| **Set Item** | `localStorage.setItem(key, value)` | Store data |
| **Get Item** | `localStorage.getItem(key)` | Retrieve data |
| **Remove Item** | `localStorage.removeItem(key)` | Delete specific item |
| **Clear All** | `localStorage.clear()` | Delete all localStorage data |
| **Check Key** | `localStorage.getItem(key) !== null` | Check if key exists |
| **Serialize** | `JSON.stringify(object)` | Convert object to JSON string |
| **Deserialize** | `JSON.parse(jsonString)` | Convert JSON string to object |
| **Get Keys** | `Object.keys(localStorage)` | List all storage keys |

---

## Table of Contents
1. [What is LocalStorage?](#what-is-localstorage)
2. [Basic Operations](#basic-operations)
3. [JSON Serialization](#json-serialization)
4. [Cross-Page Data Persistence](#cross-page-data-persistence)
5. [Working with Arrays](#working-with-arrays)
6. [Form Data Collection Patterns](#form-data-collection-patterns)
7. [Real-World Patterns](#real-world-patterns)
8. [Storage Limits and Best Practices](#storage-limits-and-best-practices)
9. [Common Pitfalls](#common-pitfalls)

---

## What is LocalStorage?

**LocalStorage** is a browser API that allows you to store key-value pairs persistently in a user's browser. Data remains even after the browser is closed and reopened.

### Key Characteristics

```javascript
// Data persists across:
// - Page refreshes
// - Browser restarts
// - Tab closes/reopens
// - Days, weeks, months (until explicitly deleted)

// Limitations:
// - 5-10 MB storage limit (varies by browser)
// - Only stores strings (must serialize objects)
// - Synchronous operations (blocks main thread)
// - No expiration mechanism (data stays forever)
// - Same-origin policy (per domain)
```

### LocalStorage vs SessionStorage vs Cookies

| Feature | LocalStorage | SessionStorage | Cookies |
|---------|--------------|----------------|---------|
| **Persistence** | Until deleted | Until tab closes | Expiration date |
| **Scope** | All tabs | Single tab | All tabs + server |
| **Storage Size** | ~5-10 MB | ~5-10 MB | ~4 KB |
| **Sent to Server** | No | No | Yes (with requests) |
| **API** | Simple | Simple | Complex |

---

## Basic Operations

### Storing Data

```javascript
// Store a simple string
localStorage.setItem('username', 'JohnDoe');

// Alternative syntax (not recommended)
localStorage.username = 'JohnDoe';
localStorage['username'] = 'JohnDoe';
```

### Retrieving Data

```javascript
// Get stored value
const username = localStorage.getItem('username');
console.log(username); // "JohnDoe"

// Returns null if key doesn't exist
const nonexistent = localStorage.getItem('doesNotExist');
console.log(nonexistent); // null
```

### Removing Data

```javascript
// Remove specific item
localStorage.removeItem('username');

// Remove all items
localStorage.clear();
```

### Checking if Key Exists

```javascript
// Method 1: Check for null
if (localStorage.getItem('username') !== null) {
  console.log('Username exists');
}

// Method 2: Use hasOwnProperty (less common)
if (localStorage.hasOwnProperty('username')) {
  console.log('Username exists');
}

// Method 3: Check length
if (localStorage.length > 0) {
  console.log('LocalStorage has data');
}
```

---

## JSON Serialization

LocalStorage **only stores strings**. To store objects or arrays, you must serialize them to JSON.

### Storing Objects

```javascript
const user = {
  email: 'john@example.com',
  username: 'JohnDoe',
  password: 'secret123',
  profilePicture: 'https://example.com/pic.jpg',
  bio: 'Web developer from NYC'
};

// BAD: Stores "[object Object]" string
localStorage.setItem('user', user);

// GOOD: Serialize to JSON string
localStorage.setItem('user', JSON.stringify(user));
```

### Retrieving Objects

```javascript
// Get JSON string from localStorage
let myUser = localStorage.getItem('user');

// Deserialize JSON string to JavaScript object
myUser = JSON.parse(myUser);

// Now you can access properties
console.log(myUser.username); // "JohnDoe"
console.log(myUser.email);    // "john@example.com"
```

### Complete Pattern

```javascript
// Save user data
const saveUser = (userData) => {
  localStorage.setItem('user', JSON.stringify(userData));
};

// Load user data
const loadUser = () => {
  const userJSON = localStorage.getItem('user');

  // Return null if no user exists
  if (!userJSON) return null;

  // Parse and return user object
  return JSON.parse(userJSON);
};

// Usage
saveUser({ username: 'JohnDoe', email: 'john@example.com' });
const user = loadUser();
console.log(user); // { username: 'JohnDoe', email: 'john@example.com' }
```

---

## Cross-Page Data Persistence

LocalStorage enables data sharing between different pages on the same domain.

### Pattern: Registration to Profile Flow

**Page 1: register.html**

```javascript
const form = document.querySelector("#my-form");

const email = document.getElementById("email");
const password = document.getElementById("password");
const username = document.getElementById("username");
const profilePicture = document.getElementById("profilePicture");
const bio = document.getElementById("bio");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  // Collect form data
  const user = {
    email: email.value,
    username: username.value,
    password: password.value,
    profilePicture: profilePicture.value,
    bio: bio.value
  };

  // Save to localStorage (serialize to JSON)
  localStorage.setItem('user', JSON.stringify(user));

  // Redirect to profile page
  window.location.href = "profile.html";
});
```

**Page 2: profile.html**

```javascript
const htmlBody = document.querySelector('body');

// Load user data from localStorage
let myUser = localStorage.getItem('user');

// Deserialize JSON to JavaScript object
myUser = JSON.parse(myUser);

// Check if user exists
if (!myUser) {
  htmlBody.innerHTML = '<h1>No user found. Please register first.</h1>';
} else {
  // Display user profile
  htmlBody.innerHTML = `
    <h1>Profile</h1>
    <div class="card" style="width: 18rem;">
      <img src="${myUser.profilePicture}" class="card-img-top" alt="Profile">
      <div class="card-body">
        <h5 class="card-title">${myUser.username}</h5>
        <p class="card-text">${myUser.email}</p>
        <p class="card-text">${myUser.bio}</p>
      </div>
    </div>
  `;
}
```

### Data Flow Diagram

```
[Register Page]                    [Profile Page]
     │                                   │
     │ User fills form                   │
     │ form.addEventListener("submit")   │
     ├──────────────────────────────────>│
     │                                   │
     │ Collect form data                 │
     │ const user = { ... }              │
     │                                   │
     │ Save to localStorage              │
     │ localStorage.setItem('user', JSON.stringify(user))
     │                                   │
     │ Redirect                          │
     │ window.location.href = "profile.html"
     │                                   │
     └──────────────────────────────────>│
                                         │
                                         │ Load from localStorage
                                         │ myUser = JSON.parse(localStorage.getItem('user'))
                                         │
                                         │ Display user data
                                         │ htmlBody.innerHTML = `...`
```

---

## Working with Arrays

### Adding Items to Array

```javascript
// Pattern: Add Pokemon to team
const catchPokemon = (pokeData) => {
  // Get existing team from localStorage (or empty array)
  const myTeam = JSON.parse(localStorage.getItem("myTeam")) || [];

  // Add new pokemon to array
  myTeam.push(pokeData);

  // Save updated array back to localStorage
  localStorage.setItem("myTeam", JSON.stringify(myTeam));

  alert(`Success! You caught ${pokeData.name}`);
};

// Usage
catchPokemon({
  name: 'pikachu',
  type: 'electric',
  hp: 35,
  attack: 55
});
```

### Loading and Displaying Array

```javascript
const teamContainer = document.getElementById("teamContainer");

const loadMyTeam = () => {
  // Load team from localStorage
  const myTeam = JSON.parse(localStorage.getItem("myTeam")) || [];

  // Check if team is empty
  if (myTeam.length === 0) {
    teamContainer.innerHTML = '<p class="empty-message">No Pokemon caught yet!</p>';
    return;
  }

  // Clear container
  teamContainer.innerHTML = '';

  // Display each Pokemon
  myTeam.forEach((pokemon, index) => {
    const pokemonCard = document.createElement('div');
    pokemonCard.className = 'pokemon-card';

    pokemonCard.innerHTML = `
      <img class="pokemon-pic" src="${pokemon.sprite}" alt="${pokemon.name}">
      <div class="pokemon-info">
        <h3>${pokemon.name}</h3>
        <p>${pokemon.type}</p>
      </div>
      <div class="pokemon-stats">
        <p>HP: ${pokemon.hp}</p>
        <p>Attack: ${pokemon.attack}</p>
      </div>
    `;

    teamContainer.appendChild(pokemonCard);
  });
};

// Load team when page loads
window.addEventListener('load', loadMyTeam);
```

### Removing Items from Array

```javascript
const removePokemon = (pokemonName) => {
  // Load team
  let myTeam = JSON.parse(localStorage.getItem("myTeam")) || [];

  // Filter out the pokemon to remove
  myTeam = myTeam.filter(pokemon => pokemon.name !== pokemonName);

  // Save updated team
  localStorage.setItem("myTeam", JSON.stringify(myTeam));
};

// Usage
removePokemon('pikachu');
```

### Updating Items in Array

```javascript
const updatePokemon = (pokemonName, updates) => {
  // Load team
  let myTeam = JSON.parse(localStorage.getItem("myTeam")) || [];

  // Find and update pokemon
  const index = myTeam.findIndex(p => p.name === pokemonName);

  if (index !== -1) {
    myTeam[index] = { ...myTeam[index], ...updates };
    localStorage.setItem("myTeam", JSON.stringify(myTeam));
  }
};

// Usage
updatePokemon('pikachu', { hp: 40, attack: 60 });
```

---

## Form Data Collection Patterns

### Pattern 1: Manual Collection (Explicit)

```javascript
const form = document.querySelector("#my-form");

const email = document.getElementById("email");
const password = document.getElementById("password");
const username = document.getElementById("username");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const user = {
    email: email.value,
    username: username.value,
    password: password.value
  };

  localStorage.setItem('user', JSON.stringify(user));
});
```

**Pros:** Explicit, clear what data is collected
**Cons:** Verbose, requires updating for new fields

### Pattern 2: Dynamic Collection (Automated)

```javascript
const form = document.querySelector("#my-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  // Select all form controls
  const formFields = document.querySelectorAll(".form-control");

  // Build user object dynamically
  const myUser = {};
  formFields.forEach(field => {
    myUser[field.id] = field.value;
  });

  // Save to localStorage
  localStorage.setItem('user', JSON.stringify(myUser));

  // Redirect
  window.location.href = "profile.html";
});
```

**Pros:** Automatic, scales with new fields
**Cons:** Requires consistent ID naming

### Pattern 3: FormData API

```javascript
const form = document.querySelector("#my-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const user = Object.fromEntries(formData);

  localStorage.setItem('user', JSON.stringify(user));
});
```

**Note:** Requires `name` attributes on form inputs.

---

## Real-World Patterns

### Pattern 1: Shopping List with Persistence

```javascript
const myForm = document.querySelector('form');
const itemInput = document.querySelector('#item-input');
const shoppingList = document.querySelector("#shopping-list");

// Load saved items on page load
const loadShoppingList = () => {
  const items = JSON.parse(localStorage.getItem('shoppingList')) || [];

  items.forEach(item => {
    const li = document.createElement("li");
    li.innerText = item;
    shoppingList.appendChild(li);
  });
};

// Add new item
myForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const newItemText = itemInput.value.trim();
  if (!newItemText) return;

  // Add to DOM
  const newItem = document.createElement("li");
  newItem.innerText = newItemText;
  shoppingList.appendChild(newItem);

  // Save to localStorage
  const items = JSON.parse(localStorage.getItem('shoppingList')) || [];
  items.push(newItemText);
  localStorage.setItem('shoppingList', JSON.stringify(items));

  // Clear input
  itemInput.value = "";
});

// Load on page start
window.addEventListener('load', loadShoppingList);
```

### Pattern 2: User Preferences

```javascript
// Save user theme preference
const saveTheme = (theme) => {
  localStorage.setItem('theme', theme);
  document.body.className = theme;
};

// Load theme on page load
const loadTheme = () => {
  const theme = localStorage.getItem('theme') || 'light';
  document.body.className = theme;
};

// Theme toggle button
const themeToggle = document.getElementById('theme-toggle');
themeToggle.addEventListener('click', () => {
  const currentTheme = document.body.className;
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  saveTheme(newTheme);
});

// Load theme on start
window.addEventListener('load', loadTheme);
```

### Pattern 3: Auto-Save Form

```javascript
const form = document.querySelector('#my-form');
const inputs = form.querySelectorAll('input, textarea');

// Save form data on every input change
inputs.forEach(input => {
  input.addEventListener('input', () => {
    const formData = {};
    inputs.forEach(field => {
      formData[field.id] = field.value;
    });
    localStorage.setItem('formDraft', JSON.stringify(formData));
  });
});

// Load saved form data on page load
const loadFormDraft = () => {
  const draft = JSON.parse(localStorage.getItem('formDraft'));

  if (draft) {
    inputs.forEach(input => {
      if (draft[input.id]) {
        input.value = draft[input.id];
      }
    });
  }
};

// Clear draft after successful submit
form.addEventListener('submit', (event) => {
  event.preventDefault();
  // ... submit logic ...
  localStorage.removeItem('formDraft');
});

window.addEventListener('load', loadFormDraft);
```

### Pattern 4: Login State Management

```javascript
// Check if user is logged in
const isLoggedIn = () => {
  return localStorage.getItem('authToken') !== null;
};

// Save login session
const login = (username, token) => {
  localStorage.setItem('authToken', token);
  localStorage.setItem('username', username);
  window.location.href = 'dashboard.html';
};

// Logout
const logout = () => {
  localStorage.removeItem('authToken');
  localStorage.removeItem('username');
  window.location.href = 'login.html';
};

// Protect pages (redirect if not logged in)
const protectPage = () => {
  if (!isLoggedIn()) {
    window.location.href = 'login.html';
  }
};

// Call on protected pages
window.addEventListener('load', protectPage);
```

---

## Storage Limits and Best Practices

### Storage Limits

| Browser | LocalStorage Limit |
|---------|-------------------|
| Chrome | ~10 MB |
| Firefox | ~10 MB |
| Safari | ~5 MB |
| Edge | ~10 MB |
| Mobile Browsers | ~5-10 MB |

### Checking Storage Usage

```javascript
// Estimate storage used (rough approximation)
const getStorageSize = () => {
  let total = 0;
  for (let key in localStorage) {
    if (localStorage.hasOwnProperty(key)) {
      total += localStorage[key].length + key.length;
    }
  }
  return (total / 1024).toFixed(2) + ' KB';
};

console.log('LocalStorage size:', getStorageSize());
```

### Best Practices

#### 1. Always Use Try-Catch

```javascript
const safeSetItem = (key, value) => {
  try {
    localStorage.setItem(key, value);
    return true;
  } catch (error) {
    if (error.name === 'QuotaExceededError') {
      console.error('LocalStorage quota exceeded');
    }
    return false;
  }
};

const safeGetItem = (key) => {
  try {
    return localStorage.getItem(key);
  } catch (error) {
    console.error('Error reading from localStorage:', error);
    return null;
  }
};
```

#### 2. Check for LocalStorage Availability

```javascript
const isLocalStorageAvailable = () => {
  try {
    const test = '__localStorage_test__';
    localStorage.setItem(test, test);
    localStorage.removeItem(test);
    return true;
  } catch (error) {
    return false;
  }
};

// Use before any localStorage operations
if (isLocalStorageAvailable()) {
  localStorage.setItem('key', 'value');
} else {
  console.warn('LocalStorage not available');
}
```

#### 3. Implement Expiration

LocalStorage has no built-in expiration. Implement your own:

```javascript
// Save with expiration timestamp
const setItemWithExpiry = (key, value, ttlMinutes) => {
  const now = new Date();
  const item = {
    value: value,
    expiry: now.getTime() + (ttlMinutes * 60 * 1000)
  };
  localStorage.setItem(key, JSON.stringify(item));
};

// Get item and check expiration
const getItemWithExpiry = (key) => {
  const itemStr = localStorage.getItem(key);

  if (!itemStr) return null;

  const item = JSON.parse(itemStr);
  const now = new Date();

  // Check if expired
  if (now.getTime() > item.expiry) {
    localStorage.removeItem(key);
    return null;
  }

  return item.value;
};

// Usage
setItemWithExpiry('sessionData', { user: 'John' }, 30); // 30 minutes
const data = getItemWithExpiry('sessionData');
```

#### 4. Namespace Your Keys

```javascript
// Avoid key collisions with other scripts
const APP_PREFIX = 'myApp_';

const setItem = (key, value) => {
  localStorage.setItem(APP_PREFIX + key, value);
};

const getItem = (key) => {
  return localStorage.getItem(APP_PREFIX + key);
};

// Usage
setItem('user', JSON.stringify({ name: 'John' }));
getItem('user');
```

#### 5. Don't Store Sensitive Data

```javascript
// BAD: Never store in localStorage
localStorage.setItem('creditCard', '1234-5678-9012-3456');
localStorage.setItem('password', 'myPassword123');
localStorage.setItem('ssn', '123-45-6789');

// GOOD: Store non-sensitive data only
localStorage.setItem('theme', 'dark');
localStorage.setItem('language', 'en');
localStorage.setItem('username', 'JohnDoe'); // Public info only
```

**What NOT to store:**
- Passwords
- Credit card numbers
- Social Security numbers
- Personal health information
- API keys or tokens (unless specifically designed for client-side)

---

## Common Pitfalls

### Pitfall 1: Forgetting JSON.stringify/parse

```javascript
// BAD: Stores "[object Object]"
const user = { name: 'John', age: 30 };
localStorage.setItem('user', user);
console.log(localStorage.getItem('user')); // "[object Object]"

// GOOD: Serialize first
localStorage.setItem('user', JSON.stringify(user));
const retrieved = JSON.parse(localStorage.getItem('user'));
console.log(retrieved); // { name: 'John', age: 30 }
```

### Pitfall 2: Not Checking for Null

```javascript
// BAD: Crashes if key doesn't exist
const user = JSON.parse(localStorage.getItem('user'));
console.log(user.name); // Error if user is null

// GOOD: Check for null
const userStr = localStorage.getItem('user');
if (userStr) {
  const user = JSON.parse(userStr);
  console.log(user.name);
} else {
  console.log('No user found');
}
```

### Pitfall 3: Overwriting Array Data

```javascript
// BAD: Overwrites entire array
localStorage.setItem('items', JSON.stringify(['new item']));

// GOOD: Load, modify, save
const items = JSON.parse(localStorage.getItem('items')) || [];
items.push('new item');
localStorage.setItem('items', JSON.stringify(items));
```

### Pitfall 4: Synchronous Blocking

```javascript
// LocalStorage operations are synchronous and can block UI
// For large data, consider using IndexedDB instead

// If you must store large data:
const saveLargeData = (data) => {
  // Chunk the data
  const chunkSize = 1000;
  const chunks = [];

  for (let i = 0; i < data.length; i += chunkSize) {
    chunks.push(data.slice(i, i + chunkSize));
  }

  // Save chunks separately
  chunks.forEach((chunk, index) => {
    localStorage.setItem(`data_chunk_${index}`, JSON.stringify(chunk));
  });

  // Save metadata
  localStorage.setItem('data_chunks_count', chunks.length);
};
```

### Pitfall 5: Private Browsing Mode

```javascript
// LocalStorage may not work in private/incognito mode
// Always wrap in try-catch

try {
  localStorage.setItem('test', 'value');
} catch (error) {
  console.warn('LocalStorage unavailable (private mode?)');
  // Fallback to session storage or memory storage
}
```

---

## Summary

**Key Takeaways:**
1. **Only stores strings** - use `JSON.stringify()` and `JSON.parse()` for objects
2. **Persistent storage** - data survives browser restarts
3. **Synchronous API** - operations block main thread
4. **~5-10 MB limit** - check storage usage for large data
5. **Cross-page accessible** - same domain only
6. **No expiration** - implement your own if needed
7. **Not secure** - don't store sensitive data

**Best Practice Pattern:**

```javascript
// Save
const saveData = (key, data) => {
  try {
    localStorage.setItem(key, JSON.stringify(data));
  } catch (error) {
    console.error('Failed to save to localStorage:', error);
  }
};

// Load
const loadData = (key) => {
  try {
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('Failed to load from localStorage:', error);
    return null;
  }
};

// Usage
saveData('user', { name: 'John', email: 'john@example.com' });
const user = loadData('user');
```

---

## See Also

- [JavaScript Fetch API Guide](./JavaScript_Fetch_API_Guide.md) - Fetch data and store in localStorage
- [JavaScript Async Programming Guide](./JavaScript_Async_Programming_Guide.md) - Async patterns for data loading
- [React Basics Guide](./React_Basics_Guide.md) - React state management with localStorage persistence
- [DOM Manipulation Guide](./DOM_Manipulation_Guide.md) - Display and manage localStorage data in the DOM
- [JavaScript Basics Cheat Sheet](../cheatsheets/JavaScript_Basics_Cheat_Sheet.md) - Core JavaScript syntax
- [JavaScript Objects Arrays Cheat Sheet](../cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md) - Working with JSON data structures

---
