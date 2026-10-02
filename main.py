from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ClimateInput(BaseModel):
    seasonal_rain: float
    historical_mean: float = 238.6


@app.post("/predict_water_stress")
def predict_water_stress(data: ClimateInput):
    try:
        rain = float(data.seasonal_rain)
        mean_val = float(data.historical_mean)

        # حساب نسبة العجز
        deficit = ((mean_val - rain) / mean_val) * 100

        if deficit >= 35:
            level = "CRITICAL / حرج"
            action = "High drought risk. Recommend immediate shift to supplementary irrigation."
        elif 15 <= deficit < 35:
            level = "WARNING / تحذير"
            action = "Moderate water stress. Implement rainwater harvesting."
        else:
            level = "NORMAL / طبيعي"
            action = "Proceed with standard agricultural plan."

        return {
            "threat_level": level,
            "deficit_percent": round(deficit, 2),
            "recommendation": action,
        }
    except Exception as e:
        return {"error": str(e)}
