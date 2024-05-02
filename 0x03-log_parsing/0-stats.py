#!/usr/bin/python3
'''Module reads stdin line by line & computes metrics'''
import sys
from collections import defaultdict

def parse_log():
    '''prints the status codes and file sizes'''
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    for line in sys.stdin:
        try:
            parts = line.split()
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print(f"Total file size: {total_size}")
                for code in sorted(status_codes.keys()):
                    print(f"{code}: {status_codes[code]}")

        except (IndexError, ValueError):
            pass

if __name__ == "__main__":
    try:
        parse_log()
    except KeyboardInterrupt:
        print("Keyboard Interrupted")
