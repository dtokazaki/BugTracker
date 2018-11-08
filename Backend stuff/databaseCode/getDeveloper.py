import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    developer = event['developer']
    
    response = table.query(
        IndexName='developer-index',
        KeyConditionExpression=Key('developer').eq(developer)
    )
        
    data = response['Items']
        
    return data
    