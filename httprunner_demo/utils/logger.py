# logger.py
import json
import logging
import time


class TestLogger:
    def __init__(self, log_file='test.log'):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # 文件日志处理器
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # 控制台日志处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_request_info(self, step_name, request_info):
        self.logger.info(f"接口名称: {step_name()}")
        self.logger.info(f"接口地址: {request_info['url']}")
        self.logger.info(f"接口参数: {request_info['data']}")

    def log_response_info(self, response_data):
        if isinstance(response_data, str):
            self.logger.info(f"接口响应: {response_data}")
        else:
            # 将响应数据转换为 JSON 格式的字符串
            json_response = json.dumps(response_data, ensure_ascii=False, indent=4)
            self.logger.info(f"接口响应: {json_response}")

    def log_assertion_info(self, expected_result, actual_result):
        self.logger.info(f"预期结果: {expected_result}")
        self.logger.info(f"实际结果: {actual_result}")

    def start_time(self):
        return time.time()
