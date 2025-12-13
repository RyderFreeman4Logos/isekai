import os
import sys
import subprocess

def replace_text_in_file(filepath, old_text, new_text):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_text in content:
            new_content = content.replace(old_text, new_text)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated content in: {filepath}")
            return True
    except Exception as e:
        print(f"Error reading/writing {filepath}: {e}")
    return False

def rename_file_git(old_path, new_path):
    try:
        subprocess.run(["git", "mv", old_path, new_path], check=True)
        print(f"Renamed file: {old_path} -> {new_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error renaming file {old_path}: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 rename_object.py <old_name> <new_name>")
        sys.exit(1)

    old_name = sys.argv[1]
    new_name = sys.argv[2]
    
    print(f"Renaming '{old_name}' to '{new_name}'...")

    # 1. Replace text in chapters/ and docs/
    target_dirs = ["chapters", "docs"]
    for d in target_dirs:
        if not os.path.exists(d):
            continue
        for root, dirs, files in os.walk(d):
            for file in files:
                if file.endswith(".md") or file.endswith(".txt"):
                    filepath = os.path.join(root, file)
                    replace_text_in_file(filepath, old_name, new_name)

    # 2. Rename file in docs/names/ if exists
    names_dir = "docs/names"
    if os.path.exists(names_dir):
        for root, dirs, files in os.walk(names_dir):
            for file in files:
                if file == f"{old_name}.md":
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(root, f"{new_name}.md")
                    rename_file_git(old_path, new_path)

if __name__ == "__main__":
    main()
