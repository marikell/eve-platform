from service.user_job import UserJob

class FupJob():
    def __init__(self):
        self.user_job = UserJob()
    def execute_routine(self):
        #user routine
        self.user_job.run()
        