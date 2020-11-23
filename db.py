from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from api import config

DefaultSessionFactory = sessionmaker(
    bind = create_engine(config.get_sql_uri()))
Base = declarative_base()