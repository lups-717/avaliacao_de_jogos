from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
##import sys; print(sys.path)

Base = declarative_base()
db = SQLAlchemy()