
loadStackedBar();
loadMonthPie();


//https://dmitripavlutin.com/fetch-with-json/
async function loadStackedBar() {
  const daily_chart = document.getElementById("daily-chart");

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
  const monthly_pie = document.getElementById("monthly-pie")
  // const data = {
  //   labels: ['data 1', 'data 2', 'data 3', 'data 4', 'data 5'],
  //   datasets: [
  //     {
  //       label: 'Dataset 1',
  //       data: [10, 20, 15, 30, 25],
  //       backgroundColor: ["#fc0303", "#1703fc", "#a903fc", "#03c6fc", "#d3f54c"],
  //     }
  //   ]
  // };


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