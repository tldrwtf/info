# Modern Fullstack Guide: Next.js & Firebase Auth

This guide covers building modern full-stack applications using **Next.js** (Frontend/API Routes) and **Firebase** (Authentication/Firestore).

## 1. Firebase Setup

### Initialization (`utils/firebase.js`)
Initialize the Firebase SDK using environment variables.

```javascript
import firebase from "firebase/app";
import "firebase/auth";

const firebaseCredentials = {
  apiKey: process.env.NEXT_PUBLIC_FIREBASE_API_KEY,
  authDomain: process.env.NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN,
  projectId: process.env.NEXT_PUBLIC_FIREBASE_PROJECT_ID,
  storageBucket: process.env.NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.NEXT_PUBLIC_FIREBASE_APP_ID,
};

// Prevent multiple initializations during hot-reloads
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseCredentials);
}
  
export default firebase;
```

---

## 2. The Authentication Hook

Create a custom React hook to manage the Firebase auth state and provide utility functions.

### `utils/useFirebaseAuth.jsx`
```javascript
import { useState, useEffect } from "react";
import firebase from "./firebase";

export default function useFirebaseAuth() {
  const [authUser, setAuthUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Observer for auth state changes
  const authStateChanged = async (authState) => {
    if (!authState) {
      setAuthUser(null);
      setLoading(false);
      return;
    }

    setAuthUser({
      uid: authState.uid,
      email: authState.email,
    });
    setLoading(false);
  };

  const signInWithEmailAndPassword = (email, password) =>
    firebase.auth().signInWithEmailAndPassword(email, password);

  const createUserWithEmailAndPassword = (email, password) =>
    firebase.auth().createUserWithEmailAndPassword(email, password);

  const signOut = () => firebase.auth().signOut();

  useEffect(() => {
    const unsubscribe = firebase.auth().onAuthStateChanged(authStateChanged);
    return () => unsubscribe();
  }, []);

  return {
    authUser,
    loading,
    signInWithEmailAndPassword,
    createUserWithEmailAndPassword,
    signOut,
  };
}
```

---

## 3. Auth Context API

To make the user state accessible throughout the entire app without "prop drilling," use the React Context API.

### `contexts/AuthUserContext.jsx`
```javascript
import { createContext, useContext } from "react";
import useFirebaseAuth from "../utils/useFirebaseAuth";

const authUserContext = createContext({
  authUser: null,
  loading: true,
  signInWithEmailAndPassword: async () => {},
  createUserWithEmailAndPassword: async () => {},
  signOut: async () => {},
});

export function AuthUserProvider({ children }) {
  const auth = useFirebaseAuth();
  return (
    <authUserContext.Provider value={auth}>
      {children}
    </authUserContext.Provider>
  );
}

// Custom hook for consuming the context
export const useAuth = () => useContext(authUserContext);
```

### Wrapping the App (`pages/_app.js`)
```javascript
import { AuthUserProvider } from "../contexts/AuthUserContext";

function MyApp({ Component, pageProps }) {
  return (
    <AuthUserProvider>
      <Component {...pageProps} />
    </AuthUserProvider>
  );
}

export default MyApp;
```

---

## 4. Protected Routes

Use the `useAuth` hook to redirect unauthorized users.

```javascript
import { useEffect } from "react";
import { useRouter } from "next/router";
import { useAuth } from "../contexts/AuthUserContext";

const Dashboard = () => {
  const { authUser, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!loading && !authUser) {
      router.push("/login");
    }
  }, [authUser, loading]);

  if (loading) return <div>Loading...</div>;

  return <h1>Welcome back, {authUser.email}</h1>;
};
```

---

## See Also
- **[React Basics Guide](React_Basics_Guide.md)** - Understanding Hooks and Context.
- **[CI/CD Pipeline Guide](CI_CD_Pipeline_Guide.md)** - Deploying Next.js to platforms like Vercel.
