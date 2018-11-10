import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key

def getAllForms(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    response = table.scan()
        
    data = response['Items']
        
    return data