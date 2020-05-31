import sys,os
sys.path.append(os.getcwd())

import requests
import unittest
from Commonlib.ReadExc import Read_Ex

class Test_Tq(unittest.TestCase):
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")

    def test01(self):
        res1 = Read_Ex()
        data = res1.read_excel()
        for i in data:
            url = "http://v.juhe.cn/weather/index"
            para = {"cityname":i["cityname"],"key":i["key"]}
            res = requests.get(url,params=para)
            r = res.json()

            # print(r["error_code"])
            # print(int(i["exp"]))
            self.assertEqual(r["error_code"],int(i["exp"]))

if __name__ == '__main__':
    unittest.main()
