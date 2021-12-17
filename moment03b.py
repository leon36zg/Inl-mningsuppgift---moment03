lön = int(input("skriv/ange din månadslön: ")) 

landstigns_skatt = 0.1148

kommunal_skatt = 0.2136 

årslön = lön * 12 



print("Utskrift:") 

print("Månadslön", lön, "kronor", "(årslön:", årslön, "kronor)" ) 

#if-sats
if årslön < 19257.00: 
    print("Du behöver inte betala skatt")  


else: 
    print("Kommunalskatt", int(lön * kommunal_skatt), "kronor") 
    print("Landstingsskatt", int(lön * landstigns_skatt), "kronor") 

#Variabler
kvar_efter_förstaskatt = lön * landstigns_skatt 
kvar_efter_andraskatt = lön * kommunal_skatt 
kvar_efter_tredjeskatt = kvar_efter_förstaskatt + kvar_efter_andraskatt 
kvar_efter_fjärdeskatt = lön - kvar_efter_tredjeskatt  


if lön < 19247: 
    print("Kvar efter SKATT!!" , int(lön), "kronor")  


else: 
    print("Kvar efter SKATT!!" , int(kvar_efter_fjärdeskatt), "kronor")   

