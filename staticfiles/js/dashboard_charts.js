const daily_chart = document.getElementById("daily-chart");
const monthly_pie = document.getElementById("monthly-pie");
const yearly_chart = document.getElementById("year-chart");
const yearly_pie = document.getElementById("year-pie");

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
  const config = {
    type: 'bar',
    options: {
      plugins: {
        title: {
          display: true,
          text: heading
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
  
  let stackedBar = new Chart(chart_element, config);
  const response = await fetch(`${window.location.href}raw`, {
    headers: {
      'Accept': 'application/json'
    }
  });
  const data = await response.json();
  const labels = data.data.labels;
  console.log(data.data.labels);
  console.log(data.data.datasets);
  const datasets = data.data.datasets;

  stackedBar.data.datasets = [];
  stackedBar.data.labels = [];

  stackedBar.data.labels = labels;
  datasets.forEach(dataset => {
    stackedBar.data.datasets.push(dataset);
  });

  stackedBar.update()
}

async function loadLineChart(chart_element, heading) {
  const config = {
    type: 'line',
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: heading
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

  lineChart.update()

}

async function loadPie(chart_element, heading) {
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
          text: heading
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

  pie.update()
}

