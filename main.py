from selenium import webdriver
import time


class Sveznoy:
    ''' Класс для работы с модемом связной и отправка СМС-сообщений с него'''
    def __init__(self, f_item=None, cl_item=None):
        self.f_item = f_item
        self.cl_item = cl_item

    def get_page_login(self, url, message_box_item, send_text, click_bottom, pause=3):
        driver = webdriver.Firefox()

        driver.get(str(url))
        time.sleep(pause)
        msg_box = driver.find_element_by_id(message_box_item)
        msg_box.send_keys(send_text)
        time.sleep(pause)
        login_bottom = driver.find_element_by_id(click_bottom)
        login_bottom.click()
        time.sleep(1)
        driver.close()

    def get_page_sms(self, phone, message_text):
        driver = webdriver.Firefox()
        driver.get('http://192.168.1.1/index.html#sms/smsWrite.html')
        time.sleep(1)
        phone_box = driver.find_element_by_id('phoneNumbers')
        phone_box.send_keys(phone)
        time.sleep(1)

        msg_box = driver.find_element_by_id('messageContent')
        msg_box.send_keys(message_text)

if __name__ == '__main__':
    dashboard = Sveznoy()
    dashboard.get_page_login('http://192.168.1.1/index.html#login.html', 'iptPassword', 'admin',
                             'btnLogin', 3)
    dashboard.get_page_sms(89393463310, 'Здесь текст с нашим бомбическим предложением')