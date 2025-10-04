from sqlalchemy.orm import Session
from backend.models import Reaction, ReactionType

def add_reaction_to_post(db: Session, user_id: int, post_id: int, rtype: str) -> Reaction:
    # toggle if exists
    existing = db.query(Reaction).filter(Reaction.user_id==user_id, Reaction.post_id==post_id).first()
    if existing:
        db.delete(existing)
        db.commit()
    r = Reaction(user_id=user_id, post_id=post_id, type=ReactionType(rtype))
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

def add_reaction_to_comment(db: Session, user_id: int, comment_id: int, rtype: str) -> Reaction:
    existing = db.query(Reaction).filter(Reaction.user_id==user_id, Reaction.comment_id==comment_id).first()
    if existing:
        db.delete(existing)
        db.commit()
    r = Reaction(user_id=user_id, comment_id=comment_id, type=ReactionType(rtype))
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

