import scapy.all as scapy
from flask import Flask, request, jsonify, render_template
import threading

# Flask app for the web interface
app = Flask(__name__)

# Global variable to store packet logs
packet_logs = []

# Function to analyze packets
def analyze_packet(packet):
    global packet_logs

    if packet.haslayer(scapy.IP):
        protocol = "TCP" if packet.haslayer(scapy.TCP) else "UDP" if packet.haslayer(scapy.UDP) else "Other"
        src_ip = packet[scapy.IP].src
        dst_ip = packet[scapy.IP].dst
        payload = packet[scapy.Raw].load if packet.haslayer(scapy.Raw) else ""

        log_entry = {
            "source": src_ip,
            "destination": dst_ip,
            "protocol": protocol,
            "payload": payload.decode('utf-8', errors='ignore')
        }
        
        # Check for suspicious activity
        if protocol == "TCP" and packet[scapy.TCP].flags == "S":
            log_entry["alert"] = "Potential SYN scan detected."
        elif protocol == "UDP" and len(payload) > 1000:
            log_entry["alert"] = "Large UDP payload detected."

        packet_logs.append(log_entry)

# Sniffing function
def start_sniffing():
    scapy.sniff(prn=analyze_packet, store=False)

# API endpoint to get packet logs
@app.route("/api/logs", methods=["GET"])
def get_logs():
    return jsonify(packet_logs)

# Web interface
@app.route("/")
def index():
    return render_template("index.html")

# Start Flask app and packet sniffer
if __name__ == "__main__":
    sniff_thread = threading.Thread(target=start_sniffing)
    sniff_thread.daemon = True
    sniff_thread.start()
    app.run(debug=True, port=5000)
