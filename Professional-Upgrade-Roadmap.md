# 🌾 AgroVoice AI - Professional Upgrade Roadmap
## From Basic Voice Assistant to Advanced Agricultural Intelligence Platform

---

## 📋 EXECUTIVE SUMMARY

### Current State (v1.0)
✅ Voice Input/Output (13 Indian languages)
✅ Vision-based crop disease detection
✅ Basic conversational AI
✅ Simple chat history
✅ Basic sidebar controls

### Target State (v2.0 - Professional)
🎯 Perplexity-style interface with live streaming responses
🎯 Crop-specific monitoring & prediction system
🎯 Smart alert system (fertilizer, water, weather)
🎯 Advanced sidebar with crop profiles
🎯 Real-time data visualization
🎯 Predictive analytics dashboard
🎯 Multi-crop management system

---

## 🚀 UPGRADE PHASES - STEP BY STEP

---

## **PHASE 1: PROFESSIONAL UI/UX OVERHAUL** (Week 1-2)
*Transform basic interface into Perplexity-style professional platform*

### 1.1 Modern Landing Page
**What we're building:**
```
┌─────────────────────────────────────────────────────────────┐
│  🌾 AgroVoice AI Pro                    [Profile] [Settings] │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│            ╔════════════════════════════════╗                │
│            ║  "Ask me anything about       ║                │
│            ║   your crops..."               ║                │
│            ║                                ║                │
│            ║  [🎤 Voice] [⌨️ Text] [📷 Scan] ║                │
│            ╚════════════════════════════════╝                │
│                                                               │
│  Quick Actions:                                              │
│  [📊 My Crops] [🌡️ Weather] [💧 Irrigation] [🔔 Alerts]      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Components:**
- Clean, minimal hero section
- Quick action cards
- Recent conversations preview
- Live weather widget

**Technical Implementation:**
```python
# New module: ui_components.py
def render_hero_section():
    st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">🌾 AgroVoice AI Pro</h1>
        <p class="hero-subtitle">Your AI-powered agricultural companion</p>
    </div>
    """, unsafe_allow_html=True)

def render_quick_actions():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.button("📊 My Crops", use_container_width=True)
    with col2:
        st.button("🌡️ Weather", use_container_width=True)
    # ... etc
```

---

### 1.2 Perplexity-Style Streaming Chat
**What we're building:**
```
User: "How to prevent tomato blight?"

AI: [Streaming...] ◉
    Tomato blight can be prevented through several key 
    practices. First, ensure proper spacing between plants...
    
    📚 Sources:
    [1] ICAR Guidelines 2025
    [2] Agricultural Research Journal
    
    🔗 Related:
    • Early signs of tomato blight
    • Fungicide application schedule
    • Resistant tomato varieties
```

**Features:**
- Token-by-token streaming (like ChatGPT/Perplexity)
- Source citations inline
- Related questions suggestions
- Copy/share buttons
- Voice playback option

**Technical Implementation:**
```python
def stream_ai_response(prompt):
    """Stream AI response token by token"""
    placeholder = st.empty()
    full_response = ""
    
    for chunk in groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    ):
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            placeholder.markdown(full_response + "▌")
    
    placeholder.markdown(full_response)
    return full_response
```

---

### 1.3 Advanced Sidebar (Perplexity-Style)
**What we're building:**
```
┌─────────────────────────┐
│ 🌾 AgroVoice AI Pro     │
├─────────────────────────┤
│ 📊 Dashboard            │
│ 🌱 My Crops             │
│   • Tomato (2 acres)    │
│   • Rice (5 acres)      │
│   • Wheat (3 acres)     │
│ 🔔 Active Alerts (3)    │
│ 💧 Irrigation Schedule  │
│ 🌡️ Weather Forecast     │
│ 📈 Analytics            │
│ ⚙️ Settings             │
├─────────────────────────┤
│ Recent Chats:           │
│ • Pest control...       │
│ • Fertilizer timing...  │
│ • Soil pH testing...    │
└─────────────────────────┘
```

**Features:**
- Collapsible sections
- Live status indicators
- Quick navigation
- Session history
- Crop quick-view

---

### 1.4 Modern Message Cards
**What we're building:**
```
╔══════════════════════════════════════════════════════╗
║ 👤 You • 2:30 PM                      [Copy] [Share] ║
║ How to prevent tomato blight?                        ║
╚══════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════╗
║ 🤖 AgroVoice AI • 2:30 PM    [🔊 Play] [Copy] [Share]║
║                                                       ║
║ Tomato blight can be prevented through several...    ║
║                                                       ║
║ 📚 Sources: [1] ICAR [2] Research Journal            ║
║ 🔗 Related: Early detection • Fungicides             ║
╚══════════════════════════════════════════════════════╝
```

**Features:**
- Timestamp display
- Action buttons (copy, share, regenerate)
- Source citations
- Related suggestions
- Voice playback

---

## **PHASE 2: CROP-SPECIFIC MONITORING SYSTEM** (Week 3-4)
*Build intelligent crop management & prediction engine*

### 2.1 Crop Profile System
**What we're building:**
Database schema for crop tracking

```python
# Database: crop_profiles.db

CROP_PROFILES = {
    "crop_id": "unique_id",
    "crop_name": "Tomato",
    "variety": "Roma",
    "area": 2.5,  # acres
    "planting_date": "2025-01-15",
    "expected_harvest": "2025-04-20",
    "soil_type": "Clay loam",
    "irrigation_type": "Drip",
    "location": {
        "latitude": 28.7041,
        "longitude": 77.1025,
        "state": "Delhi"
    },
    "growth_stage": "Flowering",
    "health_status": "Good",
    "alerts": [],
    "history": []
}
```

**Features:**
- Add/edit/delete crops
- Track multiple crops simultaneously
- Growth stage tracking
- Historical data storage

**UI Components:**
```
┌─────────────────────────────────────────────────────┐
│ 🌱 Add New Crop                                     │
├─────────────────────────────────────────────────────┤
│ Crop Type: [Tomato ▼]                              │
│ Variety: [Roma ▼]                                   │
│ Area (acres): [2.5]                                 │
│ Planting Date: [📅 2025-01-15]                      │
│ Soil Type: [Clay loam ▼]                           │
│ Irrigation: [Drip ▼]                                │
│                                                      │
│ [Cancel] [Save Crop]                                │
└─────────────────────────────────────────────────────┘
```

---

### 2.2 Growth Stage Tracking
**What we're building:**
Automatic growth stage detection & monitoring

```python
GROWTH_STAGES = {
    "Tomato": [
        {"stage": "Germination", "days": 7, "description": "Seed sprouting"},
        {"stage": "Seedling", "days": 21, "description": "First true leaves"},
        {"stage": "Vegetative", "days": 35, "description": "Rapid growth"},
        {"stage": "Flowering", "days": 50, "description": "Flower formation"},
        {"stage": "Fruiting", "days": 70, "description": "Fruit development"},
        {"stage": "Harvest", "days": 90, "description": "Ready for harvest"}
    ]
}

def calculate_current_stage(planting_date):
    """Calculate current growth stage based on planting date"""
    days_since_planting = (datetime.now() - planting_date).days
    # Logic to determine stage
    return current_stage
```

**Visual Display:**
```
🌱 Tomato Growth Timeline
═══════════════════════════════════════════════════════
● ─────── ● ─────── ● ─────── ◉ ─────── ○ ─────── ○
Germinate  Seedling  Vegetate  Flowering  Fruiting  Harvest
  Day 7     Day 21    Day 35    Day 50    Day 70    Day 90
                                  ▲
                              You are here
                              (Day 52)
```

---

### 2.3 Predictive Analytics Engine
**What we're building:**
ML-powered predictions for yield, harvest date, disease risk

**Models to Implement:**

**A. Yield Prediction Model**
```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class YieldPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100)
    
    def predict_yield(self, crop_data):
        """
        Inputs:
        - soil_nutrients (N, P, K)
        - weather_data (temp, rainfall, humidity)
        - crop_variety
        - growth_stage
        - historical_yields
        
        Output:
        - predicted_yield (kg/acre)
        - confidence_interval
        """
        features = self.prepare_features(crop_data)
        yield_prediction = self.model.predict(features)
        return yield_prediction
```

**B. Disease Risk Predictor**
```python
class DiseaseRiskPredictor:
    def calculate_risk(self, crop_type, weather, soil_moisture):
        """
        Calculate disease risk based on:
        - Current weather conditions
        - Soil moisture levels
        - Crop susceptibility
        - Historical disease patterns
        
        Returns:
        - risk_level: "Low", "Medium", "High"
        - likely_diseases: ["Blight", "Wilt"]
        - preventive_actions: ["Apply fungicide", "Improve drainage"]
        """
        risk_factors = {
            "high_humidity": weather["humidity"] > 80,
            "warm_temp": 20 <= weather["temp"] <= 30,
            "excessive_moisture": soil_moisture > 80
        }
        
        if sum(risk_factors.values()) >= 2:
            return {
                "risk_level": "High",
                "diseases": ["Late Blight", "Fusarium Wilt"],
                "actions": ["Apply copper fungicide", "Reduce watering"]
            }
```

**Visual Display:**
```
╔═══════════════════════════════════════════════════╗
║ 📊 Tomato - Yield Prediction                     ║
╠═══════════════════════════════════════════════════╣
║                                                   ║
║  Expected Yield: 15-18 tons/acre                 ║
║  Confidence: 87%                                  ║
║                                                   ║
║  [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░] 80% optimal conditions   ║
║                                                   ║
║  📈 Yield Factors:                                ║
║  • Soil Health: ⭐⭐⭐⭐⭐ Excellent                 ║
║  • Weather: ⭐⭐⭐⭐☆ Good                          ║
║  • Irrigation: ⭐⭐⭐☆☆ Moderate                   ║
║                                                   ║
║  💡 Recommendations:                              ║
║  • Increase potassium by 10%                     ║
║  • Monitor for leaf curl virus                   ║
╚═══════════════════════════════════════════════════╝
```

---

### 2.4 Disease Detection & History
**What we're building:**
Advanced vision system with historical tracking

```python
class CropHealthMonitor:
    def __init__(self):
        self.disease_history = []
    
    def analyze_image(self, image, crop_type):
        """
        Analyze crop image and track over time
        """
        result = {
            "timestamp": datetime.now(),
            "crop": crop_type,
            "health_score": 0.85,  # 0-1 scale
            "detected_issues": [
                {
                    "disease": "Early Blight",
                    "confidence": 0.78,
                    "severity": "Mild",
                    "affected_area": "15%",
                    "treatment": "Apply mancozeb fungicide"
                }
            ],
            "recommendations": [
                "Remove affected leaves",
                "Improve air circulation",
                "Apply organic fungicide"
            ]
        }
        
        self.disease_history.append(result)
        return result
```

**Visual Timeline:**
```
🩺 Health History - Tomato Block A

Jan 15 ●━━━━━━━━━ Healthy (Score: 95)
Jan 20 ●━━━━━━━━━ Healthy (Score: 92)
Jan 25 ⚠━━━━━━━━━ Early Blight Detected (Score: 78)
        └─ Treatment: Mancozeb applied
Jan 30 ●━━━━━━━━━ Improving (Score: 85)
Feb 04 ●━━━━━━━━━ Healthy (Score: 93)
        Current
```

---

## **PHASE 3: SMART ALERT SYSTEM** (Week 5-6)
*Intelligent notifications for irrigation, fertilization, weather*

### 3.1 Irrigation Alert System
**What we're building:**
Smart watering recommendations based on multiple factors

**Algorithm:**
```python
class IrrigationScheduler:
    def calculate_water_need(self, crop_data):
        """
        Factors considered:
        1. Soil moisture level (from sensors or estimate)
        2. Crop water requirement (based on growth stage)
        3. Weather forecast (rainfall prediction)
        4. Soil type (water retention capacity)
        5. Evapotranspiration rate
        """
        
        # Base water requirement
        base_requirement = CROP_WATER_NEEDS[crop_data["crop"]][crop_data["stage"]]
        
        # Adjust for soil moisture
        current_moisture = self.get_soil_moisture(crop_data["field_id"])
        optimal_moisture = 70  # percentage
        moisture_deficit = optimal_moisture - current_moisture
        
        # Adjust for weather
        rainfall_forecast = self.get_rainfall_forecast(crop_data["location"])
        
        # Calculate irrigation amount
        irrigation_needed = max(0, (moisture_deficit / 100) * base_requirement - rainfall_forecast)
        
        return {
            "amount": irrigation_needed,  # liters per acre
            "timing": "Early morning (6-8 AM)",
            "duration": f"{irrigation_needed / drip_rate} hours",
            "priority": "High" if moisture_deficit > 20 else "Medium"
        }
```

**Alert Display:**
```
╔═══════════════════════════════════════════════════╗
║ 💧 IRRIGATION ALERT - Tomato Block A              ║
╠═══════════════════════════════════════════════════╣
║ Priority: HIGH                                     ║
║ Current Soil Moisture: 52% (Low)                  ║
║ Optimal Range: 70-80%                             ║
║                                                    ║
║ 📅 Schedule:                                       ║
║ • Today: 6:00 AM - 8:30 AM                        ║
║ • Amount: 2,500 liters (2.5 hrs drip)             ║
║                                                    ║
║ 🌦️ Weather Impact:                                 ║
║ • No rain forecast for next 3 days                ║
║ • Temperature: 32°C (High evaporation)            ║
║                                                    ║
║ [Snooze 1hr] [Mark Done] [View Schedule]         ║
╚═══════════════════════════════════════════════════╝
```

---

### 3.2 Fertilizer Alert System
**What we're building:**
NPK-based fertilization recommendations

```python
class FertilizerAdvisor:
    def recommend_fertilizer(self, crop, stage, soil_test_data):
        """
        Recommendations based on:
        1. Crop type and growth stage
        2. Soil test results (N, P, K, pH)
        3. Previous fertilizer applications
        4. Organic vs. chemical preference
        """
        
        # Get crop-specific requirements
        requirements = FERTILIZER_REQUIREMENTS[crop][stage]
        
        # Calculate deficit
        deficit = {
            "N": requirements["N"] - soil_test_data["N"],
            "P": requirements["P"] - soil_test_data["P"],
            "K": requirements["K"] - soil_test_data["K"]
        }
        
        # Generate recommendations
        if max(deficit.values()) > 0:
            return {
                "type": "NPK Complex" if all(v > 0 for v in deficit.values()) else self.get_specific_fertilizer(deficit),
                "amount": self.calculate_amount(deficit, crop_data["area"]),
                "timing": self.optimal_timing(stage),
                "method": "Fertigation" if crop_data["irrigation"] == "Drip" else "Broadcasting",
                "organic_alternatives": self.get_organic_options(deficit)
            }
```

**Alert Display:**
```
╔═══════════════════════════════════════════════════╗
║ 🌿 FERTILIZER ALERT - Tomato Block A              ║
╠═══════════════════════════════════════════════════╣
║ Stage: Flowering → Fruiting                       ║
║ Next Application: In 3 days                       ║
║                                                    ║
║ 📊 Soil Nutrient Status:                          ║
║ Nitrogen (N):  [▓▓▓▓▓░░░░░] 55% (Low)            ║
║ Phosphorus (P):[▓▓▓▓▓▓▓░░░] 78% (Good)           ║
║ Potassium (K): [▓▓▓▓░░░░░░] 45% (Low)            ║
║                                                    ║
║ 💡 Recommended:                                    ║
║ • NPK 19-19-19: 50 kg/acre                        ║
║ • Application: Through drip irrigation            ║
║ • Timing: Early morning, 2 doses (7-day gap)      ║
║                                                    ║
║ 🌱 Organic Alternative:                            ║
║ • Vermicompost: 100 kg/acre                       ║
║ • Neem cake: 25 kg/acre                           ║
║                                                    ║
║ [Set Reminder] [View Details] [Mark Done]         ║
╚═══════════════════════════════════════════════════╝
```

---

### 3.3 Weather Alert System
**What we're building:**
Real-time weather monitoring with agricultural context

```python
class WeatherAlertSystem:
    def monitor_weather(self, location, crops):
        """
        Monitor and alert for:
        1. Heavy rainfall (flooding risk)
        2. Drought conditions
        3. Frost warnings
        4. Heatwaves
        5. Strong winds (crop damage)
        6. Hail storms
        """
        
        current_weather = self.get_weather_data(location)
        forecast = self.get_forecast(location, days=7)
        
        alerts = []
        
        # Check for adverse conditions
        if forecast["rainfall"] > 100:  # mm
            alerts.append({
                "type": "Heavy Rainfall",
                "severity": "High",
                "impact": "Possible waterlogging, disease risk",
                "action": "Improve drainage, postpone irrigation",
                "affected_crops": self.get_affected_crops(crops, "rainfall")
            })
        
        if forecast["temp_max"] > 40:  # Celsius
            alerts.append({
                "type": "Heatwave",
                "severity": "Medium",
                "impact": "Heat stress, increased water demand",
                "action": "Increase irrigation frequency, provide shade",
                "affected_crops": self.get_affected_crops(crops, "heat")
            })
        
        return alerts
```

**Alert Display:**
```
╔═══════════════════════════════════════════════════╗
║ ⚠️ WEATHER ALERT                                  ║
╠═══════════════════════════════════════════════════╣
║ Heavy Rainfall Warning                            ║
║ Next 48 hours: 120mm rainfall expected            ║
║                                                    ║
║ 🌾 Impact on Your Crops:                          ║
║                                                    ║
║ Tomato (2.5 acres) - HIGH RISK                    ║
║ • Flooding risk in low-lying areas                ║
║ • Late blight disease risk increased              ║
║ • Fruit cracking possible                         ║
║                                                    ║
║ Rice (5 acres) - MEDIUM RISK                      ║
║ • Excessive water may damage seedlings            ║
║                                                    ║
║ 🛡️ Recommended Actions:                           ║
║ 1. Clear drainage channels                        ║
║ 2. Postpone all fertilizer applications           ║
║ 3. Apply copper fungicide (preventive)            ║
║ 4. Harvest mature tomatoes early                  ║
║                                                    ║
║ [View Full Forecast] [Dismiss] [Remind in 6hrs]  ║
╚═══════════════════════════════════════════════════╝
```

---

### 3.4 Alert Management Dashboard
**What we're building:**
Centralized alert hub

```
╔═══════════════════════════════════════════════════╗
║ 🔔 ALERT CENTER (4 Active)                        ║
╠═══════════════════════════════════════════════════╣
║                                                    ║
║ TODAY                                              ║
║ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ║
║ 💧 06:00 AM - Irrigation Alert (Tomato)   [HIGH]  ║
║ 🌿 08:00 AM - Fertilizer Due (Rice)       [MED]   ║
║                                                    ║
║ TOMORROW                                           ║
║ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ║
║ ⚠️ All Day - Heavy Rainfall Warning       [HIGH]   ║
║ 🩺 10:00 AM - Pest Inspection Due         [MED]   ║
║                                                    ║
║ UPCOMING (Next 7 days)                             ║
║ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ║
║ Feb 10 - Growth Stage Change (Flowering)          ║
║ Feb 12 - Soil Test Recommended                    ║
║ Feb 15 - Harvest Window Opens (Rice)              ║
║                                                    ║
║ [Mark All Read] [Settings] [Export Schedule]     ║
╚═══════════════════════════════════════════════════╝
```

---

## **PHASE 4: ANALYTICS DASHBOARD** (Week 7-8)
*Data visualization and insights*

### 4.1 Crop Performance Dashboard
**What we're building:**

```
╔═══════════════════════════════════════════════════╗
║ 📊 CROP PERFORMANCE ANALYTICS                     ║
╠═══════════════════════════════════════════════════╣
║                                                    ║
║ ┌─────────────────────────────────────────────┐   ║
║ │ Health Score Trend (Last 30 days)           │   ║
║ │                                              │   ║
║ │ 100│     ╱╲                                 │   ║
║ │  90│    ╱  ╲    ╱╲                          │   ║
║ │  80│   ╱    ╲  ╱  ╲                         │   ║
║ │  70│  ╱      ╲╱    ╲                        │   ║
║ │    └────────────────────────────────────    │   ║
║ │      Jan    Feb    Mar    Apr              │   ║
║ └─────────────────────────────────────────────┘   ║
║                                                    ║
║ ┌──────────────┬──────────────┬──────────────┐   ║
║ │  Yield       │  Water Used  │  Fertilizer  │   ║
║ │  15.2 tons   │  2,500 L/day │  45 kg NPK   │   ║
║ │  ↑ 12% YoY   │  ↓ 8% saved  │  ↓ 5% saved  │   ║
║ └──────────────┴──────────────┴──────────────┘   ║
║                                                    ║
║ 📈 Key Insights:                                   ║
║ • Health improved 8% after fungicide treatment    ║
║ • Optimal irrigation reduced water by 8%          ║
║ • Yield prediction: 15-18 tons/acre               ║
╚═══════════════════════════════════════════════════╝
```

---

## **TECHNICAL ARCHITECTURE**

### System Architecture
```
┌─────────────────────────────────────────────────────┐
│                   Frontend (Streamlit)              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │Dashboard │  │Chat UI   │  │Alerts    │          │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘          │
├───────┼─────────────┼─────────────┼─────────────────┤
│       │   Application Layer (Python)│               │
│  ┌────▼──────┐  ┌───▼──────┐  ┌───▼──────┐         │
│  │Crop Mgmt  │  │AI Engine │  │Alert Sys │         │
│  └────┬──────┘  └────┬─────┘  └────┬─────┘         │
├───────┼──────────────┼──────────────┼──────────────┤
│       │   Data Layer │              │               │
│  ┌────▼──────┐  ┌───▼──────┐  ┌───▼──────┐         │
│  │SQLite DB  │  │ML Models │  │Weather API│         │
│  └───────────┘  └──────────┘  └───────────┘         │
└─────────────────────────────────────────────────────┘

External Integrations:
├─ Groq API (LLM + Vision)
├─ Weather API (forecast data)
├─ Soil Sensor API (optional)
└─ Market Price API (future)
```

---

## **TECHNOLOGY STACK**

### Core Technologies
```yaml
Frontend:
  - Streamlit (main framework)
  - Plotly/Altair (charts)
  - Streamlit-option-menu (navigation)
  
Backend:
  - Python 3.10+
  - SQLite (local database)
  - Pandas (data processing)
  - NumPy (calculations)
  
AI/ML:
  - Groq API (LLM & Vision)
  - Scikit-learn (predictions)
  - AI4Bharat Indic Parler-TTS (voice)
  - Whisper (speech-to-text)
  
APIs:
  - OpenWeatherMap API (weather)
  - Google Maps API (location)
  
Optional:
  - Redis (caching)
  - PostgreSQL (production DB)
  - FastAPI (REST API backend)
```

---

## **DATABASE SCHEMA**

```sql
-- Crop Profiles
CREATE TABLE crops (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    variety TEXT,
    area_acres REAL,
    planting_date DATE,
    expected_harvest DATE,
    soil_type TEXT,
    irrigation_type TEXT,
    latitude REAL,
    longitude REAL,
    growth_stage TEXT,
    health_score REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Health Records
CREATE TABLE health_records (
    id INTEGER PRIMARY KEY,
    crop_id INTEGER,
    recorded_at TIMESTAMP,
    health_score REAL,
    disease_detected TEXT,
    severity TEXT,
    treatment_applied TEXT,
    notes TEXT,
    FOREIGN KEY (crop_id) REFERENCES crops(id)
);

-- Alerts
CREATE TABLE alerts (
    id INTEGER PRIMARY KEY,
    crop_id INTEGER,
    alert_type TEXT,  -- irrigation, fertilizer, weather, disease
    severity TEXT,    -- low, medium, high
    message TEXT,
    action_required TEXT,
    created_at TIMESTAMP,
    resolved_at TIMESTAMP,
    status TEXT,      -- active, snoozed, resolved
    FOREIGN KEY (crop_id) REFERENCES crops(id)
);

-- Irrigation Schedule
CREATE TABLE irrigation_log (
    id INTEGER PRIMARY KEY,
    crop_id INTEGER,
    scheduled_date DATE,
    scheduled_time TIME,
    amount_liters REAL,
    duration_hours REAL,
    completed BOOLEAN DEFAULT FALSE,
    actual_date DATE,
    notes TEXT,
    FOREIGN KEY (crop_id) REFERENCES crops(id)
);

-- Fertilizer Applications
CREATE TABLE fertilizer_log (
    id INTEGER PRIMARY KEY,
    crop_id INTEGER,
    application_date DATE,
    fertilizer_type TEXT,
    npk_ratio TEXT,
    amount_kg REAL,
    method TEXT,
    notes TEXT,
    FOREIGN KEY (crop_id) REFERENCES crops(id)
);

-- Weather Data Cache
CREATE TABLE weather_cache (
    id INTEGER PRIMARY KEY,
    location TEXT,
    recorded_at TIMESTAMP,
    temperature REAL,
    humidity REAL,
    rainfall REAL,
    wind_speed REAL,
    forecast_data JSON
);

-- Chat History
CREATE TABLE chat_history (
    id INTEGER PRIMARY KEY,
    session_id TEXT,
    role TEXT,  -- user, assistant
    content TEXT,
    timestamp TIMESTAMP,
    language TEXT,
    crop_id INTEGER,
    FOREIGN KEY (crop_id) REFERENCES crops(id)
);
```

---

## **IMPLEMENTATION TIMELINE**

### Week 1-2: UI/UX Overhaul
- [ ] Day 1-2: Hero section & landing page
- [ ] Day 3-4: Streaming chat implementation
- [ ] Day 5-6: Advanced sidebar
- [ ] Day 7-8: Message cards & interactions
- [ ] Day 9-10: Testing & refinement

### Week 3-4: Crop Management
- [ ] Day 1-2: Database setup
- [ ] Day 3-4: Crop profile CRUD
- [ ] Day 5-6: Growth stage tracking
- [ ] Day 7-8: Predictive models (yield)
- [ ] Day 9-10: Disease history tracking

### Week 5-6: Alert System
- [ ] Day 1-2: Irrigation scheduler
- [ ] Day 3-4: Fertilizer advisor
- [ ] Day 5-6: Weather alerts
- [ ] Day 7-8: Alert dashboard
- [ ] Day 9-10: Notification system

### Week 7-8: Analytics & Polish
- [ ] Day 1-3: Dashboard charts
- [ ] Day 4-5: Performance metrics
- [ ] Day 6-7: Data export features
- [ ] Day 8-10: Testing, bug fixes, documentation

---

## **FILE STRUCTURE**

```
agro-voice-advisory/
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables
├── README.md                       # Documentation
│
├── config/
│   ├── settings.py                 # App configuration
│   ├── database.py                 # DB connection
│   └── constants.py                # Constants & configs
│
├── database/
│   ├── models.py                   # SQLAlchemy models
│   ├── schema.sql                  # Database schema
│   └── agro_voice.db               # SQLite database
│
├── modules/
│   ├── ui_components.py            # UI helper functions
│   ├── crop_manager.py             # Crop CRUD operations
│   ├── prediction_engine.py        # ML models
│   ├── alert_system.py             # Alert logic
│   ├── weather_service.py          # Weather API integration
│   ├── irrigation_scheduler.py     # Irrigation logic
│   ├── fertilizer_advisor.py       # Fertilizer recommendations
│   └── analytics.py                # Dashboard analytics
│
├── models/
│   ├── yield_predictor.pkl         # Trained ML model
│   ├── disease_classifier.pkl      # Disease detection model
│   └── risk_calculator.pkl         # Risk assessment model
│
├── assets/
│   ├── css/
│   │   └── custom_styles.css       # Custom CSS
│   ├── images/
│   │   └── crop_icons/             # Crop icon images
│   └── data/
│       ├── crop_database.json      # Crop information
│       ├── fertilizer_guide.json   # Fertilizer data
│       └── disease_database.json   # Disease info
│
└── tests/
    ├── test_crop_manager.py
    ├── test_predictions.py
    └── test_alerts.py
```

---

## **FEATURES SUMMARY**

### Phase 1 Features
✅ Perplexity-style streaming chat
✅ Professional landing page
✅ Advanced sidebar navigation
✅ Modern message cards
✅ Source citations
✅ Related questions

### Phase 2 Features
✅ Multi-crop profile management
✅ Growth stage tracking
✅ Yield prediction (ML)
✅ Disease risk assessment
✅ Historical health tracking
✅ Crop-specific recommendations

### Phase 3 Features
✅ Smart irrigation scheduling
✅ Fertilizer timing alerts
✅ Weather impact warnings
✅ Alert priority system
✅ Notification center
✅ Action tracking

### Phase 4 Features
✅ Performance dashboard
✅ Visual analytics
✅ Trend analysis
✅ Cost tracking
✅ Yield comparisons
✅ Data export

---

## **NEXT STEPS - START HERE**

### Immediate Actions:
1. **Review this roadmap** - Understand the full scope
2. **Choose starting phase** - I recommend Phase 1 (UI/UX)
3. **Set up database** - Create SQLite database
4. **Create file structure** - Organize project files

### What I Can Do Next:
1. **Generate Phase 1 code** - Complete streaming chat UI
2. **Create database schema** - SQL scripts ready to run
3. **Build crop manager module** - CRUD operations
4. **Implement alert system** - Irrigation + fertilizer logic
5. **Create analytics dashboard** - Charts and metrics

---

## **QUESTIONS FOR YOU**

Before we start coding, please confirm:

1. **Which phase do you want to start with?**
   - Phase 1 (UI/UX) - Recommended
   - Phase 2 (Crop Management)
   - Phase 3 (Alerts)
   - Phase 4 (Analytics)

2. **Do you have access to real data?**
   - Soil sensor data
   - Weather API key
   - Historical crop data

3. **Target users:**
   - Individual farmers
   - Farm cooperatives
   - Agricultural consultants

4. **Deployment plan:**
   - Local (personal use)
   - Cloud (Streamlit Community Cloud)
   - Self-hosted (VPS)

**Ready to start? Tell me which phase and I'll generate the complete code!** 🚀
