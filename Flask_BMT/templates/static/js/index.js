function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if (username === "admin" && password === "admin") {
        window.location.href = "admin_page.html";
    } else if (username === "user" && password === "user") {
        window.location.href = "user_page.html";
    } else {
        document.querySelector(".login-form").insertAdjacentHTML("beforeend", "<p class='error-message'>Invalid username or password.</p>");
    }
}
