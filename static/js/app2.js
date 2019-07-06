
function buildPlot() {
    /* data route */
  var url = "/piedata";
  d3.json(url).then(function(response) {
  
    console.log(response);
  
    var data = [response];

    var layout = {
      height: 400,
      width: 500
      }
  
    Plotly.newPlot('pie', data, layout);
    
  });
  }

  
  buildPlot();