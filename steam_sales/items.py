from scrapy.item import Item, Field


class SteamSalesItem(Item):
    game_name = Field()
    new_price = Field()
    old_price = Field()
    sale = Field()
