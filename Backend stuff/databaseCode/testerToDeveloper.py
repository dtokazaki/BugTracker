import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def testerToDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    text=event['text']
    
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    lastAction=""
    data = response['Item']
        
    myTuple= ("Solution incomplete or incorrect. Sent back to ",str(data['developer']))

            
    data['testerDescription']= str(text)        
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= str(data['tester'])
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "issue"

    table.put_item(Item = data)
    
    return 0
    