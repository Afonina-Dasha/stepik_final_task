#чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:NoSuchElementException 
from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
#метод-конструктор, который вызывается когда мы создаем объект; в качестве параметров передаем экземпляр драйвера
#и url адрес
    def open(self):
        self.browser.get(self.url)
#данный метод открывает нужную страницу в браузере

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True