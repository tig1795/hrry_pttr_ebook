

# read input file
fin = open("../02_Ebook/text/01_Harry Potter und der Stein der Weisen.txt", "rt", encoding='utf-8')
# read file contents to string
data = fin.read()
# replace all occurrences of the required string
data = data.replace('FÃ¼r', 'Für')
# close the input file
fin.close()
# open the input file in write mode
fin = open("../02_Ebook/text/01_Harry Potter und der Stein der Weisen.txt", "wt", encoding='utf-8')
# overrite the input file with the resulting data
fin.write(data)
# close the file
fin.close()
