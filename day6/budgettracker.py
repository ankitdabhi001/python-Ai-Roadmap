transac=[]

def tracolum(amount,type,category):
    transac.append(
        {"amount":amount,
         "type":type,
         "category":category
         })

def balance():
    income=sum(b["amount"] for b in transac if b["type"]=="income")
    expen=sum(a["amount"] for a in transac if a["type"]=="expense")
    balance=income-expen

    print(f"\n💰 Total Income: ₹{income}")
    print(f"total expense : ₹{expen}")
    print("total balance is :",balance)

def history():
    print("Your Money history:")
    for i,t in enumerate(transac,1):
            print(f"{i}.{t['type']},{t['amount']},{t['category']}")


tracolum(750,"expense","food")
tracolum(1000,"income","salary")
# print(transac)

balance()
history()