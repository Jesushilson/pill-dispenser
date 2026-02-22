import threading

# Lock to prevent race conditions
_state_lock = threading.Lock()

# State Dictionary
state = {
    "status": "idle",   # "idle" | "dispensing"
    "job": {
        "container": None,
        "size": None,
        "count": None
    }
}

def get_state():
    with _state_lock:
        return state.copy()


def set_dispensing(container, size, count):
    with _state_lock:
        state["status"] = "dispensing"
        state["job"]["container"] = container
        state["job"]["size"] = size
        state["job"]["count"] = count


def set_idle():
    with _state_lock:
        state["status"] = "idle"
        state["job"]["container"] = None
        state["job"]["size"] = None
        state["job"]["count"] = None


def set_error(message):
    with _state_lock:
        state["status"] = "error"