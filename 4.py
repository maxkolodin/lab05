text = input("Введите текст: ")
words = text.split()
mwords = []
for word in words:
    clean_word = word.strip(".,!?;:").lower()
    if not clean_word:
        continue
    if clean_word.startswith('а'):
        mwords.append(clean_word)
if mwords:
    for w in mwords:
        print(w)
    print(f"Количество: {len(mwords)}")
else:
    print("Нет совпадений")
    print("Количество: 0")
