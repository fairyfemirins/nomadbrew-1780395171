import os
import requests
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class CoffeeShop:
    name: str
    address: str
    wifi: Optional[bool] = None
    outlets: Optional[bool] = None
    vibe: Optional[str] = None
    rating: Optional[float] = None

class CoffeeShopAPI:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GOOGLE_PLACES_API_KEY")
        self.base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    def search(self, query: str, location: str) -> List[CoffeeShop]:
        """Search for coffee shops using Google Places API."""
        if not self.api_key:
            return self._mock_search(query, location)

        params = {
            "query": f"{query} in {location}",
            "key": self.api_key,
            "type": "cafe",
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()

        return [
            CoffeeShop(
                name=result["name"],
                address=result["formatted_address"],
                rating=result.get("rating"),
            )
            for result in data.get("results", [])
        ]

    def _mock_search(self, query: str, location: str) -> List[CoffeeShop]:
        """Mock data for testing."""
        return [
            CoffeeShop(
                name="Mock Coffee Shop",
                address="123 Mock Street, Mock City",
                wifi=True,
                outlets=True,
                vibe="Cozy",
                rating=4.5,
            )
        ]