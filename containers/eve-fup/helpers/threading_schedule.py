import threading

def run_threaded(job, *args):
    job_thread = threading.Thread(target=job(args))
    return job_thread
