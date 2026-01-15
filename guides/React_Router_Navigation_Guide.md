# React Router Navigation Guide

---

## Table of Contents

1. [Introduction to React Router](#introduction-to-react-router)
2. [Installation & Setup](#installation--setup)
3. [Basic Routing](#basic-routing)
4. [Navigation Components](#navigation-components)
5. [Dynamic Routing](#dynamic-routing)
6. [Programmatic Navigation](#programmatic-navigation)
7. [Route Protection](#route-protection)
8. [Best Practices](#best-practices)

---

## Introduction to React Router

**React Router** is the standard routing library for React applications. It enables navigation between different views/components in a Single Page Application (SPA) without full page reloads.

### Key Concepts

- **SPA (Single Page Application)**: All routing happens client-side
- **No page reloads**: Navigation is instant and preserves application state
- **URL synchronization**: Browser URL stays in sync with the current view
- **History management**: Back/forward browser buttons work correctly

### React Router vs Anchor Tags

```javascript
// BAD: Anchor tag causes full page reload
<a href="/about">About</a>  // Loses application state

// GOOD: React Router Link (no reload)
<Link to="/about">About</Link>  // Instant navigation
```

---

## Installation & Setup

### Install React Router

```bash
npm install react-router-dom
```

### Basic Setup Structure

```
src/
├── App.jsx          # Router configuration
├── pages/
│   ├── Home.jsx
│   ├── About.jsx
│   ├── ContactMe.jsx
│   └── Posts.jsx
└── components/
    └── Navbar/
        ├── Navbar.jsx
        └── Navbar.css
```

---

## Basic Routing

### Setting Up BrowserRouter

**App.jsx** - Main router configuration:

```javascript
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import ContactMe from "./pages/ContactMe";
import Posts from "./pages/Posts";
import Navbar from "./components/Navbar/Navbar";

// SPA - Single Page Application
function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact-me" element={<ContactMe />} />
        <Route path="/posts" element={<Posts />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
```

### Key Components

1. **`<BrowserRouter>`** - Wraps your entire app, enables routing
2. **`<Routes>`** - Container for all Route components
3. **`<Route>`** - Defines a route with path and element to render

### Route Patterns

```javascript
<Route path="/" element={<Home />} />           // Exact match: /
<Route path="/about" element={<About />} />     // Matches: /about
<Route path="/contact-me" element={<ContactMe />} />  // Matches: /contact-me
<Route path="/posts/:id" element={<Post />} />  // Dynamic route with parameter
<Route path="*" element={<NotFound />} />       // Catch-all for 404
```

---

## Navigation Components

### Link Component

Basic navigation without page reload:

```javascript
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <Link to="/">
        <h1>Allan</h1>
      </Link>
      <ul>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/contact-me">Contact</Link>
      </ul>
    </nav>
  );
}
```

### NavLink Component

`NavLink` is like `Link` but knows when it's active:

```javascript
import { NavLink } from "react-router-dom";

const Navbar = () => {
  return (
    <nav>
      <ul>
        <NavLink
          to="/"
          className={({ isActive }) => isActive ? 'isActive' : 'navLink'}
        >
          HOME
        </NavLink>
        <NavLink
          to="/contact-me"
          className={({ isActive }) => isActive ? 'isActive' : 'navLink'}
        >
          CONTACT
        </NavLink>
        <NavLink
          to="/about"
          className={({ isActive }) => isActive ? 'isActive' : 'navLink'}
        >
          ABOUT
        </NavLink>
        <NavLink
          to="/posts"
          className={({ isActive }) => isActive ? 'isActive' : 'navLink'}
        >
          POSTS
        </NavLink>
      </ul>
    </nav>
  );
}
```

### NavLink Styling Patterns

**CSS (Navbar.css):**

```css
.navLink {
  text-decoration: none;
  color: black;
  font-size: 20px;
  padding: 10px;
}

.isActive {
  text-decoration: underline;
  color: rgb(7, 7, 111);
  font-size: 25px;
}
```

### Link vs NavLink

| Feature | Link | NavLink |
|---------|------|---------|
| **Navigation** | Yes | Yes |
| **Prevents reload** | Yes | Yes |
| **Active state** | No | Yes (`isActive` prop) |
| **Use case** | General links | Navigation menus |

---

## Dynamic Routing

Dynamic routes use URL parameters to determine what content to display.

### Defining Dynamic Routes

```javascript
// In App.jsx
<Routes>
  <Route path="/posts" element={<Posts />} />
  <Route path="/post/:id" element={<Post />} />  {/* :id is a parameter */}
</Routes>
```

### Accessing URL Parameters with useParams

**Post.jsx** - Component using dynamic route parameter:

```javascript
import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import PostCard from "../components/PostCard";

const Post = () => {
  const { id } = useParams();  // Extract :id from URL
  const [comments, setComments] = useState([]);

  useEffect(() => {
    const getComments = async () => {
      // Use id in API call
      const response = await fetch(
        `https://jsonplaceholder.typicode.com/posts/${id}/comments`
      );
      const data = await response.json();
      setComments(data);
    };
    getComments();
  }, [id]);  // Re-fetch when id changes

  return (
    <>
      <h1>Post {id}</h1>
      {comments.map(comment => (
        <PostCard
          key={comment.id}
          id={comment.id}
          title={comment.name}
          body={comment.body}
        />
      ))}
    </>
  );
}

export default Post;
```

### Linking to Dynamic Routes

```javascript
// In Posts.jsx
import { Link } from "react-router-dom";

const Posts = () => {
  const posts = [1, 2, 3, 4, 5];

  return (
    <div>
      <h1>All Posts</h1>
      {posts.map(postId => (
        <Link key={postId} to={`/post/${postId}`}>
          View Post {postId}
        </Link>
      ))}
    </div>
  );
}
```

### Multiple URL Parameters

```javascript
// Route definition
<Route path="/users/:userId/posts/:postId" element={<UserPost />} />

// Accessing parameters
const UserPost = () => {
  const { userId, postId } = useParams();

  return (
    <div>
      <h1>User {userId} - Post {postId}</h1>
    </div>
  );
}

// Navigation
<Link to={`/users/${user.id}/posts/${post.id}`}>View Post</Link>
```

---

## Programmatic Navigation

Sometimes you need to navigate programmatically (e.g., after form submission, on button click).

### useNavigate Hook

```javascript
import { useNavigate } from "react-router-dom";

const LoginForm = () => {
  const navigate = useNavigate();

  const handleLogin = async (credentials) => {
    const response = await loginUser(credentials);

    if (response.success) {
      // Navigate to dashboard after successful login
      navigate('/dashboard');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      {/* form fields */}
    </form>
  );
}
```

### Navigation Options

```javascript
const navigate = useNavigate();

// Navigate forward
navigate('/about');

// Navigate with state
navigate('/profile', { state: { from: 'login' } });

// Navigate back
navigate(-1);  // Go back one page

// Navigate forward
navigate(1);   // Go forward one page

// Replace current entry (no back button to this page)
navigate('/login', { replace: true });
```

### Conditional Navigation

```javascript
const ProductPage = () => {
  const navigate = useNavigate();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetchProduct().then(data => {
      if (!data) {
        // Product not found, redirect to 404
        navigate('/not-found');
      } else {
        setProduct(data);
      }
    });
  }, [navigate]);

  return product ? <ProductDetails product={product} /> : <Loading />;
}
```

---

## Route Protection

Protect routes that require authentication.

### Protected Route Component

```javascript
import { Navigate } from "react-router-dom";

const ProtectedRoute = ({ children, isAuthenticated }) => {
  if (!isAuthenticated) {
    // Redirect to login if not authenticated
    return <Navigate to="/login" replace />;
  }

  return children;
}

export default ProtectedRoute;
```

### Using Protected Routes

```javascript
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProtectedRoute from "./components/ProtectedRoute";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login setAuth={setIsAuthenticated} />} />

        {/* Protected routes */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/profile"
          element={
            <ProtectedRoute isAuthenticated={isAuthenticated}>
              <Profile />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
```

### Role-Based Protection

```javascript
const ProtectedRoute = ({ children, isAuthenticated, requiredRole, userRole }) => {
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  if (requiredRole && userRole !== requiredRole) {
    return <Navigate to="/unauthorized" replace />;
  }

  return children;
}

// Usage
<Route
  path="/admin"
  element={
    <ProtectedRoute
      isAuthenticated={isAuthenticated}
      requiredRole="admin"
      userRole={currentUser.role}
    >
      <AdminPanel />
    </ProtectedRoute>
  }
/>
```

---

## Best Practices

### 1. Organize Routes by Feature

```javascript
// routes/index.jsx
export const publicRoutes = [
  { path: "/", element: <Home /> },
  { path: "/about", element: <About /> },
];

export const protectedRoutes = [
  { path: "/dashboard", element: <Dashboard /> },
  { path: "/profile", element: <Profile /> },
];

// App.jsx
import { publicRoutes, protectedRoutes } from "./routes";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {publicRoutes.map(route => (
          <Route key={route.path} path={route.path} element={route.element} />
        ))}
        {protectedRoutes.map(route => (
          <Route
            key={route.path}
            path={route.path}
            element={<ProtectedRoute>{route.element}</ProtectedRoute>}
          />
        ))}
      </Routes>
    </BrowserRouter>
  );
}
```

### 2. Use Nested Routes for Layout

```javascript
<Routes>
  <Route path="/" element={<Layout />}>
    <Route index element={<Home />} />
    <Route path="about" element={<About />} />
    <Route path="contact" element={<Contact />} />
  </Route>
</Routes>

// Layout.jsx
import { Outlet } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <Navbar />
      <main>
        <Outlet />  {/* Renders child route */}
      </main>
      <Footer />
    </>
  );
}
```

### 3. Lazy Load Routes for Performance

```javascript
import { lazy, Suspense } from "react";

const Dashboard = lazy(() => import("./pages/Dashboard"));
const Profile = lazy(() => import("./pages/Profile"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<Loading />}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

### 4. Handle 404 Pages

```javascript
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  {/* Catch-all route for 404 */}
  <Route path="*" element={<NotFound />} />
</Routes>
```

### 5. Use Relative Paths

```javascript
// Instead of absolute paths
<Link to="/products/electronics/phones">Phones</Link>

// Use relative paths when nested
<Link to="phones">Phones</Link>  // Relative to current route
<Link to="../tablets">Tablets</Link>  // Up one level
```

---

## Navigation Cheat Sheet

### Ways to Navigate in React Router

| Method | Use Case | Example |
|--------|----------|---------|
| **Link** | Simple navigation | `<Link to="/about">About</Link>` |
| **NavLink** | Navigation with active state | `<NavLink to="/about">About</NavLink>` |
| **useNavigate** | Programmatic navigation | `navigate('/dashboard')` |
| **Navigate** | Declarative redirects | `<Navigate to="/login" />` |

### Common Patterns

```javascript
// Link to a page
<Link to="/about">About</Link>

// Link with active styling
<NavLink
  to="/about"
  className={({ isActive }) => isActive ? 'active' : ''}
>
  About
</NavLink>

// Navigate on button click
const handleClick = () => navigate('/profile');

// Navigate with URL parameter
<Link to={`/post/${post.id}`}>View Post</Link>

// Access URL parameter
const { id } = useParams();

// Navigate back
navigate(-1);

// Redirect component
if (!isAuthenticated) return <Navigate to="/login" />;
```

---

## Summary

React Router enables powerful navigation in SPAs:

- **`<BrowserRouter>`** - Wraps app to enable routing
- **`<Routes>` & `<Route>`** - Define route configuration
- **`<Link>` & `<NavLink>`** - Create navigation links
- **`useParams()`** - Access dynamic route parameters
- **`useNavigate()`** - Programmatic navigation
- **Protected Routes** - Control access to routes

**Next Steps:**
- Combine with [React Context](./React_Context_State_Management_Guide.md) for global auth state
- Learn [React State Management](./React_Basics_Guide.md) for complex applications
- Explore [React useEffect](./React_Basics_Guide.md#useeffect) for data fetching in routes

---

**See Also:**
- [React Router Official Docs](https://reactrouter.com/)
- [React Context Guide](./React_Context_State_Management_Guide.md)
- [React State Guide](./React_Basics_Guide.md)
