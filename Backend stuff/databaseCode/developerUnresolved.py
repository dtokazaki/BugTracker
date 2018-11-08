import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def developerUnresolved(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    developer = event['developer']
    
    try:
        response = table.get_item(
            Key={
                'code': id
            }
        )
    
        myTuple= (developer, "marked bug unresolved: No Further action will be taken")
        lastAction=""
        data = response['Item']
        
        data['developer']=""
        data['tester']=""
        data['manager']=""
        data['lastUpdatedDate']= str(datetime.datetime.now().date()
        data['lastUpdatedBy']= developer
        data['lastAction']= lastAction.join(myTuple)
        data['status']= "unresolved"

        table.put_item(Item = data)
        return 0
    except: 
        return -1