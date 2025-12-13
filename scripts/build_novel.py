import os
import re

CHAPTERS_DIR = "chapters"
EXPORT_TXT_DIR = "export/txt"
FULL_NOVEL_PATH = "full_novel.txt"

def main():
    # Ensure export directory exists
    os.makedirs(EXPORT_TXT_DIR, exist_ok=True)
    
    files = sorted(os.listdir(CHAPTERS_DIR))
    full_content = []
    
    # Regex to match filename pattern: {n:08}_第{n}章 {章节名}.md
    # Example: 00000001_第1章 这个物质资源有限的世界实际上是个地狱.md
    pattern = re.compile(r"^(\d+)_第(\d+)章\s+(.+)\.md$")
    
    for filename in files:
        if not filename.endswith(".md"):
            continue
            
        match = pattern.match(filename)
        if not match:
            print(f"Skipping non-conforming file: {filename}")
            continue
            
        # raw_n_str is like '00000001', n_str is '1'
        raw_n_str, n_str, title = match.groups()
        
        input_path = os.path.join(CHAPTERS_DIR, filename)
        
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            
        # Format header
        header = f"第{n_str}章 {title}"
        formatted_content = f"{header}\n\n{content}"
        
        # Write individual TXT
        # Naming convention: same as md but .txt suffix
        txt_filename = filename.replace(".md", ".txt")
        output_path = os.path.join(EXPORT_TXT_DIR, txt_filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(formatted_content)
            
        print(f"Processed: {filename} -> {output_path}")
        
        full_content.append(formatted_content)

    # Write full novel
    with open(FULL_NOVEL_PATH, "w", encoding="utf-8") as f:
        # Join chapters with 4 empty lines (which means 5 newlines total between text blocks)
        # "章与章之间空4行" usually means 4 blank lines.
        f.write("\n\n\n\n\n".join(full_content))
        
    print(f"Generated full novel at: {FULL_NOVEL_PATH}")

if __name__ == "__main__":
    main()
