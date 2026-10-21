ma_may_in = input("Nhập mã máy: ")
cong_suat_in = input("Nhập công suất W: ")
so_phut_in = input("Nhập số phút: ")
don_gia_in = input("Nhập đơn giá điện: ")
print(type(ma_may_in), type(cong_suat_in), type(so_phut_in), type(don_gia_in))
cong_suat_w = float(cong_suat_in)
so_phut = int(so_phut_in)
don_gia_kwh = float(don_gia_in)
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print(f"Điện năng tính lại: {dien_nang_kwh} kWh")
print(f"Chi phí tính lại: {chi_phi} VND")