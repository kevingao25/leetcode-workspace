#!/usr/bin/env python3
import os
from datetime import datetime
import re

progress_file = "PROGRESS.md"

if not os.path.exists(progress_file):
    print("No progress tracked yet! Solve some problems and use finish.py first.")
    exit(0)

with open(progress_file, "r") as f:
    lines = f.readlines()

to_review = []
today = datetime.now()

for line in lines:
    line = line.strip()
    if not line or not line.startswith("|") or "Problem Name" in line or "---" in line:
        continue
        
    parts = [p.strip() for p in line.split('|')]
    if len(parts) >= 5:
        # Format: | Problem | Date | Time | Conf |
        problem = parts[1]
        date_str = parts[2]
        conf_str = parts[4]
        
        try:
            conf = int(conf_str)
            last_date = datetime.strptime(date_str, "%Y-%m-%d")
            days_ago = (today - last_date).days
            
            # Spaced repetition logic
            needs_review = False
            if conf <= 2 and days_ago >= 1:
                needs_review = True
            elif conf == 3 and days_ago >= 3:
                needs_review = True
            elif conf == 4 and days_ago >= 7:
                needs_review = True
            elif conf == 5 and days_ago >= 14:
                needs_review = True
                
            if needs_review:
                to_review.append((problem, days_ago, conf))
        except ValueError:
            pass

print("🧠 Spaced Repetition Review 🧠\n")

if not to_review:
    print("🎉 You're all caught up! No problems need reviewing today.")
else:
    print(f"You have {len(to_review)} problem(s) to review:\n")
    # Sort by lowest confidence first, then by oldest
    to_review.sort(key=lambda x: (x[2], -x[1]))
    
    for prob, days, conf in to_review:
        print(f"🔹 {prob}")
        print(f"   Confidence: {'⭐' * conf}{'☆' * (5-conf)} | Last attempted: {days} days ago\n")
