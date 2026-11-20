from pathlib import Path
from types import ModuleType
from typing import Dict, List

from faker import Faker
from openpyxl import load_workbook

from maykr import utils
from maykr.environments import variables_deqa21
from maykr.config import Config
from maykr.generator.body import Body
from maykr.generator.header import Header

class Filler:

    def __init__(self, environment: ModuleType = variables_deqa21) -> None:
        self.template = Path(__file__).parent / "assets" / "template.xlsx"
        self.workbook = load_workbook(self.template)
        self.fake = Faker()
        self.utils = utils.Utils()
        self.config = Config()
        self.variables = environment
        self.body = Body(environment)
        self.header = Header()
        self.SHEETS: List = ["Company Data", "New Addresses", "Individuals"]
        self.CURRENT_DATA: List[Dict] = [{}]


    def company_data(self) -> Dict:
        header = self.header.company()
        body = self.body.company()
        data = {
            # general company data
            "A": (header["company_id"], body["company_id"]),  # mandatory for appointments, not mando for company create
            "B": (header["company_name"], body["company_name"]),  # mandatory
            "C": (header["country_code"], body["country_code"]),  # mandatory
            "D": (header["area"], body["area"]),
            "E": (header["registration_number"], body["registration_number"]),  # mandatory
            "F": (header["incorporation_date"], body["incorporation_date"]),
            "G": (header["status"], body["status"]),
            "H": (header["email"], body["email"]),
            "I": (header["date_of_dissolved"], body["date_of_dissolved"]),
            "J": (header["event_date"], body["event_date"]),
            "K": (header["company_type"], body["company_type"]),
            # connected addresses
            "L": (header["registered_office_address1"], body["registered_office_address1"]),
            "M": (header["registered_office_address2"], body["registered_office_address2"]),
            "N": (header["registered_office_post_town"], body["registered_office_post_town"]),
            "O": (header["registered_office_post_code"], body["registered_office_post_code"]),
            "P": (header["trading_at_address1"], body["trading_at_address1"]),
            "Q": (header["trading_at_address2"], body["trading_at_address2"]),
            "R": (header["trading_at_post_town"], body["trading_at_post_town"]),
            "S": (header["trading_at_post_code"], body["trading_at_post_code"]),
            # other stuff
            "V": (header["udf_text"], body["udf_text"]),
            "W": (header["security_group"], body["security_group"]),
            "X": (header["additional_info"], body["additional_info"]),
            "Y": (header["user_group"], body["user_group"]),
        }
        return data

    # def add_appointments(self) -> None: #TODO
    #
    #     data = {
    #         # connected individuals
    #         "": (
    #             self.utils.pick_header(synonyms.EVENT_DATE_HEADERS),
    #             lambda: self.utils.random_date(),
    #         ),  # mandatory
    #         "": (
    #             self.utils.pick_header(synonyms.BOARD_MEETING_DATE_HEADERS),
    #             lambda: self.utils.random_date(),
    #         ),  # mandatory
    #         "": (
    #             self.utils.pick_header(synonyms.CONSENT_TO_ACT_HEADERS),
    #             lambda: self.utils.pick_random(["true", "false", " "]),
    #         ),
    #         "": (
    #             self.utils.pick_header(synonyms.DOES_NOT_ATTEND_MEETINGS_HEADERS),
    #             lambda: self.utils.pick_random(["true", "false", " "]),
    #         ),
    #         "": (
    #             self.utils.pick_header(synonyms.APPOINTMENT_NOTES_HEADERS),
    #             lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
    #         ),
    #         "": (
    #             self.utils.pick_header(synonyms.SHOW_NOTES_ON_REGISTER_HEADERS),
    #             lambda: self.utils.pick_random(["true", "false", " "]),
    #         ),
    #         # "": (self.utils.pick_header(synonyms.ENTITY_REFERENCE_HEADERS), lambda: self.),
    #         # appointments.appointmentTypeIds #mandatory
    #         # appointments.jobTitle
    #         # appointments.appointmentGroupId
    #         # appointments.appointmentLevel
    #         # appointments.appointmentStatusId #mandatory
    #         # appointments.appointmentReminderDate
    #         # appointments.alternateToEntityId #Conditionally mandatory for alternate positions.
    #         # appointments.eventDate
    #         # trackingStatus.trackingStatusId
    #         # trackingStatus.assignedToId
    #         # trackingStatus.reminderDate
    #         # trackingStatus.trackingNotes
    #         # workflowStatus.workflowCode
    #     }
    #
    def addresses(self) -> Dict:
        header = self.header.address()
        body = self.body.address()
        data = {
            "A": (header["address_reference_number"], body["address_reference_number"]),
            "B": (header["street_address"], body["street_address"]),  # mandatory
            "C": (header["secondary_address"], body["secondary_address"]),
            "D": (header["third_address"], body["third_address"]),
            "E": (header["town_city"], body["town_city"]),  # mandatory
            "F": (header["area"], body["area"]),
            "G": (header["country_code"], body["country_code"]),  # mandatory
            "H": (header["postcode"], body["postcode"]),  # mandatory
            "I": (header["latitude"], body["latitude"]),
            "J": (header["longitude"], body["longitude"]),
            "K": (header["is_global"], body["is_global"]),
            "L": (header["additional_info"], body["additional_info"]),
            "M": (header["address_type"], body["address_type"]),
        }
        return data

    def individuals(self) -> Dict:
        header = self.header.individual()
        body = self.body.individual()
        data = {
            "A": (header["first_name"], body["first_name"]),  # mandatory
            "B": (header["last_name"], body["last_name"]),  # mandatory
            "C": (header["display_as"], body["display_as"]),  # mandatory
            "D": (header["entity_reference"], body["entity_reference"]),
            "E": (header["title"], body["title"]),
            "F": (header["salutation"], body["salutation"]),
            "G": (header["honours"], body["honours"]),
            "H": (header["occupation"], body["occupation"]),
            "I": (header["nationality"], body["nationality"]),
            "J": (header["date_of_birth"], body["date_of_birth"]),
            "K": (header["date_of_death"], body["date_of_death"]),
            "L": (header["nationality_identification"], body["nationality_identification"]),
            "M": (header["passport_number"], body["passport_number"]),
            "N": (header["country_code"], body["country_code"]),
            "O": (header["area"], body["area"]),
            "P": (header["previous_name"], body["previous_name"]),
            "Q": (header["security_group"], body["security_group"]),
            "R": (header["file_reference"], body["file_reference"]),
            "S": (header["partner_id"], body["partner_id"]),
            "T": (header["managed_by"], body["managed_by"]),
            "U": (header["is_historic"], body["is_historic"]),
            # connected addresses
            "V": (header["individual_address1"], body["individual_address1"]),  # mandatory
            "W": (header["individual_address2"], body["individual_address2"]),
            "X": (header["individual_city"], body["individual_city"]),  # mandatory
            "Y": (header["individual_postcode"], body["individual_postcode"]),  # mandatory
        }
        return data


    #TODO notes
    #create records(quantity)
    #save records done

    #current data should be a dict no? so i can CURRENT_DATA["Individuals"]["first_name"] smt like that


    #fill wave1(company, address, individual) sheets with records
    #fill wave2(new addresses) sheets with records
    #fill wave3(appointment) sheets with records

    def create_and_save_sheet_data(self) -> List:

        action_items = [
            ("Company Data", self.company_data(), self.config.number_of_companies),
            ("New Addresses", self.addresses(), self.config.number_of_addresses),
            ("Individuals", self.individuals(), self.config.number_of_individuals),
            ]

        self.CURRENT_DATA.append(action_items)
        return action_items

    def fill_all_sheets(self) -> None:

        self.create_and_save_sheet_data()

        if self.CURRENT_DATA:
            for sheet, data, quantity in self.CURRENT_DATA:
                self.utils.fill_sheet(data, self.workbook[sheet], quantity)
        else:
            raise ValueError("Data has not been created, or well idk, current data is empty")
