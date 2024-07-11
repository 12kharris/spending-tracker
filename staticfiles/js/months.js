const month_selector = document.getElementById("month-selector");
const year_selectors = document.getElementsByClassName("year-selector");
const year_selector = document.getElementById("year-selector");
const today = new Date();
const current_year = today.getFullYear();
const current_month = today.getMonth() + 1;
const url_dirs = window.location.href.split("/")
const selected_year = url_dirs[4];
const selected_month = url_dirs[5];

for (let selector of year_selectors) {
    let year_element;
    let year_options = selector.getElementsByTagName("option");
    for(let option of year_options) {
        if(option.innerText == selected_year) {
            year_element = option;
        }
    }
    selector.value = year_element.value;

    selector.addEventListener("change", getValidMonths);
}


getValidMonths();
populateMonth();


function getValidMonths() {
    month_selector.innerHTML = "";
    month_selector.innerHTML += "<option>All</option>";
    if (year_selector.value == current_year) {
        for (let i = 1; i <= current_month; i++) {
            month_selector.innerHTML += `<option>${i}</option>`;
        }  
    }
    else {
        for (let i = 1; i <= 12; i++) {
            month_selector.innerHTML += `<option>${i}</option>`;
        } 
    }
}

function populateMonth() {
    let month_element;
    let month_options = month_selector.getElementsByTagName("option");
    if (selected_month === "") {
        month_element = month_options[0];
    }

    for(let option of month_options) {
        if(option.innerText == selected_month) {
            month_element = option;
        }
    }

    month_selector.value = month_element.value;
} 