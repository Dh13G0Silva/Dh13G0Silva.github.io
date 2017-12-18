from datetime import datetime
import os


# Nome da Postagem
Name = raw_input("Name of Post:")  
# para ver o que quer basta colocar now.year = mes now.month = mes now.day=dia 
now = datetime.now()
Title= raw_input ("Title of Post:")
Tag= raw_input ("Tag of Post")


#Ano Mes e Dia 
year  = now.year
month = now.month
day   = now.day 
# Criando o Arquivo na pasta _post
Result = ("%s-%s-%s-%s" %(year, month, day, Name))
print ("Como ficou %s"%(Result))
#--------------------------------------------------------
named = "/home/rvbk/Documents/MySite/Dh13G0Silva.github.io/_posts/%s.markdown" %(Result)
file = open(named ,"w") 
file.write('---')
file.write("layout: post\n") 
file.write("title:  %s\n"%(Title)) 
file.write("date:   %s-%s-%s\n"%(year, month, day)) 
file.write("tags:   %s\n"%(Tag)) 
file.write('---')
file.close() 
