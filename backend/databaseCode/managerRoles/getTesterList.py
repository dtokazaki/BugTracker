import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
    context (object): information about the function 
returns data (list): a list of the usernames of all testers

this function is used to look up the usernames of everyone with a tester permission level
'''
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
    
