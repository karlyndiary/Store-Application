var loginApiURL = 'http://127.0.0.1:5000/login';

// Example data (you would get these values from your login form)
var userCredentials = {
    username: 'exampleUser',
    password: 'examplePassword'
};

// Sending POST request with credentials to the server
fetch(loginApiURL, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',  // Tell the server it's JSON
    },
    body: JSON.stringify(userCredentials)  // Convert the user credentials to JSON
})
    .then(response => response.json())  // Parse the JSON response from the server
    .then(data => {
        if (data.success) {
            console.log('Login successful:', data);
            // Optionally, redirect the user to a dashboard or home page
            window.location.href = '/dashboard';
        } else {
            console.log('Login failed:', data.message);
            // Handle login failure (e.g., show error message to user)
        }
    })
    .catch(error => {
        console.error('Error logging in:', error);
    });