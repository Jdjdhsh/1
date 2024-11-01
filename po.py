import requests
import time

# Địa chỉ website bạn muốn gửi yêu cầu
url = input("Nhập URL của website: ")

# Số lần gửi yêu cầu
num_requests = 1000000

# Khoảng thời gian giữa các yêu cầu (giây)
delay = 0,2

for i in range(num_requests):
    try:
        response = requests.get(url)
        print(f"Lần gửi yêu cầu {i+1}: Mã trạng thái {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi: {e}")
    
    time.sleep(delay)
