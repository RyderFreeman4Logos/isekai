build:
    python3 scripts/build_novel.py

txt-gen msg="Update novel build": build
    git add .
    git commit -m "{{msg}}"

rename old new:
    python3 scripts/rename_object.py {{old}} {{new}}
