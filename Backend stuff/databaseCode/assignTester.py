import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime


def assignTester(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
        
    myTuple= ("Manager assigned bug to ",str(tester)," for testing")
    lastAction=""
    data = response['Item']
                
    data['tester'] = tester
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= manager
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "testing"

    table.put_item(Item = data)
    return 0