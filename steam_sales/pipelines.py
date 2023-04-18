import sqlite3


class SteamSalesPipeline:
    def __init__(self):
        self.con = sqlite3.connect('steam_sales/sales.db')
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            game_name TEXT,
            new_price TEXT,
            old_price TEXT,
            sale TEXT
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO sales (game_name, new_price, old_price, sale) VALUES (?, ?, ?, ?)
        """,
                         (
                             item['game_name'][0],
                             item['new_price'][0],
                             item['old_price'][0],
                             item['sale'][0]
                         ))
        self.con.commit()
        return item
