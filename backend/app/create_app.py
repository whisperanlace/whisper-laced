from fastapi import FastAPI

def _cors_config():
    try:
        from .cors import get_cors_config
        return get_cors_config()
    except Exception:
        return {
            "allow_origins": ["http://localhost:3000","http://127.0.0.1:3000"],
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }

def create_app() -> FastAPI:
    app = FastAPI()
    # CORS
    try:
        from fastapi.middleware.cors import CORSMiddleware
        cors = _cors_config()
        app.add_middleware(
            CORSMiddleware,
            allow_origins=cors["allow_origins"],
            allow_credentials=cors["allow_credentials"],
            allow_methods=cors["allow_methods"],
            allow_headers=cors["allow_headers"],
        )
    except Exception:
        pass
    # routes
    try:
        from .bind_routes import bind_routes
        bind_routes(app)
    except Exception:
        pass
    # errors/events if present
    for modname, funcname in (("error_handlers","register_error_handlers"),
                              ("events","register_events")):
        try:
            mod = __import__(f"backend.app.{modname}", fromlist=[funcname])
            getattr(mod, funcname)(app)
        except Exception:
            pass
    return app
