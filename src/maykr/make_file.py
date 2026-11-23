from pathlib import Path
from types import ModuleType

from openpyxl import load_workbook

from maykr.config import Config
from maykr.environments import variables_deqa21
from maykr.filler import Filler
from maykr.utils import Utils


class MakeFile:
    """makes the files and fills them"""
    #TODO: maybe filling should not be here? idk

    def __init__(self, environment: ModuleType = variables_deqa21) -> None:
        self.config = Config()
        self.filler = Filler(environment)
        self.utils = Utils()

    def generate_files(self) -> None:
        config = self.config.load_config()

        output_directory = Path(config["output_directory"]).expanduser() / "maykr"
        output_directory.mkdir(parents=True, exist_ok=True)

        for _ in range(self.config.number_of_files_to_generate):
            self.filler.workbook = load_workbook(self.filler.template)
            self.filler.fill_all_sheets()

            file_path = output_directory / self.utils.new_file_name()
            self.filler.workbook.save(file_path)

            print("File generated:", file_path)
