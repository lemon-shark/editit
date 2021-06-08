const usernameField = document.querySelector('#usernameField');
const feedbackArea= document.querySelector('.invalid_feedback');
const emailField = document.querySelector('#emailField');
const emailFeedBackArea= document.querySelector('.emailFeedBackArea');

emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;
    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";

    if(emailVal.length >0 ) {
        fetch("/authentication/validate-email",{
        body: JSON.stringify({ email: emailVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.email_error);
                if(data.email_error) {
                    usernameField.classList.add("is-invalid");
                    emailFeedBackArea.style.display = "block";
                    emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`
                }
        });
    }
})

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display = "none";

    if(usernameVal.length >0 ) {
        fetch("/authentication/validate-username",{
        body: JSON.stringify({ username: usernameVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.username_error);
                if(data.username_error) {
                    usernameField.classList.add("is-invalid");
                    feedbackArea.style.display = "block";
                    feedbackArea.innerHTML=`<p>${data.username_error}</p>`
                }
        });
    }
})