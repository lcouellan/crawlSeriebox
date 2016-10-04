import scrapy
import win32api

class SaoSpyder(scrapy.Spider):
    name = "sao"

    def start_requests(self):
        url = 'http://www.seriebox.com/serie/sword-art-online.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sao in response.css('div.col-md-6#fiche_v2_header_title'):
            yield {
            	'nom': sao.css('h1::text').extract_first(),
            	'dateDiffusion': sao.css('p#item_year::text').extract_first(),
                'statut': sao.css('p#item_year .status_serie::text').extract_first(),
                'dureeEp':sao.css('h3::text').extract_first(),
                'genres': sao.css('h3#item_genre a::text').extract(),
                'producteur': sao.css('h2 a::text').extract_first(), 
                'acteurs': sao.css('h2 a::text').extract(),
                'pays': sao.css('img::attr(alt)').extract_first()            
            }
        for sao in response.css('#fiche_v2_header_average'):
        	yield {
        		'note': sao.css('span.average_number::text').extract_first(),
        		'nombreVotes': sao.css('span.nbrevotes_number::text').extract_first()
        	}
        for sao in response.css('div#row_manage_serie'):
        	yield {
        		'synopsis': sao.css('div#tvshow_synopsis p::text').extract_first()
        	}