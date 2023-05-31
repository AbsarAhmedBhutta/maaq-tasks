from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
formatted_time = now.strftime("%H:%M:%S")
print(formatted_date)
print(formatted_time)