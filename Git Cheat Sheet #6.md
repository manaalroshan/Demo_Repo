# 📘 GIT REBASE & SQUASH

## 🔹 git rebase
🧠 What it does

Reapplies your commits on top of another base

→ creates a clean, linear history

**⚙️ Common Usage**
```
git rebase main
```

👉 Moves your current branch commits on top of main

🧩 Example
Before:

main:      A──B

feature:       └──C──D

After rebase:

main:      A──B──C'──D'

👉 New commits (C', D') are recreated


### 🔁 Variations
```
git rebase -i HEAD~3
# interactive rebase (edit commits)
```

```
git rebase --continue
# after resolving conflict
```

```
git rebase --abort
# cancel rebase
```

⚠️ Important
- Rebase rewrites history
- Don’t use on shared branches (unless you know what you're doing)

---

## 🔹 Interactive Rebase (-i)
🧠 What it does

Lets you:
* rename commits
* reorder commits
* squash commits

**⚙️ Usage**
```
git rebase -i HEAD~3
```

**🧩 What you see**
```
pick a1b2c3 commit 1
pick d4e5f6 commit 2
pick g7h8i9 commit 3
```

## 🔹 Options in Interactive Rebase
**✏️ reword (r)**
```
reword a1b2c3 commit 1
```

👉 edit commit message

**🔀 pick**
```
pick a1b2c3 commit 1
```

👉 keep commit as is

**🔻 squash (s)**
```
pick a1b2c3 commit 1
squash d4e5f6 commit 2
```

👉 combine commits (edit message)

**⚡ fixup (f)**
```
pick a1b2c3 commit 1
fixup d4e5f6 commit 2
```
👉 combine commits (discard message)

---

## 🔹 Squash (Main Concept)
🧠 What it does

Combines multiple commits into one clean commit

**⚙️ Usage**
```
git rebase -i HEAD~3
```

Then:
* pick first commit
* squash second commit
* squash third commit

🧾 Final step

Edit combined message:
```
Add multiply feature with improvements
```

**🔁 After Rebase/Squash**
```
git push --force
```

👉 because history changed

**⚠️ Important Rules**
- Only squash your own commits
- Avoid rewriting shared history
- Use before pushing (best practice)

---
