
class Number(object):
    isinstance = None


    def __new__(cls, *args, **kwargs):
        if cls.isinstance is None:
            cls.isinstance = super().__new__(cls)
        return cls.isinstance

    def __init__(self, value):
        self.value = value

    def __str__(self):#для преобразованя в читаемую форму
        return f' {self.value} '

    def __repr__(self):#для преобразованя в читаемую форму
        return f'{self.value}'

num = Number(5)
print(num)
num2 = Number(1)
print(num2)
print(num2 == num)