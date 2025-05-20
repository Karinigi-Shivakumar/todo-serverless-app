import boto3
import os

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TASKS_TABLE"])

def put_item(item):
    table.put_item(Item=item)

def get_item(task_id):
    response = table.get_item(Key={"id": task_id})
    return response.get("Item")

def delete_item(task_id):
    response = table.delete_item(Key={"id": task_id}, ReturnValues="ALL_OLD")
    return "Attributes" in response
