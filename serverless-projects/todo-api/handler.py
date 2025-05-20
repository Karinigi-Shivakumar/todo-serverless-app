# import json


# def hello(event, context):
#     body = {
#         "message": "Go Serverless v4.0! Your function executed successfully!",
#     }

#     response = {"statusCode": 200, "body": json.dumps(body)}

#     return response

import json
from service.todo import create_task, get_task, delete_task

def create(event, context):
    body = json.loads(event["body"])
    task = create_task(body["id"], body["title"])
    return {"statusCode": 201, "body": json.dumps(task)}

def get(event, context):
    task_id = event["pathParameters"]["id"]
    task = get_task(task_id)
    if not task:
        return {"statusCode": 404, "body": json.dumps({"error": "Task not found"})}
    return {"statusCode": 200, "body": json.dumps(task)}

def delete(event, context):
    task_id = event["pathParameters"]["id"]
    deleted = delete_task(task_id)
    if not deleted:
        return {"statusCode": 404, "body": json.dumps({"error": "Task not found"})}
    return {"statusCode": 204}import json


def hello(event, context):
    body = {
        "message": "Go Serverless v4.0! Your function executed successfully!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
