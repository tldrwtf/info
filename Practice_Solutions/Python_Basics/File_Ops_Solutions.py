import os
import json

# ==========================================
# TASK 11.1: Log Analyzer (Text Files)
# ==========================================
def analyze_logs():
    """
    1. Creates a dummy log file.
    2. Reads it line by line.
    3. Counts 'ERROR' occurrences.
    4. Writes a summary report.
    """
    filename = "dummy_server.log"
    report_file = "log_report.txt"
    
    # Setup: Create dummy log
    with open(filename, 'w') as f:
        f.write("INFO: Server started\n")
        f.write("WARNING: High memory usage\n")
        f.write("ERROR: Database connection failed\n")
        f.write("INFO: Health check passed\n")
        f.write("ERROR: Timeout waiting for service\n")
    
    print(f"--- Created {filename} ---")

    # Logic: Analyze
    error_count = 0
    try:
        with open(filename, 'r') as f:
            for line in f:
                if "ERROR" in line:
                    error_count += 1
                    print(f"Found Error: {line.strip()}")
    except FileNotFoundError:
        print("Log file not found.")
        return

    # Output: Write Report
    with open(report_file, 'w') as f:
        f.write(f"Log Analysis Report\n")
        f.write(f"Total Errors Found: {error_count}\n")
    
    print(f"--- Written {report_file} ---")
    
    # Cleanup (Optional)
    # os.remove(filename)
    # os.remove(report_file)

# ==========================================
# TASK 11.2: JSON Configuration Handler
# ==========================================
def update_config(key, value):
    """
    1. Reads a JSON config file (creates if missing).
    2. Updates a specific key.
    3. Saves it back.
    """
    config_file = "app_config.json"
    
    # Default Config
    data = {"theme": "light", "version": "1.0.0", "debug": False}
    
    # Read existing if available
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("Corrupt JSON, starting fresh.")
    
    # Update
    print(f"Old Config: {data}")
    data[key] = value
    print(f"New Config: {data}")
    
    # Write
    with open(config_file, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"--- Saved to {config_file} ---")

if __name__ == "__main__":
    analyze_logs()
    update_config("theme", "dark")
    update_config("debug", True)
