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

def prod_bertambah(rata2, predikat):
    if rata2>=142 and rata2<148:
        x=(predikat*6)+142
    elif rata2>=148 and rata2<155:
        x=155-(predikat*7)
    else:
        x=0
    return x

def prod_agakBertambah(rata2, predikat):
    if rata2>=136 and rata2<142:
        x=(predikat*6)+136
    elif rata2>=142 and rata2<148:
        x=148-(predikat*6)
    else:
        x=0
    return x

def prod_berkurang(rata2, predikat):
    if rata2>=130 and rata2<136:
        x=(predikat*6)+130
    elif rata2>=136 and rata2<142:
        x=142-(predikat*6)
    else:
        x=0
    return x
    
jml_produk=[148.0, 150.9, 146.5, 143.1, 146.53, 142.73, 136.73, 140.77, 135.97, 149.73, 153.27, 152.13, 148.00, 150.63, 147.63, 141.47, 145.67, 140.20, 142.10, 146.53, 142.17, 138.70, 141.40, 138.30, 133.33, 138.53, 133.77]

himpunan_produk=[]
a_predikat=[]

"""
berkurang  agak   bertambah
          btambah  
      /\    /\    /\
     /  \  /  \  /  \
    /    \/    \/    \
   /     /\    /\     \
  /     /  \  /  \     \
 /     /    \/    \     \
130   136   142   148   155
"""
# ***************************** INFERENCE ************************
# [1] if suhu RENDAH, kebisingan TENANG, cahaya REDUP => JML PRODUK = 148.0 (BERTAMBAH)
alpha = min(a,d,g)
a_predikat.append(alpha)
rata = jml_produk[0]
R1 = prod_bertambah(rata,alpha)
himpunan_produk.append(R1)
# [2] if suhu RENDAH, kebisingan TENANG, cahaya AGAK TERANG => JML PRODUK = 150.9 (BERTAMBAH)
alpha = min(a,d,h)
a_predikat.append(alpha)
rata = jml_produk[1]
R2 = prod_bertambah(rata,alpha)
himpunan_produk.append(R2)
# [3] if suhu RENDAH, kebisingan TENANG, cahaya TERANG => JML PRODUK = 146.5 (AGAK BERTAMBAH)
alpha = (min(a,d,i))
a_predikat.append(alpha)
rata = jml_produk[2]
R3 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R3)
# [4] if suhu RENDAH, kebisingan AGAK BISING, cahaya REDUP => JML PRODUK = 143.1 (AGAK BERTAMBAH)
alpha = (min(a,e,g))
a_predikat.append(alpha)
rata = jml_produk[3]
R4 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R4)
# [5] if suhu RENDAH, kebisingan AGAK BISING, cahaya AGAK TERANG => JML PRODUK = 146.53 (AGAK BERTAMBAH)
alpha = (min(a,e,h))
a_predikat.append(alpha)
rata = jml_produk[4]
R5 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R5)
# [6] if suhu RENDAH, kebisingan AGAK BISING, cahaya TERANG => JML PRODUK = 142.73 (AGAK BERTAMBAH)
alpha = (min(a,e,i))
a_predikat.append(alpha)
rata = jml_produk[5]
R6 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R6)
# [7] if suhu RENDAH, kebisingan BISING, cahaya REDUP => JML PRODUK = 136.73 (BERKURANG)
alpha = (min(a,f,g))
a_predikat.append(alpha)
rata = jml_produk[6]
R7 = prod_berkurang(rata,alpha)
himpunan_produk.append(R7)
# [8] if suhu RENDAH, kebisingan BISING, cahaya AGAK TERANG => JML PRODUK = 140.77 (BERKURANG)
alpha = (min(a,f,h))
a_predikat.append(alpha)
rata = jml_produk[7]
R8 = prod_berkurang(rata,alpha)
himpunan_produk.append(R8)
# [9] if suhu RENDAH, kebisingan BISING, cahaya TERANG => JML PRODUK = 135.97 (BERKURANG)
alpha = (min(a,f,i))
a_predikat.append(alpha)
rata = jml_produk[8]
R9 = prod_berkurang(rata,alpha)
himpunan_produk.append(R9)

# [10] if suhu NORMAL, kebisingan TENANG, cahaya REDUP => JML PRODUK = 149.73 (BERTAMBAH)
alpha = (min(b,d,g))
a_predikat.append(alpha)
rata = jml_produk[9]
R10 = prod_bertambah(rata,alpha)
himpunan_produk.append(R10)
# [11] if suhu NORMAL, kebisingan TENANG, cahaya AGAK TERANG => JML PRODUK = 153.27 (BERTAMBAH)
alpha = (min(b,d,h))
a_predikat.append(alpha)
rata = jml_produk[10]
R11 = prod_bertambah(rata,alpha)
himpunan_produk.append(R11)
# [12] if suhu NORMAL, kebisingan TENANG, cahaya TERANG => JML PRODUK = 152.13 (BERTAMBAH)
alpha = (min(b,d,i))
a_predikat.append(alpha)
rata = jml_produk[11]
R12 = prod_bertambah(rata,alpha)
himpunan_produk.append(R12)
# [13] if suhu NORMAL, kebisingan AGAK BISING, cahaya REDUP => JML PRODUK = 148 (BERTAMBAH)
alpha = (min(b,e,g))
a_predikat.append(alpha)
rata = jml_produk[12]
R13 = prod_bertambah(rata,alpha)
himpunan_produk.append(R13)
# [14] if suhu NORMAL, kebisingan AGAK BISING, cahaya AGAK TERANG => JML PRODUK = 150.63 (BERTAMBAH)
alpha = (min(b,e,h))
a_predikat.append(alpha)
rata = jml_produk[13]
R14 = prod_bertambah(rata,alpha)
himpunan_produk.append(R14)
# [15] if suhu NORMAL, kebisingan AGAK BISING, cahaya TERANG => JML PRODUK = 147.63 (BERTAMBAH)
alpha = (min(b,e,i))
a_predikat.append(alpha)
rata = jml_produk[14]
R15 = prod_bertambah(rata,alpha)
himpunan_produk.append(R15)
# [16] if suhu NORMAL, kebisingan BISING, cahaya REDUP => JML PRODUK = 141.47 (AGAK BERTAMBAH)
alpha = (min(b,f,g))
a_predikat.append(alpha)
rata = jml_produk[15]
R16 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R16)
# [17] if suhu NORMAL, kebisingan BISING, cahaya AGAK TERANG => JML PRODUK = 145.67 (AGAK BERTAMBAH)
alpha = (min(b,f,h))
a_predikat.append(alpha)
rata = jml_produk[16]
R17 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R17)
# [18] if suhu NORMAL, kebisingan BISING, cahaya TERANG => JML PRODUK = 140.2 (BERKURANG)
alpha = (min(b,f,i))
a_predikat.append(alpha)
rata = jml_produk[17]
R18 = prod_berkurang(rata,alpha)
himpunan_produk.append(R18)

# [19] if suhu TINGGI, kebisingan TENANG, cahaya REDUP => JML PRODUK = 142.10 (AGAK BERTAMBAH)
alpha = (min(c,d,g))
a_predikat.append(alpha)
rata = jml_produk[18]
R19 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R19)
# [20] if suhu TINGGI, kebisingan TENANG, cahaya AGAK TERANG => JML PRODUK = 146.53 (BERTAMBAH)
alpha = (min(c,d,h))
a_predikat.append(alpha)
rata = jml_produk[19]
R20 = prod_bertambah(rata,alpha)
himpunan_produk.append(R20)
# [21] if suhu TINGGI, kebisingan TENANG, cahaya TERANG => JML PRODUK = 142.17 (AGAK BERTAMBAH)
alpha = (min(c,d,i))
a_predikat.append(alpha)
rata = jml_produk[20]
R21 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R21)
# [22] if suhu TINGGI, kebisingan AGAK BISING, cahaya REDUP => JML PRODUK = 138.7 (BERKURANG)
alpha = (min(c,e,g))
a_predikat.append(alpha)
rata = jml_produk[21]
R22 = prod_berkurang(rata,alpha)
himpunan_produk.append(R22)
# [23] if suhu TINGGI, kebisingan AGAK BISING, cahaya AGAK TERANG => JML PRODUK = 141.4 (AGAK BERTAMBAH)
alpha = (min(c,e,h))
a_predikat.append(alpha)
rata = jml_produk[22]
R23 = prod_agakBertambah(rata,alpha)
himpunan_produk.append(R23)
# [24] if suhu TINGGI, kebisingan AGAK BISING, cahaya TERANG => JML PRODUK = 138.3 (BERKURANG)
alpha = (min(c,e,i))
a_predikat.append(alpha)
rata = jml_produk[23]
R24 = prod_berkurang(rata,alpha)
himpunan_produk.append(R24)
# [25] if suhu TINGGI, kebisingan BISING, cahaya REDUP => JML PRODUK = 133.33 (BERKURANG)
alpha = (min(c,f,g))
a_predikat.append(alpha)
rata = jml_produk[24]
R25 = prod_berkurang(rata,alpha)
himpunan_produk.append(R25)
# [26] if suhu TINGGI, kebisingan BISING, cahaya AGAK TERANG => JML PRODUK = 138.33 (BERKURANG)
alpha = (min(c,f,h))
a_predikat.append(alpha)
rata = jml_produk[25]
R26 = prod_berkurang(rata,alpha)
himpunan_produk.append(R26)
# [27] if suhu TINGGI, kebisingan BISING, cahaya TERANG => JML PRODUK = 133.77 (BERKURANG)
alpha = (min(c,f,i))
a_predikat.append(alpha)
rata = jml_produk[26]
R27 = prod_berkurang(rata,alpha)
himpunan_produk.append(R27)

# ********************** DEFUZZYFIKASI ********************
print("\n")
a_predikat_x_produk = 0
total_a_predikat = 0
z = 0 

for i in range(27):
    a_predikat_x_produk += a_predikat[i]*himpunan_produk[i]
    total_a_predikat += a_predikat[i]
print(f"total a_pred*produk: {a_predikat_x_produk}")
print(f"total a_predikat: {total_a_predikat}")

# ********************** CRISP OUTPUT ********************
if total_a_predikat == 0:
    print("nilai fuzzy undefined")
else:
    z = a_predikat_x_produk / total_a_predikat
    z_2dig = "{:.2f}".format(z)
    print(f"fuzzy out: {z_2dig}")
