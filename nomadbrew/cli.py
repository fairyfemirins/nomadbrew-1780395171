import click
from nomadbrew.api import CoffeeShopAPI, CoffeeShop
from nomadbrew.data import CoffeeShopData

@click.group()
def cli():
    """NomadBrew: Find the perfect coffee shop for digital nomads."""
    pass

@cli.command()
@click.argument("location")
def search(location: str):
    """Search for coffee shops in a city."""
    api = CoffeeShopAPI()
    shops = api.search("coffee shop", location)
    data = CoffeeShopData()
    shops.extend(data.get_all())
    
    for shop in shops:
        click.echo(f"{shop.name} - {shop.address}")
        if shop.rating:
            click.echo(f"  Rating: {shop.rating}")
        if shop.wifi:
            click.echo("  Wi-Fi: ✓")
        if shop.outlets:
            click.echo("  Outlets: ✓")
        if shop.vibe:
            click.echo(f"  Vibe: {shop.vibe}")

@cli.command()
@click.argument("name")
@click.argument("address")
@click.option("--wifi/--no-wifi", default=True, help="Does the shop have Wi-Fi?")
@click.option("--outlets/--no-outlets", default=True, help="Does the shop have outlets?")
@click.option("--vibe", help="Describe the vibe (e.g., cozy, quiet, busy).")
def add(name: str, address: str, wifi: bool, outlets: bool, vibe: str):
    """Add a new coffee shop to the database."""
    data = CoffeeShopData()
    shop = CoffeeShop(name=name, address=address, wifi=wifi, outlets=outlets, vibe=vibe)
    data.add(shop)
    click.echo(f"Added {name} to the database!")

@cli.command()
@click.argument("name")
@click.argument("rating", type=float)
def rate(name: str, rating: float):
    """Rate a coffee shop."""
    data = CoffeeShopData()
    data.rate(name, rating)
    click.echo(f"Rated {name} as {rating}!")

if __name__ == "__main__":
    cli()