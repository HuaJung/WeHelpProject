const newDiv = document.createElement('div');
newDiv.className = 'text-center p-3 mb-2 bg-light text-dark';
var serachInput = document.getElementById('search-input')
var updateInput = document.getElementById('update-input')

// Trigger a Button Click on Enter
serachInput.addEventListener('keypress', (e)=> {
    if (e.key === 'Enter') {
        e.preventDefault();
        document.getElementById('search-btn').click();
    };
});

updateInput.addEventListener('keypress', (e)=> {
    if (e.key === 'Enter') {
        e.preventDefault();
        document.getElementById('update-btn').click();
    };
});

// onclick serach button
function search() {
    const usernameEntered = serachInput.value;
    let url = new URL(`${window.origin}/api/member`); 
    url.searchParams.set("username", usernameEntered);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.data === null) {
                newDiv.textContent = `${usernameEntered} not exist`
            } else {
                const name = data.data.name;
                const username = data.data.username;
                newDiv.textContent = `${name} (${username})`;
            };          
            document.querySelector('#search-card').appendChild(newDiv);
    });
};

// onclick update button
function update() {
    const newName = {name: updateInput.value};
    let url = new URL(`${window.origin}/api/member`);
    fetch(url, {
        'method': 'PATCH',
        'headers': {'Content-Type': 'application/json'},
        'body': JSON.stringify(newName),
    })
    .then(response => response.json())
    .then(data => {
        if (data.ok === true) {
            newDiv.textContent = 'update successful!';
        } else if (data.error === false) {
            newDiv.textContent = 'fail to update!';
        } else {
            newDiv.textContent = 'something went wrong';
        };
        document.querySelector('#update-card').appendChild(newDiv);
    });
};






