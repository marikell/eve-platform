import schedule
import time
from helpers.logging import get_log
from service.fup_service import routine

def run_fup():
    get_log('Running Eve Fup Routine...')
    routine()


schedule.every().day.at("00:19").do(run_fup)
while True:
    schedule.run_pending()
    time.sleep(1)