# PMP-Interview-bank

歡迎參加我們的面試，請依照以下指示作答：

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
## 題目 4：資料結構—List 與 Dictionary

**題目描述：**

1. **List 操作：**  
   - 建立一個 List `fruits`，內容包含 `"apple"`, `"banana"`, `"cherry"`。  
   - 請先輸出原始 List。  
   - 接著新增 `"orange"`，再輸出更新後的 List。  
   - 最後，輸出 List 中第一個元素。

2. **Dictionary 操作：**  
   - 建立一個 Dictionary `person`，初始內容如下：  
     - `"name": "Alice"`  
     - `"age": 30`  
     - `"city": "Taipei"`  
   - 請輸出原始 Dictionary。  
   - 接著將 `"age"` 更新為 31，再新增一個鍵值對 `"job": "Engineer"`。  
   - 分別輸出更新後的 `"age"` 與整個 Dictionary。

提示：  
利用 List 的 `append()` 方法與 Dictionary 的鍵值存取操作進行修改。

**預期輸出：**  
```terminal
原始 List: ['apple', 'banana', 'cherry']
更新後的 List: ['apple', 'banana', 'cherry', 'orange']
第一個水果: apple
原始 Dictionary: {'name': 'Alice', 'age': 30, 'city': 'Taipei'}
更新後的 age: 31
更新後的 Dictionary: {'name': 'Alice', 'age': 31, 'city': 'Taipei', 'job': 'Engineer'}
```
## 題目 5：檔案操作

**題目描述：**  
假設有一個純文字檔案 `sample.txt`，其內容如下：
Hello, this is a sample file. Welcome to Python programming.
請撰寫一段 Python 程式碼，用以讀取該檔案內容並輸出到螢幕上。  

提示：  
請使用 `with open()` 來讀取檔案，並利用 `try-except` 捕捉 `FileNotFoundError`。

**預期輸出（檔案存在時）：**  
```terminal
Hello, this is a sample file.
Welcome to Python programming.
```
**預期輸出（檔案不存在時）：**  
```terminal
檔案不存在，請確認檔案名稱及路徑。
```

## 題目 6：文字檔案單詞頻率統計（進階題目）

**題目描述：**  
請撰寫一個 Python 程式，用以讀取一個名為 `data.txt` 的文字檔案.

程式需完成以下任務：
1. 忽略大小寫與標點符號（例如：逗號、句號、驚嘆號、分號等）。
2. 統計檔案中每個單詞出現的次數。
3. 輸出出現次數最高的 5 個單詞及其對應的出現次數，依照次數從高到低排序；若次數相同則依照字母順序排序。
4. 請處理檔案讀取過程中的例外情況（例如檔案不存在）。

**預期輸出：**  
```terminal
python: 3
hello: 2
is: 2
world: 2
everyone: 1
```
