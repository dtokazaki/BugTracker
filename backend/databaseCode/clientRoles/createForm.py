import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
import uuid
import datetime
import json
'''
parameters
    event (dictionary): stores data
        description (string): description of what client was doing when they found the bug
        details (string): more info about the bug
        system (string): what system the client was using when they found the bug
    context (object): information about the function 
returns id (string): unique code for the bug that was reported

this function is used to create a new bug and send the form to the manager to assign a testers
'''
# Create Form
def createForm(event,context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    description = event['description']
    details = event['details']
    system=event['system']
    
    id = uuid.uuid4()

    data = {}
    data['code']= id.hex
    data['description'] = description
    data['system']= system
    data['details']=details
    data['testerDescription'] = " "
    data['developerDescription']=" "
    data["status"]="reported"
    data['dateCreated'] = str(datetime.datetime.now().date())
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy'] = " "        
    data['tester']=" "
    data['developer']=" "
    data['manager']=" "
    data['lastAction']= "Bug Reported"
    data['severity']= " "
        
        
    table.put_item(Item= data)
    return id.hex