import sched
import time

def measurement_task():
    # Your measurement task code goes here
    print("Executing measurement task")

def execute_measurement_task(interval):
    scheduler = sched.scheduler()
    running = False

    def run_task():
        nonlocal running
        while running:
            scheduler.enter(interval, 1, measurement_task, ())
            scheduler.run()

    def start_task():
        nonlocal running
        if not running:
            running = True
            run_task()

    def stop_task():
        nonlocal running
        running = False

    start_task()  # Start the task initially

    # Example usage: start and stop the measurement task
    time.sleep(10)  # Run the task for 10 seconds
    stop_task()  # Stop the task

execute_measurement_task(1)
