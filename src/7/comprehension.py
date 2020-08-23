with open('files.py') as file:
    lines = [line.strip() + 's' for line in file]
    print(lines)