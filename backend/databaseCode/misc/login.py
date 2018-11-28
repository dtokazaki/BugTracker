import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
from passlib.hash import pbkdf2_sha256
'''
parameters
    event (dictionary): stores data
        username (string): username
        password (string): password
    context (object): information about the function 
returns 
    failed to log in    -> -1 (int): error
    logged in correctly -> response['item']['permission'] (string): permission level

this function is used to log in to a user's account
'''
def login(event,context):
    # Create a DynamoDB resource
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTrackerAccounts')
    
    username = event['username']
    password = event['password']
    
     
    response = table.get_item(
        Key={
            'username': username
            }
    )
    try:
        realPassword = response['Item']['password']
    
        verify = pbkdf2_sha256.verify(password, realPassword)
        if verify:
            return response['Item']['permission']
        else:
            return -1
    except:
        return -1