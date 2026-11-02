from enum import Enum

import typer

from maykr.assets import variables_deqa21, variables_derg11, variables_aws_regression
from maykr.maykr import Maykr

app = typer.Typer()


class Env(str, Enum):
    derg11 = "derg11"
    deqa21 = "deqa21"
    aws = "aws"


VARIABLES = {
    Env.derg11: variables_derg11,
    Env.deqa21: variables_deqa21,
    Env.aws: variables_aws_regression,
}


@app.callback()
def main() -> None:
    """Maykr CLI"""


@app.command()
def create(env: Env) -> None:
    """Generate files for an environment."""
    Maykr(VARIABLES[env]).generate_files()


if __name__ == "__main__":
    app()
