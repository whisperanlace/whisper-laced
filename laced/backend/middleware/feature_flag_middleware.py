# middleware/Feature_flag_middleware.py

from fastapi import Request, HTTPException

ENABLED_FEATURES = {"new_dashboard": True, "beta_editor": False}

async def feature_flag_middleware(request: Request, call_next):
    feature = request.query_params.get("feature")
    if feature and not ENABLED_FEATURES.get(feature, False):
        raise HTTPException(status_code=403, detail="Feature disabled")
    response = await call_next(request)
    return response
