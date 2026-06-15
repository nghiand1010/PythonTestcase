#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check sodep2 cụ thể
"""

from playwright.sync_api import sync_playwright
import time

USERNAME = "thinhdt"
PASSWORD = "Th09051989@"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Login
    print("🔐 Đăng nhập...")
    page.goto("https://oj.tica.edu.vn/accounts/login/")
    page.fill('input[name="username"]', USERNAME)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"]')
    page.wait_for_load_state("networkidle")
    print("✅ Đã đăng nhập\n")
    
    # Check sodep2
    print("🔍 Kiểm tra sodep2...")
    page.goto("https://oj.tica.edu.vn/problem/sodep2/test_data")
    time.sleep(2)
    
    html = page.content()
    
    # Lưu HTML để xem
    with open("debug_sodep2.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("✅ Đã lưu HTML: debug_sodep2.html")
    
    # Tìm lỗi
    if "does not exist" in html:
        print("\n❌ Có lỗi:")
        import re
        errors = re.findall(r'(Input|Output) file for case \d+ does not exist: ([\w\.]+)', html)
        for err in errors:
            print(f"   - {err[0]} file missing: {err[1]}")
    else:
        print("\n✅ Không có lỗi 'does not exist'")
    
    print("\n⏸️  Đợi 5s để xem trang...")
    time.sleep(5)
    
    browser.close()
