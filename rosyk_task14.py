from datetime import datetime, timedelta

from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook


class Multiset:
    def __init__(self, items=None):
        self.items = {} if items is None else items.copy()

    def clear(self):
        self.items.clear()

    def is_empty(self):
        return not bool(self.items)

    def add(self, item):
        self.items[item] = self.items.get(item, 0) + 1

    def remove(self, item):
        try:
            if self.items[item] > 1:
                self.items[item] -= 1
            else:
                del self.items[item]
        except KeyError as exc:
            raise ValueError('Element not found') from exc

    def count(self, item):
        return self.items.get(item, 0)

    def union(self, other_set):
        union_set = Multiset(self.items)
        for item, count in other_set.items.items():
            if item in union_set.items:
                union_set.items[item] = max(union_set.items[item], count)
            else:
                union_set.items[item] = count
        return union_set

    def intersection(self, other_set):
        intersection_set = Multiset()
        for item, count in self.items.items():
            if item in other_set.items:
                intersection_set.items[item] = min(count, other_set.items[item])
        return intersection_set

    def __str__(self):
        return str(self.items)


def exel_weather(city):
    url = 'https://sinoptik.ua/погода-' + city
    work_book = Workbook()
    work_sheet = work_book.active
    work_sheet.append(["date", "max temperature", "min temperature"])
    response = requests.get(url, timeout=None)
    soup = BeautifulSoup(response.content, 'html.parser')
    weather_blocks = soup.find_all('div', {'class': 'main'}, limit=5)
    for i, day in enumerate(weather_blocks):
        min_temp = str(day.find('div', {'class': 'temperature'}).find('div', {'class': 'min'}).text).strip('мин. ')
        max_temp = str(day.find('div', {'class': 'temperature'}).find('div', {'class': 'max'}).text).strip('макс. ')
        date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
        work_sheet.append([date, max_temp, min_temp])
        work_book.save("weather_forecast.xlsx")


if __name__ == '__main__':
    m = Multiset()
    print(m.is_empty())
    m.add(3)
    m.add(3)
    print(m)
    print(m.union(Multiset({4: 2})))
    print(m.intersection(Multiset({3: 1})))
    exel_weather('киев')
