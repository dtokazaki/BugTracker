import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key
from passlib.hash import pbkdf2_sha256
'''
parameters
    event (dictionary): stores data
        username (string): username
        password (string): password
        permission (string): permission level (tester or developer)
    context (object): information about the function 
returns 
    -1 (int): username in use
    0 (int): account created

this function is used to make a new account and assign it a username, password, and permission level
'''
def makeAccount(event,context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('bugTrackerAccounts')
    
    username = event['username']
    password = event['password']
    permission = event['permission']

    response = table.get_item(
        Key={
            'username': username
            }
    )
    
    try:
        username = response["Item"]['username']
        return -1
    except:
        hashPassword = pbkdf2_sha256.encrypt(password, rounds=100, salt_size=16)
    
        data = {}
        data['password']= hashPassword
        data['username'] = username
        data['permission'] = permission

        table.put_item(Item= data)
        return 0
