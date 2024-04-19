#!/usr/bin/python3
import requests
import sys

def TODO_REQUESTS(ID):
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={ID}"
    ).json()
    user_info = requests.get(
        f"https://jsonplaceholder.\
typicode.com/users/{ID}"
    ).json()
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    print(
        f"Employee {user_info['name']} is done with tasks\
({len(completed_tasks)}/{len(todos)}):"
    )
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    ID = sys.argv[1]

    TODO_REQUESTS(ID)
