import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

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