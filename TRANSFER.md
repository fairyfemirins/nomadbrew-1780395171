## Note: GitHub Namespace Mismatch

This repository was published under the authenticated GitHub user (`fairyfemirins`) due to a namespace mismatch in cron mode. To transfer this repository to the intended namespace (`femirins`), follow these steps:

### Transfer Instructions
1. **Fork the Repository**:
   - Visit: [https://github.com/fairyfemirins/nomadbrew-1780395171](https://github.com/fairyfemirins/nomadbrew-1780395171)
   - Click **Fork** and select `femirins` as the destination.

2. **Clone the Fork**:
   ```bash
   git clone https://github.com/femirins/nomadbrew.git
   cd nomadbrew
   ```

3. **Add Original as Upstream (Optional)**:
   ```bash
   git remote add upstream https://github.com/fairyfemirins/nomadbrew-1780395171.git
   ```

4. **Push to New Repository**:
   ```bash
   gh repo create femirins/nomadbrew --public --push --source=. --description "NomadBrew: CLI tool for digital nomads to find work-friendly coffee shops"
   ```

5. **Clean Up**:
   - Delete the original repository (`fairyfemirins/nomadbrew-1780395171`) if no longer needed.

### Why This Happened
- **Cron Mode Limitation**: GitHub CLI (`gh`) cannot create repositories under a namespace other than the authenticated user in cron mode.
- **Fallback**: The repository was published under `fairyfemirins` with a timestamp to avoid conflicts.

### Repository URL
- Original: [https://github.com/fairyfemirins/nomadbrew-1780395171](https://github.com/fairyfemirins/nomadbrew-1780395171)