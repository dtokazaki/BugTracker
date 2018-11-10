import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getTester(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    tester = event['tester']
    
    response = table.query(
        IndexName='status-index',
        KeyConditionExpression=Key('status').eq("testing")
    )
    
    allTesters= response['Items']
    
    data=[]
    for test in allTesters:
        if test['tester']== tester:
            data.append(test)
    
    return data
    