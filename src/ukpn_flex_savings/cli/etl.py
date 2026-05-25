import typer

from rich import print

from ukpn_flex_savings.connectors import UKPNFlexDispatchesConnector
from ukpn_flex_savings.services import UKPNFlexDispatchesService
from ukpn_flex_savings.repositories import UKPNFlexDispatchesRepository

from ukpn_flex_savings.connectors.ocf_solar_estimates_connectors import OCFSolarEstimatesConnector
from ukpn_flex_savings.repositories.ocf_solar_estimate_repository import OCFEstimateRepository
from ukpn_flex_savings.services.ocf_estimates_service import OCFEstimatesService
from ukpn_flex_savings.config import settings

etl = typer.Typer()

@etl.command("fetch-flex-dispatches")
def fetch_flex_dispatches() -> None:
    ukpn_connector = UKPNFlexDispatchesConnector(settings.ukpn_dispatches_url, settings.ukpn_api_key)
    repository = UKPNFlexDispatchesRepository(settings.data_dir)
    
    
    service = UKPNFlexDispatchesService(ukpn_connector, repository)
    saving_path =service.fetch_and_save_dispatches(settings.start_time, settings.end_time)
    print(f"[green]Saved UKPN data to:[/green] {saving_path}")
    
@etl.command("ocf-estimates")
def fetch_ocf_estimates(filename: str) -> None:
    repository = OCFEstimateRepository(settings.data_dir)
    connector = OCFSolarEstimatesConnector(settings.data_dir)
    service = OCFEstimatesService(connector, repository)
    ocf_estimates = service.get_and_save_ocf_estimates(filename)
    print(ocf_estimates.head())
    print(f"[green]Loaded OCF estimates from:[/green] {filename}")
    
if __name__ == "__main__":
    etl()