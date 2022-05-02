const login = () => {
  fetch('http://127.0.0.1:8000/account/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'admin@admin.com',
      password: 'admin123',
    }),
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
};

const register = () => {
  fetch('http://127.0.0.1:8000/account/register/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'satish1',
      firstname: 'Satish',
      lastname: 'Pokala',
      email: 'satish@satish.com',
      password: 'satish123',
      cnf_password: 'satish123',
    }),
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
};

const logout = () => {
  console.log('Logging out');
  fetch('http://127.0.0.1:8000/account/logout/')
    .then((response) => response.json())
    .then((data) => console.log(data));
};