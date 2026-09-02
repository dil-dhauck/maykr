from pathlib import Path
import json

class Config:
    
    def __init__(self) -> None:
        self.config = self.load_config()

    def load_config(self) -> dict:
        config_path = Path.home() / ".config" / "maykr" / "config.json"
        with config_path.open("r") as f:
            return json.load(f)
