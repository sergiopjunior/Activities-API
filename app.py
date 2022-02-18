from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from utils import *

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verify_password(username, password):
    if username and password:
        admin = get_admin_by_username(username)
        if admin:
            return password == admin["password"]
    return False


# Administrator class methods #
class Administrator(Resource):
    @auth.login_required
    def put(self):
        response = None
        try:
            data = request.json
            new_admin = add_admin(data)
            response = {
                "Status": "Success",
                "Admin Added": new_admin
            }
        except Exception as e:
            print("Error: {}, Message: {}".format(type(e), e))
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response


# Person class methods #
class Person(Resource):
    def get(self, pid):
        response = None
        try:
            response = get_person_by_id(pid)
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "Person not found"
            }
        except Exception as e:
            print("Error: {}, Message: {}".format(type(e), e))
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response

    @auth.login_required
    def put(self, pid):
        response = None
        try:
            data = request.json
            new_person = add_person(data)
            response = {
                "Status": "Success",
                "Person Added": new_person
            }
        except Exception as e:
            print("Error: {}, Message: {}".format(type(e), e))
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response

    @auth.login_required
    def post(self, pid):
        response = None
        try:
            data = request.json
            old_person, new_person = alter_person_by_id(pid, data)
            response = {
                "Status": "Success",
                "Altered Person": {
                    "Old Data": old_person,
                    "New Data": new_person
                }
            }
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "Person not found"
            }
        except Exception as e:
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response

    @auth.login_required
    def delete(self, pid):
        response = None
        try:
            deleted_person = delete_person_by_id(pid)
            response = {
                "Status": "Success",
                "Deleted Person": deleted_person
            }
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "Person not found"
            }
        except Exception as e:
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response


class PersonList(Resource):
    def get(self):
        return [p.to_dict() for p in get_person_list()]


# Activity class methods #
class Activity(Resource):
    def get(self, aid):
        response = None
        try:
            response = get_activity_by_id(aid)
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "Activity not found"
            }
        except Exception as e:
            print("Error: {}, Message: {}".format(type(e), e))
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response

    @auth.login_required
    def put(self, aid):
        response = None
        try:
            data = request.json
            new_activity = add_activity(data)
            response = {
                "Status": "Success",
                "Person Added": new_activity
            }
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "The person responsible for the task was not found. Please check the PID provided"
            }
        except Exception as e:
            print("Error: {}, Message: {}".format(type(e), e))
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response

    @auth.login_required
    def post(self, aid):
        response = None
        try:
            data = request.json
            old_activity, new_activity = alter_activity_by_id(aid, data)
            response = {
                "Status": "Success",
                "Altered Activity": {
                    "Old Data": old_activity,
                    "New Data": new_activity
                }
            }
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "Activity not found"
            }
        except Exception as e:
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response

    @auth.login_required
    def delete(self, aid):
        response = None
        try:
            deleted_activity = delete_activity_by_id(aid)
            response = {
                "Status": "Success",
                "Deleted Activity": deleted_activity
            }
        except AttributeError:
            response = {
                "Status": "Error",
                "Message": "Activity not found"
            }
        except Exception as e:
            response = {
                "Status": f"{type(e).__name__}",
                "Message": f"{e}"
            }
        finally:
            return response


class ActivityList(Resource):
    def get(self):
        return [{"id": a.id, "name": a.name, "responsible": a.person.to_dict()} for a in get_activity_list()]


api.add_resource(Administrator, "/admin/")
api.add_resource(Person, "/person/<int:pid>/")
api.add_resource(PersonList, "/person/")
api.add_resource(Activity, "/activity/<int:aid>/")
api.add_resource(ActivityList, "/activity/")

if __name__ == '__main__':
    app.run(debug=True)
