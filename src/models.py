import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favourites = relationship('Favourite', backref='user', lazy=True)

class Favourite(Base):
    __tablename__ = 'favourite'
  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))

class Character(Base):
    __tablename__ = 'character'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    favourites = relationship('Favourite', backref='character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250))
    favourites = relationship('Favourite', backref='planet', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    favourites = relationship('Favourite', backref='vehicle', lazy=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
