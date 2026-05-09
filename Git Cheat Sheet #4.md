# 📘 GIT MERGE CONFLICTS


## 🔹 What is a Merge Conflict?
🧠 Simple Meaning
When Git can’t decide which change to keep

**🧩 When does it happen?**

Same file

Same line

Changed differently in two branches

---

### ⚠️ Example Conflict
**Branch A**
return a + b + 1

**Branch B**
return a + b + 2

**👉 Git gets confused → conflict**

---

## 🔥 What Git Shows
<<<<<<< HEAD

return a + b + 1

=======

return a + b + 2

>>>>>>> feature-branch

---

**🧠 Meaning**

**Part**             **Meaning**

HEAD	       =       current branch

=======	     =       separator

below	       =     incoming branch

---

## 🔧 How to Fix Conflict (Step-by-Step)
- 🔹 1. Open conflicted file

- 🔹 2. Choose final code
Example:
```
return a + b + 3
```

- 🔹 3. Remove markers
```
<<<<<<<
=======
>>>>>>>
```

- 🔹 4. Mark as resolved
```
git add <file>
```

- 🔹 5. Complete merge
```
git commit -m "Resolved merge conflict"
```

---

## 🧠 Conflict During Rebase
### 🔹 Fix process
```
# fix file manually
git add .
git rebase --continue
```

**🔁 If stuck**
```
git rebase --abort
```

---

## 🔹 Conflict During Merge
### 🔹 Fix process
```
# fix file
git add .
git commit
```

---
