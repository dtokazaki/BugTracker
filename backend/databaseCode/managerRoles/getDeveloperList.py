import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
    context (object): information about the function 
returns data (list): a list of the usernames of all developers

this function is used to look up the usernames of everyone with a developer permission level
'''
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
    
