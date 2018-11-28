import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
        id (string): bug ID
    context (object): information about the function 
returns data (list): the bug (and associated information) that has the given id

this function is used to return the bug with a given id
'''
def getForm(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
        
    data = response['Item']
        
    return data