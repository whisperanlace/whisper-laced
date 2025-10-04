import logging, json, sys, os

class JsonFormatter(logging.Formatter):
    def format(self, record):
        base = {
            "level": record.levelname.lower(),
            "msg": record.getMessage(),
            "logger": record.name,
        }
        if hasattr(record, "request_id"):
            base["request_id"] = record.request_id
        return json.dumps(base)

def setup_logging():
    root = logging.getLogger()
    if not root.handlers:
        h = logging.StreamHandler(sys.stdout)
        h.setFormatter(JsonFormatter())
        root.addHandler(h)
    root.setLevel(os.environ.get("LOG_LEVEL", "INFO").upper())

def get_logger(name: str = "app"):
    setup_logging()
    return logging.getLogger(name)
