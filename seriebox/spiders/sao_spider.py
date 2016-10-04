import scrapy
import win32api

class SaoSpyder(scrapy.Spider):
    name = "sao"

    def start_requests(self):
        url = 'http://www.seriebox.com/serie/sword-art-online.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sao in response.css('div#fiche_v2_header_title'):
            yield {
                'nom': sao.css('h1::text').extract(),
                'statut': sao.css('p#item_year .status_serie::text').extract(),
                'synopsis':sao.css('div#tvshow_synopsis p::text').extract()
            }