function login(){
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email == "user" && password == "user"){
    window.location = "profile.html";
    return false;
    }
    else if(email == "admin" && password == "admin"){
    window.location = "adminviewrecords.html";
    return false;
    }
    else{
    alert("email: user \n password: user\n or \n email: admin \n password: admin");
    }
}