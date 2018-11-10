import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def assignToDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    developer = event['developer']
    
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    myTuple= ("manager assigned bug to ",str(developer)," for development")
    lastAction=""
    data = response['Item']
    
    data['manager'] = " "
    data['developer'] = developer
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= "manager"
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "issue"

    table.put_item(Item = data)
    return 0