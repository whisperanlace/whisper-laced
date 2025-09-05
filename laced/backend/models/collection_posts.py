# models/collection_posts.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base

collection_posts = Table(
    "collection_posts",
    Base.metadata,
    Column("collection_id", Integer, ForeignKey("collections.id", ondelete="CASCADE"), primary_key=True),
    Column("post_id", Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
)
