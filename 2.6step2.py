class UserMail:

    def __init__(self, login, email):
        self.login = login
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if type(email) is str and email.count('@') == 1 and email.find('@') < email.find('.'):
            self.__email = email
        else:
            print('Ошибочная почта')


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait

