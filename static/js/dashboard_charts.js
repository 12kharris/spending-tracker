const daily_chart = document.getElementById("daily-chart");
const monthly_pie = document.getElementById("monthly-pie");
const yearly_chart = document.getElementById("year-chart");
const yearly_pie = document.getElementById("year-pie");

//this script is used across yearly and monthly dashboards
//therefore must account for case where some elements don't exist
if (daily_chart !== null) {
  loadStackedBar(daily_chart, 'Spending by Day');
}
else if (yearly_chart !== null) {
  loadLineChart(yearly_chart, "Spending by Month");
}

if (monthly_pie !== null) {
  loadPie(monthly_pie, 'Monthly Spending Split');
}
else if (yearly_pie !== null) {
  loadPie(yearly_pie, "Yearly Spending Split");
}


//https://dmitripavlutin.com/fetch-with-json/
async function loadStackedBar(chart_element, heading) {
  /**
   * Populate the given stacked bar chart_element with data and load the chart
   */
  const config = {
    type: 'bar',
    options: {
      plugins: {
        title: {
          display: true,
          text: heading,
          font: {
            size: 20
          }
        },
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          stacked: true,
          title: {
            display: true,
            text: 'Date',
            font: {
              size: 16
            }
          }
        },
        y: {
          stacked: true,
          title: {
            display: true,
            text: 'Expenditure',
            font: {
              size: 16
            }
          }
        }
      }
    }
  };
  
  let stackedBar = new Chart(chart_element, config);
  const response = await fetch(`${window.location.href}raw`, {
    headers: {
      'Accept': 'application/json'
    }
  });
  const data = await response.json();
  const labels = data.data.labels;
  const datasets = data.data.datasets;

  stackedBar.data.datasets = [];
  stackedBar.data.labels = [];

  stackedBar.data.labels = labels;
  datasets.forEach(dataset => {
    stackedBar.data.datasets.push(dataset);
  });

  stackedBar.update();
}

async function loadLineChart(chart_element, heading) {
  /**
   * Populate the given line chart chart_element with data and load the chart
   */
  const config = {
    type: 'line',
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          display: "false",
        },
        title: {
          display: true,
          text: heading,
          font: {
            size: 20
          }
        }
      },
      scales: {
        x: {
          stacked: true,
          title: {
            display: true,
            text: 'Month Number',
            font: {
              size: 16
            }
          }
        },
        y: {
          stacked: true,
          title: {
            display: true,
            text: 'Total Expenditure',
            font: {
              size: 16
            }
          }
        }
      }
    },
  };

  let lineChart = new Chart(chart_element, config);

  const response = await fetch(`${window.location.href}raw`, {
    headers: {
      'Accept': 'application/json'
    }
  });
  const data = await response.json();
  const labels = data.data.labels;
  const datasets = data.data.datasets;

  lineChart.data.datasets = [];
  lineChart.data.labels = [];

  lineChart.data.labels = labels;
  datasets.forEach(dataset => {
    lineChart.data.datasets.push(dataset);
  });

  lineChart.update();

}

async function loadPie(chart_element, heading) {
  /**
   * Populate the given pie chart chart_element with data and load the chart
   */
  const config = {
    type: 'pie',
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: heading,
          font: {
            size: 20
          }
        }
      }
    },
  };

  let pie = new Chart(chart_element, config);
  const response = await fetch(`${window.location.href}split`, {
    headers: {
      'Accept': 'application/json'
    }
  });
  const data = await response.json();
  const labels = data.data.labels;
  const datasets = data.data.datasets;

  pie.data.datasets = [];
  pie.data.labels = [];

  pie.data.labels = labels;
  datasets.forEach(dataset => {
    pie.data.datasets.push(dataset);
  });

  pie.update();
}

