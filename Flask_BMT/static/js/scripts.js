function signup() {



const form = document.querySelector('#form');
const userName = document.querySelector('#userName');
const email = document.querySelector('#email');
const employeeId = document.querySelector('#employeeId');
const password1 = document.querySelector('#password1');
const password2 = document.querySelector('#password2');

form.addEventListener("submit", (event) => {
  event.preventDefault();


    validateInputs();
});

    const setError = (element, message) => {
        const inputBox = element.parentElement;
        const errorDisplay = inputBox.querySelector('.error');
    
        errorDisplay.innerText = message;
        inputBox.classList.add('error');
        inputBox.classList.remove('success')
    }
    
    const setSuccess = element => {
        const inputBox = element.parentElement;
        const errorDisplay = inputBox.querySelector('.error');
    
        errorDisplay.innerText = '';
        inputBox.classList.add('success');
        inputBox.classList.remove('error');
    };
    
    const isValidEmail = email => {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
    
    const validateInputs = () => {
        const userNameValue = userName.value.trim();
        const emailValue = email.value.trim();
        const password1Value = password1.value.trim();
        const password2Value = password2.value.trim();
    
        if(userNameValue === '') {
            setError(userName, 'Username is required');
        } else {
            setSuccess(userName);
        }
    
        if(emailValue === '') {
            setError(email, 'Email is required');
        } else if (!isValidEmail(emailValue)) {
            setError(email, 'Provide a valid email address');
        } else {
            setSuccess(email);
        }
    
        if(password1Value === '') {
            setError(password1, 'Password is required');
        } else if (password1Value.length < 8 ) {
            setError(password1, 'Password must be at least 8 character.')
        } else {
            setSuccess(password1);
        }
    
        if(password2Value === '') {
            setError(password2, 'Please confirm your password');
        } else if (password2Value !== password1Value) {
            setError(password2, "Passwords doesn't match");
        } else {
            setSuccess(password2);
          
        }
    
 
    
    };

              
        if (document.querySelectorAll('.success').length === 4) {
            window.location.replace("login-form.html");
          }
   
  
  
}

