#!/usr/bin/python3
"""script to export data in the CSV format"""
import csv
import sys
import requests

if __name__ == "__main__":
    num = sys.argv[1]
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{num}')
    url = f'https://jsonplaceholder.typicode.com/users/{num}/todos'
    task = requests.get(url)
    name = users.json()['username']
    with open(f'{num}.csv', mode='w') as employee_file:
        for i in task.json():
            employee_writer = csv.writer(employee_file, delimiter=',', quoting=csv.QUOTE_ALL)
            employee_writer.writerow([num, name, i['completed'], i['title']])
