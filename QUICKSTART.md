# QUICK START - Download đề bài về trước, testcase tính sau

## 🚀 Bước 1: Download tất cả đề bài về (quan trọng nhất!)

```bash
# Cài đặt (chỉ 1 lần)
setup.bat

# Cấu hình - Mở scrape_tica.py, sửa:
TICA_USERNAME = "thinhdt"          # Username của bạn
TICA_PASSWORD = "Th09051989@"      # Password của bạn  
MAX_PROBLEMS = 3                   # Test với 3 bài trước, sau đó đổi thành None để lấy hết

# Chạy download
py scrape_tica.py

# Đợi 5-10 phút, script sẽ:
# ✅ Đăng nhập TICA OJ
# ✅ Lấy danh sách bài (chỉ bài chưa solved)
# ✅ Vào trang /edit của mỗi bài
# ✅ Download Problem Body + Editorial (nếu có)
# ✅ Lưu vào thư mục riêng: problems/{problem_id}/
```

## 📁 Kết quả sau khi download

```
problems/
├── tica_dayso32/
│   ├── problem.md        # Đề bài đầy đủ
│   ├── editorial.txt     # Code đáp án (nếu có)
│   └── info.json         # Metadata (title, url, constraints...)
├── qninh_bdxau/
│   ├── problem.md
│   ├── editorial.txt
│   └── info.json
└── sokhao_tongdayso4/
    ├── problem.md
    └── info.json         # Bài này không có editorial
```

## 🎯 Bước 2: Tạo testcase (sau khi có đề)

**Cách 1: Tự động (cho bài có editorial Python)**
```bash
py auto_testcase.py

# Script sẽ:
# - Đọc problems/ và tica_problems.json
# - Chỉ generate cho bài có editorial Python
# - Tạo 11 testcase/bài
# - Output: daura_{problem_id}/ với input/output
```

**Cách 2: Thủ công (cho bài quan trọng/phức tạp)**
```bash
# Đọc đề từ problems/{problem_id}/problem.md
# Viết code trong taotestcase.py
# Chạy để tạo testcase chất lượng cao
```

**Cách 3: Dùng AI (recommend!)**
- Nói với AI: "Phân tích bài tica_dayso32 và tạo testcase thông minh"
- AI sẽ đọc đề + editorial, hiểu logic, tạo edge cases

## ⚡ TL;DR - Nếu vội

```bash
setup.bat                  # Cài đặt
# Sửa username/password trong scrape_tica.py
py scrape_tica.py         # Download hết về (2-3 giờ cho 500 bài)
# => Có folder problems/ với đầy đủ đề bài
# => Testcase tính sau, không vội!
```

## ⚠️ Lưu ý

1. **Editorial Python:** Chỉ auto được bài có editorial Python. Bài C++/Java cần xử lý thủ công.

2. **Kiểm tra kết quả:** Một số bài sinh testcase có thể sai format. Cần review thủ công.

3. **Network:** Cần internet ổn định. Nếu bị disconnect, chạy lại là được (script sẽ tiếp tục từ bài chưa lấy).

## 📚 Chi tiết hơn

Xem file `README_TOOL.md` để biết thêm chi tiết và troubleshooting.

## 🆘 Gặp lỗi?

1. **Không login được:** Kiểm tra username/password
2. **Filter không hoạt động:** Chạy `py explore_tica_page.py` để xem
3. **Testcase sai format:** Xem `auto_testcase.py` để adjust logic
4. **Lỗi khác:** Mở issue hoặc xem README_TOOL.md

---

**Made with ❤️ for TICA OJ contestants**
