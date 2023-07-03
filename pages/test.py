l = ["a","b","c"]
nama = ['endang','sukijem','larry']
no = ['00','01','02']
p = {}
o = 0
for x,y in zip(nama,no) :
    p[f"data{o}"]= {'nama': x,'no': y}
    o += 1

print(p)
print(p.get("data0"))