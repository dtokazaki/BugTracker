var url = 'https://052stnmylg.execute-api.us-west-1.amazonaws.com/firstTest';
var data = {id: 'ea4cec393c2c4694a176930ee8c5cc11'};

fetch(url, {
    headers:{
        'Content-Type': 'application/json',
        'x-api-key': 'IRhxCk4NmV4mpQHK75NsL4GEqSocd4X56fFgX7BS'
    },
    'mode':'no-cors'

}).then(res => res.json())
.then(response => console.log('Success:', JSON.stringify(response)))
.catch(error => console.error('Error:', error));


