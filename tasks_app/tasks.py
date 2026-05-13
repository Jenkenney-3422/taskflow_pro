from celery import shared_task
import time

@shared_task
def process_task_data(task_id):
    print(f"Processing task: {task_id}")
    time.sleep(10)
    return f"Finished task {task_id}!"