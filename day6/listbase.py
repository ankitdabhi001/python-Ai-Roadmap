# list based data processor

def data_processor(data):

    if not data:
        print("no datta found")
        return
    
    total=sum(data)
    minimum=min(data)
    maximum=max(data)

    print(f"your total is : {total}")
    print(f"your minimum is : {minimum}")
    print(f"your maximum is: {maximum}")

    top3=sorted(data,reverse=True)[:3]
    print(f"top 3 is here : {top3}")


dataw=[1200, 1500, 1100, 1800, 1600, 1700, 1250, 1400, 1550, 1650]

data_processor(dataw)