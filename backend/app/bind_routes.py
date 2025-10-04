from fastapi import FastAPI
import importlib, pkgutil

def bind_routes(app: FastAPI) -> None:
    try:
        import backend.routes as routes_pkg
    except Exception:
        return
    for _, modname, ispkg in pkgutil.iter_modules(routes_pkg.__path__):
        if ispkg or not modname.endswith("_routes"):
            continue
        try:
            module = importlib.import_module(f"backend.routes.{modname}")
            router = getattr(module, "router", None)
            if not router:
                continue
            prefix = "/" + modname[:-8]  # strip "_routes"
            app.include_router(router, prefix=prefix, tags=[modname[:-8]])
        except Exception:
            # don't crash API if one module has issues
            continue
