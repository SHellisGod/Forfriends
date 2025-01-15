# Network Security Bot with TCP/UDP Monitoring

This project is a network security bot designed to monitor TCP and UDP traffic in real-time. It uses Python's `Scapy` library to sniff packets, analyze them for potential threats, and displays the data on a Flask-based web dashboard.

## Features
- Packet capture and analysis.
- Detection of SYN scans and large UDP payloads.
- Web dashboard for real-time monitoring.
- API endpoint for accessing logs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-security-bot.git
   cd network-security-bot
# Network Security Bot with TCP/UDP Monitoring

This project is a network security bot designed to monitor TCP and UDP traffic in real-time. It uses Python's `Scapy` library to sniff packets, analyze them for potential threats, and displays the data on a Flask-based web dashboard.

## Features

- **Packet Capture:** Monitors TCP and UDP packets, extracting source IP, destination IP, protocol, and payload.
- **Threat Detection:** Identifies potential SYN scans and large UDP payloads.
- **Web Dashboard:** Displays packet logs dynamically in a user-friendly web interface.
- **API Endpoint:** Provides access to packet logs via a REST API.

## Project Structure

```
project-root
├── app.py             # Main Flask application
├── requirements.txt   # Python dependencies
├── templates
│   └── index.html     # Frontend HTML for the dashboard
└── static
    └── style.css      # Frontend styles (optional)
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/network-security-bot.git
   cd network-security-bot
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and visit `http://localhost:5000` to view the dashboard.

## API Endpoints

- `GET /api/logs` - Retrieve all packet logs in JSON format.

## Example Usage

- Start the application and monitor traffic on your network.
- Use the web dashboard to observe captured packets and flagged threats.
- Integrate additional rules for threat detection by modifying the `analyze_packet` function.

## Dependencies

- Python 3.7+
- Flask
- Scapy

To install these dependencies, use:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
