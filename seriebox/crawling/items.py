# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Episode(scrapy.Item):
    numero = scrapy.Field()
    titreEn = scrapy.Field()
    titreFr = scrapy.Field()
    dateDiffusion = scrapy.Field()
    note = scrapy.Field()
class Saison(scrapy.Item):
    numero = scrapy.Field()
    episode = scrapy.Field(serializer=Episode)
class Serie(scrapy.Item):
    nom = scrapy.Field()
    synopsis = scrapy.Field()
    dureeEp = scrapy.Field()
    pays = scrapy.Field()
    producteur = scrapy.Field()
    acteurs = scrapy.Field()
    dateDiffusion = scrapy.Field()
    etat = scrapy.Field()
    note = scrapy.Field()
    nombreVotes = scrapy.Field()
    genres = scrapy.Field()
    saison = scrapy.Field(serializer=Saison)
