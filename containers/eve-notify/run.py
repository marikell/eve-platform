from config.configuration import EVE_API
from enums.enums import TipTypeEnum
import requests
import json
import os
import schedule
import time
import traceback
from datetime import datetime
from datetime import date
from jobs.notify_job import NotifyJob
from utils.logger import get_module_logger


schedule.every().day.at(os.environ['RUN_TIME']).do(NotifyJob().run)
get_module_logger().info("Notification Job is going to run at {}...".format(os.environ['RUN_TIME']))
while True:
    try:
        schedule.run_pending()
        time.sleep(10)
    except Exception as e:
        get_module_logger().info("[ERROR] {}".format(str(e)))