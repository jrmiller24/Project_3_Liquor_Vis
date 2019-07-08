function buildPlot() {
  /* data route */
var url = "/chartdata";
d3.json(url).then(function(response) {

  console.log(response);

  var data = [response];

  var layout = {
    title: "License by Classification in Denver",
    xaxis: {
      title: "Liquor License Classification"
    },
    yaxis: {
      title: "Number of Licenses"
    }
  };

  Plotly.newPlot("plot", data, layout);

});

}
  
buildPlot();
