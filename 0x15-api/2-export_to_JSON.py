#!/usr/bin/python3
""" export the data to a CSV file """
from json import dump
from json import loads
from urllib import request
from sys import argv


def makeFormat(user_id, user, tasks):
    name = user[user_id - 1].get("username")
    my_list = []
    last = user_id * 20
    i = last - 20

    while (i < last):
        data = {"task": tasks[i].get("title")}
        data["completed"] = tasks[i].get("completed")
        data["username"] = name
        my_list.append(data)
        i += 1

    return {str(user_id): my_list}


if __name__ == "__main__":
    user_id = int(argv[1])
    my_file = open(argv[1] + ".json", "w")
    user_req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    task_req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    users = loads(user_req.read().decode("UTF-8"))
    tasks = loads(task_req.read().decode("UTF-8"))

    dump(makeFormat(user_id, users, tasks), my_file)
