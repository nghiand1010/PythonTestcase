# HƯỚNG DẪN XỬ LÝ 3 BÀI CÓ LỖI TESTCASE

> **Ngày**: 23/05/2026  
> **Bài lỗi**: bdsochia2, sodep2, stickers  
> **Lỗi**: "Missing 1 input files" - Testcase files không tồn tại

---

## 📋 TÓM TẮT QUY TRÌNH

```
1. Scrape editorial từ trang /edit  
   ↓
2. Convert editorial sang stdin/stdout (nếu dùng file I/O)  
   ↓
3. Tạo generator.py tự động cho từng bài  
   ↓
4. Chạy generator → tạo 11 testcases + ZIP  
   ↓
5. Upload ZIP lên TICA OJ (xóa cũ → upload → Apply)  
   ↓
6. Auto-submit editorial.py  
   ↓
7. Verify không còn lỗi
```

---

## 🚀 CHẠY PIPELINE TỰ ĐỘNG

### Bước 1: Tạo testcases
```bash
py auto_pipeline_3_bai.py
```

**Output:**
- Tạo `generator.py` cho 3 bài
- Chạy generator → sinh 11 testcases
- Tạo ZIP file (11 testcases, sau đó xóa test 11)
- Kết quả: 3 file ZIP trong `problems/*/`

### Bước 2: Upload testcases
```bash
py auto_upload_3_bai.py
```

**Quy trình upload:**
1. Login vào TICA OJ
2. Mở test_data page của từng bài
3. Nếu có testcases cũ → Xóa (check delete-all → Apply)
4. Upload ZIP file
5. Nhấn Apply để xử lý ZIP
6. Verify có testcases (22 testcases = 11 * 2 input/output, trừ test 11)

**Lưu ý quan trọng:**
- ⚠️ **PHẢI nhấn Apply sau khi select ZIP file**
- ⚠️ **KHÔNG được upload đè lên testcases cũ** (sẽ lỗi "Failed to open as ZIP file")
- ✅ Quy trình đúng: Xóa cũ → Verify = 0 → Upload → Apply

### Bước 3: Submit editorial
```bash
py auto_submit_3_bai.py
```

**Quy trình submit:**
1. Login vào TICA OJ
2. Mở submit page của từng bài
3. Fill code vào Ace editor + sync textarea
4. Select Python 3 (value=9)
5. Submit và lấy submission ID

---

## 📂 CẤU TRÚC THƯ MỤC

```
problems/
├── bdsochia2/
│   ├── editorial.txt          # Editorial gốc từ trang /edit
│   ├── editorial.py           # Converted sang stdin/stdout
│   ├── generator.py           # Auto-generated
│   ├── input1.txt ... input10.txt
│   ├── output1.txt ... output10.txt
│   └── bdsochia2_testcases.zip
├── sodep2/
│   ├── editorial.txt
│   ├── editorial.py
│   ├── generator.py
│   └── sodep2_testcases.zip
└── stickers/
    ├── editorial.txt
    ├── editorial.py           # ⚠️ Đã sửa từ file I/O → stdin/stdout
    ├── generator.py
    └── stickers_testcases.zip
```

---

## 📊 PHÂN TÍCH TỪNG BÀI

### 1. bdsochia2
- **Input format**: `n = int(input())` - Single integer
- **Range**: 1 ≤ n ≤ 10^9
- **Testcases**: 
  - Test 1-3: n = 1, 2, 10
  - Test 4-7: n = 100, 1K, 10K, 100K
  - Test 8-10: n = 1M, 10M, 100M
  - Test 11: n = 1B (xóa sau khi tạo ZIP)

### 2. sodep2
- **Input format**: 
  ```
  T = int(input())          # Số test cases
  for _ in range(T):
      a, b = map(int, input().split())
  ```
- **Range**: 1 ≤ T ≤ 100, 1 ≤ a,b ≤ 10^18
- **Testcases**:
  - Test 1-3: T = 1, 2, 3 với a,b nhỏ
  - Test 4-7: T = 5-50 với a,b medium-large
  - Test 8-10: T = 100 với a,b = 10^9 đến 10^18
  - Test 11: T = 100 với a,b random lớn

### 3. stickers
- **Input format**: 
  ```
  T = input().strip()       # String chứa chữ số
  S = input().strip()       # String chứa chữ số
  ```
- **Range**: Độ dài ≤ 10^5
- **⚠️ Đã sửa**: Editorial gốc dùng file I/O → Đã convert sang stdin/stdout
- **Testcases**:
  - Test 1-3: Strings ngắn (10-20 chars)
  - Test 4-7: Medium (100 - 50K chars)
  - Test 8-10: Large (100K chars)
  - Test 11: Stress (100K chars)

---

## 🔑 CÁC SELECTOR QUAN TRỌNG

```python
# Login
page.fill('input[name="username"]', USERNAME)
page.fill('input[name="password"]', PASSWORD)

# Test data page
delete_all_checkbox = page.locator('input#delete-all')  # Xóa tất cả
apply_button = page.locator('input[type="submit"][value="Apply!"]')  # Apply button
file_input = page.locator('input#id_problem-data-zipfile')  # Upload ZIP

# Submit page
ace_editor = ace.edit("ace_source")  # Ace editor
language_select = page.select_option('select#id_language', '9')  # Python 3
submit_button = page.click('button#submit-button')  # Submit
```

---

## 🐛 XỬ LÝ LỖI

### Lỗi: "Failed to open as ZIP file"
- **Nguyên nhân**: Upload đè lên testcases cũ
- **Giải pháp**: Xóa hết testcases cũ trước khi upload

### Lỗi: "Input file does not exist"
- **Nguyên nhân**: Đã upload ZIP nhưng chưa nhấn Apply
- **Giải pháp**: Nhấn Apply button sau khi select ZIP

### Lỗi: Upload thành công nhưng không có testcases
- **Nguyên nhân**: Chưa nhấn Apply hoặc Apply chưa xử lý xong
- **Giải pháp**: Nhấn Apply và đợi 5s trước khi reload

### Lỗi: stickers dùng file I/O
- **Nguyên nhân**: Editorial gốc dùng `open("STICKERS.INP")` và `open("STICKERS.OUT")`
- **Giải pháp**: Đã sửa trong `editorial.py` sang `input()` và `print()`

---

## ✅ CHECKLIST

- [ ] Đã scrape editorial từ trang /edit (3/3 bài)
- [ ] Đã convert stickers editorial sang stdin/stdout
- [ ] Đã tạo generator.py cho 3 bài
- [ ] Đã chạy generator → tạo ZIP files
- [ ] Đã upload 3 ZIP lên TICA OJ (xóa cũ → upload → Apply)
- [ ] Đã verify không còn lỗi trên test_data page
- [ ] Đã submit 3 editorial.py
- [ ] Đã kiểm tra submissions thành công

---

## 📞 TÀI NGUYÊN

- **Script gốc**: 
  - `scrape_from_edit.py` - Scrape từ trang /edit
  - `create_editorial_py.py` - Convert editorial
  - `smart_generator_creator.py` - Tạo generator (reference)
  - `reupload_all_testcases.py` - Upload workflow (reference)

- **Script mới (cho 3 bài)**:
  - `auto_pipeline_3_bai.py` - Tạo generator + testcases
  - `auto_upload_3_bai.py` - Upload ZIP
  - `auto_submit_3_bai.py` - Submit editorial

- **Login TICA OJ**:
  - URL: https://oj.tica.edu.vn/accounts/login/
  - Username: thinhdt
  - Password: Th09051989@

---

## 🎯 KẾT QUẢ MONG MUỐN

Sau khi chạy xong pipeline:

1. ✅ 3 bài có đầy đủ testcases (22 files mỗi bài = 10 input + 10 output)
2. ✅ Không còn lỗi "Missing input files" trên test_data page
3. ✅ 3 editorial đã được submit thành công
4. ✅ Có submission ID cho cả 3 bài

---

**Cập nhật lần cuối**: 23/05/2026  
**Trạng thái**: Đã tạo xong 3 script tự động, chưa chạy
