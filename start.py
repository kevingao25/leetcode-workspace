#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import re
import time
import textwrap
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = []
    def handle_data(self, d):
        self.text.append(d)
    def handle_starttag(self, tag, attrs):
        if tag in ["p", "br", "li"]:
            self.text.append("\n")
    def get_data(self):
        return "".join(self.text)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    text = re.sub(r"\n\s*\n", "\n\n", s.get_data()).strip()
    wrapped_lines = []
    for paragraph in text.split("\n\n"):
        wrapped_lines.append(textwrap.fill(paragraph, width=100))
    return "\n\n".join(wrapped_lines)

def get_leetcode_data(problem_name):
    # Remove leading numbers and dots
    name = re.sub(r"^\d+\.\s*", "", problem_name).lower()
    # Replace special characters and punctuation with spaces, then collapse spaces
    name = re.sub(r"[^\w\s-]", "", name)
    title_slug = "-".join(name.split())
    
    url = "https://leetcode.com/graphql"
    query = """
    query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        codeSnippets {
          lang
          langSlug
          code
        }
      }
    }
    """
    variables = {"titleSlug": title_slug}
    data = json.dumps({"query": query, "variables": variables}).encode('utf-8')
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.getcode() == 200:
                res_data = response.read().decode('utf-8')
                parsed = json.loads(res_data)
                return parsed.get("data", {}).get("question", None)
    except Exception as e:
        print(f"⚠️ Could not fetch LeetCode data: {e}")
    return None

if len(sys.argv) < 3:
    print("Usage: ./start.py <Category_Folder> <Problem_Name>")
    print("Example: ./start.py 01_Array_String '1768. Merge Strings Alternately'")
    sys.exit(1)

category = sys.argv[1]
problem = sys.argv[2]
# Sanitize problem name for file name
safe_problem_name = problem.replace(" ", "_").replace(".", "").replace("/", "").lower()

if not os.path.exists(category):
    os.makedirs(category)
    print(f"📁 Created directory: {category}")

md_path = os.path.join(category, f"{safe_problem_name}.md")
# By default, creates a Python file, but you can change this to .ts, .cpp, .rs, etc.
code_path = os.path.join(category, f"{safe_problem_name}.py")

# Create Markdown notes from template
if not os.path.exists(md_path):
    if os.path.exists("TEMPLATE.md"):
        with open("TEMPLATE.md", "r") as f:
            template = f.read()
        template = template.replace("[Problem Name]", problem)
        with open(md_path, "w") as f:
            f.write(template)
        print(f"✅ Created notes file: {md_path}")
    else:
        print("⚠️ TEMPLATE.md not found. Generating an empty markdown file.")
        with open(md_path, "w") as f:
            f.write(f"# {problem}\n")
else:
    print(f"⚠️ Notes file already exists: {md_path}")

# Create code file
if not os.path.exists(code_path):
    print(f"🔍 Fetching problem details from LeetCode...")
    lc_data = get_leetcode_data(problem)
    description = ""
    starter_code = ""
    
    if lc_data:
        content_html = lc_data.get("content")
        if content_html:
            description = strip_tags(content_html)
            
        snippets = lc_data.get("codeSnippets") or []
        for snip in snippets:
            if snip.get("langSlug") == "python3":
                starter_code = snip.get("code", "")
                break
                
    with open(code_path, "w") as f:
        f.write(f'"""\n{problem}\n')
        if description:
            f.write(f'\n{description}\n')
        f.write('"""\n\n')
        
        if starter_code:
            f.write(f'{starter_code}\n')
        else:
            f.write('# Write your solution here\n')
            
    print(f"✅ Created code file: {code_path}")
else:
    print(f"⚠️ Code file already exists: {code_path}")

print("\n🚀 Happy coding! Don't forget to update the tracker with ./finish when you're done.")

# Log start time
tracker_file = ".leetcode_tracker.json"
try:
    if os.path.exists(tracker_file):
        with open(tracker_file, "r") as f:
            data = json.load(f)
    else:
        data = {}
    
    data[problem] = time.time()
    with open(tracker_file, "w") as f:
        json.dump(data, f)
except Exception:
    pass
