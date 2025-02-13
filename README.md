#Metadata-Tampering-Tool
The Metadata Tampering Detection Tool is designed to analyze files associated with blockchain transactions, validate their integrity, and detect potential tampering. It compares file metadata (timestamps and hash) with blockchain-stored data to ensure authenticity and generates reports and visualizations to assist in investigations.

## Features
- Extract file metadata (timestamps and SHA256 hash).
- Validate file metadata against blockchain data.
- Detect anomalies in timestamps and file hashes.
- Generate CSV reports and timeline visualizations.
- Real-time monitoring of a directory for new files.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/metadata-tampering-tool.git
   cd metadata-tampering-tool
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure `config/settings.json`:
   ```json
   {
       "infura_api_key": "your-infura-api-key",
       "data_directory": "./data/",
       "output_directory": "./outputs/"
   }
   ```

## Usage
1. Add files to the `data/` directory.
2. Run the program:
   ```bash
   python src/main.py
   ```
3. View results in the `outputs/` directory:
   - **CSV Report**: `anomaly_report.csv`
   - **Visualizations**: Timeline PNG files.

## Example Files
### `wallet.dat`
Contains binary data representing a cryptocurrency wallet. This typically includes:
- Wallet addresses
- Private keys
- Transaction history

### `invoice.pdf`
A sample invoice document. This typically includes:
- Invoice number
- Blockchain transaction ID
- Payment amount (e.g., in cryptocurrency)
- Transaction date

## License
This project is licensed under the MIT License.

