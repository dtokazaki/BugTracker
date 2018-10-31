import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def testerToManager(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    manager=event['manager']
    text=event['text']
    
    try:
        response = table.get_item(
            Key={
                'code': id
            }
        )
    
        myTuple= (str(tester)," Confirmed Bug and sent to ", str(manager))
        lastAction=""
        data = response['Item']
        
            
        data['testerDescription']= str(text)
        data['manager'] = manager
        data['tester']=tester
        data['lastUpdatedTime']= str(datetime.datetime.time(datetime.datetime.now()))
        data['lastUpdatedBy']= str(data['tester'])
        data['lastAction']= lastAction.join(myTuple)
        data['status']= "Bug Confirmed and sent to Manager"

        table.put_item(Item = data)
        return 0
    except: 
        return -1
