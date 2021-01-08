class U:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten

    @property
    def email(self):
        return self.ho + self.ten + '@cs50.com'

    @property
    def ho_va_ten(self):
        return self.ho + ' ' + self.ten

    def __str__(self):
        return self.ho + ' '+ self.ten + ', email:' + self.email
    
    @ho_va_ten.setter
    def ho_va_ten(self, tenmoi):
        ho_moi, ten_moi = tenmoi.split(' ')
        self.ten = ten_moi
        self.ho = ho_moi

    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ten = None
        print('Đã xóa')

u1 = U('Dang', 'Thuy')
print(u1.email)
print(u1.ho_va_ten)
u1.ten = 'Duc'
print(u1.email)
print(u1.ho_va_ten)
u1.ho_va_ten = 'Ho Hang'
print(u1.ho_va_ten)
del u1.ho_va_ten
print(u1.ho)
print(u1.ten)