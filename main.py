import os
from openpyxl import load_workbook
from faker import Faker


class Maykr:

    number_of_files_to_generate = 5
    number_of_companies = 35

    def __init__(self):
        self.workbook = load_workbook("template.xlsx")
        self.sheet = self.workbook["Entity Details"]
        self.fake = Faker()

    def new_file_name(self) -> str:
        return f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"

    def pick_random_company_type(self) -> str:
        company_types = [
            "Private Limited Company",
            "Public Limited Company",
        ]
        return self.fake.random_element(company_types)

    def pick_random_company_status(self) -> str:
        company_statuses = [
            "Active",
            "Inactive",
            "Dissolved",
        ]
        return self.fake.random_element(company_statuses)

    def pick_random_country(self) -> str:
        countries = [
            # "United States", #TODO not yet
            "United Kingdom",
        ]
        return self.fake.random_element(countries)
 
    def pick_random_subcountry(self) -> str:
        subcountries = [
            "England and Wales",
        ]
        return self.fake.random_element(subcountries)

    def write_titles(self):
        self.sheet["A1"] = "Entity Code"
        self.sheet["B1"] = "Entity Name"
        self.sheet["C2"] = "Company Type"
        self.sheet["D2"] = "Company Status"
        self.sheet["E2"] = "Registration Number"
        self.sheet["F2"] = "Incorporation Date"
        self.sheet["G2"] = "Country"
        self.sheet["H2"] = "Reg. Office Line 1"
        self.sheet["I2"] = "Reg. Office Line 2"
        self.sheet["J2"] = "Reg. Office Post Town"
        self.sheet["K2"] = "Reg. Office Region"
        self.sheet["L2"] = "Reg. Office Post Code"

    def write_company_data(self):
        for row in range(2, self.number_of_companies):
            self.sheet[f"A{row}"] = self.fake.unique.random_int(min=100000, max=999999)
            self.sheet[f"B{row}"] = self.fake.company()
            self.sheet[f"C{row}"] = self.pick_random_company_type()
            self.sheet[f"D{row}"] = self.pick_random_company_status()
            self.sheet[f"E{row}"] = self.fake.unique.random_int(min=10000000, max=99999999)
            self.sheet[f"F{row}"] = self.fake.date_between(start_date="-10y", end_date="today")
            self.sheet[f"G{row}"] = self.pick_random_country()
            self.sheet[f"H{row}"] = self.fake.street_address()
            self.sheet[f"I{row}"] = self.fake.secondary_address()
            self.sheet[f"J{row}"] = self.fake.city()
            self.sheet[f"K{row}"] = self.pick_random_subcountry()
            self.sheet[f"L{row}"] = self.fake.postcode()

    def generate_files(self):
        os.makedirs("./generated", exist_ok=True)
        for _ in range(self.number_of_files_to_generate):
            self.write_titles()
            self.write_company_data()

            file_path = os.path.join("./generated", self.new_file_name())
            self.workbook.save(file_path)
            print("File generated:", file_path)


if __name__ == "__main__":
    maykr = Maykr()
    maykr.generate_files()
