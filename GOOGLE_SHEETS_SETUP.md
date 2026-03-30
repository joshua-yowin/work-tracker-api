# Work Tracker with Google Sheets - Complete Setup Guide 📊

## 🎯 What's Integrated:

✅ **Your Original Features:**
- `/log` endpoint - Your existing task logging to Google Sheets
- Automatic Google Sheets recording
- Project assignment tracking

✅ **New Dashboard Features:**
- WiFi detection (GND-4)
- Start/Stop tracking
- Task management
- Activity visualization
- Report generation
- All data synced to Google Sheets!

## 📋 Google Sheets Structure

Your "Work Tracker" sheet should have two worksheets:

### Sheet 1: Main Tracking (existing)
Headers:
```
Timestamp | Task | Duration | Status | Location | Project
```

### Sheet 2: Tasks (auto-created)
Headers:
```
Timestamp | Task | Priority | Status | Completed Date
```

## 🔧 Setup Steps

### 1. **Google Cloud Setup (If not done already)**

If you don't have `credentials.json`:

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable **Google Sheets API** and **Google Drive API**
4. Create Service Account:
   - Go to "IAM & Admin" → "Service Accounts"
   - Create Service Account
   - Grant "Editor" role
   - Create JSON key
   - Download as `credentials.json`

5. **Share your Google Sheet:**
   - Open your "Work Tracker" sheet
   - Click "Share"
   - Add the service account email (from credentials.json)
   - Give "Editor" permissions

### 2. **Local Development Setup**

```bash
# In VS Code terminal
cd ~/Desktop/server

# Create virtual environment (if not exists)
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Add your credentials.json to the project root
# (The file you downloaded from Google Cloud)

# Create .env file (optional)
echo "GOOGLE_CREDENTIALS=" > .env

# Test locally
python app.py
```

Visit: `http://localhost:8000` - You should see "Work Tracker API Running 🚀"

### 3. **Test Endpoints**

```bash
# Test original logging
curl -X POST http://localhost:8000/log \
  -H "Content-Type: application/json" \
  -d '{"task": "Testing", "time": "30 mins", "location": "Home", "project": "Work Tracker"}'

# Test new tracking
curl -X POST http://localhost:8000/api/track \
  -H "Content-Type: application/json" \
  -d '{"event": "start", "location": "office", "timestamp": "2026-03-28T12:00:00"}'

# Check dashboard
curl http://localhost:8000/api/dashboard
```

### 4. **Azure Deployment with Credentials**

#### Option A: Using Environment Variable (Recommended)

1. **Prepare credentials for Azure:**
```bash
# Convert credentials.json to single line
cat credentials.json | jq -c . | pbcopy  # Mac
# or
cat credentials.json | jq -c . | xclip -selection clipboard  # Linux
# or just copy the entire JSON as one line
```

2. **Add to Azure Environment Variables:**
   - Go to Azure Portal → Your Web App
   - Settings → Configuration → Application settings
   - Click "New application setting"
   - Name: `GOOGLE_CREDENTIALS`
   - Value: Paste the JSON (as single line)
   - Click OK → Save

#### Option B: Upload credentials.json (Less secure)

```bash
# Add credentials.json to your repo (NOT RECOMMENDED for public repos)
# Make sure .gitignore does NOT include credentials.json

git add credentials.json
git commit -m "Add credentials"
git push
```

**⚠️ Warning:** Never commit credentials to public repositories!

### 5. **Update .gitignore (Important!)**

```bash
# Add to .gitignore if using local credentials
echo "credentials.json" >> .gitignore
```

### 6. **Deploy to Azure**

```bash
# Commit and push
git add .
git commit -m "Integrated Google Sheets with dashboard"
git push origin main

# GitHub Actions will automatically deploy!
```

### 7. **Verify Azure Deployment**

1. Visit your Azure app: 
   ```
   https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net
   ```

2. Check logs in Azure Portal:
   - Go to your Web App → Monitoring → Log stream
   - Look for: "✅ Connected to Google Sheets"

3. Test the endpoints:
   ```bash
   curl -X POST https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net/log \
     -H "Content-Type: application/json" \
     -d '{"task": "Azure Test", "time": "5 mins"}'
   ```

4. Check your Google Sheet - new row should appear!

## 🎨 Frontend Setup

The `work-tracker-dashboard.html` is already configured with your Azure URL!

**To use it:**

1. **Option 1: Open directly**
   - Just open the HTML file in a browser
   - Works immediately!

2. **Option 2: Host on Azure**
   - Create a `static` folder in your project
   - Put `work-tracker-dashboard.html` there
   - Update `app.py` to serve it:
   ```python
   @app.route('/')
   def index():
       return send_from_directory('static', 'work-tracker-dashboard.html')
   ```

3. **Option 3: GitHub Pages**
   - Create `gh-pages` branch
   - Push HTML file
   - Enable Pages in GitHub settings

## 📊 Data Flow

```
Frontend Dashboard
    ↓
    POST /api/track
    ↓
Flask Backend (Azure)
    ↓
    ├─→ JSON file (backup)
    └─→ Google Sheets (primary)
```

## 🔍 Monitoring Your Data

### View in Google Sheets:
1. Open your "Work Tracker" sheet
2. See real-time data appearing!

### View in Dashboard:
1. Open `work-tracker-dashboard.html`
2. Click "Start Tracking"
3. Watch activity feed update!

## 🚨 Troubleshooting

### "Google credentials not found"
- Check `credentials.json` is in project root OR
- Verify `GOOGLE_CREDENTIALS` environment variable in Azure

### "Permission denied" on Google Sheets
- Make sure you shared the sheet with the service account email
- Check the email in `credentials.json` → `client_email`

### Data not appearing in sheet
- Check Azure logs for errors
- Verify sheet name is exactly "Work Tracker"
- Test the `/health` endpoint

### CORS errors in browser
- Check if Flask-CORS is installed
- Verify `CORS(app)` is in app.py

## 📱 Using the System

### Daily Workflow:

1. **Open Dashboard** (HTML file or hosted version)
2. **Click "Start Tracking"**
   - If WiFi = GND-4 → Starts automatically at "Office"
   - If not → Select location (Home/Client/Other)
3. **Work on tasks**
   - Add tasks in the Tasks tab
   - Check them off when complete
4. **View Activity**
   - See real-time tracking in Activity feed
   - Check weekly stats
5. **End of Day**
   - Click "Stop Tracking"
   - Generate report if needed

### All data automatically logs to Google Sheets! 📊

## 🎯 Next Steps

1. ✅ Test locally
2. ✅ Set up Google Sheets credentials
3. ✅ Deploy to Azure
4. ✅ Open dashboard and start tracking!

## 📞 API Endpoints Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | API status page |
| `/log` | POST | Original logging (backward compatible) |
| `/api/check-network` | POST | Check if on office WiFi |
| `/api/track` | POST | Track start/stop/heartbeat |
| `/api/dashboard` | GET | Get stats for dashboard |
| `/api/report` | POST | Generate work report |
| `/api/activities` | GET/POST | Manage activities |
| `/api/tasks` | GET/POST/PUT | Manage tasks |
| `/health` | GET | Health check + Sheet status |

## 🎉 You're All Set!

Your Work Tracker now:
- ✅ Tracks work time
- ✅ Detects office WiFi
- ✅ Logs everything to Google Sheets
- ✅ Shows beautiful dashboard
- ✅ Manages tasks
- ✅ Generates reports
- ✅ Runs on Azure
- ✅ Auto-deploys from GitHub

---

**Your Setup:**
- Backend: `https://worktracker-api-joshua123-hzd0fzepcpb9cuec.centralindia-01.azurewebsites.net`
- Office WiFi: `GND-4`
- Google Sheet: "Work Tracker"
