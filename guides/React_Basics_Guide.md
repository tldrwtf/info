# React Basics Guide

React is a JavaScript library for building user interfaces, primarily based on **Components** and **State**.

## Quick Reference

| Concept | Description | Example |
| :--- | :--- | :--- |
| **Component** | Reusable UI piece | `function Button() { ... }` |
| **JSX** | HTML-in-JavaScript syntax | `return <div>Hello</div>;` |
| **Props** | Data passed *down* to components | `<Welcome name="Alice" />` |
| **State** | Data managed *inside* a component | `const [count, setCount] = useState(0);` |
| **Hooks** | Functions to hook into React features | `useState`, `useEffect` |

---

## 1. Components & JSX

React apps are built from components. A component is a JavaScript function that returns markup (JSX).

### Basic Component
```jsx
// App.js
function Welcome({ name }) {
  return <h1>Hello, {name}</h1>;
}

export default function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}
```

**Rules of JSX:**
1.  **Return a single root element:** Wrap adjacent elements in a `<div>` or Fragment `<>...</>`.
2.  **Close all tags:** `<img />` (self-closing), not `<img>`.
3.  **camelCase properties:** `className` instead of `class`, `onClick` instead of `onclick`.

---

## 2. Props (Passing Data)

Props are read-only. They allow parent components to pass data down to children.

```jsx
function UserProfile({ user }) {
  return (
    <div className="card">
      <img src={user.avatarUrl} alt={user.name} />
      <h3>{user.name}</h3>
    </div>
  );
}

// Usage
<UserProfile user={{ name: "Alice", avatarUrl: "..." }} />
```

---

## 3. State (Interactivity)

State allows components to "remember" things (e.g., current input value, open/closed modal).

### `useState` Hook
```jsx
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0); // [currentValue, updateFunction]

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```

---

## 4. Effects (Side Effects)

The `useEffect` hook lets you synchronize a component with an external system (fetching data, subscriptions).

```jsx
import { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // This runs after the component renders
    fetch('https://api.example.com/data')
      .then(res => res.json())
      .then(data => setData(data));
      
    // Optional cleanup function
    return () => console.log('Cleanup if needed');
  }, []); // Empty array [] means run only once on mount

  if (!data) return <div>Loading...</div>;
  return <div>{data.message}</div>;
}
```

---

## 5. Rendering Lists

Use the `.map()` array method to transform data into lists of elements.

```jsx
function ShoppingList() {
  const products = [
    { title: 'Cabbage', id: 1 },
    { title: 'Garlic', id: 2 },
    { title: 'Apple', id: 3 },
  ];

  return (
    <ul>
      {products.map(product => (
        <li key={product.id}>
          {product.title}
        </li>
      ))}
    </ul>
  );
}
```

---

---

## 6. Advanced Hooks

### useReducer - Complex State Management

When state updates depend on previous state or involve complex logic, `useReducer` is more maintainable than multiple `useState` calls.

```jsx
import { useReducer } from 'react';

// Reducer function: (currentState, action) => newState
function counterReducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    default:
      return state;
  }
}

function Counter() {
  // useReducer returns [state, dispatch]
  const [state, dispatch] = useReducer(counterReducer, { count: 0 });

  return (
    <div>
      <p>Count: {state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
}
```

**When to use useReducer:**
- Multiple related state values
- Next state depends on previous state
- Complex state update logic
- Want to separate state logic from component

---

### useContext - Share Data Without Prop Drilling

Context lets you pass data through the component tree without manually passing props at every level.

```jsx
import { createContext, useContext, useState } from 'react';

// 1. Create a context
const ThemeContext = createContext();

// 2. Provider component wraps the app
function App() {
  const [theme, setTheme] = useState('light');

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Toolbar />
    </ThemeContext.Provider>
  );
}

// 3. Consume context in any child component
function Toolbar() {
  return <div><ThemeButton /></div>;
}

function ThemeButton() {
  // Access context value without props
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button
      onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}
      style={{
        background: theme === 'light' ? '#fff' : '#333',
        color: theme === 'light' ? '#000' : '#fff'
      }}
    >
      Current theme: {theme}
    </button>
  );
}
```

**Context pattern for auth:**
```jsx
// contexts/AuthContext.jsx
import { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (userData) => setUser(userData);
  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// Custom hook for consuming auth context
export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}
```

**Context with LocalStorage Persistence:**

Persist context state across page reloads using localStorage.

```jsx
// contexts/ThemeContext.jsx
import { createContext, useContext, useState, useEffect } from 'react';

const ThemeContext = createContext();

export function ThemeProvider({ children }) {
  // Initialize theme from localStorage or default to 'light'
  const [isDarkMode, setIsDarkMode] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved === 'dark'; // Returns true if dark, false otherwise
  });

  // Persist theme to localStorage whenever it changes
  useEffect(() => {
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  }, [isDarkMode]);

  const toggleTheme = () => {
    setIsDarkMode(prev => !prev);
  };

  const value = {
    isDarkMode,
    toggleTheme,
    theme: isDarkMode ? 'dark' : 'light'
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

// Custom hook for consuming theme context
export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// Usage in components:
function App() {
  return (
    <ThemeProvider>
      <Header />
      <Content />
    </ThemeProvider>
  );
}

function Header() {
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <header style={{
      backgroundColor: isDarkMode ? '#333' : '#fff',
      color: isDarkMode ? '#fff' : '#000'
    }}>
      <button onClick={toggleTheme}>
        Toggle to {isDarkMode ? 'Light' : 'Dark'} Mode
      </button>
    </header>
  );
}
```

**Why This Pattern Works:**
- useState initializer runs only once on mount, reading from localStorage
- useEffect syncs to localStorage on every theme change
- Custom hook provides clean API and error checking
- Theme persists across browser sessions and page reloads

---

### useMemo - Memoize Expensive Calculations

`useMemo` caches the result of a calculation between re-renders, only recalculating when dependencies change.

```jsx
import { useState, useMemo } from 'react';

function ExpensiveComponent({ data }) {
  const [filterTerm, setFilterTerm] = useState('');

  // Without useMemo, this runs on every render
  // With useMemo, only runs when data or filterTerm change
  const filteredData = useMemo(() => {
    console.log('Filtering data...');
    return data.filter(item =>
      item.name.toLowerCase().includes(filterTerm.toLowerCase())
    );
  }, [data, filterTerm]); // Dependency array

  return (
    <div>
      <input
        value={filterTerm}
        onChange={(e) => setFilterTerm(e.target.value)}
        placeholder="Filter..."
      />
      <ul>
        {filteredData.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

**When to use useMemo:**
- Expensive calculations (sorting, filtering large arrays)
- Derived values that shouldn't trigger unnecessary re-renders
- Optimizing child component props

**Warning:** Don't overuse! Only use when profiling shows a performance issue.

---

### useCallback - Memoize Function References

`useCallback` returns a memoized version of a callback function, preventing unnecessary re-renders of child components.

```jsx
import { useState, useCallback } from 'react';

function ParentComponent() {
  const [count, setCount] = useState(0);
  const [other, setOther] = useState(0);

  // Without useCallback, this function is recreated on every render
  // With useCallback, same function reference is returned unless count changes
  const handleClick = useCallback(() => {
    console.log('Count is:', count);
  }, [count]); // Only recreate if count changes

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setOther(other + 1)}>Other: {other}</button>

      {/* ChildComponent won't re-render when 'other' changes */}
      <ChildComponent onClick={handleClick} />
    </div>
  );
}

// React.memo prevents re-renders when props haven't changed
const ChildComponent = React.memo(({ onClick }) => {
  console.log('ChildComponent rendered');
  return <button onClick={onClick}>Click me</button>;
});
```

**When to use useCallback:**
- Passing callbacks to optimized child components (wrapped in React.memo)
- Dependency in useEffect or useMemo
- Functions used in context values

---

## 7. Custom Hooks

Custom hooks let you extract component logic into reusable functions. Convention: name starts with "use".

### Example 1: useLocalStorage Hook

```jsx
import { useState, useEffect } from 'react';

// Custom hook for syncing state with localStorage
function useLocalStorage(key, initialValue) {
  // Get initial value from localStorage or use initialValue
  const [value, setValue] = useState(() => {
    const item = window.localStorage.getItem(key);
    return item ? JSON.parse(item) : initialValue;
  });

  // Update localStorage when value changes
  useEffect(() => {
    window.localStorage.setItem(key, JSON.stringify(value));
  }, [key, value]);

  return [value, setValue];
}

// Usage
function UserSettings() {
  const [name, setName] = useLocalStorage('username', '');
  const [theme, setTheme] = useLocalStorage('theme', 'light');

  return (
    <div>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Your name"
      />
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
    </div>
  );
}
```

### Example 2: useFetch Hook

```jsx
import { useState, useEffect } from 'react';

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true; // Prevent setting state after unmount

    setLoading(true);
    fetch(url)
      .then(res => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then(data => {
        if (isMounted) {
          setData(data);
          setLoading(false);
        }
      })
      .catch(error => {
        if (isMounted) {
          setError(error);
          setLoading(false);
        }
      });

    return () => {
      isMounted = false; // Cleanup
    };
  }, [url]);

  return { data, loading, error };
}

// Usage
function UserProfile({ userId }) {
  const { data, loading, error } = useFetch(`/api/users/${userId}`);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h2>{data.name}</h2>
      <p>{data.email}</p>
    </div>
  );
}
```

### Example 3: useToggle Hook

```jsx
import { useState, useCallback } from 'react';

function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  const toggle = useCallback(() => {
    setValue(v => !v);
  }, []);

  return [value, toggle];
}

// Usage
function Modal() {
  const [isOpen, toggleOpen] = useToggle(false);

  return (
    <div>
      <button onClick={toggleOpen}>Open Modal</button>
      {isOpen && (
        <div className="modal">
          <p>Modal Content</p>
          <button onClick={toggleOpen}>Close</button>
        </div>
      )}
    </div>
  );
}
```

---

## 8. Component Composition Patterns

### Render Props Pattern

Pass a function as a prop that returns JSX.

```jsx
// Generic mouse tracker
function MouseTracker({ render }) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (event) => {
    setPosition({ x: event.clientX, y: event.clientY });
  };

  return (
    <div onMouseMove={handleMouseMove} style={{ height: '100vh' }}>
      {render(position)}
    </div>
  );
}

// Usage - inject custom rendering
function App() {
  return (
    <MouseTracker render={({ x, y }) => (
      <h1>Mouse position: {x}, {y}</h1>
    )} />
  );
}
```

### Compound Components Pattern

Components that work together to form a complete UI.

```jsx
// Tabs component with compound pattern
function Tabs({ children }) {
  const [activeIndex, setActiveIndex] = useState(0);

  return (
    <div className="tabs">
      {React.Children.map(children, (child, index) =>
        React.cloneElement(child, {
          isActive: index === activeIndex,
          onClick: () => setActiveIndex(index)
        })
      )}
    </div>
  );
}

function Tab({ label, children, isActive, onClick }) {
  return (
    <div onClick={onClick} className={isActive ? 'active' : ''}>
      <div className="tab-header">{label}</div>
      {isActive && <div className="tab-content">{children}</div>}
    </div>
  );
}

// Usage
<Tabs>
  <Tab label="Profile">Profile content</Tab>
  <Tab label="Settings">Settings content</Tab>
  <Tab label="Notifications">Notifications content</Tab>
</Tabs>
```

---

## 9. Performance Optimization

### React.memo - Prevent Unnecessary Re-renders

```jsx
import { memo } from 'react';

// Without memo: re-renders every time parent re-renders
// With memo: only re-renders if props change
const ExpensiveComponent = memo(function ExpensiveComponent({ data }) {
  console.log('Rendering ExpensiveComponent');
  // Heavy rendering logic...
  return <div>{data.map(/* render items */)}</div>;
});

// Custom comparison function (optional)
const MemoizedComponent = memo(
  ({ user }) => <div>{user.name}</div>,
  (prevProps, nextProps) => prevProps.user.id === nextProps.user.id
);
```

### Lazy Loading Components

```jsx
import { lazy, Suspense } from 'react';

// Lazy load heavy components
const HeavyChart = lazy(() => import('./HeavyChart'));
const Dashboard = lazy(() => import('./Dashboard'));

function App() {
  return (
    <div>
      <h1>My App</h1>

      {/* Suspense shows fallback while component loads */}
      <Suspense fallback={<div>Loading chart...</div>}>
        <HeavyChart />
      </Suspense>

      <Suspense fallback={<div>Loading dashboard...</div>}>
        <Dashboard />
      </Suspense>
    </div>
  );
}
```

### Avoid Inline Functions and Objects

```jsx
// BAD: Creates new function on every render
function BadExample() {
  return <ChildComponent onClick={() => console.log('clicked')} />;
}

// GOOD: Function reference is stable
function GoodExample() {
  const handleClick = useCallback(() => {
    console.log('clicked');
  }, []);

  return <ChildComponent onClick={handleClick} />;
}

// BAD: Creates new object on every render
<ChildComponent style={{ color: 'red' }} />

// GOOD: Define outside component or use useMemo
const style = { color: 'red' };
<ChildComponent style={style} />
```

---

## 10. Error Boundaries

Error boundaries catch JavaScript errors in child components and display fallback UI.

```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    // Update state so next render shows fallback UI
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // Log error to error reporting service
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-fallback">
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button onClick={() => this.setState({ hasError: false })}>
            Try again
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <ErrorBoundary>
      <ComponentThatMightError />
    </ErrorBoundary>
  );
}
```

**Note:** Error boundaries don't catch:
- Errors in event handlers (use try-catch)
- Errors in async code (use .catch())
- Errors in the error boundary itself
- Server-side rendering errors

---

## 11. Common React Mistakes

### 1. Mutating State Directly

```jsx
// WRONG: Mutating state array
const [items, setItems] = useState([1, 2, 3]);
items.push(4); // DON'T DO THIS!
setItems(items);

// CORRECT: Create new array
setItems([...items, 4]); // or items.concat(4)
```

### 2. Stale Closure in useEffect

```jsx
// WRONG: count is stale (always 0)
useEffect(() => {
  const interval = setInterval(() => {
    setCount(count + 1); // count is captured as 0
  }, 1000);
  return () => clearInterval(interval);
}, []); // Empty deps - count never updates!

// CORRECT: Use functional update
useEffect(() => {
  const interval = setInterval(() => {
    setCount(c => c + 1); // Gets current count
  }, 1000);
  return () => clearInterval(interval);
}, []);
```

### 3. Missing Keys in Lists

```jsx
// WRONG: Using index as key
{items.map((item, index) => (
  <div key={index}>{item.name}</div>
))}

// CORRECT: Use stable unique identifier
{items.map(item => (
  <div key={item.id}>{item.name}</div>
))}
```

### 4. Not Cleaning Up Effects

```jsx
// WRONG: Memory leak - no cleanup
useEffect(() => {
  const subscription = props.source.subscribe();
}, [props.source]);

// CORRECT: Return cleanup function
useEffect(() => {
  const subscription = props.source.subscribe();
  return () => subscription.unsubscribe();
}, [props.source]);
```

### 5. Conditional Hooks

```jsx
// WRONG: Hooks must be called unconditionally
if (condition) {
  useEffect(() => { /* ... */ });
}

// CORRECT: Condition inside hook
useEffect(() => {
  if (condition) {
    // Do something
  }
}, [condition]);
```

### 6. Forgetting Dependency Arrays

```jsx
// WRONG: Runs on every render
useEffect(() => {
  fetchData();
}); // No dependency array!

// CORRECT: Specify dependencies
useEffect(() => {
  fetchData();
}, [someValue]); // Or [] for run-once
```

---

## 12. Best Practices Summary

### State Management
- Keep state as close to where it's used as possible
- Lift state up only when necessary
- Use Context for truly global state (theme, auth, locale)
- Consider useReducer for complex state logic
- Never mutate state directly

### Performance
- Don't optimize prematurely - measure first
- Use React DevTools Profiler to find bottlenecks
- Memoize expensive calculations with useMemo
- Memoize callbacks passed to children with useCallback
- Wrap pure components in React.memo
- Code-split with lazy() and Suspense

### Component Design
- Keep components small and focused
- Extract reusable logic into custom hooks
- Prefer composition over prop drilling
- Use TypeScript for type safety
- Write components that are easy to test

### Effects
- Always include cleanup functions when needed
- List all dependencies in dependency array
- Use functional updates for state that depends on previous state
- Consider separating effects that do different things

---

## See Also

- [JavaScript Functions Guide](JavaScript_Functions_Guide.md) - Arrow functions and closures essential for React
- [JavaScript Objects/Arrays](../cheatsheets/JavaScript_Objects_Arrays_Cheat_Sheet.md) - Destructuring and map/filter methods
- [JavaScript Async Programming Guide](JavaScript_Async_Programming_Guide.md) - Async/await patterns for useEffect and data fetching
- [JavaScript LocalStorage Guide](JavaScript_LocalStorage_Guide.md) - Persisting React state with localStorage
- [React Router Guide](React_Router_Guide.md) - Navigation and routing in React applications
- [Modern React Ecommerce Guide](Modern_React_Ecommerce_Guide.md) - Advanced patterns with shopping cart and checkout flow
- [Modern Fullstack Guide](Modern_Fullstack_Guide.md) - Next.js and fullstack patterns