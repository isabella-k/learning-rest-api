from bottle import run, route, view, request, post, get, delete
from datetime import date
import requests

all_members = [dict(id = 1, name = "isabella"), dict(id = 2, name = "Tanya")]

@get('/')
def index():
    return dict(success = True, api_version = 1)

@get('/members')
def get_members():
    return dict(members = all_members, count = len(all_members), success = True)

@get('/members/:id')
def get_member_by_id(id):
    for member in all_members:
        if member['id'] == int(id):
            return dict(member = member, success = True)
    return dict(success = False, error = "user not found")

@post('/members')
def set_member():
    member = request.json
    member["id"] = len(all_members) + 1
    all_members.append(dict(member))
    return member

@delete('/members/:id')
def delete_member_by_id(id):
    for member in all_members:
        if member['id'] == int(id):
            all_members.remove(member)
            return member
    return dict(success = False, error = "user not found")

run(host='0.0.0.0', port=8080, reloader=True, debug=True)