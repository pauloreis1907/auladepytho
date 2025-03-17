def bolo(ingre ) :
    ingre= {"leite","ovo","manteiga","trigo"}
    ingreFaltando = ingre - set (ingre)
    if not ingreFaltando:
        return('todos os igredientes são nessarios')
    else:
        return('falta os seguintes igredientes',ingreFaltando)
    
    
bolo(ingre)