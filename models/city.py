#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    '''
    City for SQLAlchemy or JSON
    '''
    if models.storage_t == "db":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all,delete")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize City
        """
        super().__init__(*args, **kwargs)
