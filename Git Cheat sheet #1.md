### 📘 GIT BASIC COMMANDS — CHEAT SHEET

## 🔹 git init
🧠 What it does
Initializes a new Git repository in your folder.
```
git init
```
---

## 🔹 git status
🧠 What it does
**Shows current state of your repo:**
- changed files
- staged files
- untracked files

```
git status
```
# 🔁 Variations
```
git status -s   # short version (compact output)
```

----

## 🔹 git log
🧠 What it does
Shows commit history
```
git log
```
# 🔁 Variations
```
git log --oneline           # compact view
git log --graph             # visual branch graph
git log --oneline --graph   # best combo
git log -p                  # show changes in commits
```

---

## 🔹 git add
🧠 What it does
Moves changes from working directory → staging area

Common Usage
```
git add file.py        # add specific file
git add .              # add all files
git add *.py           # add all python files
```

# 🔁 Variations
```
git add -A   # add all changes (including deletions)
git add -u   # add only modified/deleted files (not new ones)
```

---

## 🔹 git commit
🧠 What it does
Saves staged changes into repository history

# Common Usage
```
git commit -m "your message"
```

# 🔁 Variations
```
git commit -am "message"
```
add + commit in one step (only for tracked files)
```
git commit --amend
```
edit last commit
```
git commit --amend -m "new message"
```
change last commit message

---

