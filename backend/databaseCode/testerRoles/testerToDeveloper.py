'''
parameters
    event (dictionary): stores data
        id (string): bug ID
        tester (string): tester's username
        text (string): tester's description
        severity (string): updated severity level
    context (object): information about the function 
returns 0 (int): not an error

this function is used to mark a bug as an issue and send it to the assigned developer
'''
def testerToDeveloper(event,context):
    dynamodb = resource('dynamodb')
    table = dynamodb.Table('bugTracker')
    
    id = event['id']
    tester = event['tester']
    text=event['text']
    severity= event['severity']
    
    
    response = table.get_item(
        Key={
            'code': id
        }
    )
    
    lastAction=""
    data = response['Item']
        
    myTuple= ("Solution incomplete or incorrect. Sent back to ",str(data['developer']))
    
    data['severity']=severity
    data['testerDescription']= text        
    data['lastUpdatedDate']= str(datetime.datetime.now().date())
    data['lastUpdatedBy']= data['tester']
    data['lastAction']= lastAction.join(myTuple)
    data['status']= "issue"

    table.put_item(Item = data)
    
    return 0
    