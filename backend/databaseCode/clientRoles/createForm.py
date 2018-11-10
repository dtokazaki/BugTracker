import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import uuid
import datetime
import json

# Create Form
def createForm(event,context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    description = event['description']
    details = event['details']
    
    id = uuid.uuid4()

    data = {}
    data['code']= id.hex
    data['description'] = description
    data['details']=details
    data['testerDescription'] = " "
    data['developerDescription']=" "
    data["status"]="reported"
    data['dateCreated'] = str(datetime.datetime.now().date())
    data['lastUpdatedDate']= " "
    data['lastUpdatedBy'] = " "        
    data['tester']=" "
    data['developer']=" "
    data['manager']=" "
    data['lastAction']= "Bug Reported"
    data['severity']= " "
        
        
    table.put_item(Item= data)
    return id.hex