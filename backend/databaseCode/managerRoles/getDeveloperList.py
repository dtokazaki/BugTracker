import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getDeveloperList(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTrackerAccounts')
    
    response = table.query(
        IndexName='permission-index',
        KeyConditionExpression=Key('permission').eq("developer")
    )
    
    allDevelopers= response['Items']
    
    data=[]
    for dev in allDevelopers:
        data.append(dev['username'])
    data.sort()
    return data
    
