function ValidateEmail(input) {
    {
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(input)){
           return (true)
        }
           return (false)
       }
}

function ValidatePassword(password){
    password_requirements =[]

    if(password.length < 8) { 
        password_requirements.push("Error: Password must be at least 8 characters")
    }
    if(password.search(/[a-z]/) < 0) { 
        password_requirements.push("Error: Password must contain at least one lowercase letter")
    }
    if(password.search(/[A-Z]/) < 0) { 
        password_requirements.push("Error: Password must contain at least one uppercase letter")
    }
    if(password.search(/[0-9]/) < 0) { 
        password_requirements.push("Error: Password must contain at least one number")
    } 
    console.log(password_requirements); 
    if(password_requirements > 0){
        return password_requirements
    }else{
        return true
    }

      
}
