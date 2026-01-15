# React Context API & State Management Guide

**Version:** 1.0.0
**Last Updated:** 2026-01-15

---

## Table of Contents

1. [Introduction to Context API](#introduction-to-context-api)
2. [When to Use Context vs Props](#when-to-use-context-vs-props)
3. [Creating a Context](#creating-a-context)
4. [Provider Pattern](#provider-pattern)
5. [Consuming Context](#consuming-context)
6. [Custom Context Hooks](#custom-context-hooks)
7. [Multiple Contexts](#multiple-contexts)
8. [Context with LocalStorage](#context-with-localstorage)
9. [Best Practices & Pitfalls](#best-practices--pitfalls)

---

## Introduction to Context API

The **Context API** is React's built-in solution for sharing state across components without passing props through every level of the component tree. It solves the problem of **prop drilling** - the tedious practice of passing props down through multiple component layers.

### The Prop Drilling Problem

```javascript
// BAD: Prop drilling through multiple levels
function App() {
  const [theme, setTheme] = useState('light');

  return <Header theme={theme} setTheme={setTheme} />;
}

function Header({ theme, setTheme }) {
  return <Navigation theme={theme} setTheme={setTheme} />;
}

function Navigation({ theme, setTheme }) {
  return <ThemeButton theme={theme} setTheme={setTheme} />;
}

function ThemeButton({ theme, setTheme }) {
  return <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
    Toggle Theme
  </button>;
}
```

### The Context Solution

```javascript
// GOOD: Context eliminates prop drilling
function App() {
  return (
    <ThemeProvider>
      <Header />
    </ThemeProvider>
  );
}

function Header() {
  return <Navigation />;
}

function Navigation() {
  return <ThemeButton />;
}

function ThemeButton() {
  const { theme, toggleTheme } = useTheme(); // Direct access!
  return <button onClick={toggleTheme}>Toggle Theme</button>;
}
```

---

## When to Use Context vs Props

### Use Props When:
- Data is only needed by 1-2 child components
- The component hierarchy is shallow
- You want explicit data flow that's easy to trace
- The data changes frequently and affects only specific components

### Use Context When:
- **Global state** needed across many components (theme, auth, language)
- **Deep component trees** where passing props becomes tedious
- **Shared functionality** like modals, tooltips, or notifications
- **Configuration** that rarely changes but is widely needed

### Decision Tree

```
Do you need to share data across multiple components?
├─ No → Use Props
└─ Yes
    └─ Is the data needed by deeply nested components?
        ├─ No → Use Props
        └─ Yes
            └─ Does the data change frequently?
                ├─ Yes → Consider useReducer + Context or state management library
                └─ No → Use Context API
```

---

## Creating a Context

### Basic Context Creation

```javascript
import { createContext } from 'react';

// Create context with default value (optional)
const ThemeContext = createContext();

export default ThemeContext;
```

### Context with Default Values

```javascript
const ThemeContext = createContext({
  isDarkMode: false,
  toggleTheme: () => {} // Placeholder function
});
```

**Why provide defaults?** Default values are used when a component consumes the context **outside** of a Provider. They serve as fallbacks and documentation.

---

## Provider Pattern

The Provider component wraps your app (or part of it) and makes the context value available to all child components.

### Complete ThemeContext Implementation

```javascript
import React, { createContext, useContext, useState, useEffect } from "react";

// Create the context
const ThemeContext = createContext();

// Create custom hook to consume context
export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// Create context provider
export const ThemeProvider = ({ children }) => {
  // Initialize dark/light toggle with LocalStorage persistence
  const [isDarkMode, setIsDarkMode] = useState(() => {
    const saved = localStorage.getItem("theme");
    return saved === 'dark'; // Returns true or false
  });

  // Save theme to LocalStorage whenever it changes
  useEffect(() => {
    localStorage.setItem("theme", isDarkMode ? 'dark' : "light");
  }, [isDarkMode]);

  // Function to toggle theme
  const toggleTheme = () => {
    setIsDarkMode(prev => !prev);
  };

  // Value object contains data available across app
  const value = {
    isDarkMode,
    toggleTheme
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}
```

### Key Components of the Provider Pattern

1. **State Management**: `useState` holds the context state
2. **Side Effects**: `useEffect` for persistence (LocalStorage sync)
3. **Value Object**: Contains all data and functions to share
4. **Provider Component**: Wraps children and provides value
5. **Props.children**: Enables wrapping any component tree

---

## Consuming Context

### Using the useContext Hook

Once you've created a Provider, any child component can access the context using `useContext`.

#### In App.jsx (Root Component)

```javascript
import { useTheme } from "./contexts/ThemeContext";

function App() {
  const { isDarkMode } = useTheme();

  return (
    <div style={{
      height: '100vh',
      backgroundColor: isDarkMode ? "#1f2c38ff" : "#ecf0f1"
    }}>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
```

#### In Navbar Component (Consumer)

```javascript
import { Link, NavLink } from "react-router-dom";
import { useTheme } from "../../contexts/ThemeContext";

const Navbar = () => {
  const { isDarkMode, toggleTheme } = useTheme();

  return (
    <header className={isDarkMode ? 'mainDark' : 'mainLight'}>
      <h1>My Cool App</h1>
      <nav>
        <NavLink className={isDarkMode ? 'navLinkDark' : 'navLinkLight'} to="/">
          HOME
        </NavLink>
        <NavLink className={isDarkMode ? 'navLinkDark' : 'navLinkLight'} to="/login">
          LOGIN
        </NavLink>
        <NavLink className={isDarkMode ? 'navLinkDark' : 'navLinkLight'} to="/profile">
          PROFILE
        </NavLink>
        <Link
          className={isDarkMode ? 'navLinkDark' : 'navLinkLight'}
          onClick={toggleTheme}
        >
          {isDarkMode ? "Light Mode" : "Dark Mode"}
        </Link>
      </nav>
    </header>
  );
}
```

### Consumer Component Patterns

**Pattern 1: Destructure exactly what you need**
```javascript
const { isDarkMode } = useTheme(); // Only need the state
```

**Pattern 2: Access multiple values**
```javascript
const { isDarkMode, toggleTheme } = useTheme(); // Need state + function
```

**Pattern 3: Use entire context object**
```javascript
const theme = useTheme(); // Access as theme.isDarkMode, theme.toggleTheme
```

---

## Custom Context Hooks

Custom hooks provide a clean API for consuming context and enable error handling.

### Creating useTheme() Hook

```javascript
export const useTheme = () => {
  const context = useContext(ThemeContext);

  // Error handling: Ensure component is wrapped in Provider
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }

  return context;
}
```

### Benefits of Custom Hooks

1. **Error Prevention**: Catches missing Provider at runtime
2. **Cleaner Imports**: `useTheme()` instead of `useContext(ThemeContext)`
3. **Type Safety**: Better TypeScript support
4. **Encapsulation**: Hides implementation details

### Advanced Custom Hook with Derived State

```javascript
export const useTheme = () => {
  const context = useContext(ThemeContext);

  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }

  // Add derived values
  return {
    ...context,
    themeClass: context.isDarkMode ? 'dark' : 'light',
    backgroundColor: context.isDarkMode ? '#1f2c38ff' : '#ecf0f1'
  };
}
```

---

## Multiple Contexts

Real applications often need multiple contexts (theme, auth, language, etc.). Here's how to compose them.

### Multiple Context Providers

```javascript
import { ThemeProvider } from './contexts/ThemeContext';
import { AuthProvider } from './contexts/AuthContext';
import { LanguageProvider } from './contexts/LanguageContext';

function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <LanguageProvider>
          <MainApp />
        </LanguageProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}
```

### Cleaner Approach: Compose Providers

```javascript
// contexts/AppProviders.jsx
export const AppProviders = ({ children }) => {
  return (
    <ThemeProvider>
      <AuthProvider>
        <LanguageProvider>
          {children}
        </LanguageProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}

// main.jsx
import { AppProviders } from './contexts/AppProviders';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <AppProviders>
      <App />
    </AppProviders>
  </StrictMode>
);
```

### Using Multiple Contexts in a Component

```javascript
function UserProfile() {
  const { isDarkMode } = useTheme();
  const { user, logout } = useAuth();
  const { translate } = useLanguage();

  return (
    <div className={isDarkMode ? 'profile-dark' : 'profile-light'}>
      <h1>{translate('welcome')}, {user.name}</h1>
      <button onClick={logout}>{translate('logout')}</button>
    </div>
  );
}
```

---

## Context with LocalStorage

Persist context state across browser sessions by integrating LocalStorage.

### Pattern: Load from LocalStorage on Mount

```javascript
const [isDarkMode, setIsDarkMode] = useState(() => {
  const saved = localStorage.getItem("theme");
  return saved === 'dark';
});
```

**Why use function initializer?** The function only runs once on mount, preventing unnecessary LocalStorage reads on every render.

### Pattern: Save to LocalStorage on Change

```javascript
useEffect(() => {
  localStorage.setItem("theme", isDarkMode ? 'dark' : "light");
}, [isDarkMode]);
```

### Complete User Preferences Context with LocalStorage

```javascript
const UserPreferencesProvider = ({ children }) => {
  const [preferences, setPreferences] = useState(() => {
    const saved = localStorage.getItem("userPreferences");
    return saved ? JSON.parse(saved) : {
      theme: 'light',
      language: 'en',
      fontSize: '16px',
      notifications: true
    };
  });

  useEffect(() => {
    localStorage.setItem("userPreferences", JSON.stringify(preferences));
  }, [preferences]);

  const updatePreference = (key, value) => {
    setPreferences(prev => ({
      ...prev,
      [key]: value
    }));
  };

  return (
    <UserPreferencesContext.Provider value={{ preferences, updatePreference }}>
      {children}
    </UserPreferencesContext.Provider>
  );
}
```

---

## Best Practices & Pitfalls

### Best Practices

1. **Create custom hooks for context consumption**
   ```javascript
   export const useAuth = () => useContext(AuthContext);
   ```

2. **Include error handling in custom hooks**
   ```javascript
   if (!context) throw new Error('Must be used within Provider');
   ```

3. **Keep context values stable with useMemo/useCallback**
   ```javascript
   const value = useMemo(() => ({ user, login, logout }), [user]);
   ```

4. **Split contexts by concern** (separate theme, auth, data)

5. **Place Providers as high as needed, but no higher**

6. **Document your context API**
   ```javascript
   /**
    * Theme context providing dark/light mode toggle
    * @returns {{ isDarkMode: boolean, toggleTheme: () => void }}
    */
   export const useTheme = () => { ... }
   ```

### Common Pitfalls

1. **Unnecessary Re-renders**
   ```javascript
   // BAD: New object created on every render
   <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>

   // GOOD: Memoize the value
   const value = useMemo(() => ({ isDarkMode, toggleTheme }), [isDarkMode]);
   <ThemeContext.Provider value={value}>
   ```

2. **Using Context for Everything**
   - Props are fine for 1-2 levels deep
   - Context adds complexity - use it when needed

3. **Forgetting the Provider**
   ```javascript
   // This will use default context values or throw error
   function App() {
     return <ComponentUsingContext />; // Missing Provider!
   }
   ```

4. **Over-splitting Contexts**
   - Don't create separate context for every single piece of state
   - Group related state together (e.g., user profile data)

5. **Not Handling Missing Provider**
   ```javascript
   // BAD: Silent failure
   export const useTheme = () => useContext(ThemeContext);

   // GOOD: Clear error message
   export const useTheme = () => {
     const context = useContext(ThemeContext);
     if (!context) throw new Error('useTheme requires ThemeProvider');
     return context;
   };
   ```

### When NOT to Use Context

- **Frequently changing data** → Consider useReducer + Context or state management library (Redux, Zustand)
- **Performance-critical updates** → Context causes re-renders in all consumers
- **Simple parent-child communication** → Just use props
- **Server state** → Use React Query, SWR, or similar

---

## Summary

The React Context API is a powerful tool for sharing state across your component tree without prop drilling. Key takeaways:

- **Create context** with `createContext()`
- **Provide values** with `<Context.Provider value={...}>`
- **Consume context** with `useContext(Context)` or custom hooks
- **Combine with LocalStorage** for state persistence
- **Avoid over-use** - props are often simpler
- **Optimize** with useMemo to prevent unnecessary re-renders

**Next Steps:**
- Explore the [React State Guide](./React_Basics_Guide.md) for more state management patterns
- Learn about [React Router](./React_Router_Navigation_Guide.md) for navigation (Context works great with routing!)
- Check the [React useEffect Guide](./React_Basics_Guide.md#useEffect) for side effects

---

**See Also:**
- [React Official Context Docs](https://react.dev/learn/passing-data-deeply-with-context)
- [React State Management Guide](./React_Basics_Guide.md)
- [LocalStorage Guide](./JavaScript_LocalStorage_Guide.md)
