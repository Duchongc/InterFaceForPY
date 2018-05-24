# coding:utf-8
import os, unittest, time, HTMLTestRunner_jpg
from Common.email import Email
cur_path = os.path.dirname(os.path.realpath(__file__))

def add_case(casename='case',rule='test*.py'):
    case_path = os.path.join(cur_path, casename)
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover
def run_case(allcase,reportName='report'):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)
    if not os.path.exists(report_path): os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+'result.html')
    print('report path:%s'% report_abspath)
    fp = open(report_abspath, 'wb')
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
                                               title='接口自动化测试报告',
                                               description='用例执行情况')
    runner.run(allcase)
    fp.close()
def get_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print('最新报告：'+lists[-1])
    report_file = os.path.join(report_path, lists[-1])
    return report_file
if __name__ == '__main__':
    all_case = add_case()  # 加载用例
    run_case(all_case)     # 执行用例
    report_path = os.path.join(cur_path,'report')  # 用例文件夹
    report_file = get_report_file(report_path)  # 获取最新的测试报告
    print(report_file)
    e = Email(title='测试报告',
              message='这是今天的测试报告，请查收！',
              receiver='1978529954@qq.com',
              server='smtp.163.com',
              sender='m18625680375_1@163.com',
              password='yueyue520',
              path=report_file,

              )
    e.send()
