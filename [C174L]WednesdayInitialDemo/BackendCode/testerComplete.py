import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def testerComplete(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    
    try:
        response = table.get_item(
            Key={
                'code': id
            }
        )
    
        myTuple= (" Bug resolved ")
        lastAction=""
        data = response['Item']
        
        if data['tester'] == " ":
            return -2
        
        data['developer']=" "
        data['tester']=" "
        data['manager']=" "
        data['lastUpdatedTime']= str(datetime.datetime.time(datetime.datetime.now()))
        data['lastUpdatedBy']= tester
        data['lastAction']= lastAction.join(myTuple)
        data['status']= str("Bug Resolved")

        table.put_item(Item = data)
        return 0
    except: 
        return -1
