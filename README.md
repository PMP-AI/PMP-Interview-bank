# PMP-Interview-bank

歡迎參加我們的技術面試。本次面試將以 Git 進行版本控制，請依照以下指示作答：

---

## 作答說明

1. **作答環境：**  
   面試期間，電腦環境已經設定好，請直接在環境中編寫並執行 Python 代碼。

2. **版本控制：**  
   完成所有題目後，請自行建立一個新的 branch（例如：`interview-branch-您的姓名`），並將您的答案 commit 並 push 到該 branch，以便後續審查。

---

## 題目 1：變數與資料型態

**題目描述：**  
請解釋什麼是變數，以及 Python 中常見的資料型態有哪些？  
請撰寫一段程式碼，宣告以下變數：  
- `number` 為整數 10  
- `pi` 為浮點數 3.14  
- `greeting` 為字串 "Hello"  
- `is_active` 為布林值 True  

並依序輸出這些變數。

提示：
請使用 print() 來輸出變數值。

**預期輸出：**  
```terminal
10 3.14 Hello True
```

## 題目 2：流程控制—條件判斷與迴圈

**題目描述：**  
請撰寫一段程式碼，利用 `for` 迴圈從 1 到 10 遍歷每個數字，並使用 `if-else` 判斷該數字是奇數或偶數，然後依據下列格式輸出結果：  
- 當數字為 1 時，輸出：`1 是奇數`  
- 當數字為 2 時，輸出：`2 是偶數`  
依此類推，直到 10。

提示：  
可利用 `range(1, 11)` 與模運算符 `%` 來判斷奇偶。

**預期輸出：**  
```terminal
1 是奇數
2 是偶數
3 是奇數
4 是偶數
5 是奇數
6 是偶數
7 是奇數
8 是偶數
9 是奇數
10 是偶數
```
## 題目 3：函式的定義與使用

**題目描述：**  
請撰寫一個 Python 函式 `add_numbers`，該函式接收兩個數字作為參數並回傳它們的總和。  
請呼叫該函式並傳入數字 3 與 4，然後輸出結果：  


提示：  
定義函式後，記得呼叫並印出回傳結果。

**預期輸出：**  
```bash
總和為: 7
```
