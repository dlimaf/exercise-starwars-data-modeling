import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250),unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    password = Column(String(10),nullable=False)

    table_args = (
        UniqueConstraint('email','username'),
    )

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String)
    eye_color = Column(String)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String)
    population = Column(Integer)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String)
    starship_class = Column(String)

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    director = Column(String)
    producer = Column(String)

class FavoritesCharacters(Base):
    __tablename__ = 'favoritescharacters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_characters = Column(Integer, ForeignKey('characters.id'))
    user = relationship(User)
    characters = relationship(Characters)

    def to_dict(self):
        return {}

class FavoritesPlanets(Base):
    __tablename__ = 'favoritesplanets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_planets = Column(Integer, ForeignKey('planets.id'))
    user = relationship(User)
    planets = relationship(Planets)

    def to_dict(self):
        return {}

class FavoritesStarships(Base):
    __tablename__ = 'favoritesstarships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_starships = Column(Integer, ForeignKey('starships.id'))
    user = relationship(User)
    starships = relationship(Starships)

    def to_dict(self):
        return {}

class FavoritesFilms(Base):
    __tablename__ = 'favoritesfilms'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name_films = Column(Integer, ForeignKey('films.id'))
    user = relationship(User)
    films= relationship(Films)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
