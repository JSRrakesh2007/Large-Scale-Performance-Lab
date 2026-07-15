"""
Project : Large Scale Performance Lab

This program simulates multiple users sending requests
to a website and generates a simple performance report.
"""

import requests
import threading
import time

# Website to test
URL = "https://example.com"

# Number of simulated users
TOTAL_USERS = 20

# Store results
response_times = []


def send_request(user_id):
    """Send one HTTP request and record its response time."""
    try:
        start = time.time()

        response = requests.get(URL)

        end = time.time()

        response_time = end - start

        response_times.append(response_time)

        print(
            f"User {user_id:02d} | "
            f"Status: {response.status_code} | "
            f"Time: {response_time:.3f} sec"
        )

    except Exception as error:
        print(f"User {user_id:02d} Failed: {error}")


print("=" * 50)
print("LARGE SCALE PERFORMANCE LAB")
print("=" * 50)

threads = []

for user in range(1, TOTAL_USERS + 1):
    thread = threading.Thread(target=send_request, args=(user,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nTest Completed")

if response_times:
    average = sum(response_times) / len(response_times)

    print("\nPerformance Summary")
    print("-----------------------------")
    print(f"Total Users      : {TOTAL_USERS}")
    print(f"Successful Tests : {len(response_times)}")
    print(f"Average Time     : {average:.3f} sec")

    with open("performance_report.txt", "w") as report:
        report.write("Large Scale Performance Lab Report\n")
        report.write("----------------------------------\n")
        report.write(f"Website : {URL}\n")
        report.write(f"Total Users : {TOTAL_USERS}\n")
        report.write(f"Successful Requests : {len(response_times)}\n")
        report.write(f"Average Response Time : {average:.3f} sec\n")

print("\nReport saved as performance_report.txt")