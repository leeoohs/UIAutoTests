import logging


class TestCaseIndexTest:
    # 这里省略了其他代码

    def test_start(self):
        # 设置 root logger 的日志级别为 ERROR
        logging.basicConfig(level=logging.ERROR)

        for step in self.teststeps:
            request = step.request
            # 日志记录请求信息
            logging.info(f"接口名称: {step.name}")
            logging.info(f"接口地址: {request.url}")
            logging.info(f"接口参数: {request.params}")
            logging.info(f"请求头部: {request.headers}")
            logging.info(f"请求cookies: {request.cookies}")
            logging.info(f"请求数据: {request.data}")

            response = request.run()  # 执行请求并获取响应数据

            # 过滤日志级别，只记录 error 级别的日志
            if response.status_code != 200:
                logging.error(f"请求失败，状态码：{response.status_code}")
            else:
                logging.info("请求成功")

            # 日志记录响应信息
            logging.info(f"响应数据: {response.text}")

            # 断言逻辑
            # 此处添加你的断言逻辑
