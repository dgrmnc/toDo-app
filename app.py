import time
import csv
import re
import os
from flask import Flask, render_template, request, redirect, url_for

class toDo:
    
    todo_file = "todo.csv"
    
    def __init__(self):
        self.todo = self.load_todo(toDo.todo_file)

    @staticmethod
    def load_todo(filename):
        if os.path.exists(filename):
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        return []

    @staticmethod
    def save_todo(filename,todo):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['todo']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(todo)

    def add_task(self):
        while True:
            try:
                task_input = input("Please enter a task: ").lower().capitalize()
                if task_input:
                    self.todo.append({'todo':task_input}) # new task
                    self.save_todo(toDo.todo_file, self.todo) # save updated list
                    print("to do has been added to the list!..")
                else:
                    print("Task cannot be empty. Please try again.")
            except ValueError as e:
                print("Upps :( '{e}'.. Something went wrong")
            break

    def listTask(self):
        if not self.todo:
            print("No to Do exists..")
        else:
            print("Current To Do's: ")
            for index, task in enumerate(self.todo):
                print(f"{index + 1}. To Do: {task['todo']}")  

    def delete_todo(self):
        if not self.todo:
            print("There is no to Do left to be deleted. Good job!")
            return
        self.listTask()
        try:
            delete_input = int(input("Which to do you want to eliminate?(Please enter a number): "))
            if 1 <= delete_input <= len(self.todo):
                deleted_task = self.todo.pop(delete_input - 1) 
                self.save_todo(toDo.todo_file, self.todo) # will save updated list
                print(f"Deleted: {deleted_task['todo']}")
            else:
                print("Invalid to do! Choose again.")
        except ValueError as e:
            print(f"{e}")
           

if __name__ == '__main__':
    todo  = toDo()
    
    while True:
        print("Please choose below given options: ")
        print("1. Add To Do ")
        print("2. Delete To Do ")
        print("3. List all To Do ")
        print("4. Exiting the app..")
        try:
            option = int(input("Please enter your option: "))
            
            if option == 1:
                todo.add_task()
            elif option == 2:
                todo.delete_todo()
            elif option == 3:
                todo.listTask()
            elif option == 4:
                print("Exiting.. Bye!")
                time.sleep(1)
                break
            else:
                print("Invalid option!")
        except ValueError as e:
            print(f"{e}")
        