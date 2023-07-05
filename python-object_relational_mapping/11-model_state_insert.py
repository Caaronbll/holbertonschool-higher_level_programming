#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State)
    new_state = states.filter_by(name=argv[4]).first()

    if new_state:
        print("{}".format(new_state.id))
    else:
        print("Not found")

    session.close()
