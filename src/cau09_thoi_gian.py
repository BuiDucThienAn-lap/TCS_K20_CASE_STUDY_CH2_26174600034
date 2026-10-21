from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))


# Dự đoán kết quả của phép trừ:
# Thời gian bắt đầu: 13:15, thời gian kết thúc: 15:05 cùng ngày.
# Kết quả phép trừ (thoi_luong) sẽ là: 1 hour, 50 minutes (hoặc dạng 1:50:00)

# Giải thích sự khác nhau giữa datetime, str và timedelta trong ví dụ:
# datetime: Đối tượng biểu diễn mốc thời gian đầy đủ (gồm cả năm, tháng, ngày, giờ, phút, giây), hỗ trợ các phép toán tính toán thời gian
# str (chuỗi): Dữ liệu dạng văn bản thuần túy (được tạo ra qua .strftime()), chỉ để hiển thị hoặc in ra màn hình chứ không thực hiện được phép trừ ngày tháng
# timedelta: Đối tượng biểu diễn khoảng thời gian chênh lệch (duration) sinh ra khi lấy một đối tượng datetime trừ cho một đối tượng datetime khác