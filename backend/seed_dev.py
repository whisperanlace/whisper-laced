import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from sqlalchemy.orm import Session
from backend.db import SessionLocal, Base, engine
# ensure models are imported
import backend.models  # noqa
from backend.models import Tier
from backend.models import User

Base.metadata.create_all(bind=engine)
db: Session = SessionLocal()

tier = db.query(Tier).filter_by(name="Standard").first()
if not tier:
    tier = Tier(name="Standard", description="Dev seed")
    db.add(tier)
    db.commit()
    db.refresh(tier)

user = db.get(User, 1)
if not user:
    # Minimal fields; adjust if your model requires more
    user = User(id=1)
    try:
        setattr(user, "email", "dev@example.com")
    except Exception:
        pass
    try:
        setattr(user, "username", "dev")
    except Exception:
        pass
    setattr(user, "tier_id", getattr(tier, "id", None))
    db.add(user)
    db.commit()
    db.refresh(user)

print("Seeded: tier id =", tier.id, "user id =", user.id)

