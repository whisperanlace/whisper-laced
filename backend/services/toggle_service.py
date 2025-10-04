from sqlalchemy.orm import Session
from backend.models import Toggle
from backend.models import FeatureToggle
from backend.models import SystemFlag
from backend.schemas.toggle_schema import ToggleCreate
from backend.schemas.feature_toggle_schema import FeatureToggleCreate
from backend.schemas.system_flag_schema import SystemFlagCreate

# --- Generic Toggle ---
def create_toggle(db: Session, toggle: ToggleCreate) -> Toggle:
    db_toggle = Toggle(name=toggle.name, enabled=toggle.enabled)
    db.add(db_toggle)
    db.commit()
    db.refresh(db_toggle)
    return db_toggle

def get_toggles(db: Session):
    return db.query(Toggle).all()

# --- Feature Toggles ---
def create_feature_toggle(db: Session, feature: FeatureToggleCreate) -> FeatureToggle:
    db_feature = FeatureToggle(feature_name=feature.feature_name, enabled=feature.enabled)
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature

def get_feature_toggles(db: Session):
    return db.query(FeatureToggle).all()

# --- System Flags ---
def create_system_flag(db: Session, flag: SystemFlagCreate) -> SystemFlag:
    db_flag = SystemFlag(key=flag.key, value=flag.value)
    db.add(db_flag)
    db.commit()
    db.refresh(db_flag)
    return db_flag

def get_system_flags(db: Session):
    return db.query(SystemFlag).all()

