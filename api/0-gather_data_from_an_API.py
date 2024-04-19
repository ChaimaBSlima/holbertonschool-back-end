#!/usr/bin/python3
import requests
import sys


def main(a):
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={a}"
    ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{a}"
    ).json()
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    print(
        f"Employee {user_info['name']} is done with tasks\
({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print("\t {}".format(task))

if __name__ == "__main__":
    a = sys.argv[1]
    main(a)
