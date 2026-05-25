import typer


from ukpn_flex_savings.cli.etl import etl


app = typer.Typer()

app.add_typer(etl, name="etl")

if __name__ == "__main__":
    app()