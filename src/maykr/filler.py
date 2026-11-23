import random
from pathlib import Path
from types import ModuleType
from typing import Callable, Dict, List, Tuple

from faker import Faker
from openpyxl import load_workbook

from maykr import utils
from maykr.environments import variables_deqa21
from maykr.config import Config
from maykr.generator.body import Body
from maykr.generator.header import Header


COMPANY_COLUMNS: Dict[str, str] = {
    # general company data
    "A": "company_id",  # mandatory for appointments, not mando for company create
    "B": "company_name",  # mandatory
    "C": "country_code",  # mandatory
    "D": "area",
    "E": "registration_number", # mandatory
    "F": "incorporation_date",
    "G": "status",
    "H": "email",
    "I": "date_of_dissolved",
    "J": "event_date",
    "K": "company_type",
    # connected addresses
    "L": "registered_office_address1",
    "M": "registered_office_address2",
    "N": "registered_office_post_town",
    "O": "registered_office_post_code",
    "P": "trading_at_address1",
    "Q": "trading_at_address2",
    "R": "trading_at_post_town",
    "S": "trading_at_post_code",
    # other stuff
    "V": "udf_text",
    "W": "security_group",
    "X": "additional_info",
    "Y": "user_group",
}

# appointments are written on the "Company Data" sheet, to the right of the company columns,
# so every company row gets one appointment next to it
APPOINTMENT_COLUMNS: Dict[str, str] = {
    "Z": "appointment_date",  # mandatory
    "AA": "board_meeting_date",
    "AB": "consent_to_act",
    "AC": "does_not_attend_meetings",
    "AD": "appointment_notes",
    "AE": "show_notes_on_register",
    "AF": "entity_id",
    "AG": "appointment_type_id",  # mandatory
    "AH": "job_title",
    "AI": "appointment_group_id",
    "AJ": "appointment_level",
    "AK": "appointment_status_id",  # mandatory
    "AL": "appointment_reminder_date",
    # tracking status
    "AM": "tracking_status_id",
    "AN": "tracking_assigned_to_id",
    "AO": "tracking_reminder_date",
    "AP": "tracking_notes",
}

ADDRESS_COLUMNS: Dict[str, str] = {
    "A": "address_reference_number",
    "B": "street_address",  # mandatory
    "C": "secondary_address",
    "D": "third_address",
    "E": "town_city",  # mandatory
    "F": "area",
    "G": "country_code",  # mandatory
    "H": "postcode",  # mandatory
    "I": "latitude",
    "J": "longitude",
    "K": "is_global",
    "L": "additional_info",
    "M": "address_type",
}

INDIVIDUAL_COLUMNS: Dict[str, str] = {
    "A": "first_name",  # mandatory
    "B": "last_name",  # mandatory
    "C": "display_as",  # mandatory
    "D": "entity_reference",
    "E": "title",
    "F": "salutation",
    "G": "honours",
    "H": "occupation",
    "I": "nationality",
    "J": "date_of_birth",
    "K": "date_of_death",
    "L": "nationality_identification",
    "M": "passport_number",
    "N": "country_code",
    "O": "area",
    "P": "previous_name",
    "Q": "security_group",
    "R": "file_reference",
    "S": "partner_id",
    "T": "managed_by",
    "U": "is_historic",
    # connected addresses
    "V": "individual_address1",  # mandatory
    "W": "individual_address2",
    "X": "individual_city",  # mandatory
    "Y": "individual_postcode",  # mandatory
}



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
        self.CURRENT_DATA: Dict[str, Dict] = {}

    def build_sheet(
            self,
            headers: Dict[str, str],
            make_record: Callable[[], Dict],
            columns: Dict[str, str],
            quantity: int,
        ) -> Tuple[Dict[str, str], List[Dict]]:

            sheet_headers = {col: headers[field] for col, field in columns.items()}
            records = [make_record() for _ in range(quantity)]
            return sheet_headers, records

    def create_and_save_sheet_data(self) -> None:
        items = [
            ("Company Data", self.header.company(), self.body.company, COMPANY_COLUMNS, self.config.number_of_companies),
            ("New Addresses", self.header.address(), self.body.address, ADDRESS_COLUMNS, self.config.number_of_addresses),
            ("Individuals", self.header.individual(), self.body.individual, INDIVIDUAL_COLUMNS, self.config.number_of_individuals),
        ]
        for sheet, headers, make_record, columns, qty in items:
            sheet_headers, records = self.build_sheet(headers, make_record, columns, qty)
            self.CURRENT_DATA[sheet] = {"sheet": sheet, "columns": columns, "headers": sheet_headers, "records": records}

        # needs the companies and individuals above, so it has to run after them
        self.add_appointments()

    def add_appointments(self) -> None:
        companies = self.CURRENT_DATA["Company Data"]["records"]
        individuals = self.CURRENT_DATA["Individuals"]["records"]
        if not companies or not individuals:
            raise ValueError("Appointments need at least one company and one individual")

        headers = self.header.appointment()
        sheet_headers = {col: headers[field] for col, field in APPOINTMENT_COLUMNS.items()}

        # one appointment per company row, each with a random existing individual
        records = [
            self.body.appointments(random.choice(individuals), company)
            for company in companies
        ]

        self.CURRENT_DATA["Appointments"] = {
            "sheet": "Company Data",  # same sheet as the companies, columns Z onwards
            "columns": APPOINTMENT_COLUMNS,
            "headers": sheet_headers,
            "records": records,
        }

    def fill_all_sheets(self) -> None:
        self.create_and_save_sheet_data()
        if not self.CURRENT_DATA:
            raise ValueError("No sheet data was created, CURRENT_DATA is empty")

        for data in self.CURRENT_DATA.values():
            self.utils.write_records(
                self.workbook[data["sheet"]],
                data["columns"],
                data["headers"],
                data["records"],
            )
