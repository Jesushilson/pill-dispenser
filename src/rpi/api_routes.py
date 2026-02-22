from flask import Flask, jsonify, request
from job import submit_dispense_job
from state import get_state
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
    
    # Check the status of the system
    @app.get("/status")
    def status():
        return jsonify(get_state())
    
    # Post a request for a pill to be dispensed
    @app.post("/dispense")
    def dispense():
        data = request.get_json(silent=True)

        container = data.get("container")
        size = data.get("size")
        count = data.get("count")

        # Validation: check if we can find the data
        if container is None or count is None or size is None:
            return jsonify({
                "accepted": False,
                "error": "Missing container or count or size"
            }), 400
        state = get_state()
        # Check if busy: If any of the containers are currently dispensing then 
        if state["status"] == "dispensing":
            return jsonify({
                "accepted": False,
                "error": "busy"
            }), 409

        job_id = submit_dispense_job(container, size, count)
        
        # Successfully recieved the data
        return jsonify({
            "accepted": True,
            "accepted": True,
            "job_id": job_id
        }), 202
    
