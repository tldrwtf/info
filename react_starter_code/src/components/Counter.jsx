import { useState } from 'react';

/**
 * Counter Component
 * Demonstrates the 'useState' hook for managing local interactivity.
 */
const Counter = () => {
  // count: the current value
  // setCount: the function used to update it
  const [count, setCount] = useState(0);

  return (
    <div className="card">
      <p>Current Count: <strong>{count}</strong></p>
      <div className="button-group">
        <button onClick={() => setCount(count + 1)}>Increase</button>
        <button onClick={() => setCount(count - 1)}>Decrease</button>
        <button onClick={() => setCount(0)} className="btn-secondary">Reset</button>
      </div>
    </div>
  );
};

export default Counter;
