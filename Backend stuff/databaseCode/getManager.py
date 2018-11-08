import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getManager(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    response = table.query(
        IndexName='manager-index',
        KeyConditionExpression=Key('manager').eq("manager")
    )
        
    data = response['Items']
        
    return data
    