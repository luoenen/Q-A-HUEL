DEBUG = True
import os
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:luosenen@127.0.0.1:3306/python?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False