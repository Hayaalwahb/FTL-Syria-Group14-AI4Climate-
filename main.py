from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Climate Action Dashboard")


class ClimateInput(BaseModel):
    seasonal_rain: float
    historical_mean: float = 238.6


@app.post("/predict_water_stress")
def predict(data: ClimateInput):
    # استدعاء دالة التقييم هنا
    level, deficit, action = evaluate_seasonal_water_stress(
        data.seasonal_rain, data.historical_mean
    )
    return {
        "threat_level": level,
        "deficit_percent": deficit,
        "recommendation": action,
    }
