import pytest
import allure
import requests
from Commonlib.ReadExc import Read_Ex

class Test_Tq():
    def setup_class(self):
        print("开始")

    def tearddown_class(self):
        print("结束")

    res1 = Read_Ex()
    r = res1.read_excel()

    @pytest.mark.parametrize("cityname,key,exp",res1.read_excel())
    def test_tq(self,cityname,key,exp):
        url = "http://v.juhe.cn/weather/index"
        para = {"cityname":cityname,"key":key}
        res2 = requests.get(url,params=para)
        print(res2["error_code"])
        print(exp)

        assert res2["error_code"] == int(exp)