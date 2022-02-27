from ast import In
from turtle import back
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from short_links.db import Base
from datetime import datetime

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_link_id = Column(String(8), unique=True, nullable=False, index=True)
    original_url = Column(String(255), nullable=False)
    expiration_date = Column(DateTime(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)
    updated_at = Column(DateTime(), default=datetime.now(), nullable=False)
    stat_id = Column(Integer, ForeignKey('stats.id', ondelete="CASCADE"))
    stat = relationship("Stat", back_populates="link")

    def __init__(self, short_link_id, original_url, expiration_date, *args, **kwargs):
        self.short_link_id = short_link_id
        self.original_url = original_url
        self.expiration_date = expiration_date  

class Stat(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    clicks = Column(Integer, default=0)
    link = relationship('Link', back_populates='stat', uselist=False)
