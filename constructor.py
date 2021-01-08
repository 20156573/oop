class SieuNhan:
    suc_manh = 13
    so_thu_tu = 1
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1

    def xin_chao(self):
        return f'Xin chào, ta là siêu nhân {self.ten}'

sna = SieuNhan('A', 'Đỏ')
print(sna.ten)
print(sna.mau)
print(sna.xin_chao())
print('giá trị thuộc tính khai báo trong lớp là giá trị của đối tượng luôn')
print(SieuNhan.suc_manh)
print(sna.suc_manh)
print('thay đổi chỉ mỗi giá trị thuộc tính đã được khai báo trong lớp bằng việc thông qua đối tượng\
    chỉ làm thay đổi giá trị thuộc tính đó ở đối tượng đó')
sna.suc_manh = 14
print(sna.suc_manh)
print(SieuNhan.suc_manh)
print('Có thể cập nhật giá trị này trong constructor')
print(SieuNhan.so_thu_tu, sna.so_thu_tu, sna.stt)
snb = SieuNhan('B', 'Xanh')
print(SieuNhan.so_thu_tu, snb.so_thu_tu, snb.stt)
