from datetime import datetime

def add_task(data, title, due=None):
    task = {
        "id": int(datetime.utcnow().timestamp()),
        "title": title,
        "due": due,
        "done": False
    }
    data.setdefault("tasks", []).append(task)
    return task

def list_tasks(data):
    return data.get("tasks", [])

def mark_done(data, task_id):
    for t in data["tasks"]:
        if t["id"] == task_id:
            t["done"] = True
            return t
    return None

def delete_task(data, task_id):
    tasks = data.get("tasks", [])
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            return tasks.pop(i)
    return None
