from openpyxl import load_workbook
from faker import Faker
from maykr import utils
from maykr.assets import variables
from maykr.assets import synonyms
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
            "A": (self.utils.pick_random(synonyms.COMPANY_ID_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "B": (self.utils.pick_random(synonyms.COMPANY_NAME_HEADERS), lambda: self.fake.company()), #mandatory
            "C": (self.utils.pick_random(synonyms.COMPANY_TYPE_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.COMPANY_TYPES), " "])),
            "D": (self.utils.pick_random(synonyms.COMPANY_STATUS_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.COMPANY_STATUSES), " "])),
            "E": (self.utils.pick_random(synonyms.COMPANY_REGISTRATION_HEADERS), lambda: self.fake.unique.random_int(min=10000000, max=99999999)), #mandatory
            "F": (self.utils.pick_random(synonyms.COMPANY_INCORPORATION_DATE_HEADERS), lambda: self.utils.pick_random([self.fake.date_between(start_date="-10y", end_date="today")," "])),
            "G": (self.utils.pick_random(synonyms.COUNTRY_CODE_HEADERS), lambda: self.utils.pick_random(variables.COUNTRIES)),
            "H": (self.utils.pick_random(synonyms.REG_OFFICE_LINE_1_HEADERS), lambda: self.utils.pick_random([self.fake.street_address()," "])),
            "I": (self.utils.pick_random(synonyms.REG_OFFICE_LINE_2_HEADERS), lambda: self.fake.secondary_address()),
            "J": (self.utils.pick_random(synonyms.TOWN_CITY_HEADERS), lambda: self.utils.pick_random([self.fake.city()," "])),
            "K": (self.utils.pick_random(synonyms.AREA_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.SUBCOUNTRIES)," "])),
            "L": (self.utils.pick_random(synonyms.POSTCODE_HEADERS), lambda: self.fake.postcode()),
            "M": (self.utils.pick_random(synonyms.COMPANY_EMAIL_HEADERS), lambda: self.utils.pick_random([self.fake.email()," "])),
            "N": (self.utils.pick_random(synonyms.DATE_OF_DISSOLVED_HEADERS), lambda: self.utils.pick_random([self.fake.date()," "])),
            "O": (self.utils.pick_random(synonyms.EVENT_DATE_HEADERS), lambda: self.fake.date()),
            "P": (self.utils.pick_random(synonyms.IS_LIVE_HEADERS), lambda: self.utils.pick_random([self.fake.boolean()," "])),
            "Q": (self.utils.pick_random(synonyms.SECURITY_GROUP_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.DEQA_SECURITY_GROUPS), " "])),
            "R": (self.utils.pick_random(synonyms.ADDITIONAL_INFO_HEADERS), lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50)," "])),
        }

        for column, (header, generator) in data.items():
            self.company_data_sheet[f"{column}1"] = header
            for row in range(2, self.config.number_of_companies + 2):
                self.company_data_sheet[f"{column}{row}"] = generator()

    def write_addresses(self):
        data = {
            "A": (self.utils.pick_random(synonyms.AREA_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.SUBCOUNTRIES), " "])),
            "B": (self.utils.pick_random(synonyms.COUNTRY_CODE_HEADERS), lambda: self.utils.pick_random(variables.COUNTRIES)),
            "C": (self.utils.pick_random(synonyms.ADDRESS_IS_GLOBAL), lambda: self.utils.pick_random([self.fake.boolean(), " "])),
            "D": (self.utils.pick_random(synonyms.LATITUDE_HEADERS), lambda: self.utils.pick_random([self.fake.latitude(), " "])),
            "E": (self.utils.pick_random(synonyms.LONGITUDE_HEADERS), lambda: self.utils.pick_random([self.fake.longitude(), " "])),
            "F": (self.utils.pick_random(synonyms.POSTCODE_HEADERS), lambda: self.fake.postcode()),
            "G": (self.utils.pick_random(synonyms.TOWN_CITY_HEADERS), lambda: self.fake.city()),
            "H": (self.utils.pick_random(synonyms.ADDRESS_REFERENCE_NUMBER_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "I": (self.utils.pick_random(synonyms.STREET_ADDRESS_HEADERS), lambda: self.fake.street_address()),
            "J": (self.utils.pick_random(synonyms.SECONDARY_ADDRESS_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "K": (self.utils.pick_random(synonyms.THIRD_ADDRESS_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "L": (self.utils.pick_random(synonyms.ADDITIONAL_INFO_HEADERS), lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50)," "]))
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
