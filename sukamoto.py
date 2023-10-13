# suhu = 20
inputan_suhu = input("input nilai suhu: ")
inputan_suara = input("input nilai suara: ")
inputan_cahaya = input("input nilai cahaya: ")

# ------------------- SUHU
def u_rendah(suhu):
    if suhu>=18 and suhu<=22:
        x = (suhu-18)/4
        return x
    elif suhu>=22 and suhu<=26:
        x = (26-suhu)/4
        return x
    else:
        return 0 
    
def u_normal(suhu):
    if suhu>=22 and suhu<=26:
        x = (suhu-22)/4
        return x
    elif suhu>=26 and suhu<=32:
        x = (32-suhu)/6
        return x
    else:
        return 0

def u_tinggi(suhu):
    if suhu>=26 and suhu<=32:
        x = (suhu-26)/6
        return x
    elif suhu>=32 and suhu<=38:
        x = (38-suhu)/6
        return x
    else:
        return 0
    
# ------------------- SUARA
def u_tenang(suara):
    if suara>=35 and suara<=55:
        x = (suara-35)/20
        return x
    elif suara>=55 and suara<=75:
        x = (75-suara)/20
        return x
    else:
        return 0

def u_agakBising(suara):
    if suara>=55 and suara<=75:
        x = (suara-55)/20
        return x
    elif suara>=75 and suara<=90:
        x = (90-suara)/15
        return x
    else:
        return 0

def u_bising(suara):
    if suara>=75 and suara<=90:
        x = (suara-75)/15
        return x
    elif suara>=90 and suara<=105:
        x = (105-suara)/15
        return x
    else:
        return 0
    
# ------------------- CAHAYA
def u_redup(cahaya):
    if cahaya>=0 and cahaya<=150:
        x = (cahaya-0)/150
        return x
    elif cahaya>=150 and cahaya<=300:
        x = (300-cahaya)/150
        return x
    else:
        return 0

def u_agakTerang(cahaya):
    if cahaya>=150 and cahaya<=300:
        x = (cahaya-150)/150
        return x
    elif cahaya>=300 and cahaya<=500:
        x = (500-cahaya)/200
        return x
    else:
        return 0
    
def u_terang(cahaya):
    if cahaya>=300 and cahaya<=500:
        x = (cahaya-300)/200
        return x
    elif cahaya>=500 and cahaya<=700:
        x = (700-cahaya)/200
        return x
    else:
        return 0


a = u_rendah(float(inputan_suhu))
print(f"keanggotaan suhu rendah: {a}")
b = u_normal(float(inputan_suhu))
print(f"keanggotaan suhu normal: {b}")
c = u_tinggi(float(inputan_suhu))
print(f"keanggotaan suhu tinggi: {c}")

d = u_tenang(float(inputan_suara))
print(f"keanggotaan tenang: {d}")
e = u_agakBising(float(inputan_suara))
print(f"keanggotaan agak bising: {e}")
f = u_bising(float(inputan_suara))
print(f"keanggotaan bising: {f}")

g = u_redup(float(inputan_cahaya))
print(f"keanggotaan redup: {g}")
h = u_agakTerang(float(inputan_cahaya))
print(f"keanggotaan agak terang: {h}")
i = u_terang(float(inputan_cahaya))
print(f"keanggotaan terang: {i}")