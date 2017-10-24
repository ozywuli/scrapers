import scrapy

class BlogSpider(scrapy.Spider):
    # name = 'blogspider'
    # start_urls = ['https://blog.scrapinghub.com']

    # def parse(self, response):
    #     for title in response.css('h2.entry-title'):
    #         yield {'title': title.css('a ::text').extract_first()}

    #     for next_page in response.css('div.prev-post > a'):
    #         yield response.follow(next_page, self.parse)



    # scrapy runspider myspider.py -o henkubao.csv -t csv

    name = 'henkubao'
    start_urls = ['https://henkubao.com']

    def parse(self, response):
        for title in response.css('.article-grid__card'):
            yield {
                'title': title.css('h3 a ::text').extract_first(),
                'subtitle': title.css('.article-grid__excerpt ::text').extract_first()
            }