print("_________________________________________________________________________") 
print("""
Problem Statement :- During trial at single cylinder of a 4-stroke petrol engine
having diameter 600mm and stroke length is 400 mm.Mean effective pressure is 6
bar and torque is 407N-m.Speed is 250 rpm at consumption of 4kg/hr and calorific
value is 43000 Kj/hr.cooling water rate is 4.5 kg/min.air used per kg of fuel is
30 kg.The rise in cooling water temp is 45°c and tempreture at exhaust is 420°c
and room tempreture is 20°c.specific heat of water and air is 4.187 and 1 resp.
find brake power ,indicated power amd draw heat balance sheet.""")
print("_________________________________________________________________________")

print("Solution:")
#Given

d=int(input("Bore Diameter=")) # mm 
l=int(input("Length of stroke="))# mm
mep=float(input("Mean Effective pressure=")) # bar
n=int(input("Speed=")) #RPM
cv=int(input("Calorific value=")) #KJ/KG
ma=int(input("Mass of air=")) #kg
mf=int(input("mass of fuel=")) #Kg 
t=int(input("Torque=")) #N/m
cpw=float(input("Specific heat of water=")) 
cpg=float(input("Specific heat of gas="))

print("_________________________________________________________________________")
bp=(2*3.14*n*t)/60000  #Brake Power 
print("•)Brake Power={:0.2f}".format(bp),"KW")

Q=mf*cv
print("•)Heat Supplied to Engine={:0.2f}".format(Q),"KJ/hr") 

print("_________________________________________________________________________")
Q1=((2*3.14*n*t)/60000)*3600
print("1)Heat to the Brake Power={:0.1f}".format(Q1),"KJ/hr")

mw=float(input("mass of water ="))
temp=int(input("Tempreture difference=")) #°C

Q2=mw*60*cpw*temp
print("2)Heat Rejection in cooling tower={:0.1f}".format(Q2),"KJ/hr")

mg=ma+1
print("Mass of flue gases=",mg,"kg/kg of fuel")
mg1=mg*mf
print(mg1,"kj/kg")
tg=int(input("Tempreture of exhaust gases="))
ta=int(input("Tempreture of room tempreture="))

Q3=mg1*cpg*(tg-ta)
print("3)Heat carried by dry flue gases={:0.1f}".format(Q3),"KJ/hr")

Q4=Q-(Q1+Q2+Q3)
print("4)Unaccounted heat rejection={:0.1f}".format(Q4),"KJ/hr")

print("_________________________________________________________________________")
Total=Q1+Q2+Q3+Q4
print("Total Heat rejection=",Total,"kj/hr")
print("_________________________________________________________________________")

q1=(Q1/Q)*100
print("1)Heat to Brake Power={:0.2f}".format(q1),"%")

q2=(Q2/Q)*100
print("2)Heat rejection in cooling tower={:0.2f}".format(q2),"%")

q3=(Q3/Q)*100
print("3)Heat carried by dry flue gases={:0.2f}".format(q3),"%")

q4=(Q4/Q)*100
print("4)Unaccounted heat rejection={:0.2f}".format(q4),"%")

print("_________________________________________________________________________")

E=q1+q2+q3+q4
print("Total percentage of heat rejection=",E,"%")

print("_________________________________________________________________________")
