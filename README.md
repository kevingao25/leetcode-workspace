# LeetCode 75 Master Tracker

Welcome to your LeetCode 75 tracking matrix. Tackling two questions per day will get you through this in about 38 days!

## Progress Tracking

Your progress is tracked in [PROGRESS.md](PROGRESS.md).

* **Confidence 5**: Could code it flawlessly on a whiteboard.
* **Confidence 1**: Had to look at the solution.
* *Schedule a review 3-4 days later if confidence is 3 or below.*

## Structure

Organized by fundamental patterns, aligned with the LeetCode 75 groupings:
- `01_Array_String/`
- `02_Two_Pointers/`
- `03_Sliding_Window/`
- `04_Prefix_Sum/`
- `05_Hash_Map_Set/`
- `...`

## Features

* **Auto-Fetch**: `./start.py` pulls the problem description and starter code directly from LeetCode.
* **Time Tracking**: The workspace silently logs how long it takes you to solve a problem.
* **Local Testing**: Generates a local test block at the bottom of your Python files.
* **Spaced Repetition**: `./review.py` automatically tells you which problems you should practice today.
* **Git Automation**: `./finish.py` automatically commits your progress.

## The Workflow

1. **Daily Review**: Run `./review.py` to see what past problems you need to practice today based on spaced repetition.
2. **Start a Problem**: Run `./start.py "01_Array_String" "1768. Merge Strings Alternately"`. This generates a one-pager template and your code file with the LeetCode description and starter code.
3. **Solve & Test**: Implement your solution locally and verify it using the test block.
4. **Document**: Fill out the generated Markdown one-pager using the template for future reference.
5. **Track & Commit**: Run `./finish.py 4` (with your confidence score 1-5) to update `PROGRESS.md`, record your time, and automatically commit to Git!

---

*“It is much better to deeply understand 40 pattern-defining questions than to scrape through all 75 without retaining the underlying logic.”*
