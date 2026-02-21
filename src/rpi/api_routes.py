from flask import Flask, jsonify, request
from datetime import datetime, timezone


def register_routes(app):
    # Check the health of the RPI server
    @app.get("/health")
    def health():
        return jsonify({
            "ok": True,
            "ts": datetime.now(timezone.utc).isoformat(),
            "service": "pill-dispenser-api"
        })
    # State Dictionary
    state = {
        "status": "idle",
        "job": {
            "container": 0,
            "queue": 0
        }
    }
    # Check the status of the system
    @app.get("/status")
    def status():
        return jsonify(state)
    
    # Post a request for a pill to be dispensed
    @app.post("/dispense")
    def dispense():
        data = request.get_json()

        container = data.get("container")
        count = data.get("count")

        # Validation: check if we can find the data
        if container is None or count is None:
            return jsonify({
                "ok": False,
                "error": "Missing container or count"
            }), 400

        # Check if busy: If any of the containers are currently dispensing then 
        if state["status"] == "dispensing":
            return jsonify({
                "ok": False,
                "error": "busy"
            }), 409

        # job_id = submit_dispense_job(container, count)
        
        # Successfully recieved the data
        return jsonify({
            "ok": True,
            "accepted": True,
            "job_id": 1923
        }), 202
    
