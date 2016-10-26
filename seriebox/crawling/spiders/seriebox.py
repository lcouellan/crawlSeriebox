# -*- coding: utf-8 -*-
import scrapy
import encodings
import win32api
from crawling.items import Serie


class SerieBoxSpider(scrapy.Spider):
    name = "seriebox"


    def start_requests(self):
        url = 'http://www.seriebox.com/serie/listing_shows.php'
        yield scrapy.Request(url=url, callback=self.parseSeries)

    def parseSeries(self, response):
        liensSeries = response.css('ul.listing_series li')
        for lien in liensSeries:
            url = lien.css('.infos_series h3 a::attr(href)').extract_first()
            if url is not None:
                url = response.urljoin(url)
                req = scrapy.Request(url=url, callback=self.parseSerie)
                req.meta['serie'] = Serie()
                yield req
        next_page = response.css('a.link_suivant::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parseSeries)

    def parseSerie(self, response):
        serie = response.meta['serie']
        el = response.css('body')
        serie['nom'] = el.css('#fiche_v2_header_title h1::text').extract_first(),
        serie['dateDiffusion'] = el.css('#fiche_v2_header_title p#item_year::text').extract_first(),
        serie['etat'] = el.css('#fiche_v2_header_title p#item_year .status_serie::text').extract_first(),
        serie['dureeEp'] = el.css('#fiche_v2_header_title h3::text').extract_first(),
        serie['genres'] =  el.css('#fiche_v2_header_title h3#item_genre a::text').extract(),
        serie['producteur'] =  el.css('#fiche_v2_header_title h2 a::text').extract_first(), 
        serie['acteurs'] =  el.css('#fiche_v2_header_title h2 a::text').extract(),
        serie['pays'] = el.css('#fiche_v2_header_title h2 img::attr(alt)').extract_first(),            
        serie['note'] = el.css('#fiche_v2_header_average span.average_number::text').extract_first(),
        serie['nombreVotes'] = el.css('#fiche_v2_header_average span.nbrevotes_number::text').extract_first(),
        serie['synopsis'] = el.css('#row_manage_serie #tvshow_synopsis p::text').extract_first()
        
        return serie
