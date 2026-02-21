from flask import Flask, jsonify
from datetime import datetime, timezone


def register_routes(app):
    @app.get("/health")
    def health():
        return jsonify({
            "ok": True,
            "ts": datetime.now(timezone.utc).isoformat(),
            "service": "pill-dispenser-api"
        })