def main():
    while True:
        print('Menu'.center(50,'*'))
        secim = input('1- Add Medicine \n2- Get Medicines\n3- Exit\n ')
        if secim == '3':
            break
        else:
            if secim == '1':
                inputAdd()
            elif secim == '2':
                getMedicine()
            else:
                print('wrong choice')
        
def inputAdd():
    medName= input( "Name:") 
    medPrice= input( "Price:") 
    onSale= input( "On sale:") 
    addMedicine(medName,medPrice,onSale)

def addMedicine(name,price,sale):
    meds=[]
    med = {
        "medName": name,
        "price": price,
        "sale": sale,
    }
    meds.append(med)
    import json
    with open("medicines.json","w") as file:
        json.dump(meds,file,ensure_ascii=False,indent=2)


def getMedicine():
    import json
    with open("medicines.json") as file:
        meds = json.load(file)
    print(meds)

main()
