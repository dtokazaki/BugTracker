import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

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
    