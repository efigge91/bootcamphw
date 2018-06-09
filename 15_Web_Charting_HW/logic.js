// Store our API endpoint urls
var earthquakeURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";
var faultsURL = "https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json";
  
// Function with urls
renderMap(earthquakeURL, faultsURL);
  
function renderMap(earthquakeURL, faultsURL) {
    // Perform a GET request to the earthquake URL
    d3.json(earthquakeURL, function(data) {    
     // Stores response in earthquakeData
     var earthquakeData = data;
     console.log(earthquakeData);
     // Performs GET request to the fault lines URL
     d3.json(faultsURL, function(data) {
         // Stores response into faultLineData
         var faultData = data;
         console.log(faultData);
  
    // Once we get a response, send the data objects to the createFeatures function
    createFeatures(earthquakeData, faultData);
    });
  });
  
  // Define a function we want to run once for each feature in the features array
  function createFeatures(earthquakeData,faultData) {
  
    // Create markers based on magnitude and popup describing the place and time of the earthquake
    function onEachQuakeLayer(feature, layer) {
      return new L.circleMarker([feature.geometry.coordinates[1], feature.geometry.coordinates[0]], {
        fillOpacity: .7,
        color: chooseColor(feature.properties.mag),
        fillColor: chooseColor(feature.properties.mag),
        radius:  markerSize(feature.properties.mag)
      });
    }
    function onEachEarthquake(feature, layer) {
      layer.bindPopup("<h3>" + feature.properties.place +
        "</h3><hr><p>" + "Magnitude: " + feature.properties.mag + ". " + new Date(feature.properties.time) + "</p>");
    };
  
    // Create fault lines
    function onEachFault(feature, layer) {
    L.polyline(feature.geometry.coordinates);
    };
  
    // Creates a GeoJSON layer containing the features array of the earthquakeData object
    var earthquakes = L.geoJSON(earthquakeData, {
      onEachFeature: onEachEarthquake,
      pointToLayer: onEachQuakeLayer
    });
  
  // Creates a GeoJSON layer containing the features array of the faultLineData object
  // Run the onEachFaultLine function once for each element in the array
    var faultLines = L.geoJSON(faultData, {
      onEachFeature: onEachFault,
      style: {
        weight: 2,
        color: 'blue'
      }
    });
    
    
    // Creates a Timeline layer containing the features array of the earthquakeData object
    // Run getInterval function to get the time interval for each earthquake (length based on magnitude)
    // Run the onEachEarthquake & onEachQuakeLayer functions once for each element in the array
    var timelineLayer = L.timeline(earthquakeData, {
        getInterval: function(feature) {
          return {
            start: feature.properties.time,
            end: feature.properties.time + feature.properties.mag * 10000000
          };
        },
        pointToLayer: onEachQuakeLayer,
        onEachFeature: onEachEarthquake
    });
  
    // Sends earthquakes, fault lines and timeline layers to the createMap function
    createMap(earthquakes, faultLines, timelineLayer);
  };
  
  
  function   createMap(earthquakes, faultLines, timelineLayer) {
    // Define variables for our base layers
    let mapboxUrl = 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}';
    let accessToken = 'pk.eyJ1IjoicmluY2tkIiwiYSI6ImNpamc3ODR1aDAxMmx0c2x0Zm9lc3E1OTAifQ.pIkP7PdJMrR5TBIp93Dlbg';
    let streetMap = L.tileLayer(mapboxUrl, {id: 'mapbox.light', maxZoom: 20, accessToken: accessToken});
    let darkMap = L.tileLayer(mapboxUrl, {id: 'mapbox.dark', maxZoom: 20, accessToken: accessToken});
    let outdoorsMap = L.tileLayer(mapboxUrl, {id: 'mapbox.outdoors', maxZoom: 20, accessToken: accessToken});
    let satelliteMap = L.tileLayer(mapboxUrl, {id: 'mapbox.satellite', maxZoom: 20, accessToken: accessToken});
  
  
    // Define a baseMaps object to hold our base layers
    var baseMaps = {
      "Street Map": streetMap,
      "Dark Map": darkMap,
      "Outdoors": outdoorsMap,
      "Satellite": satelliteMap
    };
  
    // Create overlay object to hold our overlay layer
    var overlayMaps = {
      "Earthquakes": earthquakes,
      "Fault Lines": faultLines
    };
  
    // Create our map, giving it the streetmap and earthquakes layers to display on load
    var myMap = L.map("map", {
      center: [
        37.09, -95.71
      ],
      zoom: 4,
      layers: [outdoorsMap, faultLines],
      scrollWheelZoom: false
    });
  
    // Create a layer control
    // Pass in our baseMaps and overlayMaps
    // Add the layer control to the map
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);
  
    // Adds Legend
    var legend = L.control({position: 'bottomright'});
  
    legend.onAdd = function (myMap) {
    
        var div = L.DomUtil.create('div', 'info legend'),
            colors = ["red", "orange", "gold", "yellow", "yellowgreen","greenyellow"]
            grades = [0,1,2,3,4,5];
            div.innerHTML = '<h3>Magnitude</h3>'
        // loop through our intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
          div.innerHTML +=
              '<i class="legend" style="background:' + colors[i] + '; color:' + colors[i] + ';">....</i> ' +
              grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '++');
      }
      return div;
    };
    
    legend.addTo(myMap);
    
    var timelineControl = L.timelineSliderControl({
          formatOutput: function(date) {
          return new Date(date).toString();
          }
      });
      timelineControl.addTo(myMap);
      timelineControl.addTimelines(timelineLayer);
      timelineLayer.addTo(myMap);
      };
  }
  
  // Returns color for each grade parameter using ternary expressions
  function chooseColor(magnitude) {
    return magnitude > 5 ? "red":
           magnitude > 4 ? "orange":
           magnitude > 3 ? "gold":
           magnitude > 2 ? "yellow":
           magnitude > 1 ? "yellowgreen":
                           "greenyellow"; // <= 1 default
  };
  
 

  // Function to amplify circle size by earthquake magnitude
  function markerSize(magnitude) {
      return magnitude * 4;
  };
