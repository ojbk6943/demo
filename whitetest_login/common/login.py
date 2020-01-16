from whitetest_login.util.services import Services


class Login:

    def input_uname(self,driver,content):
        Services.input(driver,'ID','username',content)

    def input_upass(self,driver,content):
        Services.input(driver, 'ID', 'password', content)

    def input_verifycode(self,driver,content):
        Services.input(driver, 'ID', 'verifycode', content)

    def click_login(self,driver):
        Services.click_ele(driver,'SELECTOR','button.form-control')

    def do_login(self,driver,inff):
        self.input_uname(driver,inff[0])
        self.input_upass(driver,inff[1])
        self.input_verifycode(driver,inff[2])
        self.click_login(driver)

