const firstnameField = document.querySelector('#firstnameField');
const lastnameField = document.querySelector('#lastnameField');
const schoolField = document.querySelector('#schoolField');
const postalField = document.querySelector('#postalField');
const usernameField = document.querySelector('#usernameField');
const birthYearField = document.querySelector('#birthField');
const yearField = document.querySelector('#yearField');
const firstnamefeedbackArea= document.querySelector('.firstname_feedback');
const lastnamefeedbackArea= document.querySelector('.lastname_feedback');
const schoolfeedbackArea= document.querySelector('.school_feedback');
const postalfeedbackArea= document.querySelector('.postal_feedback');
const birthYearfeedbackArea= document.querySelector('.birth_feedback');
const yearfeedbackArea= document.querySelector('.year_feedback');
const feedbackArea= document.querySelector('.invalid_feedback');
const emailField = document.querySelector('#emailField');
const passwordField = document.querySelector('#passwordField');
const emailFeedBackArea= document.querySelector('.emailFeedBackArea');
const showPasswordToggle= document.querySelector('.showPasswordToggle');
const submitBtn = document.querySelector('.submit-btn');

const handleToggleInput = (e) => {
  if (showPasswordToggle.textContent === "SHOW") {
    showPasswordToggle.textContent = "HIDE";
    passwordField.setAttribute("type", "text");
  } else {
    showPasswordToggle.textContent = "SHOW";
    passwordField.setAttribute("type", "password");
  }
};

showPasswordToggle.addEventListener("click", handleToggleInput);

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
                    submitBtn.disabled = true;
                    usernameField.classList.add("is-invalid");
                    emailFeedBackArea.style.display = "block";
                    emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
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
                    submitBtn.disabled = true;
                    usernameField.classList.add("is-invalid");
                    feedbackArea.style.display = "block";
                    feedbackArea.innerHTML=`<p>${data.username_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})


firstnameField.addEventListener("keyup", (e) => {
    const firstnameVal = e.target.value;

    firstnameField.classList.remove("is-invalid");
    firstnamefeedbackArea.style.display = "none";

    if(firstnameVal.length >0 ) {
        fetch("/authentication/validate-firstname",{
        body: JSON.stringify({ firstname: firstnameVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.firstname_error);
                if(data.firstname_error) {
                    submitBtn.disabled = true;
                    firstnameField.classList.add("is-invalid");
                    firstnamefeedbackArea.style.display = "block";
                    firstnamefeedbackArea.innerHTML=`<p>${data.firstname_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})


lastnameField.addEventListener("keyup", (e) => {
    const lastnameVal = e.target.value;

    lastnameField.classList.remove("is-invalid");
    lastnamefeedbackArea.style.display = "none";

    if(lastnameVal.length >0 ) {
        fetch("/authentication/validate-lastname",{
        body: JSON.stringify({ lastname: lastnameVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.lastname_error);
                if(data.lastname_error) {
                    submitBtn.disabled = true;
                    lastnameField.classList.add("is-invalid");
                    lastnamefeedbackArea.style.display = "block";
                    lastnamefeedbackArea.innerHTML=`<p>${data.lastname_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})


schoolField.addEventListener("keyup", (e) => {
    const schoolVal = e.target.value;

    schoolField.classList.remove("is-invalid");
    schoolfeedbackArea.style.display = "none";

    if(schoolVal.length >0 ) {
        fetch("/authentication/validate-school",{
        body: JSON.stringify({ school: schoolVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.school_error);
                if(data.school_error) {
                    submitBtn.disabled = true;
                    schoolField.classList.add("is-invalid");
                    schoolfeedbackArea.style.display = "block";
                    schoolfeedbackArea.innerHTML=`<p>${data.school_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})


postalField.addEventListener("keyup", (e) => {
    const postalVal = e.target.value;

    postalField.classList.remove("is-invalid");
    postalfeedbackArea.style.display = "none";

    if(postalVal.length >0 ) {
        fetch("/authentication/validate-postal",{
        body: JSON.stringify({ postal: postalVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.postal_error);
                if(data.postal_error) {
                    submitBtn.disabled = true;
                    postalField.classList.add("is-invalid");
                    postalfeedbackArea.style.display = "block";
                    postalfeedbackArea.innerHTML=`<p>${data.postal_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})


birthYearField.addEventListener("keyup", (e) => {
    const birthYearVal = e.target.value;

    birthYearField.classList.remove("is-invalid");
    birthYearfeedbackArea.style.display = "none";

    if(birthYearVal.length >0 ) {
        fetch("/authentication/validate-birth",{
        body: JSON.stringify({ birth: birthYearVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.birth_error);
                if(data.birth_error) {
                    submitBtn.disabled = true;
                    birthYearField.classList.add("is-invalid");
                    birthYearfeedbackArea.style.display = "block";
                    birthYearfeedbackArea.innerHTML=`<p>${data.birth_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})


yearField.addEventListener("keyup", (e) => {
    const yearVal = e.target.value;

    yearField.classList.remove("is-invalid");
    yearfeedbackArea.style.display = "none";

    if(yearVal.length >0 ) {
        fetch("/authentication/validate-year",{
        body: JSON.stringify({ year: yearVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data.year_error);
                if(data.year_error) {
                    submitBtn.disabled = true;
                    yearField.classList.add("is-invalid");
                    yearfeedbackArea.style.display = "block";
                    yearfeedbackArea.innerHTML=`<p>${data.year_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }
        });
    }
})