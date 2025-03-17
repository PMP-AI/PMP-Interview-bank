import string
from collections import Counter

def process_text(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()  

        text = text.lower().translate(str.maketrans("", "", string.punctuation))

        words = text.split()

        word_count = Counter(words)

        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

        top_5_words = sorted_word_count[:5]

        for word, count in top_5_words:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("檔案不存在，請確認檔案名稱及路徑。")

process_text("data.txt")
