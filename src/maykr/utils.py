import random
from typing import Dict

from faker import Faker

from maykr.config import Config

class Utils():

    def __init__(self):
        self.fake = Faker()
        self.config = Config()

    def pick_random(self, items: list) -> str:
        return random.choice(items)

    def pick_header(self, items: list) -> str:
        return random.choice(items)

    def random_date(self) -> str:
        return self.pick_random([str(self.fake.date_between(start_date="-10y", end_date="today")), " "])

    def new_file_name(self) -> str:
        return (
            f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"
        )

    def fill_sheet(self, data: Dict, workbook, quantity: int) -> None:
        for column, (header, value) in data.items():
            workbook[f"{column}1"] = header
            for row in range(2, quantity + 2):
                workbook[f"{column}{row}"] = value()
