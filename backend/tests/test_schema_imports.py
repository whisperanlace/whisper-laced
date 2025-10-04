from pathlib import Path
import importlib
import sys

# Ensure backend root is on sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

def test_all_schema_imports():
    schemas_path = Path(__file__).resolve().parent.parent / "schemas"
    schema_files = [f.stem for f in schemas_path.glob("*.py") if f.name != "__init__.py"]

    for schema in schema_files:
        try:
            # FIX: use backend.schemas instead of schemas
            importlib.import_module(f"backend.schemas.{schema}")
            print(f"? Successfully imported: {schema}")
        except Exception as e:
            print(f"? Failed to import {schema}: {e}")

if __name__ == "__main__":
    test_all_schema_imports()
