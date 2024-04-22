#!/usr/bin/python3
""" export the data to a CSV file """
from json import dump
from json import loads
from urllib import request


def makeFormat(user, tasks):
    my_dictionary = {}
    count = 1

    while (count <= 10):
        uid = count
        name = user[count - 1].get("username")
        my_list = []
        last = count * 20
        i = last - 20
        while (i < last):
            data = {"username": name}
            data["task"] = tasks[i].get("title")
            data["completed"] = tasks[i].get("completed")
            my_list.append(data)
            i += 1
        my_dictionary[str(uid)] = my_list
        count += 1

    return my_dictionary


if __name__ == "__main__":
    my_file = open("todo_all_employees.json", "w")
    user_req = request.urlopen("https://jsonplaceholder.typicode.com/users")
    task_req = request.urlopen("https://jsonplaceholder.typicode.com/todos")
    users = loads(user_req.read().decode("UTF-8"))
    tasks = loads(task_req.read().decode("UTF-8"))

    dump(makeFormat(users, tasks), my_file)
