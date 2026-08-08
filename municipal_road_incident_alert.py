# Install required libraries if running fresh in Colab
# !pip install requests pandas

import json
import requests
import pandas as pd
from datetime import datetime

# 1. Define Road / Municipality Incident Data
incident_data = {
    "municipality_ward": "Ward 14 - Dhone",
    "issue_type": "Severe Pothole",
    "latitude": 15.3911,
    "longitude": 77.8600,
    "severity_level": "High",
    "timestamp": datetime.utcnow().isoformat(),
    "status": "Open"
}

# Convert to DataFrame for local analysis/display
df_incident = pd.DataFrame([incident_data])
print("Logged Incident Details:")
display(df_incident)

# 2. Setup Municipal Alert Dispatcher
# Replace with your target municipal endpoint or mock webhook (e.g., webhook.site)
MUNICIPAL_WEBHOOK_URL = "https://webhook.site"

def send_municipal_alert(data, url):
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            print("Alert successfully dispatched to municipal authority!")
        else:
            print(f"Failed to send alert. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to webhook: {e}")

# Trigger the alert
send_municipal_alert(incident_data, MUNICIPAL_WEBHOOK_URL)

# 3. Export data locally to save/commit
df_incident.to_csv("municipal_road_alert.csv", index=False)
