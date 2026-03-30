import requests
import datetime
import subprocess
import time

AZURE_URL = "https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net/log"

def get_wifi_name():
    try:
        result = subprocess.check_output(
            ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"]
        ).decode()
        for line in result.split("\n"):
            if " SSID" in line:
                return line.split(":")[1].strip()
    except:
        return "Unknown"

def get_uptime():
    try:
        result = subprocess.check_output(["uptime"]).decode()
        return result.strip()
    except:
        return "Unknown"

def send_log():
    wifi = get_wifi_name()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    uptime = get_uptime()
    data = {
        "task": f"Active | WiFi: {wifi} | {uptime}",
        "time": now
    }
    try:
        response = requests.post(AZURE_URL, json=data)
        print(f"[{now}] Logged: {response.json()}", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)

while True:
    send_log()
    time.sleep(3600)