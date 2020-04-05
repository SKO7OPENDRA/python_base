# def print_human_name(human):
#     print(human['name'])
#
# h1 = {'name': 'ABC'}
# h2 = {'name': 'CDE'}
# h3 = {'full_name': 'EAS'}
#
# print_human_name(h3)


class Phone: # CamelStyle
    def __init__(self, phone_model):
        self._model = phone_model
        self._loading()
        self._serial_number = 987654321645
    def _loading(self):
        print(self._model, 'loading')
    def get_serial_number(self):
        return self._serial_number
    def get_model(self):
        return self._model

# my_phone1 = Phone('nokia 3310')
# my_phone2 = Phone('nokia 1100')
# my_phone1._loading()
# my_phone1._serial_number = 0
# print(my_phone1._serial_number)
# print(my_phone1.get_serial_number())
# print(my_phone1.get_model())
# print(my_phone1.get_model())

class SmartPhone(Phone):
    def sms(self, txt):
        print('SMS sending', txt)
    def email(self):
        print('email sending')

# my_smartphone = SmartPhone('IPhone')
# print(my_smartphone.get_model())
# my_smartphone.sms('123')
# print(my_smartphone._model)

class Iphone(SmartPhone):
    def __init__(self, phone_model):
        super().__init__(phone_model)
        # SmartPhone(self).__init__(phone_model)
        print('Logo showing')
    def player(self):
        print('playing music')
    def browser(self):
        print('browser opening')
    def sms(self, txt):
        print('MMS sending', txt)

# iphone = Iphone('6')
# iphone.sms('12312312')

class NextGenerationSmartPhone(Iphone):
    def touch_id(self):
        print('touch id is working')
    def pay(self):
        print('pay is working')

# class Samsung(NextGenerationSmartPhone):
#     pass
# class Huawei(NextGenerationSmartPhone):
#     pass

class Samsung(NextGenerationSmartPhone):
    def call(self):
        print('своя звонилка самсунговская')
class Huawei(NextGenerationSmartPhone):
    def call(self):
        print('своя звонилка хуавеевская')

samsung = Samsung('S10')
huawei = Huawei('P30')

def my_call(phone):
    phone.call()

my_call(samsung)
my_call(huawei)
