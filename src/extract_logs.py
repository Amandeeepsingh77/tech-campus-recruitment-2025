import sys
import os

def extract_logs(date):
    log_file_path = 'test_logs.log'  
    output_dir = 'output'  
    output_file_path = os.path.join(output_dir, f'output_{date}.txt')


    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
            for line in log_file:
                if line.startswith(date):
                    output_file.write(line)
        print(f"Logs for {date} have been written to {output_file_path}")
    except FileNotFoundError:
        print(f"Error: The log file '{log_file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py YYYY-MM-DD")
        sys.exit(1)

    date_arg = sys.argv[1]
    extract_logs(date_arg)
