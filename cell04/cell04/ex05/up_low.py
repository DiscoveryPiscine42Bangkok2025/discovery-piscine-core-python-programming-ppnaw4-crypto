text = input()
result = ""

for ch in text:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

print("Converted:", result)
