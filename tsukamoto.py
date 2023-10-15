# ********************** CRISP INPUT ********************
inputan_suhu = input("input nilai suhu: ")
inputan_suara = input("input nilai suara: ")
inputan_cahaya = input("input nilai cahaya: ")
print("\n")

# ********************** FUZZYFIKASI ********************
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

# *********************** FUZZY INPUT ******************
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


jml_produk=[]
a_predikat=[]

# ***************************** INFERENCE ************************
# [1] if suhu RENDAH, kebisingan TENANG, cahaya REDUP => JML PRODUK = 148.0
a_predikat.append(min(a,d,g))
jml_produk.append(148.0)
# [2] if suhu RENDAH, kebisingan TENANG, cahaya AGAK TERANG => JML PRODUK = 150.9
a_predikat.append(min(a,d,h))
jml_produk.append(150.9)
# [3] if suhu RENDAH, kebisingan TENANG, cahaya TERANG => JML PRODUK = 146.5
a_predikat.append(min(a,d,i))
jml_produk.append(146.5)
# [4] if suhu RENDAH, kebisingan AGAK BISING, cahaya REDUP => JML PRODUK = 143.1
a_predikat.append(min(a,e,g))
jml_produk.append(143.1)
# [5] if suhu RENDAH, kebisingan AGAK BISING, cahaya AGAK TERANG => JML PRODUK = 146.53
a_predikat.append(min(a,e,h))
jml_produk.append(146.53)
# [6] if suhu RENDAH, kebisingan AGAK BISING, cahaya TERANG => JML PRODUK = 142.73
a_predikat.append(min(a,e,i))
jml_produk.append(142.73)
# [7] if suhu RENDAH, kebisingan BISING, cahaya REDUP => JML PRODUK = 136.73
a_predikat.append(min(a,f,g))
jml_produk.append(136.73)
# [8] if suhu RENDAH, kebisingan BISING, cahaya AGAK TERANG => JML PRODUK = 140.77
a_predikat.append(min(a,f,h))
jml_produk.append(140.77)
# [9] if suhu RENDAH, kebisingan BISING, cahaya TERANG => JML PRODUK = 135.97
a_predikat.append(min(a,f,i))
jml_produk.append(135.97)

# [10] if suhu NORMAL, kebisingan TENANG, cahaya REDUP => JML PRODUK = 149.73
a_predikat.append(min(b,d,g))
jml_produk.append(149.73)
# [11] if suhu NORMAL, kebisingan TENANG, cahaya AGAK TERANG => JML PRODUK = 153.27
a_predikat.append(min(b,d,h))
jml_produk.append(153.27)
# [12] if suhu NORMAL, kebisingan TENANG, cahaya TERANG => JML PRODUK = 152.13
a_predikat.append(min(b,d,i))
jml_produk.append(152.13)
# [13] if suhu NORMAL, kebisingan AGAK BISING, cahaya REDUP => JML PRODUK = 148
a_predikat.append(min(b,e,g))
jml_produk.append(148)
# [14] if suhu NORMAL, kebisingan AGAK BISING, cahaya AGAK TERANG => JML PRODUK = 150.63
a_predikat.append(min(b,e,h))
jml_produk.append(150.63)
# [15] if suhu NORMAL, kebisingan AGAK BISING, cahaya TERANG => JML PRODUK = 147.63
a_predikat.append(min(b,e,i))
jml_produk.append(147.63)
# [16] if suhu NORMAL, kebisingan BISING, cahaya REDUP => JML PRODUK = 141.47
a_predikat.append(min(b,f,g))
jml_produk.append(141.47)
# [17] if suhu NORMAL, kebisingan BISING, cahaya AGAK TERANG => JML PRODUK = 145.67
a_predikat.append(min(b,f,h))
jml_produk.append(145.67)
# [18] if suhu NORMAL, kebisingan BISING, cahaya TERANG => JML PRODUK = 140.2
a_predikat.append(min(b,f,i))
jml_produk.append(140.2)

# [19] if suhu TINGGI, kebisingan TENANG, cahaya REDUP => JML PRODUK = 142.10
a_predikat.append(min(c,d,g))
jml_produk.append(142.10)
# [20] if suhu TINGGI, kebisingan TENANG, cahaya AGAK TERANG => JML PRODUK = 146.53
a_predikat.append(min(c,d,h))
jml_produk.append(146.53)
# [21] if suhu TINGGI, kebisingan TENANG, cahaya TERANG => JML PRODUK = 142.17
a_predikat.append(min(c,d,i))
jml_produk.append(142.17)
# [22] if suhu TINGGI, kebisingan AGAK BISING, cahaya REDUP => JML PRODUK = 138.7
a_predikat.append(min(c,e,g))
jml_produk.append(138.7)
# [23] if suhu TINGGI, kebisingan AGAK BISING, cahaya AGAK TERANG => JML PRODUK = 141.4
a_predikat.append(min(c,e,h))
jml_produk.append(141.4)
# [24] if suhu TINGGI, kebisingan AGAK BISING, cahaya TERANG => JML PRODUK = 138.3
a_predikat.append(min(c,e,i))
jml_produk.append(138.3)
# [25] if suhu TINGGI, kebisingan BISING, cahaya REDUP => JML PRODUK = 133.33
a_predikat.append(min(c,f,g))
jml_produk.append(133.33)
# [26] if suhu TINGGI, kebisingan BISING, cahaya AGAK TERANG => JML PRODUK = 138.33
a_predikat.append(min(c,f,h))
jml_produk.append(138.33)
# [27] if suhu TINGGI, kebisingan BISING, cahaya TERANG => JML PRODUK = 133.77
a_predikat.append(min(c,f,i))
jml_produk.append(133.77)


# ********************** DEFUZZYFIKASI ********************
print("\n")
a_pred_x_prod = 0
total_a_pred = 0
z = 0

for i in range(27):
    a_pred_x_prod += a_predikat[i]*jml_produk[i]
    total_a_pred += a_predikat[i]
print(a_pred_x_prod)
print(total_a_pred)

if total_a_pred == 0:
    print("nilai fuzzy undefined")
else:
    z = a_pred_x_prod / total_a_pred
    z_2dig = "{:.2f}".format(z)
    print(f"fuzzy out: {z_2dig}")