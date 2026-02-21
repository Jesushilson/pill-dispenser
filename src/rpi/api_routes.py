from flask import Flask, jsonify
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
        return jsonify({
            state
        })
