import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
'''
parameters
    event (dictionary): stores data
    context (object): information about the function 
returns data (list): all bugs 

this function is used to return a list of all bugs
'''
def getAllForms(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    response = table.scan()
        
    data = response['Items']
        
    return data