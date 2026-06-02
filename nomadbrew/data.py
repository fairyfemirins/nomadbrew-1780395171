import yaml
import os
from typing import List, Dict
from dataclasses import asdict
from nomadbrew.api import CoffeeShop

class CoffeeShopData:
    def __init__(self, data_file: str = "~/.nomadbrew/data.yaml"):
        self.data_file = os.path.expanduser(data_file)
        if self.data_file != ":memory:":
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        self.shops: List[CoffeeShop] = self._load() if self.data_file != ":memory:" else []

    def _load(self) -> List[CoffeeShop]:
        """Load data from YAML file."""
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r") as f:
            data = yaml.safe_load(f) or []
        return [CoffeeShop(**shop) for shop in data]

    def _save(self) -> None:
        """Save data to YAML file."""
        if self.data_file == ":memory:":
            return
        with open(self.data_file, "w") as f:
            yaml.dump([asdict(shop) for shop in self.shops], f)

    def add(self, shop: CoffeeShop) -> None:
        """Add a new coffee shop."""
        self.shops.append(shop)
        self._save()

    def rate(self, name: str, rating: float) -> None:
        """Rate a coffee shop."""
        for shop in self.shops:
            if shop.name == name:
                shop.rating = rating
        self._save()

    def get_all(self) -> List[CoffeeShop]:
        """Get all coffee shops."""
        return self.shops