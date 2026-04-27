@echo off
echo ========================================
echo TICA OJ Testcase Tool - Cai dat
echo ========================================
echo.

echo Buoc 1: Cai dat Python packages...
pip install -r requirements.txt

echo.
echo Buoc 2: Cai dat Playwright browsers...
playwright install chromium

echo.
echo ========================================
echo Da cai dat xong!
echo ========================================
echo.
echo Buoc tiep theo:
echo 1. Mo file scrape_tica.py
echo 2. Thay doi TICA_USERNAME va TICA_PASSWORD
echo 3. Chay: py scrape_tica.py
echo.
pause
