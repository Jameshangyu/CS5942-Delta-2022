const ctx = document.getElementById('myChart').getContext('2d');

//1st chart scripts
const labels1 = [
    'Mon',
    'Tue',
    'Wed',
    'Thur',
    'Fri',
    'Sat',
  ];

  const data1 = {
    labels: labels1,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    },
    {
        label: 'My Second dataset',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [0, 15, 55, 25, 2, 3, 40],
      }]
  };

  const config1 = {
    type: 'line',
    data: data1,
    options: {}
  };

  const myChart1 = new Chart(
    document.getElementById('myChart'),
    config1
  );



//2nd chart scripts
const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
  ];

  const data = {
    labels: labels,
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: [0, 10, 5, 2, 20, 30, 45],
    }] 
  };

  const config = {
    type: 'line',
    data: data,
    options: {}
  };

  const myChart2 = new Chart(
    document.getElementById('myChart2'),
    config
  );
  const myChart3 = new Chart(
    document.getElementById('myChart3'),
    config
  );
  const myChart4 = new Chart(
    document.getElementById('myChart4'),
    config1
  );
  const myChart5 = new Chart(
    document.getElementById('myChart5'),
    config1
  );
  const myChart6 = new Chart(
    document.getElementById('myChart6'),
    config
  );

  

  var piectx = document.getElementById("pieChart").getContext('2d');
var myChart = new Chart(piectx, {
  type: 'pie',
  data: {
    labels: ["Green", "Blue", "Purple", "Yellow", "Red", "Black"],
    datasets: [{
      backgroundColor: [
        "#2ecc71",
        "#3498db",
        "#9b59b6",
        "#f1c40f",
        "#e74c3c",
        "#34495e"
      ],
      data: [12, 19, 17, 28, 24, 7]
    }]
  }
});
// // pieChart for colour analysis
// const pieconfig = {
//   type: 'pie',
//   data: piedata,
//   options: {
//     responsive: true,
//     plugins: {
//       legend: {
//         position: 'top',
//       },
//       title: {
//         display: true,
//         text: 'Chart.js Pie Chart'
//       }
//     }
//   },
// };


// const piedata = {
//   labels: ["Green", "Blue", "Gray", "Purple", "Yellow", "Red", "Black"],
//     datasets: [{
//       backgroundColor: [
//         "#2ecc71",
//         "#3498db",
//         "#95a5a6",
//         "#9b59b6",
//         "#f1c40f",
//         "#e74c3c",
//         "#34495e"
//       ],
//       data: [12, 19, 3, 17, 28, 24, 7]
//     }]
// };

// const piechart = new Chart(
//   document.getElementById('pieChart'),
//   pieconfig
// );