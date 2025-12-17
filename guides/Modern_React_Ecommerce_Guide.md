# Modern React E-Commerce Architecture

This guide documents the architectural patterns used in the "Ecommerce" project. It features a modern frontend stack using **Vite**, **TypeScript**, **Firebase Authentication**, and **TanStack Query**.

## Table of Contents
1.  [Tech Stack & Dependencies](#tech-stack--dependencies)
2.  [Project Structure](#project-structure)
3.  [State Management (Context + Reducer)](#state-management-context--reducer)
4.  [Data Fetching (TanStack Query)](#data-fetching-tanstack-query)
5.  [Authentication (Firebase)](#authentication-firebase)
6.  [CI/CD Workflow](#cicd-workflow)

---

## Tech Stack & Dependencies

*   **Build Tool:** Vite (`npm create vite@latest`)
*   **Language:** TypeScript
*   **Routing:** React Router DOM v6+
*   **State:** React Context API + `useReducer`
*   **Server State:** TanStack Query (`@tanstack/react-query`)
*   **Auth:** Firebase v9+ (Modular SDK)
*   **HTTP Client:** Axios
*   **Testing:** Jest, React Testing Library

---

## Project Structure

```
src/
├── api/                # Axios instances and API calls
├── components/         # Reusable UI components (ProductCard, Navbar)
├── context/            # Global state (Auth, Products)
├── lib/                # Third-party config (Firebase)
├── pages/              # Route views (Home, Login, Profile)
├── types/              # TypeScript interfaces
└── main.tsx            # Entry point
```

---

## State Management (Context + Reducer)

The project uses the **Context API** combined with `useReducer` for complex state logic (like managing a product list with filters).

### Type Definitions (`types.ts`)
```typescript
export interface Product {
  id: number;
  title: string;
  price: number;
  category: string;
  image: string;
}

export interface ProductState {
  products: Product[];
  selectedCategory: string;
}
```

### The Provider Pattern (`context/ProductContext.tsx`)
```typescript
// 1. Define Actions
type ProductAction =
  | { type: 'SET_PRODUCTS'; payload: Product[] }
  | { type: 'SET_SELECTED_CATEGORY'; payload: string };

// 2. Create Reducer
const productReducer = (state: ProductState, action: ProductAction): ProductState => {
  switch (action.type) {
    case 'SET_PRODUCTS':
      return { ...state, products: action.payload };
    case 'SET_SELECTED_CATEGORY':
      return { ...state, selectedCategory: action.payload };
    default:
      throw new Error(`Unhandled action type`);
  }
};

// 3. Create Provider & Custom Hook
export const ProductProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(productReducer, initialState);

  return (
    <ProductContext.Provider value={{ ...state, dispatch }}>
      {children}
    </ProductContext.Provider>
  );
};

export const useProductContext = () => {
    const context = useContext(ProductContext);
    if (!context) throw new Error("Must be used within ProductProvider");
    return context;
}
```

---

## Data Fetching (TanStack Query)

Instead of `useEffect` fetching, the project uses **TanStack Query** for caching, loading states, and error handling.

### API Layer (`api/api.ts`)
```typescript
import axios from "axios";
const apiClient = axios.create({ baseURL: 'https://fakestoreapi.com' });

export const fetchProducts = () => apiClient.get<Product[]>('/products');
```

### Usage in Components (`pages/Home.tsx`)
```typescript
const { data, isLoading, isError } = useQuery({
  queryKey: ['products'],
  queryFn: fetchProducts,
});

// Automatic loading/error handling
if (isLoading) return <h1>Loading...</h1>;
if (isError) return <h2>Error loading products</h2>;
```

---

## Authentication (Firebase)

Authentication is handled via a dedicated `AuthenticationContext` that listens to Firebase's `onAuthStateChanged`.

### Setup (`lib/firebase/firebase.ts`)
```typescript
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = { /* ... */ };
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
```

### Auth Context Logic
```typescript
useEffect(() => {
  const unsubscribe = onAuthStateChanged(auth, (user) => {
    setUser(user ? user : null);
  });
  return () => unsubscribe(); // Cleanup subscription on unmount
}, []);
```

---

## CI/CD Workflow

The project includes a GitHub Actions workflow (`.github/workflows/ci-cd.yml`) for automated testing and deployment.

**Triggers:** Push or Pull Request to `main`.

**Jobs:**
1.  **Build:**
    *   Checkout code
    *   Install dependencies (`npm install`)
    *   Run tests (`npm test`)
    *   Build app (`npm run build`)
2.  **Deploy:**
    *   Runs only if Build succeeds.
    *   Deploys to Vercel using the Vercel CLI.
