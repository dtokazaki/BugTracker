import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def developerToTester(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    developer=event['developer']
    text=event['text']
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    data = response['Item']
    
    myTuple= (str(developer)," Solution Complete and sent to ", str(data['tester']))
    lastAction=""
            
    data['developerDescription']= text
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= developer
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "testing"

    table.put_item(Item = data)
    return 0
    