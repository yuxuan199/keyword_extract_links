from keyword_extract_links.extract_links import Extract
import unittest
from tests.request import get_html


class TestExtract(unittest.TestCase):
    # @classmethod
    # @lru_cache()
    # def setUpClass(cls):
    #     url_list = [
    #         "https://tieba.baidu.com/f/search/res?ie=utf-8&qw=%E6%98%93%E6%AC%A1%E5%85%83",
    #         "https://s.weibo.com/weibo?q=%E6%98%93%E6%AC%A1%E5%85%83&Refer=STopic_history"
    #         "https://www.douban.com/group/search?cat=1019&q=%E6%98%93%E6%AC%A1%E5%85%83",
    #         "https://bcy.net/search/home?k=%E6%98%93%E6%AC%A1%E5%85%83"
    #     ]
    #
    #     extract = Extract("https://tieba.baidu.com/f/search/res?ie=utf-8&qw=%E6%98%93%E6%AC%A1%E5%85%83")
    #     print("execute setUpClass")
    #
    # @classmethod
    # def tearDownClass(cls):
    #
    #     print("execute tearDownClass")
    #
    # def setUp(self):
    #     print("execute setUp")
    #
    # def tearDown(self):
    #     print("execute tearDown")

    # def test_get_url_font_website(self):
    #     url_list = [
    #                    "https://tieba.baidu.com/f/search/res?ie=utf-8&qw=%E6%98%93%E6%AC%A1%E5%85%83",
    #                    "https://s.weibo.com/weibo?q=%E6%98%93%E6%AC%A1%E5%85%83&Refer=STopic_history"
    #                    "https://www.douban.com/group/search?cat=1019&q=%E6%98%93%E6%AC%A1%E5%85%83",
    #                    "https://bcy.net/search/home?k=%E6%98%93%E6%AC%A1%E5%85%83"
    #                ]
    #     result_list = [
    #                     ('https', 'tieba.baidu.com'),
    #                     ('https', 's.weibo.com'),
    #                     ('https', 'www.douban.com'),
    #                     ('https', 'bcy.net')
    #                   ]
    #     extract = Extract()
    #
    #     result = zip([
    #
    #     ], result_list)

    def test_judge_u_and_num(self):
        case_list = [
            "https://weibo.com/u/6509857538?nick=%E7%BD%91%E6%98%93%E6%98%93%E6%AC%A1%E5%85%83",
            "https://weibo.com/u/5783158100",
            "https://weibo.com/p/100808accc4e454fc47fd62825826564655357/super_index"
        ]
        case_result = [False, False, True]
        result = zip([Extract.judge_u_and_num(url) for url in case_list], case_result)
        for each_result in result:
            self.assertIs(each_result[0] == each_result[1], True)
        print('execute judge_u_and_num')

    def test_get_url_list(self):
        url_list = [
                       "https://tieba.baidu.com/f/search/res?ie=utf-8&qw=%E6%98%93%E6%AC%A1%E5%85%83",
                       "https://s.weibo.com/weibo?q=%E6%98%93%E6%AC%A1%E5%85%83&Refer=STopic_history"
                   ]
        for url in url_list:
            print(url)
            html = get_html(url)
            extract = Extract(url, html, "易次元")
            url_list = extract.get_url_list()
            print(url_list)


if __name__ == '__main__':
    unittest.main()
