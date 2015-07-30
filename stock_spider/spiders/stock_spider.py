import scrapy

class StockSpider(scrapy.spiders.Spider):
    name = "stock"

    def __init__(self):
        base = "http://finance.sina.com.cn/realstock/company/%s/nc.shtml"

        self.start_urls = []
        stockCodeBase = "sh"

        for x in range(600000, 602000):
            stockCode = stockCodeBase + str(x)

            self.start_urls.append(base % stockCode)
        # print self.start_urls

    def parse(self, response):
        name = response.xpath('//h1[@id="stockName"]/text()')[0].extract()
        price = response.xpath('//h1[@id="price"]/text()')[0].extract()

        print name + ":" + price
        # for sel in response.selector.xpath('//div[@id="stock_name"]'):
        #     print "======"
        #     print sel
        #     stock_name = sel.extract()
        #     print stock_name
