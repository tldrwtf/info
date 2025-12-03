import time
import functools

# ==========================================
# TASK 12.1: Custom Decorator (Timer)
# ==========================================
def execution_timer(func):
    """
    Decorator that measures how long a function takes to run.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.4f} seconds to execute.")
        return result
    return wrapper

@execution_timer
def heavy_computation(n):
    print(f"Computing sum of range({n})...")
    total = sum(range(n))
    return total

# ==========================================
# TASK 12.2: Custom Context Manager
# ==========================================
class FileManager:
    """
    A custom context manager that mimics 'open()', 
    but adds logging on enter and exit.
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f">> Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"<< Closing file: {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"!! An error occurred: {exc_val}")
        # Return True to suppress exception, False to propagate it
        return False 

def test_context_manager():
    try:
        with FileManager('test_ctx.txt', 'w') as f:
            f.write("Hello from custom context manager!")
            # raise ValueError("Oops") # Uncomment to test error handling
    except Exception as e:
        print(f"Caught outside: {e}")

if __name__ == "__main__":
    heavy_computation(1000000)
    test_context_manager()
