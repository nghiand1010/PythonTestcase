"""
Script để tự động tạo testcase từ thông tin đã scrape
Đọc file tica_problems.json và tự động tạo test cases
"""

import json
import re
import random
from typing import Dict, List, Tuple

def parse_constraint(constraint_text: str) -> Dict:
    """
    Phân tích constraint để lấy min, max
    VD: "1 ≤ N ≤ 15" -> {'var': 'N', 'min': 1, 'max': 15}
    """
    # Xử lý 10^5 -> 100000
    constraint_text = re.sub(r'10\^(\d+)', lambda m: str(10**int(m.group(1))), constraint_text)
    
    # Pattern: min ≤ var ≤ max
    match = re.search(r'(\d+)\s*[≤<=]+\s*([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', constraint_text)
    if match:
        return {
            'var': match.group(2),
            'min': int(match.group(1)),
            'max': int(match.group(3))
        }
    
    # Pattern: var ≤ max
    match = re.search(r'([a-zA-Z_]\w*)\s*[≤<=]+\s*(\d+)', constraint_text)
    if match:
        return {
            'var': match.group(1),
            'min': 1,
            'max': int(match.group(2))
        }
    
    return None

def detect_input_structure(input_format: str) -> List[str]:
    """
    Phân tích cấu trúc input
    Trả về: ['n S', 'array n']
    """
    lines = []
    
    # Tìm các pattern thường gặp
    if re.search(r'dòng.*?đầu.*?(hai|2).*?số', input_format, re.IGNORECASE):
        # Dòng đầu có 2 số
        vars_match = re.findall(r'\b([a-zA-Z_]\w*)\b', input_format)
        if len(vars_match) >= 2:
            lines.append(f"{vars_match[0]} {vars_match[1]}")
    
    if re.search(r'dòng.*?(thứ hai|tiếp theo).*?(\w+)\s+số', input_format, re.IGNORECASE):
        # Dòng thứ 2 có n số
        lines.append("array n")
    
    return lines

def generate_testcase_code(problem: Dict) -> str:
    """Tạo code Python để generate testcase cho bài toán"""
    
    problem_id = problem['id']
    constraints = problem.get('constraints', [])
    
    # Parse constraints
    parsed_constraints = {}
    for c in constraints:
        parsed = parse_constraint(c)
        if parsed:
            parsed_constraints[parsed['var']] = parsed
    
    # Phát hiện cấu trúc
    input_structure = detect_input_structure(problem['input_format'])
    
    # Template code
    code = f'''
# Testcase cho bài: {problem['title']}
# ID: {problem_id}
# URL: {problem['url']}

# Constraints:
{chr(10).join(f"# {c}" for c in constraints)}

for i in range(1, 12):
    if i == 1:
        # Test case 1: Giá trị nhỏ nhất
'''
    
    # Generate test cases based on structure
    if parsed_constraints:
        main_var = list(parsed_constraints.keys())[0]
        constraint = parsed_constraints[main_var]
        
        code += f'''        {main_var} = {constraint['min']}
'''
        
        code += f'''    elif i == 2:
        # Test case 2: Giá trị lớn nhất (giảm xuống nếu quá lớn)
        {main_var} = min({constraint['max']}, 10000)  # Giới hạn để tránh timeout
'''
        
        code += f'''    else:
        # Test case ngẫu nhiên
        {main_var} = tao_so_ngau_nhien({constraint['min']}, min({constraint['max']}, 10000))
'''
    
    code += '''
    # TODO: Tạo input_value dựa trên cấu trúc đầu vào
    # input_value = f"{n} {S}\\n"
    # input_value += " ".join(map(str, array)) + "\\n"
    
    with open(f'{filename}/input{i}.in', "w", encoding="utf-8") as f:
        f.write(input_value)
    
    out_put = run_algo(input_value, 'algo.py')
    
    with open(f'{filename}/output{i}.out', 'w', encoding="utf-8") as f:
        f.write(out_put.rstrip('\\n'))
'''
    
    return code

def generate_all_testcases(json_file: str = "tica_problems.json"):
    """Tạo code testcase cho tất cả bài toán"""
    
    with open(json_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    print(f"Đọc được {len(problems)} bài toán")
    
    # Tạo file cho từng bài
    for problem in problems:
        problem_id = problem['id']
        
        # Tạo code
        code = generate_testcase_code(problem)
        
        # Lưu vào file
        filename = f"testcase_{problem_id}.py"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(code)
        
        print(f"✅ Đã tạo {filename}")
    
    print(f"\n{'='*60}")
    print(f"✅ Hoàn thành! Đã tạo {len(problems)} file testcase")
    print(f"⚠️  Lưu ý: Bạn cần xem lại và điều chỉnh các file này")
    print(f"   vì cấu trúc input của mỗi bài có thể khác nhau")

if __name__ == "__main__":
    print("🚀 TICA Testcase Generator")
    print("="*60)
    
    try:
        generate_all_testcases()
    except FileNotFoundError:
        print("❌ Không tìm thấy file tica_problems.json")
        print("   Vui lòng chạy scrape_tica.py trước!")
