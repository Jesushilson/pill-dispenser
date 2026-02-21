from flask import Flask, jsonify
from api_routes import register_routes

# Function that returns a flask object
def create_app() -> Flask:
    
    # Creates the flask application(Creates the server object)
    app = Flask(__name__)

    # Register the endpoints
    register_routes(app)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
