import time

def tail_log_file(filepath):
    with open(filepath, 'r') as f:
        f.seek(0, 2)  # Move to the end of file
        while True:
            line = f.readline()
            if line:
                yield line.strip()
            else:
                time.sleep(0.5)
