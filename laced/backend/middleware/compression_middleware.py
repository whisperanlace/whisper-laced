# middleware/Compression_middleware.py

from starlette.middleware.gzip import GZipMiddleware

def get_compression_middleware(app):
    app.add_middleware(GZipMiddleware, minimum_size=1000)
