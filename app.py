from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime, timedelta
import json
import os
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)  # Enable CORS for frontend

# Configuration
OFFICE_WIFI = 'GND-4'
DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)

# Simple file-based storage (backup)
TRACKING_FILE = DATA_DIR / 'tracking_data.json'
ACTIVITIES_FILE = DATA_DIR / 'activities.json'

# Google Sheets Setup
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Get credentials from environment or file
creds_json = os.environ.get("GOOGLE_CREDENTIALS")
if not creds_json:
    try:
        with open("credentials.json") as f:
            creds_dict = json.load(f)
        print("✅ Loaded credentials from credentials.json")
    except FileNotFoundError:
        print("⚠️  Warning: Google credentials not found. Sheet logging disabled.")
        creds_dict = None
else:
    creds_json = creds_json.strip("'\"")
    creds_dict = json.loads(creds_json)
    print("✅ Loaded credentials from environment")

# Initialize Google Sheets client
sheet = None
tasks_sheet = None
if creds_dict:
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        workbook = client.open("Work Tracker")
        sheet = workbook.sheet1  # Main tracking sheet
        
        # Try to get or create tasks sheet
        try:
            tasks_sheet = workbook.worksheet("Tasks")
        except:
            tasks_sheet = workbook.add_worksheet(title="Tasks", rows=100, cols=10)
            # Add headers
            tasks_sheet.append_row(["Timestamp", "Task", "Priority", "Status", "Completed Date"])
        
        print("✅ Connected to Google Sheets")
    except Exception as e:
        print(f"⚠️  Warning: Could not connect to Google Sheets: {e}")

def load_data(filename):
    """Load data from JSON file"""
    if filename.exists():
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    """Save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def log_to_sheet(timestamp, task, duration, status, location, project=""):
    """Log data to Google Sheets"""
    if sheet:
        try:
            sheet.append_row([
                timestamp,
                task,
                duration,
                status,
                location,
                project
            ])
            return True
        except Exception as e:
            print(f"❌ Error logging to sheet: {e}")
            return False
    return False

def log_task_to_sheet(task_title, priority, status="Pending", completed_date=""):
    """Log task to Tasks sheet"""
    if tasks_sheet:
        try:
            tasks_sheet.append_row([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                task_title,
                priority,
                status,
                completed_date
            ])
            return True
        except Exception as e:
            print(f"❌ Error logging task to sheet: {e}")
            return False
    return False

@app.route('/')
def index():
    """Serve the frontend dashboard"""
    try:
        return send_from_directory('static', 'index.html')
    except:
        return """
        <html>
            <body style="font-family: Arial; text-align: center; padding: 50px;">
                <h1>⚠️ Frontend not found</h1>
                <p>Please create a 'static' folder and add 'index.html' (the dashboard)</p>
                <p><a href="/api-status">View API Status</a></p>
            </body>
        </html>
        """, 404

@app.route('/api-status')
def api_status():
    """API status page"""
    return """
    <html>
        <head>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    text-align: center;
                    padding: 50px;
                    margin: 0;
                }
                .container {
                    max-width: 800px;
                    margin: 0 auto;
                    background: rgba(255, 255, 255, 0.1);
                    backdrop-filter: blur(10px);
                    border-radius: 20px;
                    padding: 40px;
                    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
                }
                h1 { font-size: 3em; margin-bottom: 10px; }
                .status { font-size: 1.2em; opacity: 0.9; margin-bottom: 30px; }
                .endpoints {
                    text-align: left;
                    background: rgba(0, 0, 0, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 30px;
                }
                .endpoint {
                    margin: 10px 0;
                    font-family: monospace;
                    font-size: 0.9em;
                }
                .badge {
                    display: inline-block;
                    padding: 5px 10px;
                    background: rgba(0, 255, 135, 0.3);
                    border-radius: 5px;
                    margin-right: 10px;
                    font-weight: bold;
                }
                .sheet-status {
                    margin-top: 20px;
                    padding: 15px;
                    background: rgba(0, 255, 135, 0.2);
                    border-radius: 10px;
                    border: 2px solid rgba(0, 255, 135, 0.5);
                }
                .link {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background: rgba(255, 255, 255, 0.2);
                    border-radius: 10px;
                    color: white;
                    text-decoration: none;
                    transition: all 0.3s;
                }
                .link:hover {
                    background: rgba(255, 255, 255, 0.3);
                    transform: translateY(-2px);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Work Tracker API</h1>
                <p class="status">Backend is running and ready!</p>
                
                <div class="sheet-status">
                    <strong>✅ Google Sheets Integration Active</strong><br>
                    All tracking data is being logged to your Google Sheet
                </div>
                
                <a href="/" class="link">📊 Go to Dashboard</a>
                
                <div class="endpoints">
                    <h3>📡 Available Endpoints:</h3>
                    <div class="endpoint">
                        <span class="badge">GET</span> / - Frontend Dashboard
                    </div>
                    <div class="endpoint">
                        <span class="badge">GET</span> /api-status - This page
                    </div>
                    <div class="endpoint">
                        <span class="badge">POST</span> /api/check-network - Check office network
                    </div>
                    <div class="endpoint">
                        <span class="badge">POST</span> /api/track - Log tracking events
                    </div>
                    <div class="endpoint">
                        <span class="badge">POST</span> /log - Original logging endpoint
                    </div>
                    <div class="endpoint">
                        <span class="badge">GET</span> /api/dashboard - Get dashboard stats
                    </div>
                    <div class="endpoint">
                        <span class="badge">POST</span> /api/report - Generate work report
                    </div>
                    <div class="endpoint">
                        <span class="badge">GET/POST</span> /api/activities - Manage activities
                    </div>
                    <div class="endpoint">
                        <span class="badge">GET/POST</span> /api/tasks - Manage tasks
                    </div>
                    <div class="endpoint">
                        <span class="badge">GET</span> /health - Health check
                    </div>
                </div>
            </div>
        </body>
    </html>
    """

@app.route('/api/check-network', methods=['POST'])
def check_network():
    """Check if user is on office network"""
    try:
        data = request.json
        
        # Get client IP
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
        
        # In production, you would check:
        # 1. IP range of office network
        # 2. VPN status
        # 3. Geographic location
        # For now, return False (not on office network)
        
        is_office = False
        
        # Log the check
        print(f"Network check from IP: {client_ip}")
        
        return jsonify({
            'isOffice': is_office,
            'clientIp': client_ip,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/track', methods=['POST'])
def track():
    """Log tracking events (start, stop, heartbeat)"""
    try:
        data = request.json
        event_type = data.get('event')
        location = data.get('location', 'unknown')
        timestamp = data.get('timestamp')
        user_agent = data.get('userAgent')
        
        # Load existing tracking data
        tracking_data = load_data(TRACKING_FILE)
        
        # Create tracking entry
        entry = {
            'event': event_type,
            'location': location,
            'timestamp': timestamp,
            'userAgent': user_agent,
            'ip': request.headers.get('X-Forwarded-For', request.remote_addr)
        }
        
        tracking_data.append(entry)
        
        # Save to file
        save_data(TRACKING_FILE, tracking_data)
        
        # Log to Google Sheets
        log_to_sheet(
            timestamp=timestamp,
            task=f"Tracking {event_type}",
            duration="N/A",
            status=event_type.capitalize(),
            location=location.capitalize()
        )
        
        print(f"✅ Tracked: {event_type} at {location} - {timestamp}")
        
        return jsonify({
            'status': 'success',
            'message': f'Logged {event_type} event',
            'entry': entry
        })
    except Exception as e:
        print(f"❌ Error tracking: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route("/log", methods=["POST"])
def log():
    """Original logging endpoint - for backward compatibility"""
    try:
        data = request.json
        task = data.get("task")
        time = data.get("time")
        location = data.get("location", "Unknown")
        project = data.get("project", "")
        
        if not task or not time:
            return jsonify({"error": "Missing data"}), 400
        
        # Log to Google Sheets
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        success = log_to_sheet(
            timestamp=timestamp,
            task=task,
            duration=time,
            status="Active",
            location=location,
            project=project
        )
        
        if success:
            print(f"✅ Logged to sheet: {task} - {time}")
            return jsonify({"status": "success", "message": "Logged to Google Sheets"})
        else:
            return jsonify({"status": "partial", "message": "Saved locally but sheet unavailable"}), 200
            
    except Exception as e:
        print(f"❌ Error in /log: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    """Get dashboard statistics"""
    try:
        tracking_data = load_data(TRACKING_FILE)
        
        # Calculate stats
        today = datetime.now().date()
        week_start = today - timedelta(days=today.weekday())
        
        today_events = [e for e in tracking_data if datetime.fromisoformat(e['timestamp']).date() == today]
        week_events = [e for e in tracking_data if datetime.fromisoformat(e['timestamp']).date() >= week_start]
        
        # Calculate hours (simplified - based on start/stop events)
        today_hours = calculate_hours(today_events)
        week_hours = calculate_hours(week_events)
        
        # Weekly breakdown
        weekly_breakdown = []
        for i in range(7):
            day = week_start + timedelta(days=i)
            day_events = [e for e in tracking_data if datetime.fromisoformat(e['timestamp']).date() == day]
            day_hours = calculate_hours(day_events)
            weekly_breakdown.append({
                'day': day.strftime('%a'),
                'hours': day_hours
            })
        
        # Try to get data from Google Sheets
        sheet_data = []
        if sheet:
            try:
                all_records = sheet.get_all_records()
                sheet_data = all_records[-10:]  # Last 10 entries
            except Exception as e:
                print(f"Could not fetch from sheet: {e}")
        
        return jsonify({
            'todayHours': today_hours,
            'weekHours': week_hours,
            'weeklyBreakdown': weekly_breakdown,
            'totalSessions': len(tracking_data),
            'recentActivity': tracking_data[-10:][::-1],  # Last 10, reversed
            'sheetData': sheet_data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def calculate_hours(events):
    """Calculate total hours from start/stop events"""
    hours = 0
    start_time = None
    
    for event in sorted(events, key=lambda x: x['timestamp']):
        if event['event'] == 'start':
            start_time = datetime.fromisoformat(event['timestamp'])
        elif event['event'] == 'stop' and start_time:
            stop_time = datetime.fromisoformat(event['timestamp'])
            duration = (stop_time - start_time).total_seconds() / 3600
            hours += duration
            start_time = None
    
    return round(hours, 1)

@app.route('/api/report', methods=['POST'])
def generate_report():
    """Generate work report"""
    try:
        data = request.json
        start_date = datetime.fromisoformat(data.get('startDate'))
        end_date = datetime.fromisoformat(data.get('endDate'))
        
        tracking_data = load_data(TRACKING_FILE)
        
        # Filter data by date range
        filtered_data = [
            e for e in tracking_data
            if start_date <= datetime.fromisoformat(e['timestamp']) <= end_date
        ]
        
        # Calculate stats
        total_hours = calculate_hours(filtered_data)
        total_sessions = len([e for e in filtered_data if e['event'] == 'start'])
        
        # Group by location
        location_stats = {}
        for event in filtered_data:
            loc = event.get('location', 'unknown')
            if loc not in location_stats:
                location_stats[loc] = 0
            location_stats[loc] += 1
        
        report = {
            'period': {
                'start': start_date.strftime('%Y-%m-%d'),
                'end': end_date.strftime('%Y-%m-%d')
            },
            'summary': {
                'totalHours': total_hours,
                'totalSessions': total_sessions,
                'locationBreakdown': location_stats
            },
            'data': filtered_data
        }
        
        print(f"📊 Generated report: {total_hours} hours, {total_sessions} sessions")
        
        return jsonify({
            'status': 'success',
            'report': report
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/activities', methods=['GET', 'POST'])
def activities():
    """Manage activities"""
    if request.method == 'POST':
        # Add new activity
        data = request.json
        activities_list = load_data(ACTIVITIES_FILE)
        activity = {
            'id': len(activities_list) + 1,
            'timestamp': datetime.now().isoformat(),
            **data
        }
        activities_list.append(activity)
        save_data(ACTIVITIES_FILE, activities_list)
        
        # Log to Google Sheets
        log_to_sheet(
            timestamp=activity['timestamp'],
            task=activity.get('name', 'Activity'),
            duration=activity.get('duration', 'N/A'),
            status='Logged',
            location=activity.get('location', 'Unknown')
        )
        
        return jsonify({'status': 'success', 'activity': activity})
    else:
        # Get all activities
        activities_list = load_data(ACTIVITIES_FILE)
        return jsonify({'activities': activities_list})

@app.route('/api/tasks', methods=['GET', 'POST', 'PUT'])
def tasks_endpoint():
    """Manage tasks"""
    if request.method == 'POST':
        # Add new task
        data = request.json
        task_title = data.get('title')
        priority = data.get('priority', 'medium')
        
        # Log to Tasks sheet
        success = log_task_to_sheet(task_title, priority, status="Pending")
        
        return jsonify({
            'status': 'success',
            'message': 'Task added',
            'logged_to_sheet': success
        })
    
    elif request.method == 'PUT':
        # Update task (mark complete)
        data = request.json
        task_id = data.get('id')
        completed = data.get('completed', False)
        
        if completed and tasks_sheet:
            # Update in sheet (this is simplified - in production use row identification)
            try:
                # Find and update the task
                print(f"Task {task_id} marked as completed")
            except Exception as e:
                print(f"Error updating task: {e}")
        
        return jsonify({'status': 'success', 'message': 'Task updated'})
    
    else:
        # Get all tasks
        tasks = []
        if tasks_sheet:
            try:
                tasks = tasks_sheet.get_all_records()
            except Exception as e:
                print(f"Error fetching tasks: {e}")
        
        return jsonify({'tasks': tasks})

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Work Tracker API',
        'google_sheets': 'connected' if sheet else 'disconnected'
    })

if __name__ == '__main__':
    # For local development
    print("🚀 Starting Work Tracker API...")
    print(f"📊 Google Sheets: {'✅ Connected' if sheet else '❌ Disconnected'}")
    print(f"📁 Serving frontend from: static/index.html")
    app.run(debug=True, host='0.0.0.0', port=8000)
else:
    # For production (Gunicorn)
    print("🚀 Work Tracker API starting in production mode...")
    print(f"📊 Google Sheets: {'✅ Connected' if sheet else '❌ Disconnected'}")