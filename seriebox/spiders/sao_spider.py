import scrapy
import win32api

class SaoSpyder(scrapy.Spider):
    name = "sao"

    def start_requests(self):
        url = 'http://www.seriebox.com/serie/sword-art-online.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for sao in response.css('body'):
            yield {
            	'nom': sao.css('#fiche_v2_header_title h1::text').extract_first(),
            	'dateDiffusion': sao.css('#fiche_v2_header_title p#item_year::text').extract_first(),
                'statut': sao.css('#fiche_v2_header_title p#item_year .status_serie::text').extract_first(),
                'dureeEp':sao.css('#fiche_v2_header_title h3::text').extract_first(),
                'genres': sao.css('#fiche_v2_header_title h3#item_genre a::text').extract(),
                'producteur': sao.css('#fiche_v2_header_title h2 a::text').extract_first(), 
                'acteurs': sao.css('#fiche_v2_header_title h2 a::text').extract(),
                'pays': sao.css('#fiche_v2_header_title h2 img::attr(alt)').extract_first(),            
        		'note': sao.css('#fiche_v2_header_average span.average_number::text').extract_first(),
        		'nombreVotes': sao.css('#fiche_v2_header_average span.nbrevotes_number::text').extract_first(),
        		'synopsis': sao.css('#row_manage_serie #tvshow_synopsis p::text').extract_first()
        	}