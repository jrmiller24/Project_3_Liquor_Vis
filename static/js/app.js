
function buildPlot() {
  /* data route */
var url = "/chartdata";
d3.json(url).then(function(response) {

  console.log(response);

  var data = [response];

  var layout = {
    title: "Liquor by Type in Denver",
    xaxis: {
      title: "Class"
    },
    yaxis: {
      title: "Count"
    }
  };

  Plotly.newPlot("plot", data, layout);
});
}

buildPlot();
