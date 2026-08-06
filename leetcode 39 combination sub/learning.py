# 📝 Combination Sum (LC 39) — Key Learnings Summary
# 1. Time Complexity Analysis
# Formula: O(n^(T/m)) — kabhi kabhi extra O(T/m) factor ke saath (combination copy karne ke liye jab result mein store karte hain)
# Kaise derive kiya:
# n = number of candidates (har level pe max branching factor)
# T/m = max possible depth (agar smallest candidate m baar baar use ho target T tak pahunchne ke liye)
# Tree ka size roughly n^depth hota hai → exponential
# Why exponential okay hai: Problem ki nature hi combinatorial hai — humein saari valid combinations chahiye, na ke sirf ek best answer. Isse better order-wise possible nahi.
# 2. Bug: Duplicate Combinations in Result (pehla attempt wala)

# Problem tha: total == target check loop ke bahar/pehle kiya tha, jabke parent apna ek hi element add karke total update kar chuka tha. Loop ke andar jitni baar bhi child call hoti, sab same (already-matched) total ke saath call hoti, aur har child independently match record kar deti → same combination multiple baar result mein chala jata.

# Fix: Check (total == target) ko turant apna element add karne ke baad rakho, loop shuru hone se pehle — taake match sirf ek baar detect ho, per unique path.

# Key insight: Jab bhi backtracking mein duplicate results aayein, sabse pehle yeh check karo — kahin match/base-case check galat jagah (bahar loop ke, multiple sibling calls ke through) to nahi ho raha.

# 3. Optimization: Copying res vs Share-and-Undo (Backtracking core pattern)

# Kya galat tha (inefficient version):

# python
# back(cand, target, n, total, list(res))  # har call pe NAYI copy

# Har recursive call pe list(res) naya list banata hai — O(len(res)) cost per call, jo already-exponential tree ke upar multiply hoke extra slow-down deta hai.

# Optimal fix — Share-and-Undo pattern:

# python
# res.append(choice)      # choice le lo (shared list modify)
# # ... recursive calls, same res object pass karo (no copy) ...
# res.pop()                # undo — taake next sibling clean state pae
# Saari recursive calls same list object ko reference se share karti hain (Python lists mutable hain)
# Jab ek branch apna kaam khatam kare, woh apna daala hua element pop kar deta hai — taake sibling branches ko fresh/clean list mile
# Result mein store karte waqt hi list(res) copy karo — sirf wahi ek jagah, kyunki wahi permanent snapshot chahiye (baaki jagah reference hi kaafi hai)

# Why better: Append/pop dono O(1) operations hain (list ke end pe) → total extra cost O(N) (N = tree nodes) instead of O(N × depth). Bada farak padta hai jab depth (T/m) bada ho.

# General rule for backtracking: Jab bhi recursive backtracking likho jahan tum ek shared "path so far" (list/string/set) build kar rahe ho — copy karne ke bajaye share + undo (pop/remove) pattern use karo. Yeh standard optimization hai jo har backtracking problem mein applicable hai (Subsets, Permutations, Word Search, N-Queens, etc.)

# 4. Python Gotcha: Mutable Default Arguments

# Problem:

# python
# def back(cand, target, i=0, total=0, res=[]):

# Python default arguments sirf ek baar evaluate hote hain — function define hone ke time pe, har call pe nahi. Agar function bina res diye multiple baar call ho, saari calls same list object share karengi — leftover data leak ho sakta hai previous calls se. Yeh silent, intermittent bug hai (order-dependent, catch karna mushkil).

# Do valid fixes:

# Option A: res=None default rakho, function ke andar if res is None: res = [] se fresh list banao
# Option B (cleaner, jo tune final version mein use kiya): res ko required parameter bana do (no default at all) — tab koi bhi call bina res diye ho hi nahi sakti, risk automatically eliminate ho jata hai

# General rule: Kabhi bhi mutable default (list, dict, set) function signature mein directly mat likho — hamesha None default + lazy init, ya required parameter rakho.

# 5. Quick Checklist for Backtracking Problems (aage ke liye)
#  Base case check sahi jagah hai? (loop se pehle, apna choice add karne turant baad)
#  Result mein store karte waqt copy (list(...)) ho raha hai, but baaki jagah share ho raha hai?
#  Har return path pe undo (pop()/remove()) present hai?
#  Mutable default arguments to nahi use kiye function signature mein?
#  Time complexity derive kiya: branching factor × max depth se?