import typer

from maykr.maykr import Maykr

app = typer.Typer()

class Main:

    @app.command()
    def set_path() -> None:
        #TODO
        print("not yet implemented")

    @app.command()
    def create() -> None:
        maykr = Maykr()
        maykr.generate_files()


if __name__ == "__main__":
    main = Main()
    app()
