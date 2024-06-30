#!/usr/bin/python3
"""
 a script that changes the name of a State
 object from the database hbtn_0e_6_usa
 """

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
            3306/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.id == 2).first()
    states.name = "New Mexico"
    session.commit()
    session.close()
