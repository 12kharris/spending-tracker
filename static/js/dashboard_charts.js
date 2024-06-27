const daily_chart = document.getElementById("daily-chart");

const data_rows = document.getElementsByTagName("tr");

console.log(data_rows);

let transactions = {};
let labels = [];
let data = [];
let counter = 0;

/**
 * get transactions from the data on the page
 */
for(row of data_rows) {
    if(row.getAttribute("id") == "table-headers") continue; // ignore the header
    let amount = row.getElementsByClassName("amount")[0].innerText;
    let ref = row.getElementsByClassName("reference")[0].innerText;
    let cat = row.getElementsByClassName("category")[0].innerText;
    let date = row.getElementsByClassName("date")[0].innerText;
    
    transactions[counter] = {
        "amount": amount,
        "reference": ref,
        "category": cat,
        "date": date
    };

    labels[counter] = date;
    data[counter] = amount;
    counter++;
}



new Chart(daily_chart, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Expenditure',
        data: data,
        borderWidth: 1
      }]
    },
    options: {
        maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });