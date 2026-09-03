from openpyxl import load_workbook
from faker import Faker
from maykr import utils
from maykr.assets import variables
from maykr.config import Config
from pathlib import Path

class Maykr:

    def __init__(self):
        self.template = Path(__file__).parent / "assets" / "template.xlsx"
        self.workbook = load_workbook(self.template)
        self.company_data_sheet = self.workbook["Entity Details"]
        self.addresses_sheet = self.workbook["New Addresses"]
        self.fake = Faker()
        self.utils = utils.Utils()
        self.config = Config()

    def new_file_name(self) -> str:
        return f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"

    def write_company_data(self) -> None:
        data = {
            "A": ("Company ID", lambda: self.fake.unique.random_int(min=100000, max=999999)),
            "B": ("Company Name", lambda: self.fake.company()),
            "C": ("Company Type", lambda: self.utils.pick_random(variables.COMPANY_TYPES)),
            "D": ("Company Status", lambda: self.utils.pick_random(variables.COMPANY_STATUSES)),
            "E": ("Company Registration Number", lambda: self.fake.unique.random_int(min=10000000, max=99999999)),
            "F": ("Company Incorporation Date", lambda: self.fake.date_between(start_date="-10y", end_date="today")),
            "G": ("Company Country", lambda: self.utils.pick_random(variables.COUNTRIES)),
            "H": ("Reg. Office line 1", lambda: self.fake.street_address()),
            "I": ("Reg. Office line 2", lambda: self.fake.secondary_address()),
            "J": ("Reg. Office Post Town", lambda: self.fake.city()),
            "K": ("Region", lambda: self.utils.pick_random(variables.SUBCOUNTRIES)),
            "L": ("Reg. Office Postcode", lambda: self.fake.postcode()),
            "M": ("Company Email", lambda: self.fake.email()),
            "N": ("Date of Dissolved", lambda: self.fake.date()),
            "O": ("Event date", lambda: self.fake.date()),
            "P": ("Is Live", lambda: self.fake.boolean()),
            "Q": ("Security Group", lambda: self.utils.pick_random([self.utils.pick_random(variables.DEQA_SECURITY_GROUPS), " "])),
            "R": ("Additional Info", lambda: self.fake.text(max_nb_chars=50)),
        }

        for column, (header, generator) in data.items():
            self.company_data_sheet[f"{column}1"] = header
            for row in range(2, self.config.number_of_companies + 2):
                self.company_data_sheet[f"{column}{row}"] = generator()

    def write_addresses(self):
        data = {
            "A": ("Region / State", lambda: self.utils.pick_random([self.utils.pick_random(variables.SUBCOUNTRIES), " "])),
            "B": ("Country", lambda: self.utils.pick_random(variables.COUNTRIES)),
            "C": ("Shared", lambda: self.utils.pick_random([self.fake.boolean(), " "])),
            "D": ("Latitude", lambda: self.utils.pick_random([self.fake.latitude(), " "])),
            "E": ("Longitude", lambda: self.utils.pick_random([self.fake.longitude(), " "])),
            "F": ("Postcode", lambda: self.fake.postcode()),
            "G": ("Town/City", lambda: self.fake.city()),
            "H": ("Reference Number", lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "I": ("Street Address", lambda: self.fake.street_address()),
            "J": ("Secondary Address", lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "K": ("Third Address", lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "L": ("Additional Info", lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50)," "]))
            }

        for column, (header, generator) in data.items():
            self.addresses_sheet[f"{column}1"] = header
            for row in range(2, self.config.number_of_addresses + 2):
                self.addresses_sheet[f"{column}{row}"] = generator()

    def generate_files(self) -> None:
        config = self.config.load_config()

        output_directory = Path(config["output_directory"]).expanduser() / "maykr"
        output_directory.mkdir(parents=True, exist_ok=True)

        for _ in range(self.config.number_of_files_to_generate):
            self.write_company_data()
            self.write_addresses()

            file_path = output_directory / self.new_file_name()
            self.workbook.save(file_path)

            print("File generated:", file_path)
