const express = require("express");
const path = require("path");
const mongoClient = require('mongodb').MongoClient;
const app = express();

app.use(express.static(path.join(__dirname,"../client")));

app.get('/test', (req, res) => {
	mongoClient.connect("mongodb://localhost:27017/seriebox", (err, db) => {
		if (err) {
			return console.dir(err);
		}
		const series = db.collection('series');
		series.find().toArray((err, items) => {
			res.json(items);
			db.close();
		});
	});

})

app.listen(3000, () => {
	console.log("Le serveur est en train d'écouter...");
});