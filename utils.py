from models import Person, db_session


def add_person(person):
    """
    Add a new person record
    :param person: New person data
    :return: None
    """
    new_person = Person(
        name=person["name"],
        age=person["age"]
    )
    db_session.add(new_person)
    db_session.commit()


def get_person_list():
    """
    Returns all records of type person
    :return: A list of all records
    """
    return Person.query.all()


def get_person_by_id(pid):
    """
    Returns the record of type person with the given ID
    :param pid: Person ID
    :return: Person type object
    """
    return Person.query.filter_by(id=pid).first()


def alter_person_by_id(pid, person_data):
    """
    Change the person type record with the given ID
    :param pid: Person ID
    :param person_data: New person data
    :return: None
    """
    person = Person.query.filter_by(id=pid).first()

    person.name = person_data["name"]
    person.age = person_data["age"]

    db_session.add(person)
    db_session.commit()


def delete_person_by_id(pid):
    """
    Deletes the person type record with the given ID
    :param pid: Person ID
    :return: None
    """
    person = Person.query.filter_by(id=pid).first()

    db_session.delete(person)
    db_session.commit()