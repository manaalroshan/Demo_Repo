# 📘 GIT RESET & REVERT

## 🔹 git reset
🧠 What it does

Moves your project back to a previous commit (can also affect staging & files depending on type)

### 🔥 Types of Reset

#### 🟢 1. Soft Reset
```
git reset --soft <commit-hash>
```
🧠 What it does

Moves HEAD back

Keeps changes staged

🧩 Use case

👉 Rewrite commits / regroup changes

---

## 🟡 2. Mixed Reset (default)
```
git reset <commit-hash>
```
`same as: git reset --mixed`

🧠 What it does

Moves HEAD back

Keeps changes in files

Unstages changes

🧩 Use case

👉 Redo staging cleanly

---

## 🔴 3. Hard Reset
```
git reset --hard <commit-hash>
```

🧠 What it does

Moves HEAD back

Deletes changes from:

staging

working directory

⚠️ Warning

👉 Data loss if not careful

---

## 🔹 Reset File (Unstage)
```
git reset HEAD <file>
```

🧠 What it does

Removes file from staging area

🧠 Reset Summary

soft   → keep staged

mixed  → unstage changes

hard   → delete everything after commit

---

## 🔹 git revert

🧠 What it does

Creates a new commit that undoes a previous commit

**⚙️ Usage**
```
git revert <commit-hash>
```
🧠 What happens

Old commit stays

New commit added

History remains safe

---

## ⚠️ When to Use What

**🟢 Use RESET when:**
- working locally
- fixing your own commits
- cleaning history


**🟢 Use REVERT when:**
- code already pushed
- working in team
- want safe undo

---

## 🔹 Force Push (Important with reset)
```
git push --force
```

🧠 What it does

Overwrites remote history

**⚠️ Use only when:**
* you understand reset
* working solo

---

**🧠 Useful Recovery Command**
## 🔹 git reflog
```
git reflog
```

🧠 What it does

Shows previous HEAD states (even after reset)

👉 Can recover “lost” commits

---
