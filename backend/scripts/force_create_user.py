from backend.db import SessionLocal, engine, Base
from backend.models import User
from backend.core import auth as core_auth

def main():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        email = "whisperandlaced@gmail.com"
        username = email  # ensure NOT NULL username gets a value

        # if already exists by email or username, just update password + flags
        q = db.query(User)
        u = None
        if hasattr(User, "email"):
            u = q.filter(User.email == email).first()
        if not u and hasattr(User, "username"):
            u = q.filter(User.username == username).first()

        if not u:
            u = User()
            if hasattr(u, "email"): u.email = email
            if hasattr(u, "username"): u.username = username
            db.add(u)

        # set password using our compat helper
        pwd = core_auth.get_password_hash("AandD03022022$")
        for f in ("password_hash","hashed_password","password"):
            if hasattr(u, f):
                setattr(u, f, pwd)
                break

        # set safe flags if present
        for k,v in (("is_active",True),("is_admin",True),("active",True),("admin",True),("verified",True)):
            if hasattr(u, k): setattr(u, k, v)

        db.commit()
        db.refresh(u)
        print(f"[force_create_user] OK id={getattr(u,'id',None)} email={getattr(u,'email',None)} username={getattr(u,'username',None)}")
    finally:
        db.close()

if __name__ == "__main__":
    main()

