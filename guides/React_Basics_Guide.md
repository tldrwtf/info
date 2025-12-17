# React Basics Guide: Modern Web Development

This guide introduces React 19+ using the modern **Vite** build tool. It consolidates concepts from the "Intro to React" workshops, covering components, props, state, and list rendering.

## Table of Contents
1. [Setup with Vite](#setup-with-vite)
2. [Component Structure](#component-structure)
3. [Props (Data Flow)](#props-data-flow)
4. [State (Interactivity)](#state-interactivity)
5. [Lists & Keys](#lists--keys)
6. [Handling Events](#handling-events)

---

## Setup with Vite

We use **Vite** instead of `create-react-app` for a faster, modern development experience.

### Commands
```bash
# Create a new project
npm create vite@latest my-react-app -- --template react

# Install dependencies
cd my-react-app
npm install

# Run the dev server
npm run dev
```

### Project Structure
*   `index.html`: The entry point (contains `<div id="root">`).
*   `src/main.jsx`: Bootstraps React and renders the App into the root.
*   `src/App.jsx`: The main component.

---

## Component Structure

React apps are built from **Components**: independent, reusable UI pieces. They are just JavaScript functions that return JSX (HTML-like syntax).

### Example (`src/components/Navbar.jsx`)
```jsx
const Navbar = () => {
  return (
    <nav>
      <h1>My App</h1>
      <ul>
        <li>Home</li>
        <li>About</li>
      </ul>
    </nav>
  );
};

export default Navbar;
```

### Importing Components
```jsx
// src/App.jsx
import Navbar from './components/Navbar';

function App() {
  return (
    <div>
      <Navbar />
      <p>Welcome to React!</p>
    </div>
  );
}
```

---

## Props (Data Flow)

**Props** (properties) allow you to pass data *down* from a parent component to a child. Props are read-only.

### Parent Component
```jsx
// src/App.jsx
import Greeting from './components/Greeting';

function App() {
  return (
    <>
      <Greeting name="Alice" role="Admin" />
      <Greeting name="Bob" role="User" />
    </>
  );
}
```

### Child Component (`src/components/Greeting.jsx`)
We use **destructuring** to unpack props directly in the function signature.
```jsx
const Greeting = ({ name, role }) => {
  return (
    <div className="card">
      <h3>Hello, {name}!</h3>
      <p>Role: {role}</p>
    </div>
  );
};

export default Greeting;
```

---

## State (Interactivity)

**State** is React's "memory". When state changes, React re-renders the component to reflect the new data. We use the `useState` hook.

### The `useState` Hook
```jsx
import { useState } from 'react';

const Counter = () => {
  // [currentValue, functionToUpdateValue] = useState(initialValue)
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      {/* update state using the setter function */}
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
};
```

---

## Lists & Keys

To render a list of data, we use the JavaScript `.map()` method.

### Data Source
```javascript
// data.js
export const recipes = [
  { id: 1, title: 'Spaghetti', type: 'Pasta' },
  { id: 2, title: 'Salad', type: 'Veggie' }
];
```

### Rendering the List
**Critical:** Every item in a list must have a unique `key` prop so React can track it efficiently.

```jsx
import { recipes } from './data';
import RecipeCard from './components/RecipeCard';

function RecipeList() {
  return (
    <div className="grid">
      {recipes.map((recipe) => (
        <RecipeCard 
          key={recipe.id} // Unique Key!
          title={recipe.title} 
          type={recipe.type} 
        />
      ))}
    </div>
  );
}
```

---

## Handling Events

React events look like standard HTML events but are camelCased (`onClick` instead of `onclick`).

### Example: Search Bar
Controlled input pattern: The input value is tied directly to React state.

```jsx
const SearchBar = ({ searchTerm, setSearchTerm }) => {
  return (
    <input 
      type="text" 
      placeholder="Search..."
      value={searchTerm}
      // Update state whenever the user types
      onChange={(e) => setSearchTerm(e.target.value)} 
    />
  );
};
```
