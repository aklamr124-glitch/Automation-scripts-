from datetime import datetime
import time

def send_notification():
    print("🔔 تذكير: خليك مركز وابدأ شغلك! الوقت:", datetime.now())

while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == "09:00":  # يرن الساعة 9 صباحًا
        send_notification()
        time.sleep(60)  # يمنع التكرار في نفس الدقيقة
