from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds_json = os.environ.get("GOOGLE_CREDENTIALS")

if not creds_json:
    with open("credentials.json") as f:
        creds_dict = json.load(f)
else:
    creds_json = creds_json.strip("'\"")
    creds_dict = json.loads(creds_json)

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open("Work Tracker").sheet1

@app.route("/")
def home():
    return "Work Tracker API Running 🚀"

@app.route("/log", methods=["POST"])
def log():
    try:
        data = request.json
        task = data.get("task")
        time = data.get("time")
        if not task or not time:
            return jsonify({"error": "Missing data"}), 400
        sheet.append_row([task, time, "Active"])
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)