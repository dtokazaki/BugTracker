import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def assignToDeveloper(event,context):
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
    
        myTuple= ("Manager assigned Bug to ",str(developer)," for development")
        lastAction=""
        data = response['Item']
                
        data['developer'] = developer
        data['lastUpdatedDate']= str(datetime.datetime.now().date())
        data['lastUpdatedBy']= manager
        data['lastAction']= lastAction.join(myTuple)
        data['status']= str("Sent to Developer")

        table.put_item(Item = data)
        return 0
    except: 
        return -1