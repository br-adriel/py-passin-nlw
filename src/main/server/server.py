from flask import Flask
from flask_cors import CORS

from src.main.routes.attendee_routes import attendee_route_bp
from src.main.routes.check_in_routes import check_in_route_bp
from src.main.routes.event_routes import event_route_bp
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)
app.register_blueprint(attendee_route_bp)
app.register_blueprint(check_in_route_bp)
