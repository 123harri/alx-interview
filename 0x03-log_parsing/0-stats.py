#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
"""

import sys


def print_stats(total_size, status_counts):
    """
    Print the accumulated metrics.
    """
    print("File size: {}".format(total_size))
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print("{}: {}".format(status, status_counts[status]))


def parse_line(line):
    """
    Parse a line of the log and extract status code and file size.
    Return a tuple of (status_code, file_size).
    """
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None


def main():
    total_size = 0
    status_counts = {
            200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
