import os

langLookup = {
    'js': 'JavaScript',
    'py': 'Python',
    'c': 'C',
    'cpp': 'C++',
    'php': 'PHP',
    'ts': 'TypeScript',
    'rb': 'Ruby',
    'java': 'Java',
    'scala': 'Scala',
    'cs': 'C#',
    'sql': 'SQL'
}

difficulties = {
    'easy': [],
    'medium': [],
    'hard': []
}

langs = {}

for d in os.walk('.'):
    if '.git' not in d[0] and './' in d[0]:
        with open(f"{d[0]}/README.md", 'r') as readme:
            for line in readme.readlines():
                if '**easy**' in line.lower():
                    difficulties['easy'].append(d[0])
                    break
                if '**medium**' in line.lower():
                    difficulties['medium'].append(d[0])
                    break
                if '**hard**' in line.lower():
                    difficulties['hard'].append(d[0])
                    break
        for each in d[2]:
            if '.md' not in each:
                ext = each.split('.')[1]
                if ext in langs:
                    langs[ext].append(d[0])
                else: 
                    langs[ext] = [d[0]]

with open("./README.md", 'w') as f:
    def createBullets(iterable):
        for each in iterable:
            f.write(f"<li><a href='{each.replace(' ', '%20')}'>{each.replace('./', '')}</a></li>\n")

    f.write("### My Leetcode Solutions\n\n---\n")

    f.write("\n<details>")
    f.write(f"\n<summary><b>Hard ({len(difficulties['hard'])}):</b></summary>\n<ul>")
    createBullets(difficulties['hard'])
    f.write("</ul>\n</details>\n")

    f.write("\n<details>")
    f.write(f"\n<summary><b>Medium ({len(difficulties['medium'])}):</b></summary>\n<ul>")
    createBullets(difficulties['medium'])
    f.write("</ul>\n</details>\n")

    f.write("\n<details>")
    f.write(f"\n<summary><b>Easy ({len(difficulties['easy'])}):</b></summary>\n<ul>")
    createBullets(difficulties['easy'])
    f.write("</ul>\n</details>\n")

    f.write("\n---\n")
    for key in sorted(langs.keys()):
        f.write("\n<details>")
        f.write(f"\n<summary><b>{langLookup[key]} ({len(langs[key])}):</b></summary>\n<ul>")
        createBullets(langs[key])
        f.write("</ul>\n</details>\n")
