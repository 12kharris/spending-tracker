const daily_chart = document.getElementById("daily-chart");

const data_rows = document.getElementsByTagName("tr");

console.log(data_rows);

let data = {}
let counter = 0
for(row of data_rows) {
    if(row.getAttribute("id") == "table-headers") continue;
    
    data[counter] = {
        "amount": row.getElementsByClassName("amount")[0].innerText,
        "reference": row.getElementsByClassName("reference")[0].innerText,
        "category": row.getElementsByClassName("category")[0].innerText,
        "date": row.getElementsByClassName("date")[0].innerText
    };
    counter++;
}
console.log(data);


new Chart(daily_chart, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
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