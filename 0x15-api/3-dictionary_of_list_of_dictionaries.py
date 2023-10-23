#!/usr/bin/python3
"""script to export data in the JSON format"""
import json
import requests

if __name__ == "__main__":
    users = requests.get(f'https://jsonplaceholder.typicode.com/users')
    dic = {}
    for i in users.json():
        user_id = i["id"]
        dic[user_id] = []
        username = i["username"]
        url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        task = requests.get(url)
        for j in task.json():
            tasks = {"username": username, "task": j["title"],
                     "completed": j["completed"]}
            dic[i["id"]].append(tasks)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dic, file)
