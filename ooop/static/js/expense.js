const amountField = document.querySelector('#amountField');
const amountFeedbackArea= document.querySelector('.amount_feedback');
const submitBtn = document.querySelector('.submit-btn');


amountField.addEventListener("keyup", (e) => {
    const amountVal = e.target.value;
    amountField.classList.remove("is-invalid");
    amountFeedbackArea.style.display = "none";

    if(amountVal.length >0 ) {
        fetch("/validate-amount",{
        body: JSON.stringify({ amount: amountVal}),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                // console.log(data.amount_error);
                if(data.amount_error) {
                    submitBtn.disabled = true;
                    amountField.classList.add("is-invalid");
                    amountFeedbackArea.style.display = "block";
                    amountFeedbackArea.innerHTML=`<p>${data.amount_error}</p>`
                } else {
                    submitBtn.removeAttribute("disabled");
                }

                if(data.amount_info) {
                    submitBtn.removeAttribute("disabled");
                    // amountField.classList.add("is-invalid");
                    amountFeedbackArea.style.display = "block";
                    amountFeedbackArea.innerHTML=`<p>${data.amount_info}</p>`

                }
        });
    }
})

document.querySelector("#today").valueAsDate = new Date();

function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}