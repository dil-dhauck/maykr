import random
from typing import Dict, Optional

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

    def random_bool(self, is_mandatory: Optional[bool] = False) -> str:
        if is_mandatory:
            return self.pick_random(["Yes", "True", "No", "False"])
        else:
            return self.pick_random(["Yes", "True", "No", "False", " "])

    def random_date(self, is_mandatory: Optional[bool] = False) -> str:
        if is_mandatory:
            return str(self.fake.date_between(start_date="-10y", end_date="today"))
        else:
            return self.pick_random([str(self.fake.date_between(start_date="-10y", end_date="today")), " "])

    def new_file_name(self) -> str:
        return (
            f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"
        )

    def write_records(self, ws, columns: Dict, headers: Dict, records: list) -> None:
        for col, header in headers.items():
            ws[f"{col}1"] = header
        for row, record in enumerate(records, start=2):
            for col, field in columns.items():
                ws[f"{col}{row}"] = record[field]

    # def fill_sheet(self, data: Dict, workbook, quantity: int) -> None:
    #     for column, (header, value) in data.items():
    #         workbook[f"{column}1"] = header
    #         for row in range(2, quantity + 2):
    #             workbook[f"{column}{row}"] = value()
