#!/usr/bin/env python3
import sys
import os
import json
import time
import subprocess
from datetime import datetime
import re

if len(sys.argv) < 2:
    print("Usage: ./finish.py <Confidence (1-5)>")
    print("Example: ./finish.py 4")
    sys.exit(1)

try:
    confidence = int(sys.argv[1])
    if confidence < 1 or confidence > 5:
        raise ValueError
except ValueError:
    print("Error: Confidence must be an integer between 1 and 5.")
    sys.exit(1)

# Read problem and time from tracker
tracker_file = ".leetcode_tracker.json"
problem = "Unknown Problem"
time_spent_str = "N/A"

if os.path.exists(tracker_file):
    try:
        with open(tracker_file, "r") as f:
            data = json.load(f)
        
        problem = data.get("problem", "Unknown Problem")
        start_time = data.get("start_time")
        
        if start_time:
            elapsed_seconds = int(time.time() - start_time)
            m, s = divmod(elapsed_seconds, 60)
            h, m = divmod(m, 60)
            if h > 0:
                time_spent_str = f"{h}h {m}m {s}s"
            elif m > 0:
                time_spent_str = f"{m}m {s}s"
            else:
                time_spent_str = f"{s}s"
                
        # Clean up tracker file since we only work on one at a time
        os.remove(tracker_file)
    except Exception as e:
        print(f"⚠️ Error reading tracker file: {e}")
else:
    print("⚠️ No active problem found. Please run ./start.py first next time!")
    # If there's a second arg, maybe they did ./finish.py "Problem" 4 by accident?
    if len(sys.argv) == 3:
        try:
            confidence = int(sys.argv[2])
            problem = sys.argv[1]
            print(f"Using provided problem name: {problem}")
        except ValueError:
            sys.exit(1)
    else:
        sys.exit(1)

date_str = datetime.now().strftime("%Y-%m-%d")
progress_file = "PROGRESS.md"

# Initialize file if it doesn't exist
if not os.path.exists(progress_file):
    with open(progress_file, "w") as f:
        f.write("# Progress Tracker\n\n")
        f.write("| Problem Name | Last Date Attempt | Time Spent | Confidence (1-5) |\n")
        f.write("| :--- | :--- | :--- | :---: |\n")

with open(progress_file, "r") as f:
    lines = f.readlines()

# find table headers
header_idx = -1
for i, line in enumerate(lines):
    if "| Problem Name |" in line:
        if "Time Spent" not in line:
            lines[i] = "| Problem Name | Last Date Attempt | Time Spent | Confidence (1-5) |\n"
            lines[i+1] = "| :--- | :--- | :--- | :---: |\n"
            for j in range(i+2, len(lines)):
                if lines[j].strip() and lines[j].startswith("|"):
                    parts = lines[j].split('|')
                    if len(parts) >= 4:
                        lines[j] = f"|{parts[1]}|{parts[2]}| N/A |{parts[3]}|\n"
        header_idx = i
        break

if header_idx == -1:
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    lines.extend([
        "\n",
        "| Problem Name | Last Date Attempt | Time Spent | Confidence (1-5) |\n",
        "| :--- | :--- | :--- | :---: |\n"
    ])
    header_idx = len(lines) - 3

# check if problem exists in the table to update it
problem_found = False
for i in range(header_idx + 2, len(lines)):
    line = lines[i].strip()
    if not line:
        continue
        
    parts = line.split('|')
    if len(parts) >= 5:
        existing_problem = parts[1].strip()
        
        def normalize(s):
            s = re.sub(r"^\d+\.\s*", "", s)
            return re.sub(r"[^\w\s]", "", s).lower().strip()
        
        if normalize(existing_problem) == normalize(problem):
            lines[i] = f"| {problem} | {date_str} | {time_spent_str} | {confidence} |\n"
            problem_found = True
            break

# If not found, append a new row
if not problem_found:
    lines.append(f"| {problem} | {date_str} | {time_spent_str} | {confidence} |\n")

with open(progress_file, "w") as f:
    f.writelines(lines)

print(f"✅ Logged progress for '{problem}' with confidence {confidence} on {date_str}")
if time_spent_str != "N/A":
    print(f"⏱️  Time spent: {time_spent_str}")

# Git Automation (No Auto Push)
print("\n🐙 Committing to Git...")
try:
    subprocess.run(["git", "add", "."], check=True, capture_output=True)
    res = subprocess.run(["git", "commit", "-m", f"Solve {problem} | Confidence: {confidence}"], check=False, capture_output=True)
    if res.returncode == 0:
        print("✅ Committed changes locally! (Run `git push` manually when ready)")
    else:
        print("⚠️  Nothing to commit.")
except Exception as e:
    print(f"⚠️  Git automation failed: {e}")
