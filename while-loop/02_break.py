number = [12,25,73,21,25,30]
divisor =6

print(f"ตัวที่หาร{divisor} ลงตัว :")
foung = 0


for i in number:
    if i % divisor == 0:
        print(f"{i} หาร {divisor} ตัวที่หารลงตัวคือ({i // divisor})")
        found += 1
        
        if found == 3:
            break