import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
    context (object): information about the function 
returns data (list): all bugs that need a tester or developer assigned to them

this function is used to return a list of all bugs that need a tester or developer assigned to them
'''
def getManager(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    response1 = table.query(
        IndexName='manager-index',
        KeyConditionExpression=Key('manager').eq("manager")
    )
    
    response2 = table.query(
        IndexName='status-index',
        KeyConditionExpression=Key("status").eq("reported")
    )
        
    man = response1['Items']
    report= response2['Items']
    
    data= man + report
        
    return data
    