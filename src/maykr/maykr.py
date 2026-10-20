from os import name

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
        self.company_data_sheet = self.workbook["Company Data"]
        self.addresses_sheet = self.workbook["New Addresses"]
        self.individuals_sheet = self.workbook["Individuals"]
        self.fake = Faker()
        self.utils = utils.Utils()
        self.config = Config()

    def new_file_name(self) -> str:
        return f"test_file_{self.fake.unique.random_int(min=10000000, max=99999999)}.xlsx"

    def write_company_data(self) -> None:
        data = {
            "A": (self.utils.pick_random(synonyms.COMPANY_ID_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "B": (self.utils.pick_random(synonyms.COMPANY_NAME_HEADERS), lambda: self.fake.company()), #mandatory
            "C": (self.utils.pick_random(synonyms.COUNTRY_CODE_HEADERS), lambda: self.utils.pick_random(variables.COUNTRIES)), #mandatory
            "D": (self.utils.pick_random(synonyms.AREA_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.SUBCOUNTRIES)," "])),
            "E": (self.utils.pick_random(synonyms.COMPANY_REGISTRATION_HEADERS), lambda: self.fake.unique.random_int(min=10000000, max=99999999)), #mandatory
            "F": (self.utils.pick_random(synonyms.COMPANY_INCORPORATION_DATE_HEADERS), lambda: self.utils.pick_random([self.fake.date_between(start_date="-10y", end_date="today")," "])),
            "G": (self.utils.pick_random(synonyms.COMPANY_STATUS_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.COMPANY_STATUSES), " "])),
            "H": (self.utils.pick_random(synonyms.COMPANY_EMAIL_HEADERS), lambda: self.utils.pick_random([self.fake.email()," "])),
            "I": (self.utils.pick_random(synonyms.DATE_OF_DISSOLVED_HEADERS), lambda: self.utils.pick_random([self.fake.date()," "])),
            "J": (self.utils.pick_random(synonyms.EVENT_DATE_HEADERS), lambda: self.fake.date()),
            "K": (self.utils.pick_random(synonyms.COMPANY_TYPE_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.COMPANY_TYPES), " "])),
            "L": (self.utils.pick_random(synonyms.SECURITY_GROUP_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.DEQA_SECURITY_GROUPS), " "])),
            "M": (self.utils.pick_random(synonyms.ADDITIONAL_INFO_HEADERS), lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50)," "])),
            "N": (self.utils.pick_random(synonyms.USER_GROUP_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.USER_GROUP_OPTIONS), " "])),
            #connected addresses
            "O": (self.utils.pick_random(synonyms.COMPANY_ADDRESS1_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "P": (self.utils.pick_random(synonyms.COMPANY_ADDRESS2_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "Q": (self.utils.pick_random(synonyms.COMPANY_REG_OFFICE_POST_TOWN_HEADERS), lambda: self.utils.pick_random([self.fake.city(), " "])),
            "R": (self.utils.pick_random(synonyms.REG_OFFICE_POST_CODE), lambda: self.utils.pick_random([self.fake.postcode(), " "])),
            "S": (self.utils.pick_random(synonyms.UDF_TEXT_HEADERS), lambda: self.utils.pick_random([self.fake.text(max_nb_chars=29), " "])),
        }


        for column, (header, generator) in data.items():
            self.company_data_sheet[f"{column}1"] = header
            for row in range(2, self.config.number_of_companies + 2):
                self.company_data_sheet[f"{column}{row}"] = generator()

    def write_addresses(self):

        data = {
            "A": (self.utils.pick_random(synonyms.ADDRESS_REFERENCE_NUMBER_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "B": (self.utils.pick_random(synonyms.STREET_ADDRESS_HEADERS), lambda: self.fake.street_address()), #mandatory
            "C": (self.utils.pick_random(synonyms.SECONDARY_ADDRESS_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "D": (self.utils.pick_random(synonyms.THIRD_ADDRESS_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "E": (self.utils.pick_random(synonyms.TOWN_CITY_HEADERS), lambda: self.fake.city()), #mandatory
            "F": (self.utils.pick_random(synonyms.AREA_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.SUBCOUNTRIES), " "])),
            "G": (self.utils.pick_random(synonyms.COUNTRY_CODE_HEADERS), lambda: self.utils.pick_random(variables.COUNTRIES)), #mandatory
            "H": (self.utils.pick_random(synonyms.POSTCODE_HEADERS), lambda: self.fake.postcode()), #mandatory
            "I": (self.utils.pick_random(synonyms.LATITUDE_HEADERS), lambda: self.utils.pick_random([self.fake.latitude(), " "])),
            "J": (self.utils.pick_random(synonyms.LONGITUDE_HEADERS), lambda: self.utils.pick_random([self.fake.longitude(), " "])),
            "K": (self.utils.pick_random(synonyms.ADDRESS_IS_GLOBAL), lambda: self.utils.pick_random(["Yes", "True"])),
            "L": (self.utils.pick_random(synonyms.ADDITIONAL_INFO_HEADERS), lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50)," "])),
            "M": (self.utils.pick_random(synonyms.ADDRESS_TYPE_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.ADDRESS_TYPES), " "])),
        }

        for column, (header, generator) in data.items():
            self.addresses_sheet[f"{column}1"] = header
            for row in range(2, self.config.number_of_addresses + 2):
                self.addresses_sheet[f"{column}{row}"] = generator()

    def write_individuals(self) -> None:
        data = {
            "A": (self.utils.pick_random(synonyms.FORENAME_HEADERS), lambda: self.fake.first_name()), #mandatory
            "B": (self.utils.pick_random(synonyms.SURNAME_HEADERS), lambda: self.fake.last_name()), #mandatory
            "C": (self.utils.pick_random(synonyms.DISPLAY_AS_HEADERS), lambda: self.utils.pick_random(['FORENAMES_SURNAME ("Jane Smith")', 'SURNAME_FORENAMES ("Smith, Jane")'])), #mandatory
            "D": (self.utils.pick_random(synonyms.ENTITY_REFERENCE_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "E": (self.utils.pick_random(synonyms.TITLE_HEADERS), lambda: self.utils.pick_random(["Mr","Mrs","Dr","Dame", "Sir", " "])),
            "F": (self.utils.pick_random(synonyms.SALUTATION_HEADERS), lambda: self.utils.pick_random(["Dear Jane", "Dear Dr Smith", " "])),
            "G": (self.utils.pick_random(synonyms.HONOURS_HEADERS), lambda: self.utils.pick_random(["QC", "FCA", "OBE", "CBE", " "])),
            "H": (self.utils.pick_random(synonyms.OCCUPATION_HEADERS), lambda: self.fake.job()),
            "I": (self.utils.pick_random(synonyms.NATIONALITY_HEADERS), lambda: self.utils.pick_random([self.fake.country(), " "])),
            "J": (self.utils.pick_random(synonyms.DATE_OF_BIRTH_HEADERS), lambda: self.fake.date_of_birth(minimum_age=18, maximum_age=90)),
            "K": (self.utils.pick_random(synonyms.DATE_OF_DEATH_HEADERS), lambda: self.utils.pick_random([self.fake.date_of_birth(minimum_age=18, maximum_age=90), " "])),
            "L": (self.utils.pick_random(synonyms.NATIONALITY_IDENTIFICATION_HEADERS), lambda: self.utils.pick_random([self.fake.random_int(min=10000000, max=99999999), " "])),
            "M": (self.utils.pick_random(synonyms.PASSPORT_NUMBER_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=10000000, max=99999999), " "])),
            "N": (self.utils.pick_random(synonyms.COUNTRY_CODE_HEADERS), lambda: self.utils.pick_random(variables.COUNTRIES)),
            "O": (self.utils.pick_random(synonyms.AREA_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.SUBCOUNTRIES)," "])),
            "P": (self.utils.pick_random(synonyms.PREVIOUS_NAME_HEADERS), lambda: self.utils.pick_random([self.fake.name(), " "])),
            "Q": (self.utils.pick_random(synonyms.SECURITY_GROUP_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.DEQA_SECURITY_GROUPS), " "])),
            "R": (self.utils.pick_random(synonyms.FILE_REFERENCE_HEADERS), lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "])),
            "S": (self.utils.pick_random(synonyms.PARTNER_ID_HEADERS), lambda: self.utils.pick_random([self.utils.pick_random(variables.DIVISION_PARTNER_OPTIONS), " "])),
            "T": (self.utils.pick_random(synonyms.MANAGED_BY_HEADERS), lambda: self.utils.pick_random(variables.MANAGED_BY_OPTIONS)),
            "U": (self.utils.pick_random(synonyms.IS_HISTORIC), lambda: self.utils.pick_random(["Yes", "True", "No", "False", " "])),

            #connected addresses
            "W": (self.utils.pick_random(synonyms.INDIVIDUAL_ADDRESS1_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "X": (self.utils.pick_random(synonyms.INDIVIDUAL_ADDRESS2_HEADERS), lambda: self.utils.pick_random([self.fake.street_address(), " "])),
            "Y": (self.utils.pick_random(synonyms.INDIVIDUAL_CITY_HEADERS), lambda: self.utils.pick_random([self.fake.city(), " "])),
            "Z": (self.utils.pick_random(synonyms.INDIVIDUAL_POSTCODE_HEADERS), lambda: self.utils.pick_random([self.fake.postcode(), " "])),
        }

        for column, (header, generator) in data.items():
            self.individuals_sheet[f"{column}1"] = header
            for row in range(2, self.config.number_of_individuals + 2):
                self.individuals_sheet[f"{column}{row}"] = generator()

    def generate_files(self) -> None:
        config = self.config.load_config()

        output_directory = Path(config["output_directory"]).expanduser() / "maykr"
        output_directory.mkdir(parents=True, exist_ok=True)

        for _ in range(self.config.number_of_files_to_generate):
            self.write_company_data()
            self.write_addresses()
            self.write_individuals()

            file_path = output_directory / self.new_file_name()
            self.workbook.save(file_path)

            print("File generated:", file_path)
