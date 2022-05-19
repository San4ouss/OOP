class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(password):
        for i in password:
            if i.isdigit():
                return False
        return True

    @staticmethod
    def is_include_all_register(password):
        lst = [i for i in password if i == i.upper()]
        return True if len(lst) < 2 else False

    @staticmethod
    def is_include_only_latin(password):
        import string
        check = string.ascii_uppercase + string.ascii_lowercase + '1234567890'
        lst = [i for i in password if i not in check]
        return True if lst else False

    @staticmethod
    def check_password_dictionary(password):
        try:
            with open('easy_passwords.txt', encoding='utf-8') as file:
                return True if password in list(file.read().split()) else False
        except FileNotFoundError:
            print('Невозможно открыть файл')

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        if login.count('@') == 0:
            raise ValueError("Login must include at least one ' @ '")
        elif login.count('.') == 0:
            raise ValueError("Login must include at least one ' . '")
        else:
            self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if type(password) is not str:
            raise TypeError("Пароль должен быть строкой")
        elif 4 > len(password) > 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif self.is_include_digit(password):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif self.is_include_all_register(password):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        elif self.is_include_only_latin(password):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        elif self.check_password_dictionary(password):
            raise ValueError('Ваш пароль содержится в списке самых легких')
        else:
            self.__password = password


c1 = Registration('asd@as.d', 'WeRwer2')
c2 = Registration('dada@asd.a', 'qwerty1234')
print(c1.login, c1.password)
print(c2.login, c2.password)

# a = 10
# if a > 0:
#     print('positive')
# elif a > 5:
#     print('more')
# else:
#     print('Error')

# try:
#     with open('easy_passwords.txt', encoding='utf-8') as file:
#         s = list(file.read().split())
#         print(s)
# except FileNotFoundError:
#     print('Невозможно открыть файл')
