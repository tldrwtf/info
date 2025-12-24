import { useState } from 'react'
import Counter from './components/Counter'
import UserList from './components/UserList'

/**
 * Main App Component
 * Demonstrates basic composition and state lifting concepts.
 */
function App() {
  return (
    <div className="container">
      <header>
        <h1>React Starter Hub</h1>
        <p>A reference implementation for the React Basics Guide.</p>
      </header>

      <main>
        <section>
          <h2>1. Internal Component State</h2>
          <Counter />
        </section>

        <hr />

        <section>
          <h2>2. Data Fetching & Side Effects</h2>
          <UserList />
        </section>
      </main>

      <footer>
        <p>&copy; 2025 Full Stack Learning Hub</p>
      </footer>
    </div>
  )
}

export default App
