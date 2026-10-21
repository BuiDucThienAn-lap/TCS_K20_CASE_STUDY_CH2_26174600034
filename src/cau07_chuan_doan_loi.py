ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Sửa: cần ép kiểu float để tính toán
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")      # Sửa: thêm _kwh vào biến dien_nang và đóng ngoặc đơn print

# --- BÁO CÁO LỖI VÀ CHÚ THÍCH ---
# Lỗi 1: TypeError khi nhân str với int ở dòng tính dien_nang do cong_suat_w nhận từ input() ở dạng str.
# Lỗi 2: SyntaxError / NameError do thiếu dấu ngoặc đơn ở hàm print cuối và gọi sai tên biến dien_nang (thiếu _kwh)