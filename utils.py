from models import Person, Activity, db_session


########################
# Person model methods #
########################
def add_person(person):
    """
    Add a new person record
    :param person: New person data
    :return: New person record
    """
    new_person = Person(
        name=person["name"],
        age=person["age"]
    )
    db_session.add(new_person)
    db_session.commit()

    return new_person


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
    :return: Record changed
    """
    person = Person.query.filter_by(id=pid).first()

    # If a record is found changes to the database are made
    if person:
        old_person = {
            "id": pid,
            "name": person.name,
            "age": person.age
        }
        person.name = person_data["name"]
        person.age = person_data["age"]

        db_session.add(person)
        db_session.commit()

        return old_person

    # If no record is found returns an AttributeErrorException
    raise AttributeError


def delete_person_by_id(pid):
    """
    Deletes the person type record with the given ID
    :param pid: Person ID
    :return: Record deleted
    """
    person = Person.query.filter_by(id=pid).first()

    # If a record is found changes to the database are made
    if person:
        db_session.delete(person)
        db_session.commit()

        return person

    # If no record is found returns an AttributeErrorException
    raise AttributeError


##########################
# Activity model methods #
##########################
def add_activity(activity):
    """
    Add a new activity record
    :param activity: New activity data
    :return: New activity record
    """
    new_activity = Activity(
        name=activity["name"],
        age=activity["person_id"]
    )
    db_session.add(new_activity)
    db_session.commit()

    return new_activity


def get_activity_list():
    """
    Returns all records of type activity
    :return: A list of all records
    """
    return Activity.query.all()


def get_activity_by_id(aid):
    """
    Returns the record of type activity with the given ID
    :param aid: Activity ID
    :return: Activity type object
    """
    return Activity.query.filter_by(id=aid).first()


def alter_activity_by_id(aid, activity_data):
    """
    Change the activity type record with the given ID
    :param aid: Activity ID
    :param activity_data: New activity data
    :return: Record changed
    """
    activity = Activity.query.filter_by(id=aid).first()

    # If a record is found changes to the database are made
    if activity:
        activity.name = activity_data["name"]
        activity.age = activity_data["age"]

        db_session.add(activity)
        db_session.commit()

        return activity

    # If no record is found returns an AttributeErrorException
    raise AttributeError


def delete_activity_by_id(aid):
    """
    Deletes the activity type record with the given ID
    :param aid: Activity ID
    :return: Record deleted
    """
    activity = Activity.query.filter_by(id=aid).first()

    # If a record is found changes to the database are made
    if activity:
        db_session.delete(activity)
        db_session.commit()

        return activity

    # If no record is found returns an AttributeErrorException
    raise AttributeError
