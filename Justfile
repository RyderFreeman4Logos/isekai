commit-all comment:
    git add -A
    git commit -m {{comment}}

txt-gen:
    python3 scripts/build_novel.py
    commit-all "build txt"

rename old new:
    python3 scripts/rename_object.py {{old}} {{new}}
