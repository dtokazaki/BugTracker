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
    
    try:
        response = table.get_item(
            Key={
                'code': id
            }
        )
    
        data = response['Item']
        if data['tester'] == " ":
            return -2
        myTuple= (str(developer)," Solution Complete and sent to ", str(data['tester']))
        lastAction=""
            
        data['developerDescription']= text
        data['lastUpdatedTime']= str(datetime.datetime.time(datetime.datetime.now()))
        data['lastUpdatedBy']= developer
        data['lastAction']= lastAction.join(myTuple)
        data['status']= "Solution Completed and sent to tester"

        table.put_item(Item = data)
        return 0
    except: 
        return -1
