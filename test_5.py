# 嘗試開啟並讀取檔案內容
try:
    with open("sample.txt", "r", encoding="utf-8") as file:  # 讀取模式 'r'
        content = file.read()  # 讀取整個檔案內容
        print(content)  # 輸出到螢幕上
except FileNotFoundError:
    print("檔案不存在，請確認檔案名稱及路徑。")
