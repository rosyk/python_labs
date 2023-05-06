import scrapy
from steam_sales.items import SteamSalesItem
from scrapy.loader import ItemLoader


class SalesSpider(scrapy.Spider):
    name = 'sales'

    start_urls = ['https://gg.deals/deals/steam-deals']

    def parse(self, response):
        self.logger.info('steam sales spider')
        games = response.xpath('//*[@id="deals-list"]/div[1]/div[1]/div')
        for game in games:
            loader = ItemLoader(item=SteamSalesItem(), selector=game)
            loader.add_xpath('game_name', 'div[@class="game-info-wrapper"]/div/a/text()')
            loader.add_xpath('new_price', 'div[3]/div[3]/a/span/text()')
            loader.add_xpath('old_price', 'div[3]/div[3]/span/text()')
            loader.add_xpath('sale', 'div[3]/div[4]/span/text()')
            sales_item = loader.load_item()
            yield sales_item
