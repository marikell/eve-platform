from utils.logger import get_module_logger

def get_log(string):
    get_module_logger().info(string)