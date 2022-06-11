from datetime import date, datetime
dayy = date.today().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
print("today is", dayy)
print("Time right now", time)
