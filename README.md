# NomadBrew

**Find the perfect coffee shop for digital nomads.**

NomadBrew is a CLI tool to help digital nomads, remote workers, and travelers find the best coffee shops to work from in any city. It combines data from public APIs (Google Places) with crowdsourced reviews to highlight work-friendly spots with good Wi-Fi, outlets, and vibes.

## Features
- **Search** for coffee shops in any city.
- **Add** new coffee shops to the database.
- **Rate** coffee shops based on your experience.
- **Offline Mode** for use in low-connectivity areas.
- **Crowdsourced Data** for community-driven recommendations.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# Search for coffee shops in a city
python -m nomadbrew search "Berlin"

# Add a new coffee shop
python -m nomadbrew add "The Coffee Shop" "123 Main St, Berlin" --wifi --outlets --vibe "Cozy"

# Rate a coffee shop
python -m nomadbrew rate "The Coffee Shop" 4.5
```

## Technical Architecture
- **CLI:** Built with `click` for a user-friendly terminal interface.
- **API:** Uses Google Places API for initial data (fallback to mock data for testing).
- **Data Layer:** Crowdsourced data stored in YAML for simplicity and portability.
- **Offline Mode:** Data is cached locally for offline access.

## License
MIT