import os
import logging
from datetime import datetime


class Logger:
    def __init__(self, name,  log_level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # 创建一个文件处理器，将日志写入到 logs 目录下的以时间命名的文件中
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        os.makedirs(log_dir, exist_ok=True)
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        log_file = os.path.join(log_dir, f"{name}_{current_time}.log")
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # 创建一个控制台处理器，将日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 定义日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到日志记录器中
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def getLogger(self):
        return self.logger
