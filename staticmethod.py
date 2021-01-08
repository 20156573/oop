class SieuNhan:
    suc_manh = 13
    def __init__(self, ten, mau):
        self.ten = 'Siêu nhân' + ten
        self.mau = mau

    @staticmethod
    def bien_hinh():
        return '1, 2, 3 BIẾN HÌNH!'

sna = SieuNhan('A', 'a')
print(sna.bien_hinh())