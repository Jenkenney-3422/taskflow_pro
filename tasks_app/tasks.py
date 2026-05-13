from celery import shared_task
import time

@shared_task
def long_running_task(task_name):
    print(f"Starting work on: {task_name}")
    time.sleep(10) # Simulate a heavy background process
    return f"Finished {task_name}!"