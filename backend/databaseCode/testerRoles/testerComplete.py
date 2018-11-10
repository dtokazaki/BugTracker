import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def testerComplete(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    myTuple = ("Bug Resolved")
            
    lastAction=""
    data = response['Item']
        
    data['developer']=" "
    data['tester']=" "
    data['manager']=" "
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= tester
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "fixed"
    table.put_item(Item = data)
    
    return 0