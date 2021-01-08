class SieuNhan:
    suc_manh = 40
    def __init__(self, ten):
        self.ten = ten
        self.smanh = SieuNhan.suc_manh
    @staticmethod
    def bien_hinh():
        print('1, 2, 3 biến hình!')

class SieuNhanGao(SieuNhan):
    suc_manh = 13
    def __init__(self, ten, su_thu):
        super().__init__(ten)
        self.su_thu = su_thu
    # Không thể truy cập super trong staticmethod
    # @staticmethod
    # def bien_hinh():
    #     super().bien_hinh()
    def __len__(self):
        return len(self.ten)

sn1 = SieuNhan('A')
sn2 = SieuNhanGao('B', 'cho')
print(sn1.__dict__)
print(sn2.__dict__)
sn1.bien_hinh()
sn2.bien_hinh()
print(sn2.__len__())