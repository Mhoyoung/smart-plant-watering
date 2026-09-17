from datetime import datetime, timedelta

print("🌱 식물 물주기 알림")

name = input("식물 이름: ")
last_watered = input("마지막으로 물을 준 날짜 (YYYY-MM-DD): ")
cycle = int(input("물주기 주기 (일): "))

last_date = datetime.strptime(last_watered, "%Y-%m-%d")
next_date = last_date + timedelta(days=cycle)

today = datetime.today()
remaining = (next_date - today).days

print("\n--------------------")
print(f"🌱 식물: {name}")
print(f"💧 다음 물주기: {next_date.strftime('%Y-%m-%d')}")

if remaining > 0:
    print(f"⏰ 물주기까지 {remaining}일 남았습니다.")
elif remaining == 0:
    print("🚨 오늘 물을 주세요!")
else:
    print(f"⚠️ 물주기가 {abs(remaining)}일 지났습니다!")