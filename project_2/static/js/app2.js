
function buildPlot() {
    /* data route */
  var url = "/piedata";
  d3.json(url).then(function(response) {
  
    console.log(response);
  
    var data = [response];

    var layout = {
      title: "License Classification in Denver",
      height: 600,
      width: 700
      }
  
    Plotly.newPlot('pie', data, layout);
    
  });
  }

  
  buildPlot();