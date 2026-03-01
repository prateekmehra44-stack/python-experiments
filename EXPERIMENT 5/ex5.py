text = input("Enter string: ").upper()

for ch in sorted(set(text)):
    if ch.isalpha():
        print(text.count(ch), ch, sep="")