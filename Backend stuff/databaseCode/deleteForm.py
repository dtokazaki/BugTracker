import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

# Delete Form
def deleteForm(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')

    id = event['id']
    
    table.delete_item(
        Key={
            'code': id
        }
    )

    return 0