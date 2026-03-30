# Work Tracker - Deployment Guide 🚀

## Your Azure Configuration
- **Backend URL**: `https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net`
- **Office WiFi**: `GND-4`

## 📁 Project Structure

```
work-tracker/
├── frontend/
│   └── work-tracker-dashboard.html    (Your dashboard UI)
├── backend/
│   ├── app.py                         (Flask/FastAPI backend)
│   ├── tracker.py                     (Your existing tracker)
│   ├── requirements.txt
│   └── .gitignore
└── README.md
```

## 🔧 Step-by-Step Deployment

### 1. **Setup GitHub Repository**

```bash
# In VS Code terminal
cd ~/Desktop/server

# Initialize git (if not already done)
git init

# Create .gitignore
echo "venv/
__pycache__/
*.pyc
.env
.DS_Store
*.log" > .gitignore

# Add files
git add .
git commit -m "Initial commit - Work Tracker with Azure backend"

# Create GitHub repo and push
git remote add origin https://github.com/YOUR_USERNAME/work-tracker.git
git branch -M main
git push -u origin main
```

### 2. **Backend API Endpoints Needed**

Your Azure backend should have these endpoints:

```python
# app.py (Flask example)
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

# Office network detection
@app.route('/api/check-network', methods=['POST'])
def check_network():
    # You can check IP ranges or other network identifiers
    data = request.json
    # Add your logic to detect if user is on office network
    is_office = False  # Replace with actual logic
    return jsonify({'isOffice': is_office})

# Start/stop tracking
@app.route('/api/track', methods=['POST'])
def track():
    data = request.json
    event_type = data.get('event')  # 'start', 'stop', 'heartbeat'
    location = data.get('location')
    timestamp = data.get('timestamp')
    
    # Save to database or file
    print(f"Tracking event: {event_type} at {location} - {timestamp}")
    
    return jsonify({'status': 'success', 'message': f'Logged {event_type} event'})

# Generate report
@app.route('/api/report', methods=['POST'])
def generate_report():
    data = request.json
    start_date = data.get('startDate')
    end_date = data.get('endDate')
    
    # Generate PDF report (use reportlab or similar)
    # For now, return sample data
    
    return jsonify({
        'status': 'success',
        'reportUrl': 'https://example.com/report.pdf'
    })

# Get dashboard data
@app.route('/api/dashboard', methods=['GET'])
def get_dashboard_data():
    return jsonify({
        'todayHours': 6.5,
        'weekHours': 32,
        'tasksCompleted': 12,
        'recentActivity': [
            {'name': 'Code Review', 'time': '2:30 PM', 'duration': '45m'},
            {'name': 'Team Meeting', 'time': '1:00 PM', 'duration': '60m'}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. **requirements.txt for Azure**

```txt
Flask==3.0.0
Flask-CORS==4.0.0
gunicorn==21.2.0
python-dotenv==1.0.0
reportlab==4.0.7
requests==2.31.0
```

### 4. **Deploy Backend to Azure (GitHub Actions)**

Create `.github/workflows/azure-deploy.yml`:

```yaml
name: Deploy to Azure Web App

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Deploy to Azure Web App
      uses: azure/webapps-deploy@v2
      with:
        app-name: 'worktracker-api-joshua123'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
```

### 5. **Get Azure Publish Profile**

1. Go to Azure Portal → Your Web App
2. Click **"Get publish profile"** (top menu)
3. Download the `.publishsettings` file
4. Copy its contents

### 6. **Add Secret to GitHub**

1. Go to your GitHub repo → Settings → Secrets and variables → Actions
2. Click **"New repository secret"**
3. Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
4. Value: Paste the publish profile content
5. Click **"Add secret"**

### 7. **Deploy Frontend**

You have 3 options:

#### Option A: Azure Static Web Apps (Recommended)
```bash
# Install Azure Static Web Apps CLI
npm install -g @azure/static-web-apps-cli

# Deploy
swa deploy ./frontend --app-name work-tracker-frontend
```

#### Option B: GitHub Pages
```bash
# Create gh-pages branch
git checkout -b gh-pages
git add frontend/work-tracker-dashboard.html
git commit -m "Deploy frontend"
git push origin gh-pages

# Enable GitHub Pages in repo settings
```

#### Option C: Same Azure Web App (Static Files)
- Add frontend HTML to your Flask app's `static` folder
- Serve it from Flask:
```python
@app.route('/')
def index():
    return send_from_directory('static', 'work-tracker-dashboard.html')
```

### 8. **Test Your Setup**

1. **Backend API**: Visit your Azure URL
   ```
   https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net
   ```

2. **Test Endpoints**:
   ```bash
   # Check network
   curl -X POST https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net/api/check-network \
     -H "Content-Type: application/json" \
     -d '{"timestamp": "2026-03-28"}'
   ```

3. **Frontend**: Open `work-tracker-dashboard.html` in browser

### 9. **Continuous Deployment Flow**

```
Local (VS Code) 
    ↓ git push
GitHub Repository
    ↓ GitHub Actions
Azure Web App (Backend)
    ↑ API calls
Frontend (HTML)
```

## 🔒 Environment Variables in Azure

Add these in Azure Portal → Configuration → Application Settings:

- `OFFICE_WIFI_SSID`: `GND-4`
- `OFFICE_IP_RANGE`: Your office IP range
- `DATABASE_URL`: If using database
- `SECRET_KEY`: For session management

## 📊 Monitoring

- **Azure Portal**: Monitor → Metrics
- **Application Insights**: Enable for detailed tracking
- **Logs**: Log stream in Azure Portal

## 🚨 Troubleshooting

### Backend not responding
1. Check Azure logs: Portal → Log stream
2. Verify CORS is enabled
3. Check if app is running: Portal → Overview

### Frontend can't connect
1. Check browser console (F12)
2. Verify BACKEND_URL in HTML
3. Check CORS headers in response

### GitHub Actions failing
1. Check publish profile is correct
2. Verify `requirements.txt` has all dependencies
3. Check Python version matches

## 📱 Next Steps

1. ✅ Push code to GitHub
2. ✅ Set up GitHub Actions secret
3. ✅ Deploy and test
4. 🔄 Make changes in VS Code
5. 🔄 Push to GitHub (auto-deploys!)

## 🎯 Quick Commands

```bash
# Update and deploy
git add .
git commit -m "Updated tracking features"
git push origin main

# View Azure logs
az webapp log tail --name worktracker-api-joshua123 --resource-group YOUR_RESOURCE_GROUP

# Restart app
az webapp restart --name worktracker-api-joshua123 --resource-group YOUR_RESOURCE_GROUP
```

---

**Your Azure URL**: https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net

**Status**: ✅ Running and ready!
