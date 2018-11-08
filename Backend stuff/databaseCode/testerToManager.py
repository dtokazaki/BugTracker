import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def testerToManager(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    severity = event['severity']
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
        data['manager'] = "manager"
        data['lastUpdatedDate']= str(datetime.datetime.now().date())
        data['lastUpdatedBy']= str(data['tester'])
        data['lastAction']= lastAction.join(myTuple)
        data['status']= "pending"
        data['severity']=severity

        table.put_item(Item = data)
        return 0
    except: 
        return -1