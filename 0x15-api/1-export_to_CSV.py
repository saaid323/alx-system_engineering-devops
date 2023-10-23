#!/usr/bin/python3
"""script to export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    num = sys.argv[1]
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{num}')
    url = f'https://jsonplaceholder.typicode.com/users/{num}/todos'
    task = requests.get(url)
    name = users.json()['username']
    with open(f'{num}.csv', mode='w') as emp_file:
        for i in task.json():
            employee = csv.writer(emp_file, delimiter=',', quoting=csv.QUOTE_ALL)
            employee.writerow([num, name, i['completed'], i['title']])
