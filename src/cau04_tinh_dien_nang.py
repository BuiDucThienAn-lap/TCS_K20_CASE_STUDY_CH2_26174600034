cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
print("Số phút 90")
print("Điện năng (kWh):", dien_nang_kwh, type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, type(chi_phi))
so_phut = 60
dien_nang_kwh_moi = cong_suat_w * so_phut / 60 / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh
print("\nSố phút 60")
print("Điện năng mới (kWh):", dien_nang_kwh_moi, type(dien_nang_kwh_moi))
print("Chi phí mới (VND):", chi_phi_moi, type(chi_phi_moi))

# DỰ ĐOÁN VÀ SO SÁNH:
# Với 90 phút: điện năng = 250 * 90 / 60 / 1000 = 0.375 kWh; chi phí = 0.375 * 3000 = 1125.0 VND.
# Với 60 phút: điện năng = 250 * 60 / 60 / 1000 = 0.25 kWh; chi phí = 0.25 * 3000 = 750.0 VND.
# Cả hai kết quả đều thuộc kiểu số thực (float) do có phép chia.