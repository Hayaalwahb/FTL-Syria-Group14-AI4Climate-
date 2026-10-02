from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Climate Action Dashboard")

# مثال: ربط البيانات أو النتائج التي قمت بتحليلها
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Climate Action Dashboard</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
                .card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
                h1 { color: #2c3e50; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🌱 FTL AI4Climate Dashboard</h1>
                <p>Welcome to our climate analysis API and web interface.</p>
                <hr>
                <h3>Main Results:</h3>
                <ul>
                    <li>Analysed indicators: Temperature & Precipitation trends</li>
                    <li>Status: Processing completed successfully</li>
                </ul>
                <p>Check interactive docs at: <a href="/docs">/docs</a></p>
            </div>
        </body>
    </html>
    """

# API Endpoint لمشاركة النتائج كـ JSON
@app.get("/api/data")
def get_climate_data():
    return {
        "project": "AI4Climate Challenge",
        "status": "Success",
        "key_metrics": {
            "avg_temp_change": "+1.5 C",
            "risk_level": "High"
        }
    }