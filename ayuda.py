
def letrasproposicionales(listafilas,listacolumna):
    cosito=[]
    for s in listafilas:
        for c in listacolumna:
            cosito.append(s+c)
    return cosito



def reglafilas (letrasproposicionales,listafilas,diccionario):
    relgam=""
    for h in listafilas:
        aux=[x for x in letrasproposicionales if x[1]=='1']
        if diccionario[h]==[1,1]:
            reglam=aux[0]+aux[1]+"~"+aux[2]+"YY"
        elif diccionario[h]==[3]:
            reglam=aux[0]+aux[1]+aux[2]
        elif diccionario[h]==[0]:
            reglam=aux[0]+"~"+aux[1]+"~"+aux[2]+"~YY"
        elif diccionario[h]==[1]:
            reglam=aux[0]+aux[1]+"~"+aux[2]+"~"+"YY"+aux[0]+"~"+aux[1]+aux[2]+"~YY"+aux[0]+"~"+aux[1]+"~"+aux[2]+"YYOO"
        elif diccionario[h]==[1]:
            reglam=aux[0]+"~"+aux[1]+aux[2]+"YY"+aux[0]+aux[1]+aux[2]+"~YYV"
    return reglam

def reglascolumnas(letrasproposicionales,listacolumnas,diccionario):
    reglan=""
    for k in listacolumnas:
        aux2=[y for y in letras porposicionales if y[1]=='1']
        if diccionario[k]==[1,1]:
                reglan=aux2[]+aux2[]+"~"+aux2[]+"YY"
        elif diccionario[k]==[3]:
            reglam=aux[]+aux[]+aux[]
        elif diccionario[k]==[0]:
            reglam=aux[]+"~"+aux[]+"~"+aux[]+"~YY"
        elif diccionario[k]==[1]:
            reglam=aux[]+aux[]+"~"+aux[]+"~"+"YY"+aux[]+"~"+aux[]+aux[]+"~YY"+aux[]+"~"+aux[]+"~"+aux[]+"YYOO"
        elif diccionario[k]==[1]:
            reglam=aux[]+"~"+aux[]+aux[]+"YY"+aux[]+aux[]+aux[]+"~YYV"
    return reglam

listafilas=['A','B','C']
listacolumnas=['1','2','3']
diccionario={"A":[1,1],"B":[3],"C":[0],"1":[2],"2":[1],"3":[2]}
letras = letrasproposicionales(listafilas, listacolumna)
#print(letras)
prueba=reglafilas(letras,listafilas,diccionario)
#print(prueba)
