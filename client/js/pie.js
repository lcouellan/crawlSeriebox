// Initialize empty array

var data = [];



// Get JSON data and wait for the response

d3.json("../data.json", function(error, json) {

  $ .each(json, function(d,i){

    data.push({

      label: i.nom,

      value: i.popularite

    })

  })



  var pie = new d3pie("pieChart", {

    "header": {

      "title": {

        "text": "Séries les plus vues",

        "fontSize": 22,

        "font": "verdana"

      },

    },

    "size": {

      "canvasHeight": 600,

      "canvasWidth":800

    },

    "data": {

      "content": data

    },

    "labels": {

      "outer": {

        "pieDistance": 32

      }

    }

  });

});