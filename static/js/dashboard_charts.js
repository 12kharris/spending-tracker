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



getChartData();



//https://dmitripavlutin.com/fetch-with-json/
async function getChartData() {
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