from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


# TODO: сделать рефактор кода (повторения)
# TODO: вместо открытия браузера сделать открытие второй вкладки во втором этапе
class Sveznoy:
    ''' Класс для работы с модемом связной и отправка СМС-сообщений с него'''

    def get_page_login(self, url, message_box_item, send_text, click_bottom, pause=3):
        opts = Options()
        opts.headless = True
        assert opts.headless

        driver = webdriver.Firefox(options=opts)
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
        opts = Options()
        opts.headless = True
        assert opts.headless

        driver = webdriver.Firefox(options=opts)
        driver.get('http://192.168.1.1/index.html#sms/smsWrite.html')
        time.sleep(1)

        phone_box = driver.find_element_by_id('phoneNumbers')
        phone_box.send_keys(phone)
        time.sleep(1)

        msg_box = driver.find_element_by_id('messageContent')
        msg_box.send_keys(message_text)
        time.sleep(1)

        btn_sent = driver.find_element_by_id('btnSent')
        btn_sent.click()
        time.sleep(5)
        driver.close()


if __name__ == '__main__':
    dashboard = Sveznoy()
    try:
        dashboard.get_page_login('http://192.168.1.1/index.html#login.html', 'iptPassword', 'admin',
                                 'btnLogin', 3)
    except Exception as e:
        print(e)
    with open('/home/appdev/Рабочий стол/Текущая/Базы/1.txt',
              'r', encoding='utf-8', errors='ignore') as txt_file:
        target_list = txt_file.readlines()
    for abonent in target_list:
        dashboard.get_page_sms(abonent, 'Здесь текст с нашим бомбическим предложением')
        print('Отправил SMS на номер {}'.format(abonent))
