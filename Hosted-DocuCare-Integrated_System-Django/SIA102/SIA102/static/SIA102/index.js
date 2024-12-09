document.getElementById("login-btn").addEventListener("click", function() {
    const loginForm = document.getElementById("login-form");
    document.getElementById("dim-bg").style.display = "block";   
    
    loginForm.style.display = "flex"; 
    const tl = gsap.timeline();

    // Animate the login form
    tl.from("#login-form", {
        y: 0,
        duration: .5,
        opacity: 0
    });
});

document.getElementById("dim-bg").addEventListener("click", function() {
    document.getElementById("dim-bg").style.display = "none";
    document.getElementById("login-form").style.display = "none";
});
