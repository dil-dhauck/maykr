from types import ModuleType
from typing import Dict, List, Optional

from faker import Faker

from maykr.environments import variables_deqa21
from maykr.utils import Utils


class Body:

    def __init__(self, environment: ModuleType = variables_deqa21) -> None:
        self.fake = Faker()
        self.utils = Utils()
        self.variables = environment

    def company(self) -> Dict:
        return {
            # general company data
            "company_id": self.fake.unique.random_int(min=100000, max=999999), #mandatory
            "company_name": self.fake.company(), #mandatory
            "country_code": self.utils.pick_random(self.variables.COUNTRIES), #mandatory
            "area": self.utils.pick_random([self.utils.pick_random(self.variables.SUBCOUNTRIES), " "]),
            "registration_number": self.fake.unique.random_int(min=10000000, max=99999999), #mandatory
            "incorporation_date": self.utils.random_date(),
            "status": self.utils.pick_random([self.utils.pick_random(self.variables.COMPANY_STATUSES), " "]),
            "email": self.utils.pick_random([self.fake.email(), " "]),
            "date_of_dissolved": self.utils.random_date(),
            "event_date": self.utils.random_date(),
            "company_type": self.utils.pick_random([self.utils.pick_random(self.variables.COMPANY_TYPES), " "]),

            # connected addresses
            "registered_office_address1": self.fake.street_address(),
            "registered_office_address2": self.fake.street_address(),
            "registered_office_post_town": self.fake.city(),
            "registered_office_post_code": self.fake.postcode(),
            "trading_at_address1": self.fake.street_address(),
            "trading_at_address2": self.fake.street_address(),
            "trading_at_post_town": self.fake.city(),
            "trading_at_post_code": self.fake.postcode(),

            # other stuff
            "udf_text": self.fake.text(max_nb_chars=29),
            "security_group": self.utils.pick_random([self.utils.pick_random(self.variables.SECURITY_GROUPS), " "]),
            "additional_info": self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
            "user_group": self.utils.pick_random([self.utils.pick_random(self.variables.USER_GROUP_OPTIONS), " "]),
            }

    def address(self) -> Dict:
        return {
            "address_reference_number": self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "]),
            "street_address": self.fake.street_address(), #mandatory
            "secondary_address": self.utils.pick_random([self.fake.street_address(), " "]),
            "third_address": self.utils.pick_random([self.fake.street_address(), " "]),
            "town_city": self.fake.city(), #mandatory
            "area": self.utils.pick_random([self.utils.pick_random(self.variables.SUBCOUNTRIES), " "]),
            "country_code": self.utils.pick_random(self.variables.COUNTRIES), #mandatory
            "postcode": self.fake.postcode(), #mandatory
            "latitude": self.utils.pick_random([self.fake.latitude(), " "]),
            "longitude": self.utils.pick_random([self.fake.longitude(), " "]),
            "is_global": self.utils.pick_random(["Yes", "True"]),
            "additional_info": self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
            "address_type": self.utils.pick_random([self.utils.pick_random(self.variables.ADDRESS_TYPES), " "]),
            }

    def individual(self) -> Dict:
        return {
            "first_name": self.fake.first_name(), #mandatory
            "last_name": self.fake.last_name(), #mandatory
            "display_as": self.utils.pick_random(['FORENAMES_SURNAME ("Jane Smith")', 'SURNAME_FORENAMES ("Smith, Jane")']), #mandatory
            "entity_reference": self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "]),
            "title": self.utils.pick_random(["Mr","Mrs","Dr","Dame", "Sir", " "]),
            "salutation": self.utils.pick_random(["Dear Jane", "Dear Dr Smith", " "]),
            "honours": self.utils.pick_random(["QC", "FCA", "OBE", "CBE", " "]),
            "occupation": self.fake.job(),
            "nationality": self.utils.pick_random(self.variables.NATIONALITY_OPTIONS),
            "date_of_birth": self.fake.date_of_birth(minimum_age=18, maximum_age=90),
            "date_of_death": self.utils.pick_random([self.fake.date_of_birth(minimum_age=18, maximum_age=90), " "]),
            "nationality_identification": self.utils.pick_random([self.fake.random_int(min=10000000, max=99999999), " "]),
            "passport_number": self.utils.pick_random([self.fake.unique.random_int(min=10000000, max=99999999), " "]),
            "country_code": self.utils.pick_random(self.variables.COUNTRIES),
            "area": self.utils.pick_random([self.utils.pick_random(self.variables.SUBCOUNTRIES)," "]),
            "previous_name": self.utils.pick_random([self.fake.name(), " "]),
            "security_group": self.utils.pick_random([self.utils.pick_random(self.variables.SECURITY_GROUPS), " "]),
            "file_reference": self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "]),
            "partner_id": self.utils.pick_random([self.utils.pick_random(self.variables.DIVISION_PARTNER_OPTIONS), " "]),
            "managed_by": self.utils.pick_random(self.variables.MANAGED_BY_OPTIONS),
            "is_historic": self.utils.pick_random(["Yes", "True", "No", "False", " "]),

            #connected addresses
            "individual_address1": self.fake.street_address(), #mandatory
            "individual_address2": self.utils.pick_random([self.fake.street_address(), " "]),
            "individual_city": self.fake.city(), #mandatory
            "individual_postcode": self.fake.postcode(), #mandatory
            }

    def appointments(self, individual: Dict, company: Optional[Dict] = None) -> Dict:
        return {
            #the company id should be read from the company data next to this, because this is on the same sheet as the company, if its needed it still can be put as company["company_id"]
            "appointment_date": self.utils.random_date(is_mandatory=True), #mandatory
            "board_meeting_date": self.utils.random_date(),
            "consent_to_act": self.utils.random_bool(),
            "does_not_attend_meetings": self.utils.random_bool(),
            "appointment_notes": self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
            "show_notes_on_register": self.utils.random_bool(),
            "entity_id": individual["entity_reference"], #TODO: hopefully this the data from an individual that it needs
            "appointment_type_id": self.utils.pick_random([self.utils.pick_random(self.variables.APPOINTMENT_TYPES), " "]),
            "job_title": self.utils.pick_random([self.utils.pick_random(self.variables.OCCUPATIONS), " "]),
            "appointment_group_id": self.utils.pick_random([self.utils.pick_random(self.variables.APPOINTMENT_GROUPS), " "]),
            "appointment_level": self.utils.pick_random(["1", "2", " "]),
            "appointment_status_id": self.utils.pick_random([self.utils.pick_random(self.variables.APPOINTMENT_STATUSES), " "]),
            "appointment_reminder_date": self.utils.random_date(),
            # "alternate_to_entity_id": #Next itaration
            # Tracking Status
            "tracking_status_id": self.utils.pick_random([self.utils.pick_random(self.variables.TRACKING_STATUSES), " "]),
            "tracking_assigned_to_id": self.utils.pick_random([self.utils.pick_random(self.variables.USER_NAMES), " "]),
            "tracking_reminder_date": self.utils.random_date(),
            "tracking_notes": self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
            # Workflow Status NEXT ITERATION
            # "workflow_code": 
            # "workflow_stage": 
            # "workflow_assigned_to_id": 
            # "workflow_due_date": 
        }
