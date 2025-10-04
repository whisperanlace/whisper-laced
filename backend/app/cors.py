import os
def get_cors_config():
    allow_local = os.getenv("ALLOW_LOCAL_CORS", "0").lower() in ("1","true","yes")
    if allow_local:
        origins = ["http://localhost:3000", "http://127.0.0.1:3000"]
    else:
        env_origins = os.getenv("ALLOW_ORIGINS", "")
        origins = [o.strip() for o in env_origins.split(",") if o.strip()] or [
            "https://app.whisper-laced.com",
            "https://admin.whisper-laced.com",
        ]
    return {
        "allow_origins": origins,
        "allow_credentials": True,
        "allow_methods": ["GET","POST","PUT","PATCH","DELETE","OPTIONS"],
        "allow_headers": ["Authorization","Content-Type","X-Request-ID"],
    }
