import time

from selenium.webdriver.common.by import By
from woniuboss_automation.gui_interface.util.Service import Service



class Marketing:

    # 点击解密
    @classmethod
    def decode(cls,driver):
        Service.get_ele(driver, By.ID, "btn-decrypt").click()

    # 查询功能 area,status,starttime,endtime
    @classmethod
    def marketing_query(cls,driver,marketing_query_data):
        # 状态对应码，对应字典
        status_dict = {"全部":1,"新入库":2,"新认领":3,"已预约":4,"已上门":5,"再投递":6,"已报名":7,
                       "可跟进":8,"无意向":9,"未联系上":10,"培训过":11,"条件不符":12}
        # 在区域下拉框选择一个区域
        select_area = Service.get_ele(driver, By.XPATH, "//select[@name='regionSelect']")
        select_area.click()
        Service.get_select_result(select_area,marketing_query_data['area'])

        #在状态下拉框选择一个状态
        select_status = Service.get_ele(driver, By.XPATH, "//select[@name='cus.last_status']")
        select_status.click()
        Service.get_select_option(select_status,status_dict[marketing_query_data['status']])


        #输入开始时间
        starttime_ele = Service.get_ele(driver, By.NAME, "s_time")
        Service.get_input(starttime_ele, marketing_query_data['starttime'])

        #输入结束时间
        endtime_ele = Service.get_ele(driver, By.NAME, "e_time")
        Service.get_input(endtime_ele, marketing_query_data['endtime'])

        # 点击查询
        marketing_query_ele = Service.get_ele(driver, By.XPATH, "//button[@class='btn btn-padding']")
        marketing_query_ele.click()