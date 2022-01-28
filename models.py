from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///activities.db")
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), index=True, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return "Person: ID: {}, Name: {}, Age: {}".format(self.id, self.name, self.age)


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    person_id = Column(Integer, ForeignKey("people.id"))
    person = relationship("Person")


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
