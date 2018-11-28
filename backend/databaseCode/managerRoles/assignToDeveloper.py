import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import datetime

'''
parameters
    event (dictionary): stores data
        id (string): bug ID
        developer (string): developer's username
    context (object): information about the function 
returns 0 (int): not an error

this function is used to assign a developer
'''
def assignToDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    developer = event['developer']
    
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    myTuple= ("manager assigned bug to ",str(developer)," for development")
    lastAction=""
    data = response['Item']
    
    data['manager'] = " "
    data['developer'] = developer
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= "manager"
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "issue"

    table.put_item(Item = data)
    return 0