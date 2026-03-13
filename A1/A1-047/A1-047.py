# --------------------------------------------------
# File Name : A1-047.py
# Problem   : Teaching Schedule
# Author    : Worralop Srichainont
# Date      : 2026-01-01
# --------------------------------------------------

# Input class periods and duration
class_periods = int(input().strip())
class_duration = int(input().strip())

# Calculate total teaching time in minutes
total_minutes = class_periods * class_duration

# Calculate hours and minutes
hours = total_minutes // 60
minutes = total_minutes % 60

# Construct the output string based on hours and minutes
result = ""
if total_minutes == 0:
    result = "No teaching"

if total_minutes > 0 and hours > 0:
    result += f"{hours} hours"
    # if hours > 1:
    #     result += "s"

if total_minutes > 0 and minutes > 0:
    result += f" {minutes} minute"
    if minutes > 1:
        result += "s"

# Print the result
print(result.strip())
