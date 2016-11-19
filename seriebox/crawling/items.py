# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Episode(scrapy.Item):
    saison = scrapy.Field()
    numero = scrapy.Field()
    titre = scrapy.Field()
    dateDiffusion = scrapy.Field()
    note = scrapy.Field()
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
    episodes = scrapy.Field(serializer=Episode)
