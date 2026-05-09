# 📘 GIT BRANCHING


## 🔹 git branch
🧠 What it does
Manages branches (create, list, delete)

**Common Usage**
```
git branch
```

👉 Lists all local branches

👉 * shows current branch

### 🔁 Variations
```
git branch feature-1      # create new branch
git branch -d feature-1   # delete branch (safe)
git branch -D feature-1   # force delete
```
---


## 🔹 git checkout
🧠 What it does
Switch between branches or commits

**Common Usage**
```
git checkout main
git checkout feature-1
```

### 🔁 Variations
```
git checkout -b feature-1           # create + switch branch
git checkout <commit-hash>          # go to specific commit (detached HEAD)

```

---

## 🔹 git switch (modern alternative)
🧠 What it does
Cleaner version of checkout for branches

**Common Usage**
```
git switch main
git switch -c feature-1
```

---


## 🔹 git merge
🧠 What it does
Combines another branch into current branch

**Common Usage**
```
git checkout main
git merge feature-1
```

### 🔁 Variations
```
git merge --no-ff feature-1         # always create merge commit
```

---

## 🔹 git branch -r
🧠 What it does
Shows remote branches
```
git branch -r
```

---


## 🔹 git branch -a
🧠 What it does
Shows all branches (local + remote)
```
git branch -a
```

---


## 🔹 git push (branch)
🧠 What it does
Push specific branch to GitHub
```
git push -u origin feature-1
```

---


## 🔹 git branch -m
🧠 What it does
Rename branch
```
git branch -m old-name new-name
```

---


**🧠 Branch Workflow (Very Important)**
main → stable code

feature-x → new feature

merge → bring into main

delete → clean up
