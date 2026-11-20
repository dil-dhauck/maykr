from types import ModuleType
from typing import Dict

from faker import Faker

from maykr.environments import variables_deqa21
from maykr.utils import Utils


class Body:

    def __init__(self, environment: ModuleType = variables_deqa21) -> None:
        self.fake = Faker()
        self.utils = Utils()
        self.variables = environment

    def company(self) -> Dict:
        company: Dict = {
            # general company data
            "company_id": lambda: self.fake.unique.random_int(min=100000, max=999999),
            "company_name": lambda: self.fake.company(),
            "country_code": lambda: self.utils.pick_random(self.variables.COUNTRIES),
            "area": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.SUBCOUNTRIES), " "]),
            "registration_number": lambda: self.fake.unique.random_int(min=10000000, max=99999999),
            "incorporation_date": lambda: self.utils.random_date(),
            "status": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.COMPANY_STATUSES), " "]),
            "email": lambda: self.utils.pick_random([self.fake.email(), " "]),
            "date_of_dissolved": lambda: self.utils.random_date(),
            "event_date": lambda: self.utils.random_date(),
            "company_type": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.COMPANY_TYPES), " "]),

            # connected addresses
            "registered_office_address1": lambda: self.fake.street_address(),
            "registered_office_address2": lambda: self.fake.street_address(),
            "registered_office_post_town": lambda: self.fake.city(),
            "registered_office_post_code": lambda: self.fake.postcode(),
            "trading_at_address1": lambda: self.fake.street_address(),
            "trading_at_address2": lambda: self.fake.street_address(),
            "trading_at_post_town": lambda: self.fake.city(),
            "trading_at_post_code": lambda: self.fake.postcode(),

            # other stuff
            "udf_text": lambda: self.fake.text(max_nb_chars=29),
            "security_group": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.SECURITY_GROUPS), " "]),
            "additional_info": lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
            "user_group": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.USER_GROUP_OPTIONS), " "]),
            }
        return company

    def address(self) -> Dict:
        address: Dict = {
            "address_reference_number": lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "]),
            "street_address": lambda: self.fake.street_address(),
            "secondary_address": lambda: self.utils.pick_random([self.fake.street_address(), " "]),
            "third_address": lambda: self.utils.pick_random([self.fake.street_address(), " "]),
            "town_city": lambda: self.fake.city(),
            "area": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.SUBCOUNTRIES), " "]),
            "country_code": lambda: self.utils.pick_random(self.variables.COUNTRIES),
            "postcode": lambda: self.fake.postcode(),
            "latitude": lambda: self.utils.pick_random([self.fake.latitude(), " "]),
            "longitude": lambda: self.utils.pick_random([self.fake.longitude(), " "]),
            "is_global": lambda: self.utils.pick_random(["Yes", "True"]),
            "additional_info": lambda: self.utils.pick_random([self.fake.text(max_nb_chars=50), " "]),
            "address_type": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.ADDRESS_TYPES), " "]),
            }
        return address

    def individual(self) -> Dict:
        individual: Dict = {
            "first_name": lambda: self.fake.first_name(),
            "last_name": lambda: self.fake.last_name(),
            "display_as": lambda: self.utils.pick_random(['FORENAMES_SURNAME ("Jane Smith")', 'SURNAME_FORENAMES ("Smith, Jane")']),
            "entity_reference": lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "]),
            "title": lambda: self.utils.pick_random(["Mr","Mrs","Dr","Dame", "Sir", " "]),
            "salutation": lambda: self.utils.pick_random(["Dear Jane", "Dear Dr Smith", " "]),
            "honours": lambda: self.utils.pick_random(["QC", "FCA", "OBE", "CBE", " "]),
            "occupation": lambda: self.fake.job(),
            "nationality": lambda: self.utils.pick_random(self.variables.NATIONALITY_OPTIONS),
            "date_of_birth": lambda: self.fake.date_of_birth(minimum_age=18, maximum_age=90),
            "date_of_death": lambda: self.utils.pick_random([self.fake.date_of_birth(minimum_age=18, maximum_age=90), " "]),
            "nationality_identification": lambda: self.utils.pick_random([self.fake.random_int(min=10000000, max=99999999), " "]),
            "passport_number": lambda: self.utils.pick_random([self.fake.unique.random_int(min=10000000, max=99999999), " "]),
            "country_code": lambda: self.utils.pick_random(self.variables.COUNTRIES),
            "area": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.SUBCOUNTRIES)," "]),
            "previous_name": lambda: self.utils.pick_random([self.fake.name(), " "]),
            "security_group": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.SECURITY_GROUPS), " "]),
            "file_reference": lambda: self.utils.pick_random([self.fake.unique.random_int(min=100000, max=999999), " "]),
            "partner_id": lambda: self.utils.pick_random([self.utils.pick_random(self.variables.DIVISION_PARTNER_OPTIONS), " "]),
            "managed_by": lambda: self.utils.pick_random(self.variables.MANAGED_BY_OPTIONS),
            "is_historic": lambda: self.utils.pick_random(["Yes", "True", "No", "False", " "]),

            #connected addresses
            "individual_address1": lambda: self.fake.street_address(),
            "individual_address2": lambda: self.utils.pick_random([self.fake.street_address(), " "]),
            "individual_city": lambda: self.fake.city(),
            "individual_postcode": lambda: self.fake.postcode(),
            }
        return individual
    
