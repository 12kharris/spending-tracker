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



// new Chart(daily_chart, {
//     type: 'line',
//     data: {
//       labels: labels,
//       datasets: [{
//         label: 'Expenditure',
//         data: data,
//         borderWidth: 1
//       }]
//     },
//     options: {
//         maintainAspectRatio: false,
//       scales: {
//         y: {
//           beginAtZero: true
//         }
//       }
//     }
//   });


const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: -100, max: 100};
  
const months = ["2024-06-01", "2024-06-02"]
  const dataset = {
    labels: labels,
    datasets: [
      {
        label: 'Car',
        data: [10.0, 25.0],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
      },
      {
        label: 'Housing',
        data: [250.0, 0],
        backgroundColor: 'rgba(255, 159, 64, 0.2)',
      },
      {
        label: 'Groceries',
        data: [4.64, 22],
        backgroundColor: 'rgba(255, 205, 86, 0.2)',
      },
    ]
  };
  
      
      

  const config = {
    type: 'bar',
    data: dataset,
    options: {
      plugins: {
        title: {
          display: true,
          text: 'Chart.js Bar Chart - Stacked'
        },
      },
      responsive: true,
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true
        }
      }
    }
  };

  const stackedBar = new Chart(daily_chart, config);