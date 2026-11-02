# variables_aws_regression.py

COUNTRIES = ["United Kingdom"]

MANAGED_BY_OPTIONS = [
        "David Hauck"
        ]

NATIONALITY_OPTIONS = [
    "Afghan", "Albanian", "Algerian", "American", "American Samoa", "Andorran",
    "Angolan", "Anguillan", "Antiguan/Barbudan", "Antillean", "Argentinian",
    "Armenian", "Aruban", "Australian", "Austrian", "Azerbaijani", "Bahamian",
    "Bahraini", "Bangladeshi", "Barbadian", "Belarusian", "Belgian", "Belizean",
    "Beninese", "Bermudan", "Bhutanese", "Bolivian", "Bosnian/Herzegovinian",
    "Botswanan", "Brazilian", "British", "British Virgin Islander", "Bruneian",
    "Bulgarian", "Burkinabe", "Burundian", "Cambodian", "Cameroonian",
    "Canadian", "Cape Verdean", "Caymanian", "Central African", "Chadian",
    "Channel Islander (Guernsey)", "Channel Islander (Jersey)", "Chilean",
    "Chinese", "Chinese (Hong Kong)", "Chinese/Taiwanese", "Christmas Islander",
    "Citizen of Guinea-Bissau", "Cocos Islander", "Colombian", "Comoran",
    "Congolese", "Cook Islander", "Costa Rican", "Croatian", "Cuban",
    "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican", "Dutch",
    "East Timorese", "Ecuadorean", "Egyptian", "Emirian", "English",
    "Equatorial Guinean", "Eritrean", "Estonian", "Ethiopian", "Faeroese",
    "Falkland Islander", "Fijian", "Finnish", "French", "Gabonese", "Gambian",
    "Georgian", "German", "Ghanaian", "Gibraltarian", "Greek", "Greenlandic",
    "Grenadian", "Guadeloupean", "Guamanian", "Guatemalan", "Guianese",
    "Guinean", "Guyanese", "Haitian", "Honduran", "Hungarian", "Icelandic",
    "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian",
    "Ivorian", "Jamaican", "Japanese", "Jordanian", "Kazakh", "Kenyan",
    "Kiribatian", "Kittitian", "Korean", "Kosovan", "Kuwaiti", "Kyrgyz", "Lao",
    "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtenstein citizen",
    "Lithuanian", "Luxembourgish", "Macanese", "Macedonian", "Madagascan",
    "Mahoran", "Malawian", "Malaysian", "Maldivian", "Malian", "Maltese",
    "Marshallese", "Martinican", "Mauritanian", "Mauritian", "Mexican",
    "Micronesian", "Moldovan", "Monacan", "Mongolian", "Montenegrin",
    "Montserratian", "Moroccan", "Mosotho", "Mozambican", "Myanmarese",
    "Namibian", "Nauruan", "Nepalese", "New Caledonian", "New Zealand",
    "Nicaraguan", "Nigerian", "Nigerien", "Niuean", "North Korean",
    "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan",
    "Palestinian", "Panamanian", "Papua New Guinean", "Paraguayan",
    "Peruvian", "Philippine", "Pitcairner", "Polish", "Polynesian",
    "Portuguese", "Puerto Rican", "Qatari", "Reunionese", "Romanian",
    "Russian", "Rwandan", "Sahrawi", "Saint Helenian", "Saint Lucian",
    "Saint Vincentian", "Salvadoran", "Sammarinese", "Samoan", "Sao Tomean",
    "Saudi Arabian", "Scottish", "Senegalese", "Serbian", "Seychellois",
    "Sierra Leonean", "Singaporean", "Slovakian", "Slovenian",
    "Solomon Islander", "Somali", "South African", "South Korean", "Spanish",
    "Sri Lankan", "Stateless", "Sudanese", "Surinamese", "Swazi", "Swedish",
    "Swiss", "Syrian", "Tadjik", "Taiwanese", "Tanzanian", "Thai", "Togolese",
    "Tokelauan", "Tongan", "Trinidadian and Tobagan", "Tristanian", "Tunisian",
    "Turkish", "Turkmen", "Turks and Caicos Islander", "Tuvaluan", "Ugandan",
    "Ukrainian", "United States Minor Outlying Island", "Unknown",
    "Uruguayan", "Uzbek", "Vanuatuan", "Vatican citizen", "Venezuelan",
    "Vietnamese", "Wallisian", "Welsh", "Yemeni", "Yugoslavian", "Zambian",
    "Zimbabwean",
]

DIVISION_PARTNER_OPTIONS = [
    "dhauck test",
]

USER_GROUP_OPTIONS = [
    "dhauck test"
]

COMPANY_TYPES = [
    "Public Limited Company",
    "Public Limited Company (Listed)",
    "Limited by Shares",
    "Limited by Guarantee",
    "Limited Liability Partnership",
    "Limited by Shares S.60",
    "Limited by Guarantee S.60",
    "European Economic Interest Grouping",
    "Unlimited with Shares",
    "Unlimited without Shares",
    "Public Company",
    "Partnership",
    "Limited Partnership",
    "Societas Europaea (SE)",
    "Community Interest Company",
    "Community Interest Public Limited Company",
    "Scottish Limited Partnership (SLP)",
    "Private Fund Limited Partnership",
    # "General Purpose Committee",
    # "Audit Committee",
    # "Remuneration Committee",
    # "Nomination Committee",
    # "Group Executive Committee",
    # "Disclosure Committee",
    # "Sustainability Committee",
    # "Chairman's Committee",
    # "Investment Committee",
    # "Risk Committee",
    # "Personnel Committee",
    # "Arbitration Committee",
    # "Mediation Committee",
    # "Oversight Committee",
    # "Regulatory Committee",
    # "Integrity Committee",
    # "Steering Committee",
    # "Reputation Committee",
    # "Operational Committee",
    # "Strategy Committee",
    # "Compensation Committee",
    # "Limited Partnership",
    # "Private Fund Limited Partnership",
    # "Limited Liability Partnership",
    # "Scotland Limited Partnership",
]

COMPANY_STATUSES = [
    "Sold",
    # "In Liquidation",
    # "In Administrative Receivership",
    # "In Administration",
    # "Liquidated (solvent)",
    # "Liquidated (insolvent)",
    # "Strike Off Requested",
    # "Struck Off",
    # "Dissolved",
    # "De-registered",
    # "Active",
    # "Closed",
    # "Open",
    # "Pending",
    # "Merged",
]

SUBCOUNTRIES = [
    "England",
    "England and Wales",
    "Northern Ireland",
    "Scotland",
    "Wales",
]

SECURITY_GROUPS = [
    "All Records Not Pending (Standard)",
    "All Records Not Pending (Read Only)",
    "All Records Pending (Standard)",
    "All Records Pending (Read Only)",
    "sj test sec group 1",
    "Individuals Test",
    "Nia UCIP test",
    "dhauck",
]

ADDRESS_TYPES = [
    "Trading At",
    "Registered Office",
    "Presenter",
    "Registered",
    "Alternate Reporting Company",
    ]
