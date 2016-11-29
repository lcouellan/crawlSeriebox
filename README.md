# crawlSeriebox

Web project for collecting data from a french website Seriebox. This website stores all the series, movies and mangas. 

It's a group project involving Lénaïc Couellan and Raphael Erfani, students in M2-DNR2i from the University of Caen.

## Installing

Clone the repository (localy or in python server)
```
git clone https://github.com/lcouellan/crawlSeriebox.git
cd crawlSeriebox
```
# Launch the spider 

Fill your database with the data from Seriebox.

```
cd seriebox
scrapy crawl seriebox
```

## Launch the application

Update your node installation and start the server.
```
cd server
npm i
node server.js
```

## Built with

* [`NodeJs`](https://nodejs.org)
* [`MongoDb`](https://www.mongodb.com/fr)
* [`MongoDb`](https://scrapy.org/)
* [`D3.js`](https://d3js.org/)
* [`Twig`](http://twig.sensiolabs.org/)


## License

This project is licensed under the GNU License - see the [LICENCE](LICENSE) file for details
