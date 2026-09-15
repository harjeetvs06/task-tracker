import json
import sys
from datetime import datetime
from pathlib import Path

TASK_FILE=Path("tasks.json")

def list_tasks(status=None):
    if status  not in["todo","in-progress","done"]:
        print("Invalid choice")
        return 

    tasks=load_tasks()

    for task_id,task in tasks.items():
        if status and task["status"]!=status:
            continue
        
        print(f"ID:{task_id}")
        print(f"Description:{task['description']}")
        print(f"Status:{task['status']}")
        print()


def load_tasks():
    if not TASK_FILE.exists():
        return{}

    with open(TASK_FILE,"r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE ,"w") as file:
        json.dump(tasks,file,indent=0)

def add_task(description:str)->None:
    tasks=load_tasks()
    today =datetime.today().isoformat(timespec="seconds")
    id=str(max(map(int ,tasks.keys()),default=0)+1)

    tasks[id]={
        "description":description,
        "status":"todo",
        "createdAt":today,
        "updatedAt":today
    }
    save_tasks(tasks)

    print(f"the task printed sucessfully (ID:{id})")

def update_tasks(task_id,description):
    tasks=load_tasks()

    if task_id in tasks:
        tasks[task_id]["description"]=description

        today=datetime.today().isoformat(timespec="seconds")
        tasks[task_id]["updatedAt"]=today
    else:
        print("Not found")

        save_tasks(tasks)

def delete_tasks(task_id):
    tasks=load_tasks()

    if task_id not in tasks:
        print("task not found")
        return

    del tasks[task_id]
    save_tasks(tasks)

def update_status(task_id,status):
    tasks=load_tasks()

    if status not in["todo","in-progress","done"]:
        print("invalid status")
        return


    if task_id in tasks:
        tasks[task_id]["status"]=status

        today=datetime.today().isoformat(timespec="seconds")
        tasks[task_id]["updatedAt"]=today

        save_tasks(tasks)


if len(sys.argv)>=3 and sys.argv[1]=="add":
    add_task(sys.argv[2])

elif len(sys.argv)>=2 and sys.argv[1]=="list":
    if len(sys.argv)==2:
        list_tasks()

    elif len(sys.argv)==3:
        list_tasks(sys.argv[2])

elif len(sys.argv)>=4 and sys.argv[1]=="update":
    update_tasks(sys.argv[2],sys.argv[3])

elif len(sys.argv)>=3 and sys.argv[1]=="delete":
    delete_tasks(sys.argv[2])

elif len(sys.argv)>=3 and sys.argv[1]=="mark-done":
    update_status(sys.argv[2],"done")

elif len(sys.argv)>=3 and sys.argv[1]=="mark-in-progress":
    update_status(sys.argv[2],"in-progress")

else:
    print("invalid command")