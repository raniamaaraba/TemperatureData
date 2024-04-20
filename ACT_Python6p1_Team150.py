# Activity Python 3: Task 1
# File: ACT_Python_HeaderTemplate_Team150_maarabrn.py 
# Date:    1 24 2024
# By:      Rania Maaraba
# Section: 09
# Team:    150
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# 

tempdata = open('TempC.txt','r')
tempF = open('TempF.txt', 'w')

List = tempdata.readlines()


for i in range(len(List)):
    List[i]= float(List[i])
    
F = []

for i in range(len(List)):
    eq = 9/5*List[i]+32
    F.append(eq)
    
print(List)
print(F)

for i in range (len(F)):
    tempF.write('{0:0.02f}\n'.format(F[i]))
tempF.close()


    


#eq = 5/9(List -32)
##tempF.write("5/9(List-32)\n".format(List))


tempdata.close()
tempF.close()


