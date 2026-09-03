from pathlib import Path
import json

class Config:
    
    def __init__(self) -> None:
        self.config = self.load_config()
        self.number_of_files_to_generate = self.config.get("number_of_files_to_generate", 5)
        self.number_of_companies = self.config.get("number_of_companies", 10)
        self.number_of_addresses = self.config.get("number_of_addresses", 10)

    def load_config(self) -> dict:
        config_path = Path.home() / ".config" / "maykr" / "config.json"
        with config_path.open("r") as f:
            return json.load(f)
