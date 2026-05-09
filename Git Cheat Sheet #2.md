# 📘 GIT REMOTE (PUSH / PULL / FETCH)

## 🔹 git remote
🧠 What it does
Manages connections to remote repos (like GitHub).

**Common Usage**
```
git remote add origin <repo-url>
```
👉 Connect your local repo to GitHub

### 🔁 Variations
```
git remote -v        # show connected remotes
git remote remove origin
git remote rename origin upstream
```

---

## 🔹 git push
🧠 What it does
Uploads your commits to remote (GitHub)

**Common Usage**
```
git push origin main
```

### 🔁 Variations
```
git push -u origin main               # sets upstream (so future push = just git push)
git push                              # works after upstream is set
git push --force                      # overwrite remote history (⚠️ dangerous)
git push origin feature-branch        # push specific branch
```

---

## 🔹 git pull
🧠 What it does
Fetch + merge changes from remote into your current branch

**Common Usage**
```
git pull origin main
```

### 🔁 Variations
```
git pull                  # works if upstream is set
git pull --rebase         # fetch + rebase instead of merge (cleaner history)
```

---

## 🔹 git fetch
🧠 What it does
Downloads changes from remote WITHOUT merging

**Common Usage**
```
git fetch
```
### 🔁 Variations
```
git fetch origin
git fetch --all
git fetch --prune         # removes deleted remote branches locally
```

---

## Key Difference
- push  → send your changes to GitHub
- pull  → get + merge changes
- fetch → get changes only (no merge)

---
