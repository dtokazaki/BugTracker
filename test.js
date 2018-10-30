const userAction = async () => {
	const response = await fetch('https://052stnmylg.execute-api.us-west-1.amazonaws.com/firstTes', {
		method: 'GET',
		body: id=ea4cec393c2c4694a176930ee8c5cc11, // string or object
		headers:{
			'Content-Type': 'application/json'
			'x-api-key':IRhxCk4NmV4mpQHK75NsL4GEqSocd4X56fFgX7BS
			}
	});
	const myJson = await response.json(); //extract JSON from the http response
		
}
