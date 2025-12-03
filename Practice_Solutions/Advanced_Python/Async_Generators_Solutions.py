import asyncio
import random

# ==========================================
# TASK 13.1: Custom Generator
# ==========================================
def fibonacci_generator(limit):
    """
    Generates Fibonacci numbers up to a limit.
    Yields values one by one to save memory.
    """
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

def test_generator():
    print("--- Fibonacci Generator (First 10) ---")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print("\n")

# ==========================================
# TASK 13.2: Asyncio Basics
# ==========================================
async def fetch_data_mock(id, delay):
    """Simulates fetching data from an API with a delay."""
    print(f"Task {id}: Fetching data...")
    await asyncio.sleep(delay) # Non-blocking sleep
    print(f"Task {id}: Done! (took {delay}s)")
    return f"Data_{id}"

async def main_async_flow():
    print("--- Starting Async Tasks ---")
    start = time.perf_counter()
    
    # Schedule 3 calls to run concurrently
    results = await asyncio.gather(
        fetch_data_mock(1, 2), # 2 seconds
        fetch_data_mock(2, 1), # 1 second
        fetch_data_mock(3, 3)  # 3 seconds
    )
    
    end = time.perf_counter()
    print(f"All tasks completed in {end - start:.2f} seconds.")
    print(f"Results: {results}")

if __name__ == "__main__":
    test_generator()
    
    # Run Async Loop
    import time
    asyncio.run(main_async_flow())
