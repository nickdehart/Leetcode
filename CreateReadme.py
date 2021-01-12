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
    'cs': 'C#'
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
        ext = d[2][0].split('.')[1]
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
    f.write("\n<summary><b>Hard:</b></summary>\n<ul>")
    createBullets(difficulties['hard'])
    f.write("</ul>\n</details>\n")

    f.write("\n<details>")
    f.write("\n<summary><b>Medium:</b></summary>\n<ul>")
    createBullets(difficulties['medium'])
    f.write("</ul>\n</details>\n")

    f.write("\n<details>")
    f.write("\n<summary><b>Easy:</b></summary>\n<ul>")
    createBullets(difficulties['easy'])
    f.write("</ul>\n</details>\n")

    f.write("\n---\n")
    for key in langs:
        f.write("\n<details>")
        f.write(f"\n<summary><b>{langLookup[key]}:</b></summary>\n<ul>")
        createBullets(langs[key])
        f.write("</ul>\n</details>\n")
