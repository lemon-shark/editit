// document.querySelector("#editDate").valueAsDate = new Date();

var today = new Date().toISOString().split('T')[0];
var sixMonthsAgo = new Date(new Date().getTime() - 184 * 24 * 60 * 60 * 1000).toISOString().split('T')[0]
document.getElementsByName("edit_date")[0].setAttribute('min', sixMonthsAgo);
document.getElementsByName("edit_date")[0].setAttribute('max', today)