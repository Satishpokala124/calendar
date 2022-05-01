const login = (() => {
	console.log('Logging in');
	fetch('http://127.0.0.1:8000/account/login/', {
		method: 'POST',
		headers: {
      		'Content-Type': 'application/json'
  		},
		body: JSON.stringify({
			username: 'admin@admin.com',
			password: 'admin123'
		})
	})
	.then(response => response.json())
	.then(data => console.log(data))
})

const logout = (() => {
	console.log('Logging out');
	fetch('http://127.0.0.1:8000/account/logout/')
	.then(response => response.json())
	.then(data => console.log(data))
})


//fetch('http://127.0.0.1:8000/users/',{
//	headers: new Headers({
//    	"Authorization": `Basic ${btoa('admin:admin')}`
//  })
//})
//.then(response => response.json())
//.then(data => console.log(data))