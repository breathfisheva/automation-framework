import time
import unittest
from lucyutils.config import Config, DATA_PATH, REPORT_PATH
from lucyutils.log import logger
from lucyutils.file_reader import ExcelReader
from lucyutils.htmltestrunner import HTMLTestRunner
from test.page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '/baidu.xlsx'

    def sub_setUp(self):
        # 初始页面是main page，传入浏览器类型打开浏览器
        self.page = BaiDuMainPage(browser_type='chrome').get(self.URL, maximize_window=False)

    def sub_tearDown(self):
        self.page.quit() #注意这里不是self.driver，这里TestBaiDu类以及没有driver了

    def test_search(self):
        datas = ExcelReader(self.excel).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setUp()
                # self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                # self.driver.find_element(*self.locator_su).click()
                self.page.search(d['search'])
                time.sleep(2)
                # links = self.driver.find_elements(*self.locator_result)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


if __name__ == '__main__':
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='从0搭建测试框架 测试', description='修改html报告')
        runner.run(TestBaiDu('test_search'))