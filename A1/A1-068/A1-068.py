# --------------------------------------------------
# File Name : A1-068.py
# Problem   : Average Score
# Author    : Worralop Srichainont
# Date      : 2026-01-03
# --------------------------------------------------

# Read number of students and their scores
students = int(input().strip())
scores = list(map(int, input().strip().split()))

# Calculate average score
average_score = sum(scores) / students

# Determine pass or fail status
is_pass = True
if average_score < 60:
    is_pass = False

if is_pass:
    for score in scores:
        if score < 50:
            is_pass = False
            break

# Output the average score and pass/fail status
print(f"{average_score:.1f}")
if is_pass:
    print("PASS")
else:
    print("FAIL")
