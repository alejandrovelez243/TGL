
def funcion_desde_case():
    print("ENTRE a funcion desde case")

def funcion_con_match(code):
    match code:
        case 300:
            print("Entre a 300")
        case 200:
            print("Entre a 200")
        case 400:
            funcion_desde_case()
        case _:
            print("Case por defecto")


funcion_con_match(400)
