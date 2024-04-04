from flask import Blueprint, jsonify, request

from src.data.attendees_handler import AttendeeHandler
from src.errors.error_handler import handle_error
from src.http_types.http_request import HttpRequest

attendee_route_bp = Blueprint("attendee_route", __name__)


@attendee_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendee(event_id):
    try:
        http_request = HttpRequest(
            param={'event_id': event_id}, body=request.json)
        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.register(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@attendee_route_bp.route('/attendees/<attendee_id>/badge', methods=['GET'])
def get_attendee_badge(attendee_id):
    try:
        http_request = HttpRequest(param={'attendee_id': attendee_id})
        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.find_attendee_badge(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code


@attendee_route_bp.route('/events/<event_id>/attendees', methods=['GET'])
def get_event_attendees(event_id):
    try:
        http_request = HttpRequest(param={'event_id': event_id})
        attendee_handler = AttendeeHandler()
        http_response = attendee_handler.find_attendees_from_event(
            http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code
