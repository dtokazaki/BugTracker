import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getTesterList(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTrackerAccounts')
    
    response = table.query(
        IndexName='permission-index',
        KeyConditionExpression=Key('permission').eq("tester")
    )
    
    allTesters= response['Items']
    
    data=[]
    for test in allTesters:
        data.append(test['username'])
    data.sort()

    return data
    
