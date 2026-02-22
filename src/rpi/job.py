from datetime import datetime
import time
import threading
from motor_control import moveToContainer, moveToSize
from state import set_dispensing, set_idle, set_error

def submit_dispense_job(container, size, count)-> str:
    job_id = "job-" +  datetime.now().strftime("%H:%M:%S")
    def worker():
        set_dispensing(container, size, count)
        # moveToContainer(container)

        # moveToSize(size)

        for i in range(count):
            # dispense(count)
            time.sleep(5)
            pass

        set_idle()
    thread = threading.Thread(target=worker)
    thread.start()

    return job_id
    