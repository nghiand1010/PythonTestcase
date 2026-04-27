# TICA OJ Testcase Generator - Hướng dẫn sử dụng

Tool tự động đọc bài toán từ TICA OJ và tạo testcase **TỰ ĐỘNG** (bao gồm cả output).

## ✨ Tính năng mới

- ✅ Vào trang **/edit** để lấy Editorial (code đáp án)
- ✅ Tự động phân tích constraints và sinh input
- ✅ Chạy editorial code để tạo output tự động
- ✅ Không cần viết code thủ công cho mỗi bài!

## 📋 Yêu cầu

```bash
pip install playwright beautifulsoup4
playwright install chromium
```

## 🚀 Cách sử dụng

### Bước 1: Cấu hình

Mở file `scrape_tica.py` và thay đổi:

```python
TICA_USERNAME = "username_cua_ban"
TICA_PASSWORD = "password_cua_ban"

# Filters
HIDE_SOLVED_PROBLEMS = True  # True = chỉ lấy bài chưa solved
MAX_PROBLEMS = None  # None = tất cả, hoặc số cụ thể (VD: 50)
```

### Bước 1.5: Khám phá cấu trúc trang (Optional nhưng khuyến nghị)

**Nếu lần đầu chạy hoặc filter không hoạt động:**

```bash
py explore_tica_page.py
```

Script này sẽ:
- Mở trang problems với browser thật
- Hiển thị tất cả checkboxes, dropdowns, filters
- Chụp screenshot lưu thành `tica_problems_page.png`
- Giúp bạn xác định chính xác selector của "Hide solved problems"

Sau khi chạy, xem output và screenshot, rồi cập nhật `scrape_tica.py` nếu cần.

### Bước 2: Scrape bài toán

Có 2 cách:

**Cách 1: Lấy danh sách tự động (test 10 bài đầu)**
```bash
py scrape_tica.py
```

**Cách 2: Chỉ định bài toán cụ thể**

Sửa file `scrape_tica.py`, thêm URLs:
```python
PROBLEM_URLS = [
    "https://oj.tica.edu.vn/problems/PROB1",
    "https://oj.tica.edu.vn/problems/PROB2",
    # ... thêm các URL khác
]
```

Sau đó chạy:
```bash
py scrape_tica.py
```

### Bước 3: Xem kết quả

File `tica_problems.json` sẽ chứa thông tin tất cả bài toán:
- Tên bài
- Problem body (đề bài đầy đủ)
- **Editorial content (code đáp án!)**
- Input format và constraints
- URL gốc + edit URL

### Bước 4: Tự động tạo testcase cho TẤT CẢ bài

**⚡ MAGIC HAPPENS HERE:**

```bash
py auto_testcase.py
```

Script sẽ:
1. Đọc `tica_problems.json`
2. Với mỗi bài có editorial Python:
   - Phân tích constraints
   - Tự động sinh 11 test cases (input)
   - Chạy editorial code để lấy output
   - Tạo thư mục `daura_{problem_id}` và file zip
3. Bỏ qua các bài không có editorial hoặc editorial không phải Python

**🎉 Kết quả:** Mỗi bài có sẵn 11 cặp input/output!

### Bước 5: Xử lý các bài còn lại (Optional)

Các bài không có editorial Python hoặc sinh testcase không đúng:
1. Xem `tica_problems.json` để tìm bài đó
2. Copy constraints vào `taotestcase.py`
3. Viết logic thủ công như trước

## 📊 Workflow tối ưu

### Cho 500 bài toán:

**Phương pháp MỚI (với auto_testcase.py):**

```bash
# Lần đầu (chỉ 1 lần):
1. setup.bat
2. Sửa username/password
3. py scrape_tica.py          # ~2-3 giờ để lấy 500 bài
4. py auto_testcase.py         # ~1-2 giờ để gen tất cả

# => Xong! Phần lớn bài đã có testcase tự động
```

**Xử lý manual (nếu cần):**
- Chỉ những bài editorial không phải Python
- Hoặc bài sinh testcase không chuẩn
- Ước tính: ~50-100 bài cần sửa thủ công

**Tổng thời gian:**
- Setup + scrape + auto: ~5-6 giờ
- Manual cho bài còn lại: ~5-10 giờ
- **TỔNG: ~10-15 giờ cho 500 bài**

**So sánh với làm tay:**
- Làm tay: 500 × 7 phút = ~58 giờ
- **Tiết kiệm: 75-80%!** 🚀

## 🎯 Tips

1. **Test nhỏ trước:** 
   - Lần đầu set `MAX_PROBLEMS = 5` trong `scrape_tica.py`
   - Chạy xem kết quả OK không
   - Sau đó mới scrape hết 500 bài

2. **Batch processing:** 
   - Chia 500 bài thành nhiều lần (mỗi lần 50-100 bài)
   - Set `MAX_PROBLEMS = 100` và chạy nhiều lần

3. **Kiểm tra editorial:**
   - Sau khi scrape, mở `tica_problems.json`
   - Tìm bài có `editorial_content` dài (>100 ký tự)
   - Những bài này có thể auto generate được

4. **Python editorial:**
   - `auto_testcase.py` chỉ chạy được với editorial Python
   - Editorial C++/Java cần convert sang Python hoặc xử lý thủ công

5. **Backup:** 
   - Lưu file `tica_problems.json` để không phải scrape lại
   - File này chứa toàn bộ thông tin cần thiết

6. **Headless mode:** 
   - Sau khi test OK, sửa `headless=True` trong `scrape_tica.py`
   - Chạy nhanh hơn và ít tốn tài nguyên

7. **Review testcases:**
   - `auto_testcase.py` sinh testcase tự động nhưng có thể không hoàn hảo
   - Nên kiểm tra vài bài đầu tiên
   - Nếu sai format, cần adjust logic trong `generate_smart_testcase()`

## 🔧 Troubleshooting

**Lỗi đăng nhập:**
- Kiểm tra username/password
- Thử đăng nhập thủ công trên browser trước

**Filter "Hide solved" không hoạt động:**
1. Chạy `py explore_tica_page.py` để xem cấu trúc trang
2. Xem output và file `tica_problems_page.png`
3. Tìm selector chính xác của checkbox/toggle
4. Cập nhật hàm `apply_filters()` trong `scrape_tica.py`
5. Hoặc tạm thời set `HIDE_SOLVED_PROBLEMS = False` và lọc thủ công sau

**Lỗi timeout:**
- Tăng `time.sleep()` trong code
- Giảm số lượng bài mỗi lần chạy (set `MAX_PROBLEMS = 50`)

**Parse sai constraints:**
- Xem lại `tica_problems.json`
- Sửa thủ công trong `taotestcase.py`

## 📝 Ví dụ

Sau khi scrape, bạn sẽ có trong `tica_problems.json`:

```json
{
  "id": "thttd_ds",
  "title": "Tổng mảng con",
  "edit_url": "https://oj.tica.edu.vn/problem/thttd_ds/edit",
  "problem_body": "Cho mảng A gồm n số nguyên...\n\nInput:\nDòng 1: n và S (2 ≤ n ≤ 10^5, S ≤ 10^6)\nDòng 2: n số nguyên a1, a2, ..., an (1 ≤ ai ≤ 10^6)",
  "editorial_content": "```python\nn, S = map(int, input().split())\na = list(map(int, input().split()))\n...\nprint(ans)\n```",
  "constraints": ["2 ≤ n ≤ 100000", "S ≤ 1000000", "1 ≤ ai ≤ 1000000"]
}
```

Sau khi chạy `auto_testcase.py`:

```
daura_thttd_ds/
  ├── input1.in    (n=2, S=random, mảng nhỏ)
  ├── output1.out  (từ editorial)
  ├── input2.in    (n=10000, S=random)
  ├── output2.out
  ...
  ├── input11.in
  └── output11.out

daura_thttd_ds.zip (sẵn sàng nộp!)
```

**🎉 Không cần viết code gì cả!**
