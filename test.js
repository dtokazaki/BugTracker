var url = 'https://052stnmylg.execute-api.us-west-1.amazonaws.com/firstTest';
var data = {id: 'ea4cec393c2c4694a176930ee8c5cc11'};

.ajax({
		url: "https://052stnmylg.execute-api.us-west-1.amazonaws.com/firstTest",
		data: {id: data},
		type: "GET",
		beforeSend: function(xhr){xhr.setRequestHeader{'x-api-key', 'IRhxCk4NmV4mpQHK75NsL4GEqSocd4X56fFgX7BS');},
		success: function() {alert('Success!" + data); }


