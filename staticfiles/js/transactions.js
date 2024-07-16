const edit_buttons = document.getElementsByClassName("btn-edit-transaction");
const submit_button = document.getElementById("btn-submit");
const cancel_button = document.getElementById("btn-cancel");
const transaction_form = document.getElementById("form-transaction");
const transaction_form_amount = document.getElementById("form-amount");
const transaction_form_reference = document.getElementById("form-ref");
const transaction_form_category = document.getElementById("form-category");
const transaction_form_date = document.getElementById("form-date");
const transaction_category_options = transaction_form_category.getElementsByTagName("option");
const datepicker = document.getElementById("form-date");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Restrict the date picker to max of current date
let todaydate = new Date();
let yr = `${todaydate.getFullYear()}`;
let mnth = `${todaydate.getMonth() + 1}`;
let day = `${todaydate.getDate()}`;
let fmt_month = mnth.padStart(2, '0');
let fmt_day = day.padStart(2, '0');

datepicker.setAttribute("max", `${yr}-${fmt_month}-${fmt_day}`);

/**
 * Add event listeners which populate the transaction form with data from the selected transaction
 */
for(let button of edit_buttons) {
    button.addEventListener("click", (e) => {
        let transaction_id = e.target.getAttribute("data-transaction_id");
        let transaction_amount = document.getElementById(`amount-${transaction_id}`).innerText;
        let transaction_reference = document.getElementById(`reference${transaction_id}`).innerText;
        let transaction_category = document.getElementById(`category-${transaction_id}`).innerText;
        let transaction_date = document.getElementById(`transaction_date-${transaction_id}`).innerText;

        let category_element;
        for(let option of transaction_category_options) {
            if(option.innerText == transaction_category) {
                category_element = option;
            }
        }

        transaction_form_amount.value = transaction_amount;
        transaction_form_category.value = category_element.value;
        transaction_form_reference.value = transaction_reference;

        //format the date to YYYY-MM-DD
        date = new Date(transaction_date);
        let yr = `${date.getFullYear()}`;
        let mnth = `${date.getMonth() + 1}`;
        let day = `${date.getDate()}`;

        let fmt_month = mnth.padStart(2, '0');
        let fmt_day = day.padStart(2, '0');

        transaction_form_date.value = `${yr}-${fmt_month}-${fmt_day}`;

        //change form action to call the transaction_edit function
        transaction_form.setAttribute("Action", `transaction_edit/${transaction_id}`);
        submit_button.innerText = "Update";
        transaction_form_category.focus();
    });
}

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let transaction_id = e.target.getAttribute("data-transaction_id");
      deleteConfirm.href = `transaction_delete/${transaction_id}`;
      deleteModal.show();
    });
  }

//clear the form when cancel is called and remove edit form action
cancel_button.addEventListener("click", (e) => {
    transaction_form_amount.value = 0.01;
    transaction_form_category.value = 1;
    transaction_form_reference.value = "";
    transaction_form_date.value = "dd/mm/yyyy";

    transaction_form.removeAttribute("Action");
    submit_button.innerText = "Add Expenditure";
});