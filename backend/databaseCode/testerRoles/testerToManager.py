import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime

'''
parameters
    event (dictionary): stores data
        id (string): bug ID
        tester (string): tester's username
        text (string): tester's description
        severity (string): updated severity level
    context (object): information about the function 
returns 0 (int): not an error

this function is used to mark a bug as an issue and send it to the manager
'''
def testerToManager(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    severity = event['severity']
    text=event['text']
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    myTuple= (tester," confirmed bug and sent to manager")
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