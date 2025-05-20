from .db import put_item, get_item, delete_item

def create_task(task_id, title):
    item = {"id": task_id, "title": title}
    put_item(item)
    return item

def get_task(task_id):
    return get_item(task_id)

def delete_task(task_id):
    return delete_item(task_id)
