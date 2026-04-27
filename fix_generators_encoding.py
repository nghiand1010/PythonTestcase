# -*- coding: utf-8 -*-
"""Fix encoding in all generators"""
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.absolute()
PROBLEMS_DIR = SCRIPT_DIR / "problems"

# Map all emojis to ASCII
EMOJI_MAP = {
    '✅': '[OK]',
    '❌': '[FAIL]',
    '📦': '[ZIP]',
    '🎯': '[TARGET]',
    '⚠️': '[WARN]',
    '💡': '[INFO]',
    '📝': '[NOTE]',
    '🔍': '[SEARCH]',
    '✓': '[OK]',
    '✗': '[FAIL]',
}

fixed = 0
for gen_file in PROBLEMS_DIR.glob("*/generator.py"):
    content = gen_file.read_text(encoding='utf-8')
    original = content
    
    for emoji, ascii_text in EMOJI_MAP.items():
        if emoji in content:
            content = content.replace(emoji, ascii_text)
    
    if content != original:
        gen_file.write_text(content, encoding='utf-8')
        print(f"Fixed: {gen_file.parent.name}")
        fixed += 1

print(f"\nFixed {fixed} files")
