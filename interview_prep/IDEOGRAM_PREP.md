# Ideogram Interview Prep Guide

Given Ideogram's focus on Generative AI, text-to-image processing, and typography, you should expect algorithmic questions that deal with 2D grids (images), string manipulation (prompts/typography), and efficient state traversal (diffusion processes).

Here is a prioritized list of problems to tackle before your interview on Monday. **Stick to the 15-minute rule**: if you don't see the pattern after 15 minutes, look at the solution, understand the "Aha!" moment, type it out, and move on.

---

## 🟥 HIGH PRIORITY (Do These First)

These patterns are the absolute bread and butter for AI and image processing companies.

### 1. 2D Matrices / Grid Traversal (DFS & BFS)

Images are just giant 2D arrays. If your friend was asked a BFS/DFS question, there is a very high chance it was on a grid.

* [X] **200. Number of Islands** (Medium) - *The absolute must-know baseline for DFS/BFS on a grid.*
* [ ] **695. Max Area of Island** (Medium) - *A slight variation of the above.*
* [X] **994. Rotting Oranges** (Medium) - *The holy grail of Multi-source BFS on a grid. Extremely high yield.*
* [ ] **542. 01 Matrix** (Medium) - *Another highly-tested Multi-source BFS pattern.*
* [ ] **130. Surrounded Regions** (Medium) - *Tests your ability to run DFS specifically from the edges of a grid.*
* [X] **733. Flood Fill** (Easy) - *Great warmup for grid DFS. Very intuitive.*
* [ ] **1091. Shortest Path in Binary Matrix** (Medium) - *Essential BFS grid question. Finding the shortest path in an 8-directional grid.*
* [X] **1926. Nearest Exit from Entrance in Maze** (Medium) - *Classic BFS pathfinding on a grid (From LeetCode 75).*
* [ ] **286. Walls and Gates** (Medium) - *Another top-tier multi-source BFS.*
* [ ] **48. Rotate Image** (Medium) - *Classic 2D array manipulation.*
* [ ] **54. Spiral Matrix** (Medium) - *Tests your ability to manage matrix boundaries without getting lost.*

### 2. String Parsing & Manipulation

Ideogram's competitive edge is typography (text in images). They care about text parsing.

* [ ] **3. Longest Substring Without Repeating Characters** (Medium) - *Classic sliding window on a string.*
* [ ] **394. Decode String** (Medium) - *Uses a Stack to parse nested strings. Highly relevant for prompt processing!*
* [ ] **20. Valid Parentheses** (Easy) - *Baseline stack/parsing question.*
* [ ] **424. Longest Repeating Character Replacement** (Medium) - *Sliding window string optimization.*

---

## 🟨 MEDIUM PRIORITY (Do These Saturday/Sunday)

These are standard, highly-tested patterns that prove you understand efficient data structures.

### 3. Graphs and BFS/DFS (State Exploration)

* [ ] **207. Course Schedule** (Medium) - *Topological sort. Proves you understand directed graphs.*
* [X] **399. Evaluate Division** (Medium) - *Classic DFS/BFS graph traversal with edge weights. Very common.*
* [ ] **133. Clone Graph** (Medium) - *Tests your ability to copy complex reference structures using Hash Maps and BFS/DFS.*
* [ ] **127. Word Ladder** (Hard/Medium) - *Finding the shortest path between words. (Skip if too hard, but good to know the BFS pattern).*
* [ ] **323. Number of Connected Components in an Undirected Graph** (Medium) - *Core graph exploration.*
* [ ] **210. Course Schedule II** (Medium) - *Follow-up to Course Schedule, requires building the actual topological sort path.*
* [ ] **785. Is Graph Bipartite?** (Medium) - *Classic graph coloring using BFS or DFS.*
* [X] **841. Keys and Rooms** (Medium) - *Excellent warmup for standard Graph DFS (From LeetCode 75).*
* [X] **547. Number of Provinces** (Medium) - *Classic connected components problem (From LeetCode 75).*
* [X] **1466. Reorder Routes to Make All Paths Lead to the City Zero** (Medium) - *Clever trick involving traversing a directed graph as if it were undirected (From LeetCode 75).*

### 4. Hash Maps & Arrays (Speed optimizations)

* [X] **56. Merge Intervals** (Medium) - *Very common pattern for array manipulation.*
* [X] **238. Product of Array Except Self** (Medium) - *Testing your ability to avoid O(N^2) brute force without using division.*

---

## 🟩 LOW PRIORITY (Topics to Ignore)

Do not spend time on these topics before Monday. They are highly unlikely to be asked and offer a poor return on time investment.

* **Bit Manipulation** (Too niche, mostly logic puzzles)
* **Tries / Prefix Trees** (Too much boilerplate for a 45-min interview)
* **Complex Dynamic Programming** (Hard DP is rarely asked for general SWE unless specifically related to an ML algorithm)
* **Advanced Math / Geometry**
* **Linked Lists** (Unless you have extra time, these are usually considered lower-tier questions compared to Arrays/Graphs)
