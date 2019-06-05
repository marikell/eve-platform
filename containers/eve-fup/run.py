import schedule
import time
from helpers.logging import get_log
from service.fup_service import FupJob

fup_job = FupJob()

schedule.every().day.at("12:42").do(fup_job.execute_routine)

while True:
    schedule.run_pending()
    time.sleep(1)