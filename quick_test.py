"""
Quick test script - Chạy thử với 1 bài toán
"""

from scrape_tica import scrape_all_problems, TICA_USERNAME

if __name__ == "__main__":
    print("🧪 QUICK TEST - Chỉ lấy 1 bài để kiểm tra")
    print("="*60)
    
    if TICA_USERNAME == "your_username":
        print("❌ Vui lòng cập nhật username/password trong scrape_tica.py trước!")
        print("   Mở file scrape_tica.py, sửa dòng 13-14")
        exit(1)
    
    # Sửa PROBLEM_URLS trong scrape_tica.py để test với 1 bài cụ thể
    print("\n⚠️  Lưu ý: Thêm 1 URL vào PROBLEM_URLS trong scrape_tica.py")
    print("   Ví dụ: PROBLEM_URLS = ['https://oj.tica.edu.vn/problems/ABC123']")
    print("\nNhấn Enter để tiếp tục hoặc Ctrl+C để hủy...")
    input()
    
    scrape_all_problems()
