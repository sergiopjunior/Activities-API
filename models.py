from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///activities.db")
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Administrator(Base):
    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), index=True, nullable=False)
    password = Column(String(16), nullable=False)

    def __repr__(self):
        return "Administrator ID: {}, Username: {}, Password: {}".format(self.id, self.username, self.password)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), index=True, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return "Person: ID: {}, Name: {}, Age: {}".format(self.id, self.name, self.age)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    status = Column(String(20), nullable=False)
    person_id = Column(Integer, ForeignKey("people.id"))
    person = relationship("Person")

    def __repr__(self):
        return "Activity: ID: {}, Name: {}, Status: {}, Person ID: {}, Person: {}".format(
            self.id, self.name, self.status, self.person_id, self.person.name)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
