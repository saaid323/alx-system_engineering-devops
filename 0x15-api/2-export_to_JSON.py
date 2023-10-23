#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests
import sys
if __name__ == "__main__":
    num = sys.argv[1]
    users = requests.get(f'https://jsonplaceholder.typicode.com/users/{num}')
    url = f'https://jsonplaceholder.typicode.com/users/{num}/todos'
    task = requests.get(url) 
    username = users.json()['username']
    dic = {num: []}
    for i in task.json():
        tasks = {"task": i["title"], "completed": i["completed"], "username": username}
        dic[num].append(tasks)
    with open(f"{num}.json", "w") as file:
        json.dump(dic, file)
