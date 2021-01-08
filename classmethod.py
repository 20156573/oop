class SieuNhan:
    suc_manh = 13
    def __init__(self, ten, mau):
        self.ten = 'Siêu nhân' + ten
        self.mau = mau
        
    @classmethod
    def cap_nhat_suc_manh(cls, csucmanh):
        cls.suc_manh = csucmanh

    @classmethod
    def get_string(cls, s):
        s = s.split('-')
        s = [sc.strip() for sc in s]
        ten, mau = s
        return cls(ten, mau)

sna = SieuNhan('Gao Đỏ', 'đỏ')
sna2 = SieuNhan('Gao Xanh', 'xanh')
print(sna.suc_manh)
sna.cap_nhat_suc_manh(14)
sna2.cap_nhat_suc_manh(22)
print('Có thể dùng lớp của đối tượng để gọi phương thức, nó có thể cập nhật cả trên class')
print(sna.suc_manh)
print(sna2.suc_manh)
print(SieuNhan.suc_manh)
print('Hoặc dùng lớp để gọi phương thức')
SieuNhan.cap_nhat_suc_manh(15)
print(SieuNhan.suc_manh)

snb = SieuNhan.get_string('Gao Vàng - Vàng')
print(snb.__dict__)