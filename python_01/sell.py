lists=[]
priceAll = 0
while True:
    dct = {}

    dct['prodCode'] = input('제품코드 입력 => ')
    if dct['prodCode'] == "exit":
        break
    dct['prodName'] = input('제품명 입력 => ')
    dct['count'] = int(input('수량 입력 => '))
    dct['price'] = int(input('단가 입력 => '))
    dct["total"] = dct['count'] * dct['price']

    lists.append(dct)

    priceAll += dct['total']



print("\n\t\t *** 상품정보 ***")
print("====================================")
print("제품코드   제품명    수량    단가    판매금액")
print("====================================")
for list in lists:
    print("%s    %3s    %2d    %3d    %2d" %(list['prodCode'],list['prodName'],list['count'],list['price'],list['total']))
print("====================================")
print("\t\t\t\t\t총금액 : %2d" %(priceAll))
