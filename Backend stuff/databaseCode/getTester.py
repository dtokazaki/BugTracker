import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getTester(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    tester = event['tester']
    
    response = table.query(
        IndexName='tester-index',
        KeyConditionExpression=Key('tester').eq(tester)
    )
        
    data = response['Items']
        
    return data
    
