# 🚀 TICA OJ Testcase Automation Pipeline

Hướng dẫn đầy đủ từ A-Z để tự động tạo và upload testcases cho TICA OJ.

---

## 📋 Mục Lục

1. [Yêu Cầu Hệ Thống](#yêu-cầu-hệ-thống)
2. [Bước 1: Tìm Bài Cần Làm](#bước-1-tìm-bài-cần-làm)
3. [Bước 2: Tạo Editorial Python](#bước-2-tạo-editorial-python)
4. [Bước 3: Tạo Generator Testcase](#bước-3-tạo-generator-testcase)
5. [Bước 4: Upload Testcases](#bước-4-upload-testcases)
6. [Bước 5: Submit Solutions](#bước-5-submit-solutions)
7. [Xử Lý Lỗi](#xử-lý-lỗi)
8. [Các Lệnh Hữu Ích](#các-lệnh-hữu-ích)

---

## 🔧 Yêu Cầu Hệ Thống

### Cài Đặt
```bash
# Python 3.14+
py -m venv .venv
.venv\Scripts\activate

# Cài đặt thư viện
pip install -r requirements.txt

# Cài đặt Playwright browser
py -m playwright install chromium
```

### Thông Tin Đăng Nhập
- **URL**: https://oj.tica.edu.vn/
- **Username**: thinhdt
- **Password**: Th09051989@
- **Login URL**: https://oj.tica.edu.vn/accounts/login/

---

## 🔍 Bước 1: Tìm Bài Cần Làm

### Mục Tiêu
Tìm các bài có **Python editorial** nhưng **chưa có testcases** trên server.

### Lệnh
```bash
py scrape_missing_testcases.py
```

### Kết Quả
- **Thư mục đầu ra**: `problems/`
- **Cấu trúc mỗi bài**:
  ```
  problems/
    <problem_id>/
      problem.json       # Metadata
      statement.md       # Đề bài
      editorial.txt      # Editorial gốc
  ```

### Script Hoạt Động Như Thế Nào?
1. **Login** vào TICA OJ
2. **Duyệt tất cả pages** của problem list
3. **Với mỗi bài**:
   - Kiểm tra có Python editorial không (tab "Editorial Python")
   - Kiểm tra có testcases trên server không (vào test_data page, đếm số testcase)
   - **Chỉ download** những bài có editorial nhưng KHÔNG có testcase
4. **Lưu thông tin** vào `tica_problems.json`

### Output Mẫu
```
============================================================
📊 TỔNG KẾT
============================================================
✅ Tổng số problems: 290
✅ Có testcases: 178
❌ Không có testcases: 112
📋 Có Python editorial: 23

✅ Đã scrape: 23 bài
```

---

## 📝 Bước 2: Tạo Editorial Python

### Mục Tiêu
Chuyển đổi `editorial.txt` (dạng text) sang `editorial.py` (executable Python code).

### Lệnh
```bash
py create_editorial_py.py
```

### Kết Quả
- Tạo file `editorial.py` trong mỗi thư mục `problems/<problem_id>/`
- Format: sử dụng `input()` và `print()` (KHÔNG dùng file I/O)

### Ví Dụ
```python
# editorial.py
n = int(input())
result = n * 2
print(result)
```

### Lưu Ý
- Editorial phải chạy được standalone
- Đúng thuật toán trong đề bài
- Output phải khớp format đề bài

---

## ⚙️ Bước 3: Tạo Generator Testcase

### Mục Tiêu
Tạo 11 testcases (10 sẽ upload, 1 để test) với phân bố thông minh.

### Lệnh
```bash
py smart_generator_creator.py
```

### Testcase Distribution
- **Test 1-3**: Small cases (n=1, 2, 10)
- **Test 4-7**: Medium cases (100 - 10,000)
- **Test 8-10**: Large cases (50,000 - 200,000)
- **Test 11**: Stress test (sẽ xóa sau khi upload)

### Kết Quả
Tạo file `generator.py` trong mỗi thư mục với cấu trúc:
```python
def generate_test(test_num):
    """Generate input for test case"""
    if test_num == 1:
        return "1\n"
    elif test_num == 2:
        return "2\n"
    # ...
    
def run_editorial(input_data):
    """Run editorial code and return output"""
    # Import và chạy editorial.py
    # ...
```

### AI Pattern Detection
Script tự động phát hiện pattern input:
1. **Single number**: `n`
2. **Two numbers**: `n m`
3. **Array**: `n` → `a1 a2 ... an`
4. **Matrix**: `n m` → `a11 a12 ... anm`
5. **String input**
6. **Multiple queries**

---

## 📤 Bước 4: Upload Testcases

### 4.1. Upload Lần Đầu (Bài Chưa Có Testcase)

#### Lệnh
```bash
py upload_testcases.py <problem1> <problem2> ...
```

#### Ví Dụ
```bash
py upload_testcases.py dem_chia3 dongho_bthuc quacau
```

#### Script Hoạt Động
1. **Login** TICA OJ
2. **Với mỗi bài**:
   - Chạy `generator.py` → tạo input/output cho 11 tests
   - Tạo file ZIP: `<problem_id>_testcases.zip`
   - Mở page `/problem/<problem_id>/test_data`
   - **Chọn ZIP file**: locator `input#id_problem-data-zipfile`
   - **Nhấn Apply!**: locator `input[type="submit"][value="Apply!"]`
   - Đợi 5s để server xử lý
3. **Xóa test 11**: Check checkbox index 10, nhấn Apply

### 4.2. Upload Đè Lên Testcase Cũ (Bị Lỗi)

#### ⚠️ VẤN ĐỀ: Upload Over Existing Testcases = Corruption!

Nếu upload ZIP khi đã có testcases → lỗi "Failed to open as ZIP file"

#### ✅ GIẢI PHÁP: Delete First, Then Upload

```bash
py reupload_all_testcases.py
```

#### Script Hoạt Động
```python
# Bước 1: Delete tất cả testcases cũ
delete_all_checkbox = page.locator('input#delete-all')
delete_all_checkbox.check()
apply_button = page.locator('input[type="submit"][value="Apply!"]')
apply_button.click()
time.sleep(3)

# Bước 2: Reload và verify đã xóa hết
page.reload()
# Check count = 0

# Bước 3: Upload ZIP mới
file_input = page.locator('input#id_problem-data-zipfile')
file_input.set_input_files(str(zip_file))
apply_button.click()  # Nhấn Apply để xử lý ZIP
time.sleep(5)
```

### 4.3. Xử Lý Trường Hợp Đặc Biệt

#### Trường Hợp: Upload ZIP Rồi Nhưng Quên Nhấn Apply

**Triệu chứng**: Delete không được (vẫn còn testcases cũ)

**Nguyên nhân**: ZIP đã upload nhưng chưa process

**Giải pháp**: Chỉ cần nhấn Apply!

```python
# Không cần delete, không cần upload lại
# Chỉ cần:
apply_button = page.locator('input[type="submit"][value="Apply!"]')
apply_button.click()
```

---

## ✅ Bước 5: Submit Solutions

### Mục Tiêu
Submit file `editorial.py` lên TICA OJ để kiểm tra AC.

### Lệnh
```bash
py auto_submit_all.py <problem1> <problem2> ...
```

### Ví Dụ
```bash
py auto_submit_all.py dem_chia3 dongho_bthuc quacau
```

### Script Hoạt Động
1. **Login** TICA OJ
2. **Với mỗi bài**:
   - Đọc file `problems/<problem_id>/editorial.py`
   - Mở page `/problem/<problem_id>/submit`
   - **Fill code vào Ace Editor**:
     ```javascript
     ace.edit("ace-editor").setValue(code)
     ```
   - **Sync sang textarea**:
     ```javascript
     document.getElementById("id_source").value = code
     ```
   - **Chọn Python 3**: `select#id_language` value="9"
   - **Submit**: `button#submit-button`
3. **Lấy submission ID** từ redirect URL
4. **In danh sách submissions**

### Output Mẫu
```
======================================================================
KẾT QUẢ SUBMIT
======================================================================
✅ Success: 16 bài
❌ Failed: 0 bài

✅ Submission IDs:
  - dem_chia3: https://oj.tica.edu.vn/submission/353929
  - dongho_bthuc: https://oj.tica.edu.vn/submission/353930
  ...
```

---

## 🐛 Xử Lý Lỗi

### 7.1. Kiểm Tra Testcase Có Lỗi Không

#### Lệnh
```bash
py check_testcase_errors.py
```

#### Tìm Lỗi "File Does Not Exist"

```bash
py find_all_testcase_errors.py
```

Script sẽ:
- Duyệt tất cả 1246 problems
- Tìm các bài có lỗi "Input/Output file does not exist"
- Lưu danh sách vào `problems_with_testcase_errors.txt`

#### Các Lỗi Thường Gặp

| Lỗi | Nguyên Nhân | Giải Pháp |
|-----|-------------|-----------|
| `Failed to open as ZIP file` | Upload over existing testcases | Delete trước, sau đó upload |
| `Input file for case X does not exist` | ZIP upload rồi nhưng chưa Apply | Nhấn Apply! button |
| `Testcase count = 0` | Quên nhấn Apply sau khi chọn ZIP | Nhấn Apply! button |
| Delete không được | ZIP đã upload trước đó | Nhấn Apply! để process ZIP trước |

### 7.2. Kiểm Tra Testcase Đã Upload Chưa

```bash
py check_uploaded.py
```

Output:
```
✅ Có testcase: 16/16
❌ Không có: 0/16
```

### 7.3. Re-submit Nếu Bị Lỗi

Nếu submission bị WA/RE/TLE:
1. Kiểm tra `editorial.py` có đúng không
2. Chạy lại generator để test local
3. Fix code và submit lại

---

## 🛠️ Các Lệnh Hữu Ích

### Debug Commands

```bash
# Kiểm tra 1 bài cụ thể
py check_sodep2.py

# Debug delete checkbox
py debug_delete.py

# Xem HTML của test_data page
py debug_undeletable.py
```

### Workflow Hoàn Chỉnh (One-shot)

```bash
# Bước 1: Tìm bài mới
py scrape_missing_testcases.py

# Bước 2: Tạo editorial
py create_editorial_py.py

# Bước 3: Tạo generators
py smart_generator_creator.py

# Bước 4: Upload testcases
py upload_testcases.py <problem_ids...>

# Bước 5: Submit solutions
py auto_submit_all.py <problem_ids...>
```

### Kiểm Tra Sau Khi Upload

```bash
# Kiểm tra testcases đã có chưa
py check_uploaded.py

# Kiểm tra có lỗi không
py check_testcase_errors.py

# Nếu có lỗi: re-upload
py reupload_all_testcases.py
```

---

## 📊 Thống Kê & Kết Quả

### Batch Hiện Tại (May 22-23, 2026)

- **Tổng số bài scrape**: 23 bài
- **Editorial tạo thành công**: 23/23
- **Generator tạo thành công**: 19/23 (4 bài skip)
- **Upload thành công**: 16/19 bài
- **Submit thành công**: 16/16 bài

### Các Bài Đã Hoàn Thành

```
✅ bupbe             ✅ chon_2stong       ✅ cuahang_sohoc
✅ dem_chia3         ✅ dongho_bthuc      ✅ nhonhatchia36
✅ quacau            ✅ tso_chia5         ✅ tuikeo_nguyenkhoa
✅ docsach_books     ✅ docsach_marisa    ✅ matran_xoanoc
✅ table_tennis      ✅ thangmay          ✅ tuoinuoc
✅ matran_xoanoc5
```

### Submission IDs
- #353926 - #353941 (16 submissions)
- Tất cả đều pass testcases

---

## 🎯 Best Practices

### 1. Luôn Check Testcase Trước Khi Submit
```bash
py check_uploaded.py
```

### 2. Delete Trước Khi Re-upload
Không bao giờ upload over existing testcases!

### 3. Nhớ Nhấn Apply!
Sau khi chọn ZIP file, phải nhấn `Apply!` button để process.

### 4. Xóa Test 11
Sau khi upload, xóa test 11 (stress test) để giữ 10 tests.

### 5. Verify Submissions
Vào TICA OJ check verdict: AC/WA/RE/TLE

---

## 🔑 Key Selectors (Quan Trọng!)

### Login
- URL: `https://oj.tica.edu.vn/accounts/login/`
- Username: `input[name="username"]`
- Password: `input[name="password"]`
- Submit: `button[type="submit"]`

### Upload Testcase
- URL: `https://oj.tica.edu.vn/problem/<problem_id>/test_data`
- Delete all: `input#delete-all`
- ZIP input: `input#id_problem-data-zipfile`
- Apply button: `input[type="submit"][value="Apply!"]`
- Delete checkbox (per test): `input[name*="DELETION_DELETE"]` (index 10 for test 11)

### Submit Solution
- URL: `https://oj.tica.edu.vn/problem/<problem_id>/submit`
- Ace editor: `#ace-editor`
- Textarea: `textarea#id_source`
- Language: `select#id_language` (value="9" for Python 3)
- Submit: `button#submit-button`

---

## 📁 Cấu Trúc Thư Mục

```
PythonTestcase/
│
├── problems/                    # Bài đã scrape
│   ├── <problem_id>/
│   │   ├── problem.json
│   │   ├── statement.md
│   │   ├── editorial.txt
│   │   ├── editorial.py         # Tạo bởi create_editorial_py.py
│   │   ├── generator.py         # Tạo bởi smart_generator_creator.py
│   │   └── <problem_id>_testcases.zip
│   │
│   └── ...
│
├── problems_ready_to_upload/    # Backup
│
├── tica_problems.json           # Metadata tất cả problems
│
├── scrape_missing_testcases.py # Bước 1: Tìm bài
├── create_editorial_py.py       # Bước 2: Tạo editorial
├── smart_generator_creator.py   # Bước 3: Tạo generator
├── upload_testcases.py          # Bước 4: Upload
├── auto_submit_all.py           # Bước 5: Submit
│
├── reupload_all_testcases.py    # Fix lỗi upload
├── check_uploaded.py            # Verify uploads
├── check_testcase_errors.py     # Check errors
├── find_all_testcase_errors.py  # Find all errors
│
└── PIPELINE_GUIDE.md            # File này
```

---

## 🚀 Quick Start cho Lần Sau

**Chạy toàn bộ pipeline trong 5 lệnh:**

```bash
# 1. Tìm bài mới (chỉ lấy bài có editorial, chưa có testcase)
py scrape_missing_testcases.py

# 2. Tạo editorial.py từ editorial.txt
py create_editorial_py.py

# 3. Tạo generator.py (AI tự động)
py smart_generator_creator.py

# 4. Upload testcases (thay <problems> bằng danh sách bài)
py upload_testcases.py <problem1> <problem2> <problem3>

# 5. Submit solutions
py auto_submit_all.py <problem1> <problem2> <problem3>
```

**Nếu có lỗi:**
```bash
# Check testcases
py check_uploaded.py

# Re-upload nếu cần
py reupload_all_testcases.py

# Re-submit
py auto_submit_all.py <problems>
```

---

## ✨ Tính Năng Đặc Biệt

### Smart Generator
- **Tự động phát hiện pattern** input từ editorial
- **6+ patterns**: single number, two numbers, array, matrix, string, queries
- **Phân bố thông minh**: edge cases → medium → large → stress
- **Random data**: đảm bảo độ đa dạng

### Smart Scraper
- **Kiểm tra server trước**: chỉ download bài thực sự cần
- **Lưu metadata**: `tica_problems.json` chứa thông tin tất cả bài
- **Tránh duplicate**: không download lại bài đã có

### Auto Upload
- **Tự động xóa test 11**: sau khi upload
- **Error detection**: phát hiện "Failed to open as ZIP file"
- **Retry logic**: delete → verify → upload

### Auto Submit
- **Ace editor sync**: sync code từ Ace sang textarea
- **Track submissions**: lưu submission IDs
- **Batch submit**: submit nhiều bài cùng lúc

---

## 📞 Support & Troubleshooting

### Playwright Issues
```bash
# Re-install browser
py -m playwright install chromium --force
```

### Login Issues
- Check username/password trong script
- Verify login URL: `https://oj.tica.edu.vn/accounts/login/`

### Upload Issues
- Verify selectors (có thể TICA OJ thay đổi)
- Check ZIP file tồn tại
- Đảm bảo nhấn Apply! sau khi chọn ZIP

### Submit Issues
- Check language ID (Python 3 = 9)
- Verify Ace editor selector
- Đảm bảo sync sang textarea

---

## 🎓 Kinh Nghiệm Rút Ra

1. **LUÔN delete trước khi re-upload**: upload over existing = lỗi
2. **Nhớ nhấn Apply!**: sau khi chọn ZIP file
3. **Verify sau mỗi bước**: dùng check scripts
4. **Test local trước**: chạy generator + editorial local
5. **Batch operations**: upload/submit nhiều bài cùng lúc hiệu quả hơn
6. **Smart selectors**: dùng ID thay vì class/tag khi có thể

---

**Chúc may mắn với lần chạy tiếp theo! 🚀**
