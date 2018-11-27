import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
from passlib.hash import pbkdf2_sha256

# Create God account
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
    else:
        return -1