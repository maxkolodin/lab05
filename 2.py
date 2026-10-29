text = input()
cleaned_text = text.replace(" ", "").lower()
if not cleaned_text:
    print("Нет текста")
else: 
    if cleaned_text == cleaned_text[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
