from backend.db import SessionLocal, engine, Base
from backend.models import User

def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        u = db.query(User).filter(User.email=="whisperandlaced@gmail.com").first()
        if not u: 
            print("No user"); return
        for k in ("is_admin","admin"):
            if hasattr(u,k): setattr(u,k,True)
        db.commit(); db.refresh(u)
        print(f"Promoted: id={u.id} is_admin={getattr(u,'is_admin',None)} admin={getattr(u,'admin',None)}")
    finally:
        db.close()

if __name__=="__main__":
    main()

