import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
        developer (string): developer's username
    context (object): information about the function 
returns data (list): all bugs assigned to a particular developer

this function is used to return a list of all bugs assigned to a certain developer
'''
def getDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    developer = event['developer']
    
    response = table.query(
        IndexName='status-index',
        KeyConditionExpression=Key("status").eq("issue")
    )
        
    allDevs = response['Items']
    data=[]
    
    for dev in allDevs:
        if dev['developer']==developer:
            data.append(dev)
        
    return data
    