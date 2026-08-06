import os
from openpyxl import load_workbook
from faker import Faker
from maykr import utils
from maykr.assets import variables
from maykr.config import Config
from pathlib import Path

class Maykr:

    number_of_files_to_generate = 5
    number_of_companies = 35

    def __init__(self):
        self.template = Path(__file__).parent / "assets" / "template.xlsx"
        self.workbook = load_workbook(self.template)
        self.sheet = self.workbook["Entity Details"]
        self.fake = Faker()
        self.utils = utils.Utils()
        self.config = Config()

    def new_file_name(self) -> str:
        return f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"

    # def write_titles(self): #TODO if there is a template.xlsx, this is not needed
    #     self.sheet["A1"] = "Entity Code"
    #     self.sheet["B1"] = "Entity Name"
    #     self.sheet["C2"] = "Company Type"
    #     self.sheet["D2"] = "Company Status"
    #     self.sheet["E2"] = "Registration Number"
    #     self.sheet["F2"] = "Incorporation Date"
    #     self.sheet["G2"] = "Country"
    #     self.sheet["H2"] = "Reg. Office Line 1"
    #     self.sheet["I2"] = "Reg. Office Line 2"
    #     self.sheet["J2"] = "Reg. Office Post Town"
    #     self.sheet["K2"] = "Reg. Office Region"
    #     self.sheet["L2"] = "Reg. Office Post Code"

    def write_company_data(self):
        for row in range(2, self.number_of_companies):
            self.sheet[f"A{row}"] = self.fake.unique.random_int(min=100000, max=999999)
            self.sheet[f"B{row}"] = self.fake.company()
            self.sheet[f"C{row}"] = self.utils.pick_random(variables.COMPANY_TYPES)
            self.sheet[f"D{row}"] = self.utils.pick_random(variables.COMPANY_STATUSES)
            self.sheet[f"E{row}"] = self.fake.unique.random_int(min=10000000, max=99999999)
            self.sheet[f"F{row}"] = self.fake.date_between(start_date="-10y", end_date="today")
            self.sheet[f"G{row}"] = self.utils.pick_random(variables.CONTRIES)
            self.sheet[f"H{row}"] = self.fake.street_address()
            self.sheet[f"I{row}"] = self.fake.secondary_address()
            self.sheet[f"J{row}"] = self.fake.city()
            self.sheet[f"K{row}"] = self.utils.pick_random(variables.SUBCOUNTRIES)
            self.sheet[f"L{row}"] = self.fake.postcode()

    def generate_files(self):
        config = self.config.load_config()

        output_directory = Path(config["output_directory"]).expanduser() / "maykr"
        output_directory.mkdir(parents=True, exist_ok=True)

        for _ in range(self.number_of_files_to_generate):
            # self.write_titles() # TODO if there is a template.xlsx, this is not needed
            self.write_company_data()

            file_path = output_directory / self.new_file_name()
            self.workbook.save(file_path)

            print("File generated:", file_path)
