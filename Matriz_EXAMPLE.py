rows = 0
cols = 0
teclado = []

#LEER EL ARCHIVO
fil=open("/Users/nglrp/OneDrive/Escritorio/Programación/Taller/text.txt", "r")
if fil.mode == 'r':
    #obtener el contenido
    lines =fil.readlines()
    c = 1
    l = 0
    #recorrer los renglones
    for line in lines:

        #encontrar el primer renglón
        if c == 1:
            row_col = line.split(' ')
            print(row_col[0], ' - ' , row_col[1])
            rows = int(row_col[0])
            cols = int(row_col[1])
        
        #encontrar las letras del teclado
        if c > 1 and c <= (rows+1):
            letters = list(line)
            letters.pop()
            teclado.append(letters)

        if c == (rows + 2):
            word = list(line)
            
        c+=1
     
print(teclado)
for x in word:
    letter = word[x]
    for a in rows:
        for b in cols:
            if teclado[b,a] == letter:
                
            b +=1
print (word)
