file_path = 'update-center.json'
changed_lines = 0

with open(file_path, 'r') as file:
    file_content = file.readlines()

for i in range(len(file_content)):
    line = file_content[i]
    if 'www.google.com' in line:
        file_content[i] = line.replace('www.google.com', 'www.example.domain')
        changed_lines += 1
    if 'updates.jenkins.io/download/plugins' in line:
        file_content[i] = line.replace('updates.jenkins.io/download/plugins', 'www.example.domainjenkins/plugins')
        changed_lines += 1

with open(file_path, 'w') as file:
    file.writelines(file_content)

print(f"Number of lines changed: {changed_lines}")
