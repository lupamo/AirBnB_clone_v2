#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import uuid
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(String, primary_key=True)
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete-orphan",
                              backref="storage"
                              )
    else:
        name = ""

    @property
    def cities(self):
        """
        method to return the list of city objects
        linked to the current state
        """
        if getenv("HBNB_TYPE_STORAGE") != "db":
            import models
            from models.city import City
            cities_lst = []
            city = models.storage.all()
            for c in city.values(City):
                if c.state_id == self.id:
                    cities_lst.append(c)
            return cities_lst
