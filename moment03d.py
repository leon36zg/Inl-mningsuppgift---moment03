lön = int(input("skriv/ange din månadslön: ")) #lön från början 

landstigns_skatt = 0.1148

kommunal_skatt = 0.2136 

#Årslön 
årslön = lön * 12  

#Statlig skatt
statlig_skatt = 0.25 


print("Utskrift:") 

print("Månadslön", lön, "kronor", "(Årslön:", årslön, "kronor)") 

#if-sats
if årslön < 19257.00: 
    print("Du behöver inte betala skatt")   

else: 
    print("Kommunalskatt", int(lön * kommunal_skatt), "kronor") 
    print("Landstingsskatt", int(lön * landstigns_skatt), "kronor") 


if årslön > 468700.00: 
    print("Statlig skatt!!", int(lön * statlig_skatt), "kronor")  


#Variabler 
kvar_efter_förstaskatt = lön * landstigns_skatt 
kvar_efter_andraskatt = lön * kommunal_skatt  
kvar_efter_tredjeskatt = lön * statlig_skatt
kvar_efter_fjärdeskatt = kvar_efter_förstaskatt + kvar_efter_andraskatt + kvar_efter_tredjeskatt 
kvar_efter_femteskatt = lön - kvar_efter_fjärdeskatt  


if lön < 19247: 
    print("Kvar efter SKATT!!" , int(lön), "kronor")  


else: 
    print("Kvar efter SKATT!!" , int(kvar_efter_fjärdeskatt), "kronor") 

total_skatt = lön - kvar_efter_femteskatt 

if lön > 19247.00: 
    print("Total skatt", int(kvar_efter_fjärdeskatt), "kronor") 

#Variabler bruttoskatt
bruttoskatt_ett = total_skatt/lön 
bruttoskatt_två = bruttoskatt_ett * 100 

if lön > 19247: 
    print("Andel av betald skatt", float(bruttoskatt_två), "%") 

