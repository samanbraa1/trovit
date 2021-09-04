import scrapy
#h22222
from scrapy.crawler import CrawlerProcess
class T1Spider(scrapy.Spider):
    name = 't1'
  #  allowed_domains = ['homes.trovit.com']
    start_urls = []
    pn=2
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1
    }
    def __init__(self):
        url = 'https://homes.trovit.com/ny/'

        for page in range(1, 6):
            self.start_urls.append(url + str(page))

    def parse(self, response):

        w=response.css('div.snippet-wrapper.js-item-wrapper')
        for h in w:
            yield{
                'name':h.css('.item-title span::text').get(),
                'img':h.css('img::attr(src)').get(),
                'price': h.css('.actual-price::text').get(),
                'des':h.css('div.item-description p::text').get()

            }

       # next_page = f"https://homes.trovit.com/ny/{T1Spider.pn}"
       # if  T1Spider.pn<=50:

           # T1Spider.pn=+1
          #  yield response.follow(next_page, callback=self.parse)



