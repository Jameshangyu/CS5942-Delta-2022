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