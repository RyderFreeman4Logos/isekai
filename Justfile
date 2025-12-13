build:
    python3 scripts/build_novel.py

commit msg="Update novel build": build
    git add .
    git commit -m "{{msg}}"
