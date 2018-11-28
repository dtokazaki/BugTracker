import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime

'''
parameters
    event (dictionary): stores data
        id (string): bug ID
        developer (string): developer's username
        text (string): developer's description
        severity (string): updated severity level
    context (object): information about the function 
returns 0 (int): not an error

this function is used to send a bug back to its assigned tester
'''
def developerToTester(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    developer=event['developer']
    text=event['text']
    severity=event['severity']
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    data = response['Item']
    
    myTuple= (str(developer)," Solution Complete and sent to ", str(data['tester']))
    lastAction=""
    
    data['severity']=severity        
    data['developerDescription']= text
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= developer
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "testing"

    table.put_item(Item = data)
    return 0