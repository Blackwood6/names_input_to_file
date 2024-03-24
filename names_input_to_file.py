
# "Enter a list of names separated by commas"
# demander au user d'entrer une liste de nom separer par une virgule
# 

n = input("Enter a list of username or names separated by a commas :")

# split the string to a list using a commas 

list_n = n.split(',')

# create or open the file name.txt in w mode

with open('names.txt', 'w') as fichier:
	# write each name of the list on a single line in the file
	for x in list_n:
		fichier.write(x.strip() + '\n')


print("Names succesfully added to names.txt.")

#author : Jerome Gee aka blackwood
# Junior Pentester 

#instagram : guevar00
#linkedIn : https://www.linkedin.com/in/guevar00-b30985291/
#twitter aka X : https://twitter.com/5PMGHOST