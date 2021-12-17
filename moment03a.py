lön = int(input("skriv/ange din månadslön: ")) 


#Landstingsskatt är 11, 48% 
landstigns_skatt = 0.1148 

#Kommunalskatt är 21.36% 
kommunal_skatt = 0.2136 



print("utskrift:")  

print("månadslön", lön, "kronor") 

print("kommunalskatt", int(lön * kommunal_skatt), "kronor")  

print("landstingsskatt", int(lön * landstigns_skatt), "kronor") 


#Variabler 
kvar_efter_förstaskatt = lön * landstigns_skatt 
kvar_efter_andraskatt = lön * kommunal_skatt 
kvar_efter_tredjeskatt = kvar_efter_förstaskatt + kvar_efter_andraskatt 
kvar_efter_fjärdeskatt = lön - kvar_efter_tredjeskatt  

print("Kvar efter SKATT!!" , int(kvar_efter_fjärdeskatt), "kronor")  

