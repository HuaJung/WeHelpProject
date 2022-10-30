var username = document.getElementById('username');
var password = document.getElementById('password');
var confirmPassword = document.getElementById('confirm');
var re = /^$|\s/;  // if spaces in a string 


function passwordValidator(){
    if (password.value !== confirmPassword.value){
        confirmPassword.setCustomValidity('Password doesn\'t match');        
    } else {  // must have else for accepting immediate modification
        confirmPassword.setCustomValidity('');
    };
}

function spaceValidator(){
    // sapce cannot be allowed for username
    if (re.test(username.value) === true) {
        username.setCustomValidity('space is not allowed');
    } else {
        username.setCustomValidity('');
    };
}

username.onchange = spaceValidator;
password.onchange = passwordValidator;
confirmPassword.onkeyup = passwordValidator;
