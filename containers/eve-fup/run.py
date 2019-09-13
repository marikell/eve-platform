import schedule
import time
from helpers.logging import get_log
from jobs.user_job import UserJob
from jobs.exam_job import ExamJob
from jobs.send_exam_job import SendExamJob
from jobs.receive_exam_job import ReceiveExamJob

# schedule.every().minute.do(UserJob().run)
# schedule.every().day.at("12:42").do(fup_job.execute_routine)
# schedule.every().week.at("20:18").do(fup_job.execute_routine)

# SendExamJob().run()
ReceiveExamJob().run()

# while True:
#     ExamJob().run()
#     schedule.run_pending()
#     time.sleep(1)