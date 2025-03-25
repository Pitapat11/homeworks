user_seconds = int(input("Enter the number of seconds '0-8640000': "))

days = user_seconds // 86400
remain_seconds = user_seconds % 86400

hours = remain_seconds // 3600
remain_seconds=remain_seconds % 3600

minutes = remain_seconds // 60
seconds = remain_seconds % 60

if days==1:
    day_word= "день"
elif 2<=days<=4:
    day_word= "днi"
else:
    day_word = "днiв"

print(f"{days} {day_word}, {hours:02d}:{minutes:02d}:{seconds:02d}")
