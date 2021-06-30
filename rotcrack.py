import string

charset = string.ascii_uppercase
enc = input("enter value")

for k in range(26):
    dec = ""
    for c in enc.upper():
        if c in charset:
            idx = charset.find(c)
            idx += k
            if idx >= len(charset):
                idx -= len(charset)
            elif idx < 0:
                idx += len(charset)
            dec += charset[idx]
        else:
            dec = dec + c   
    print(dec)