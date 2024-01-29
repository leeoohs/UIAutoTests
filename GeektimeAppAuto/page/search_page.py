from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword) -> 'SearchPage':
        query = self.driver.find_element(By.CSS_SELECTOR, "input.search-query")
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, ".search-bar .search-cta").click()
        return self

    def get_search_result(self) -> list[dict]:
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".topic-title")))

        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, ".topic-title"):
            title_list.append(element.text)

        return title_list

    def close(self):
        self.driver.quit()