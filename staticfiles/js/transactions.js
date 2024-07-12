const edit_buttons = document.getElementsByClassName("btn-edit-transaction");
const delete_buttons = document.getElementsByClassName("btn-delete-transaction");
const submit_button = document.getElementById("btn-submit");
const transaction_form = document.getElementById("form-transaction");
const transaction_form_amount = document.getElementById("form-amount");
const transaction_form_reference = document.getElementById("form-ref");
const transaction_form_category = document.getElementById("form-category");
const transaction_form_date = document.getElementById("form-date");
const transaction_category_options = transaction_form_category.getElementsByTagName("option");


/**
 * Add event listeners which populate the transaction form with data from the selected transaction
 */
for(let button of edit_buttons) {
    button.addEventListener("click", (e) => {
        let transaction_id = e.target.getAttribute("transaction_id");
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

        date = new Date(transaction_date);
        let yr = `${date.getFullYear()}`;
        let mnth = `${date.getMonth() + 1}`;
        let day = `${date.getDate()}`;

        let fmt_month = mnth.padStart(2, '0');
        let fmt_day = day.padStart(2, '0');

        transaction_form_date.value = `${yr}-${fmt_month}-${fmt_day}`;

        transaction_form.setAttribute("Action", `transaction_edit/${transaction_id}`)
        submit_button.innerText = "Update";
    })
}

