import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
        id (string): bug ID
    context (object): information about the function 
returns 0 (int): not an error

this function deletes a particular bug
'''
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