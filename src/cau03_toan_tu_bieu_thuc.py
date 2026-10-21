tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_du = tong_phut % 60
print(f"Số giờ: {so_gio}, Số phút còn lại: {so_phut_du}")

su_dung_lau = tong_phut > 60
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("su_dung_lau:", su_dung_lau)
print("du_lieu_hop_le:", du_lieu_hop_le)

# Dự đoán: 100 + 20 * 3 = 100 + 60 = 160 
print("Biểu thức 1:", 100 + 20 * 3)
# Dự đoán: (100 + 20) * 3 = 120 * 3 = 360
print("Biểu thức 2:", (100 + 20) * 3)