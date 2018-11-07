import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def assignToDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    developer = event['developer']
    manager=event['manager']
    
    try:
        response = table.get_item(
            Key={
                'code': id
            }
        )
    
        myTuple= (str(manager)," Assigned Bug to ",str(developer)," for development")
        lastAction=""
        data = response['Item']
        
        if data['developer'] == developer:
                return -2
        
        data['developer'] = developer
        data['lastUpdatedTime']= str(datetime.datetime.time(datetime.datetime.now()))
        data['lastUpdatedBy']= manager
        data['lastAction']= lastAction.join(myTuple)
        data['status']= str("Sent to Developer")

        table.put_item(Item = data)
        return 0
    except: 
        return -1
