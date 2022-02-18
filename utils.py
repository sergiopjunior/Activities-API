from models import Person, Activity, Administrator, db_session


########################
# Admin model methods  #
########################
def add_admin(admin):
    """
    Add a new admin record
    :param admin: New admin data
    :return: New admin record
    """
    new_admin = Administrator(
        username=admin["username"],
        password=admin["password"]
    )
    db_session.add(new_admin)
    db_session.commit()

    return new_admin.to_dict()


def get_admin_by_username(username):
    """
    Returns the admin with the given username
    :param username: Admin username
    :return: The record found
    """
    admin = Administrator.query.filter_by(username=username).first()
    return admin.to_dict() if admin else None


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

    return new_person.to_dict()


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
    person = Person.query.filter_by(id=pid).first()
    return person.to_dict() if person else None


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

        new_person = {
            "id": pid,
            "name": person.name,
            "age": person.age
        }

        return old_person, new_person

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
        deleted_person = {
            "id": pid,
            "name": person.name,
            "age": person.age
        }
        db_session.delete(person)
        db_session.commit()

        return deleted_person

    # If no record is found returns an AttributeErrorException
    raise AttributeError


##########################
# Activity model methods #
##########################
def add_activity(activity):
    """
    Add a new activity record
    :param pid: Person ID
    :param activity: New activity data
    :return: New activity record
    """
    person = get_person_by_id(activity["person_id"])

    # If the person responsible for the activity is found the new record is added
    if person:
        new_activity = Activity(
            name=activity["name"],
            person=person
        )
        db_session.add(new_activity)
        db_session.commit()

        new_activity_dict = {
            "id": new_activity.id,
            "name": new_activity.name,
            "responsible": new_activity.person.to_dict()
        }

        return new_activity_dict

    # If the person responsible for the activity is not found, an AttributeErrorException is returned.
    raise AttributeError


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
    activity = Activity.query.filter_by(id=aid).first()

    return activity.to_dict() if activity else None


def alter_activity_by_id(aid, activity_data):
    """
    Change the activity type record with the given ID
    :param aid: Activity ID
    :param activity_data: New activity data
    :return: Record changed
    """
    activity = Activity.query.filter_by(id=aid).first()
    person = get_person_by_id(activity_data["person_id"])

    # If a record is found changes to the database are made
    if activity and person:
        old_activity = {
            "id": aid,
            "name": activity.name,
            "responsible": activity.person.to_dict()
        }
        activity.name = activity_data["name"]
        activity.person = person

        db_session.add(activity)
        db_session.commit()

        new_activity = {
            "id": aid,
            "name": activity.name,
            "responsible": activity.person.to_dict()
        }
        return old_activity, new_activity

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
        deleted_activity = {
            "id": aid,
            "name": activity.name,
            "responsible": activity.person.to_dict()
        }
        db_session.delete(activity)
        db_session.commit()

        return deleted_activity

    # If no record is found returns an AttributeErrorException
    raise AttributeError
