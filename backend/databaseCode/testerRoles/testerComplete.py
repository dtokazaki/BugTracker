import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime

'''
parameters
    event (dictionary): stores data
        id (string): bug ID
        tester (string): tester's username
    context (object): information about the function 
returns 0 (int): not an error

this function is used to mark a bug as fixed
'''
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
        
    data['manager']=" "
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= tester
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "fixed"
    table.put_item(Item = data)
    
    return 0
