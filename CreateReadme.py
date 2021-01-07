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
    f.write("### My Leetcode Solutions\n\n---\n")
    f.write("\n**Hard:**\n")
    for each in difficulties['hard']:
        f.write(f"- [{each.replace('./', '')}](<{each}>)\n")
    f.write("\n**Medium:**\n")
    for each in difficulties['medium']:
        f.write(f"- [{each.replace('./', '')}](<{each}>)\n")
    f.write("\n**Easy:**\n")
    for each in difficulties['easy']:
        f.write(f"- [{each.replace('./', '')}](<{each}>)\n")
    f.write("\n---\n")
    for key in langs:
        f.write(f"\n**{langLookup[key]}:**\n")
        for each in langs[key]:
            f.write(f"- [{each.replace('./', '')}](<{each}>)\n")
