import hashlib

list = []


for i in range(90):

    txt = open("hash/pass{}.txt".format(str(i + 1).zfill(3)), mode="r", encoding="UTF-8")

    string = txt.read()

    hs = hashlib.sha256(string.encode()).hexdigest()

    if hs == "aff02d6ad353ebf547f3b1f8ecd21efd7931e356f3930ab5ee502a391c5802d7" or hs == "8428f87e4dbbf1e95dba566b2095d989f5068a5465ebce96dcdf0b487edb8ecb" or hs == "e82f6ff15ddc9d67fc28c4b2c575adf7252d6e829af55c2b7ac1615b304d8962":
        list.append(string)
    
    txt.close()

for n in list:
    print(n.rstrip(), end="")