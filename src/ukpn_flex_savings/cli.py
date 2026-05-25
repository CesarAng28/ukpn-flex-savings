import typer

from rich import print

from ukpn_flex_savings.connectors import UKPNFlexDispatchesConnector
from ukpn_flex_savings.services import UKPNFlexDispatchesService
from ukpn_flex_savings.repositories import UKPNFlexDispatchesRepository
from ukpn_flex_savings.config import settings

app = typer.Typer()

@app.command()
def fetch_flex_dispatches() -> None:
    ukpn_connector = UKPNFlexDispatchesConnector(settings.ukpn_dispatches_url, settings.ukpn_api_key)
    repository = UKPNFlexDispatchesRepository(settings.DATA_DIR)
    
    
    service = UKPNFlexDispatchesService(ukpn_connector, repository)
    saving_path =service.fetch_and_save_dispatches(settings.start_time, settings.end_time)
    print(f"[green]Saved UKPN data to:[/green] {saving_path}")
    
if __name__ == "__main__":
    app()
    
    

    