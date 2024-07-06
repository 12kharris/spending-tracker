const daily_chart = document.getElementById("daily-chart");

const data_rows = document.getElementsByTagName("tr");

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
        data: ["10.0", "25.0"],
        backgroundColor: 'rgba(255, 99, 132, 0.8)',
      },
      {
        label: 'Housing',
        data: [250.0, 0],
        backgroundColor: 'rgba(255, 159, 64, 0.8)',
      },
      {
        label: 'Groceries',
        data: [4.64, 22],
        backgroundColor: 'rgba(255, 205, 86, 0.8)',
      },
    ]
  };
  
      
      

  const config = {
    type: 'bar',
    options: {
      plugins: {
        title: {
          display: true,
          text: 'Spending by Day'
        },
      },
      responsive: true,
      maintainAspectRatio: false,
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

let stackedBar = new Chart(daily_chart, config);

const year = 2024;
const month = 6;

getChartData(year, month);



//https://dmitripavlutin.com/fetch-with-json/
async function getChartData(year, month) {
  console.log(window.location.href);
  const response = await fetch(`${window.location.href}${year}/${month}`, {
    headers: {
      'Accept': 'application/json'
    }
  });
  const data = await response.json();
  const labels = data.data.labels;
  const datasets = data.data.datasets;
  
  stackedBar.data.datasets = [];
  stackedBar.data.labels = [];

  console.log(data)

  stackedBar.data.labels = labels;
  datasets.forEach(dataset => {
    stackedBar.data.datasets.push(dataset);
  });
  
  stackedBar.update()
}