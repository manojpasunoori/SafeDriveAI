def compute_risk(*, temp_c: float, precipitation_mmhr: float, visibility_km: float, hour: int):
    rush = 0.1 if 17 <= hour <= 20 else 0.0
    rain = min(1.0, precipitation_mmhr * 0.25)           # 4 mm/hr -> 1.0
    vis_penalty = max(0.0, (5 - visibility_km)) * 0.12    # <=5 km visibility hurts
    cold_penalty = 0.06 if temp_c <= 0 else 0.0
    score = min(1.0, round(rush + rain + vis_penalty + cold_penalty, 3))
    feats = dict(temp_c=temp_c, precipitation_mmhr=precipitation_mmhr, visibility_km=visibility_km, hour=hour)
    return score, feats
