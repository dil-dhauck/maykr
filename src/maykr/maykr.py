from openpyxl import load_workbook
from faker import Faker
from maykr import utils
from maykr.assets import variables
from maykr.config import Config
from pathlib import Path

class Maykr:

    number_of_files_to_generate = 10
    number_of_companies = 35
    number_of_addresses = 10

    def __init__(self):
        self.template = Path(__file__).parent / "assets" / "template.xlsx"
        self.workbook = load_workbook(self.template)
        self.company_data_sheet = self.workbook["Entity Details"]
        self.addresses_sheet = self.workbook["New Addresses"]
        self.fake = Faker()
        self.utils = utils.Utils()
        self.config = Config()
        self.number_of_files_to_generate = self.config.load_config().get("number_of_files_to_generate", 10)
        self.number_of_addresses = self.config.load_config().get("number_of_addresses", 10)

    def new_file_name(self) -> str:
        return f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"

    def write_headers(self): #TODO check this
        self.company_data_sheet["A1"] = "Company ID"
        self.company_data_sheet["B1"] = "Company Name"
        self.company_data_sheet["C1"] = "Company Type"
        self.company_data_sheet["D1"] = "Company Status"
        self.company_data_sheet["E1"] = "Company Registration Number"
        self.company_data_sheet["F1"] = "Company Incorporation Date"
        self.company_data_sheet["G1"] = "Company Country"
        self.company_data_sheet["H1"] = "Reg. Office line 1"
        self.company_data_sheet["I1"] = "Reg. Office line 2"
        self.company_data_sheet["J1"] = "Reg. Office Post Town"
        self.company_data_sheet["K1"] = "Region"
        self.company_data_sheet["L1"] = "Reg. Office Postcode"
        self.company_data_sheet["M1"] = "Company Email"
        self.company_data_sheet["N1"] = "Date of Dissolved"
        self.company_data_sheet["O1"] = "Event date"
        self.company_data_sheet["P1"] = "Is Live"
        self.company_data_sheet["Q1"] = "Security Group"
        self.addresses_sheet["A1"] = "Country"
        self.addresses_sheet["B1"] = "Address Line 1"
        self.addresses_sheet["C1"] = "Address Line 2"
        self.addresses_sheet["D1"] = "Address Line 3"
        self.addresses_sheet["E1"] = "Post Town / City"
        self.addresses_sheet["F1"] = "Region / State"
        self.addresses_sheet["G1"] = "Post Code / ZIP"
        self.addresses_sheet["H1"] = "Quickref"

    def write_company_data(self):
        for row in range(2, self.number_of_companies):
            self.company_data_sheet[f"A{row}"] = self.fake.unique.random_int(min=100000, max=999999)
            self.company_data_sheet[f"B{row}"] = self.fake.company()
            self.company_data_sheet[f"C{row}"] = self.utils.pick_random(variables.COMPANY_TYPES)
            self.company_data_sheet[f"D{row}"] = self.utils.pick_random(variables.COMPANY_STATUSES)
            self.company_data_sheet[f"E{row}"] = self.fake.unique.random_int(min=10000000, max=99999999)
            self.company_data_sheet[f"F{row}"] = self.fake.date_between(start_date="-10y", end_date="today")
            self.company_data_sheet[f"G{row}"] = self.utils.pick_random(variables.COUNTRIES)
            self.company_data_sheet[f"H{row}"] = self.fake.street_address()
            self.company_data_sheet[f"I{row}"] = self.fake.secondary_address()
            self.company_data_sheet[f"J{row}"] = self.fake.city()
            self.company_data_sheet[f"K{row}"] = self.utils.pick_random(variables.SUBCOUNTRIES)
            self.company_data_sheet[f"L{row}"] = self.fake.postcode()
            self.company_data_sheet[f"M{row}"] = self.fake.email()
            self.company_data_sheet[f"N{row}"] = self.fake.date()
            self.company_data_sheet[f"O{row}"] = self.fake.date()
            self.company_data_sheet[f"P{row}"] = self.fake.boolean()
            self.company_data_sheet[f"Q{row}"] = self.utils.pick_random(variables.DEQA_SECURITY_GROUPS)

    def write_addresses(self):
        for row in range(2, self.number_of_addresses):
            self.addresses_sheet[f"A{row}"] = self.utils.pick_random(variables.COUNTRIES)
            self.addresses_sheet[f"B{row}"] = self.fake.street_address()
            self.addresses_sheet[f"C{row}"] = self.fake.street_address()
            self.addresses_sheet[f"D{row}"] = self.fake.street_address()
            self.addresses_sheet[f"E{row}"] = self.fake.city()
            self.addresses_sheet[f"F{row}"] = self.fake.state()
            self.addresses_sheet[f"G{row}"] = self.fake.postcode()


    def generate_files(self):
        config = self.config.load_config()

        output_directory = Path(config["output_directory"]).expanduser() / "maykr"
        output_directory.mkdir(parents=True, exist_ok=True)

        for _ in range(self.number_of_files_to_generate):
            self.write_headers()
            self.write_company_data()
            self.write_addresses()

            file_path = output_directory / self.new_file_name()
            self.workbook.save(file_path)

            print("File generated:", file_path)
