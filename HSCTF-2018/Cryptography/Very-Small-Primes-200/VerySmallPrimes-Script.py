'''
Finds p for N in RSA
Use if you're sure if p is relatively small
like 1 billion
'''

def factor(n):
    divisor = 3
    while True:
        if n%divisor == 0:
            print(divisor)
            print(n/divisor)
            break
        else:
            divisor+=2

print(factor(14737982625692236883087884385477907892017737821331862905021012977397735541782338859698129302010693627216960630032813261034175977953200437258123520065400601663247081499548941721335073455526493638219346114513439467057032843535731310550410416439954955643369237696321002025846503846765779372144196710544056798390715404973259683864868914402328771953034500206465975484440004818637123229904793547478358458658372755948173646593967065752907055568319575296612158337946950953335205333932581536201324056484084754034973906648480463297955872984049316474953094369926868960034276541817895218108550574360300087122784055645636563344999))
