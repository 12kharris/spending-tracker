const daily_chart = document.getElementById("daily-chart");
const monthly_pie = document.getElementById("monthly-pie")

loadStackedBar();
loadMonthPie();


//https://dmitripavlutin.com/fetch-with-json/
async function loadStackedBar() {
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

  stackedBar.update()
}

async function loadMonthPie() {
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
          text: 'Monthly Spending Split'
        }
      }
    },
  };

  let pie = new Chart(monthly_pie, config);
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

const config = {
  type: 'line',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Chart.js Line Chart'
      }
    }
  },
};