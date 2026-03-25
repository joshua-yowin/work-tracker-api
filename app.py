from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Work Tracker").sheet1


@app.route("/")
def home():
    return "Work Tracker API Running 🚀"


@app.route("/log", methods=["POST"])
def log():
    data = request.json

    task = data.get("task")
    time = data.get("time")

    # Save to Google Sheets
    sheet.append_row([task, time, "Active"])

    return jsonify({"status": "success"})