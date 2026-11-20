from typing import Dict
from maykr.assets import synonyms

from maykr.utils import Utils


class Header:

    def __init__(self) -> None:
        self.utils = Utils()

    def company(self) -> Dict:
        company: Dict = {
            # general company data
            "company_id": (self.utils.pick_header(synonyms.COMPANY_ID_HEADERS)),
            "company_name": (self.utils.pick_header(synonyms.COMPANY_NAME_HEADERS)),
            "country_code": (self.utils.pick_header(synonyms.COUNTRY_CODE_HEADERS)),
            "area": (self.utils.pick_header(synonyms.AREA_HEADERS)),
            "registration_number": (self.utils.pick_header(synonyms.COMPANY_REGISTRATION_HEADERS)),
            "incorporation_date": (self.utils.pick_header(synonyms.COMPANY_INCORPORATION_DATE_HEADERS)),
            "status": (self.utils.pick_header(synonyms.COMPANY_STATUS_HEADERS)),
            "email": (self.utils.pick_header(synonyms.COMPANY_EMAIL_HEADERS)),
            "date_of_dissolved": (self.utils.pick_header(synonyms.DATE_OF_DISSOLVED_HEADERS)),
            "event_date": (self.utils.pick_header(synonyms.EVENT_DATE_HEADERS)),
            "company_type": (self.utils.pick_header(synonyms.COMPANY_TYPE_HEADERS)),
            # connected addresses
            "registered_office_address1": (self.utils.pick_header(synonyms.REGISTERED_OFFICE_ADDRESS1_HEADERS)),
            "registered_office_address2": (self.utils.pick_header(synonyms.REGISTERED_OFFICE_ADDRESS2_HEADERS)),
            "registered_office_post_town": (self.utils.pick_header(synonyms.REG_OFFICE_POST_TOWN_HEADERS)),
            "registered_office_post_code": (self.utils.pick_header(synonyms.REG_OFFICE_POST_CODE)),
            "trading_at_address1": (self.utils.pick_header(synonyms.TRADING_AT_ADDRESS1_HEADERS)),
            "trading_at_address2": (self.utils.pick_header(synonyms.TRADING_AT_ADDRESS2_HEADERS)),
            "trading_at_post_town": (self.utils.pick_header(synonyms.TRADING_AT_POST_TOWN_HEADERS)),
            "trading_at_post_code": (self.utils.pick_header(synonyms.TRADING_AT_POST_CODE)),
            # other stuff
            "udf_text": (self.utils.pick_header(synonyms.UDF_TEXT_HEADERS)),
            "security_group": (self.utils.pick_header(synonyms.SECURITY_GROUP_HEADERS)),
            "additional_info": (self.utils.pick_header(synonyms.ADDITIONAL_INFO_HEADERS)),
            "user_group": (self.utils.pick_header(synonyms.USER_GROUP_HEADERS)),
           }
        return company

    def address(self) -> Dict:
        address: Dict = {
            "address_reference_number": (self.utils.pick_header(synonyms.ADDRESS_REFERENCE_NUMBER_HEADERS)),
            "street_address": (self.utils.pick_header(synonyms.STREET_ADDRESS_HEADERS)),
            "secondary_address": (self.utils.pick_header(synonyms.SECONDARY_ADDRESS_HEADERS)),
            "third_address": (self.utils.pick_header(synonyms.THIRD_ADDRESS_HEADERS)),
            "town_city": (self.utils.pick_header(synonyms.TOWN_CITY_HEADERS)),
            "area": (self.utils.pick_header(synonyms.AREA_HEADERS)),
            "country_code": (self.utils.pick_header(synonyms.COUNTRY_CODE_HEADERS)),
            "postcode": (self.utils.pick_header(synonyms.POSTCODE_HEADERS)),
            "latitude": (self.utils.pick_header(synonyms.LATITUDE_HEADERS)),
            "longitude": (self.utils.pick_header(synonyms.LONGITUDE_HEADERS)),
            "is_global": (self.utils.pick_header(synonyms.ADDRESS_IS_GLOBAL)),
            "additional_info": (self.utils.pick_header(synonyms.ADDITIONAL_INFO_HEADERS)),
            "address_type": (self.utils.pick_header(synonyms.ADDRESS_TYPE_HEADERS)),
           }
        return address

    def individual(self) -> Dict:
        individual: Dict = {
            "first_name": (self.utils.pick_header(synonyms.FORENAME_HEADERS)),
            "last_name": (self.utils.pick_header(synonyms.SURNAME_HEADERS)),
            "display_as": (self.utils.pick_header(synonyms.DISPLAY_AS_HEADERS)),
            "entity_reference": (self.utils.pick_header(synonyms.ENTITY_REFERENCE_HEADERS)),
            "title": (self.utils.pick_header(synonyms.TITLE_HEADERS)),
            "salutation": (self.utils.pick_header(synonyms.SALUTATION_HEADERS)),
            "honours": (self.utils.pick_header(synonyms.HONOURS_HEADERS)),
            "occupation": (self.utils.pick_header(synonyms.OCCUPATION_HEADERS)),
            "nationality": (self.utils.pick_header(synonyms.NATIONALITY_HEADERS)),
            "date_of_birth": (self.utils.pick_header(synonyms.DATE_OF_BIRTH_HEADERS)),
            "date_of_death": (self.utils.pick_header(synonyms.DATE_OF_DEATH_HEADERS)),
            "nationality_identification": (self.utils.pick_header(synonyms.NATIONALITY_IDENTIFICATION_HEADERS)),
            "passport_number": (self.utils.pick_header(synonyms.PASSPORT_NUMBER_HEADERS)),
            "country_code": (self.utils.pick_header(synonyms.COUNTRY_CODE_HEADERS)),
            "area": (self.utils.pick_header(synonyms.AREA_HEADERS)),
            "previous_name": (self.utils.pick_header(synonyms.PREVIOUS_NAME_HEADERS)),
            "security_group": (self.utils.pick_header(synonyms.SECURITY_GROUP_HEADERS)),
            "file_reference": (self.utils.pick_header(synonyms.FILE_REFERENCE_HEADERS)),
            "partner_id": (self.utils.pick_header(synonyms.PARTNER_ID_HEADERS)),
            "managed_by": (self.utils.pick_header(synonyms.MANAGED_BY_HEADERS)),
            "is_historic": (self.utils.pick_header(synonyms.IS_HISTORIC)),
            #connected addresses
            "individual_address1": (self.utils.pick_header(synonyms.INDIVIDUAL_ADDRESS1_HEADERS)),
            "individual_address2": (self.utils.pick_header(synonyms.INDIVIDUAL_ADDRESS2_HEADERS)),
            "individual_city": (self.utils.pick_header(synonyms.INDIVIDUAL_CITY_HEADERS)),
            "individual_postcode": (self.utils.pick_header(synonyms.INDIVIDUAL_POSTCODE_HEADERS)),
           }
        return individual
