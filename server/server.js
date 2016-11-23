const express = require("express");
const path = require("path");
const mongoClient = require('mongodb').MongoClient;
const app = express();
var Twig = require("twig");



app.use(express.static(path.join(__dirname,"../client")));
app.set('views', path.join(__dirname, '../client/views/'));

app.get('/index', (req, res) => {
	mongoClient.connect("mongodb://localhost:27017/seriebox", (err, db) => {
		if (err) {
			return console.dir(err);
		}
		const series = db.collection('series');
		series.find({},{_id:0 , nom:1,nombreVotes:1}).toArray((err, series) => {
			res.render('index.twig', {
                    series : series,
             });
			db.close();
		});
	});
});

app.listen(3000, () => {
	console.log("Le serveur est en train d'écouter...");
});