// Creating map object
var map = L.map('map', {
  center: [39.7392, -104.9903],
  zoom: 13
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(map);

var neighborhood_data = 'Resources/statistical_neighborhoods.geojson';
var license_data = 'Resources/license_data.geojson';

// Our style object
var mapStyle = {
color: "white",
fillColor: "gray",
fillOpacity: 0.5,
weight: 1.5
};

// Grabbing our GeoJSON data..
d3.json(neighborhood_data, function(data) {
// Creating a geoJSON layer with the retrieved data
L.geoJson(data, {
  // Passing in our style object
  style: mapStyle,

// Called on each feature
  onEachFeature: function(feature, layer) {
    // Set mouse events to change map styling
    layer.on({
      // When a user's mouse touches a map feature, the mouseover event calls this function, that feature's opacity changes to 90% so that it stands out
      mouseover: function(event) {
        layer = event.target;
        layer.setStyle({
          fillOpacity: 0.2
        });
        
      },
      // When the cursor no longer hovers over a map feature - when the mouseout event occurs - the feature's opacity reverts back to 50%
      mouseout: function(event) {
        layer = event.target;
        layer.setStyle({
          fillOpacity: 0.5
        });
      },
      // When a feature (neighborhood) is clicked, it is enlarged to fit the screen
      click: function(event) {
        map.fitBounds(event.target.getBounds());
      }
    });
    // Giving each feature a pop-up with information pertinent to it
    layer.bindPopup("<h1>" + feature.properties.NBHD_NAME + "</h1>");

  }
}).addTo(map);


});

d3.json(license_data, function(data) {
console.log(data.features); 


var arts_marker = L.markerClusterGroup();
var hotel_rest_marker = L.markerClusterGroup();
var tavern_marker = L.markerClusterGroup();
var brewery_marker = L.markerClusterGroup();
var retail_marker = L.markerClusterGroup();
var special_marker = L.markerClusterGroup();

for (var i = 0; i < data.features.length; i++) {
  var feature = data.features[i];
  var location = feature.geometry.coordinates;
  var marker_format = ("<h1>"+ feature.properties.Business_Name + "</h1>" + "<b>"
  + feature.properties.Business_Address + "<b>" + "<h3>" +
  `License Type : ${feature.properties.License_Type}`+ "<h3>");

  if (feature.properties.License_Type == 'Arts') {
    arts_marker.addLayer(L.marker([location[1], location[0]]).bindPopup(marker_format))
    ;
  } 
  else if (feature.properties.License_Type == 'Hotel / Restaurant') {
      hotel_rest_marker.addLayer(L.marker([location[1], location[0]]).bindPopup(marker_format))
      ;
  } 
  else if(feature.properties.License_Type == 'Tavern') {
      tavern_marker.addLayer(L.marker([location[1], location[0]]).bindPopup(marker_format))
      ;
  } 
  else if (feature.properties.License_Type == 'Brewery / Distillery'){
      brewery_marker.addLayer(L.marker([location[1], location[0]]).bindPopup(marker_format))
      ;
  } 
  else if (feature.properties.License_Type == 'Retail'){
      retail_marker.addLayer(L.marker([location[1], location[0]]).bindPopup(marker_format))
      ;
  } 
  else {special_marker.addLayer(L.marker([location[1], location[0]]).bindPopup(marker_format))
    ;}

}
var overlay_layers = {
  "Arts": arts_marker,
  "Hotel": hotel_rest_marker,
  "Tavern": tavern_marker,
  "Brewery": brewery_marker,
  "Retail": retail_marker,
  "Special": special_marker
};

L.control.layers(null,overlay_layers).addTo(map);



});