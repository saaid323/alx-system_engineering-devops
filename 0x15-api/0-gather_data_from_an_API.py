#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys
if __name__ == "__main__":
    num = sys.argv[1]
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{num}')
    url = f'https://jsonplaceholder.typicode.com/users/{num}/todos'
    task = requests.get(url)
    done = [todo['title'] for todo in task.json() if todo['completed']]
    name = users.json()['name']
    t = f"Employee {name} is done with tasks({len(done)}/{len(task.json())}):"
    print(t)
    for k in done:
        print(f"\t {k}")
