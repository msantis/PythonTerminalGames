import os,random


# Función borrar pantalla
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# funcion para ubicar el cursor en la pantalla
def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def marco(x1,y1,x2,y2):
    for i in range(x1,x2):
        gotoxy(i,y1)
        print("═")
    
    for i in range(x1,x2):
        gotoxy(i,y2)
        print("═")

    for i in range(y1,y2):
        gotoxy(x1,i)
        print("║")
    
    for i in range(y1,y2):
        gotoxy(x2,i)
        print("║")
    gotoxy(x1,y1)
    print("╔")
    gotoxy(x2,y1)
    print("╗")
    gotoxy(x1,y2)
    print("╚")
    gotoxy(x2,y2)
    print("╝")

def dibujar_soga(intentos_restantes):
    dibujo = [
        """
         ▄▄▄▄▄▄▄▄▄
         █/
         █
         █
         █
         █
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █
         █
         █
         █
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █      O
         █
         █
         █
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █      O
         █      ┼
         █
         █
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █      O
         █    └─┼
         █
         █
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █      O
         █    └─┼─┘
         █
         █
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █      O
         █    └─┼─┘
         █     ┌┼
         █     │
         █
        ▄█▄
        """,
        """
         ▄▄▄▄▄▄▄▄▄
         █/     │
         █      0
         █    ┌─┼─┐
         █     ┌┼┐
         █     │ │
         █
        ▄█▄
        """
    ]
    return dibujo[7 - intentos_restantes]

def tablero_init(palabra_secreta):
    temp=""
    for i in range(0,len(palabra_secreta)):
        temp=temp+"-"
    return temp

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    palabra = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra=palabra+letra
        else:
            palabra=palabra+"-"
    return palabra

def contar_letras(palabra):
    numero=0 
    for letra in palabra:
        if letra.isalpha():
            numero=numero+1
    return numero


# Código Principal
if __name__ == '__main__':
    base=[
        "LIBRO", "TELEFONO", "RELOJ", "ORDENADOR", "BOLIGRAFO", "CUADERNO", "SILLA", "MESA", "LAMPARA", 
        "TELEVISOR", "VASO", "PLATO", "TENEDOR", "CUCHILLO", "TAZA", "TETERA", "CAMARA", "BOLSA", 
        "BOTELLA", "MALETIN", "PERRO", "GATO", "ELEFANTE", "JIRAFA", "LEON", "TIGRE", "OSO", "MONO", 
        "GORILA", "ORANGUTAN", "CABALLO", "VACA", "CERDO", "OVEJA", "CABRA", "CONEJO", "RATON", 
        "HAMSTER", "ARDILLA", "CARRO", "MADRID", "PARIS", "LONDRES", "MEDELLIN", "TOKIO", 
        "MOSCU", "BERLIN", "ROMA", "PEKIN", "SIDNEY", "AMSTERDAM", "LONDRES", "WASHINGTON", 
        "OTTAWA", "BANGKOK", "DUBAI", "SIDNEY", "PEKIN", "ESPAÑA", "FRANCIA", "ITALIA", "ALEMANIA", 
        "RUSIA", "CHINA", "JAPON", "BRASIL", "ARGENTINA", "CANADA", "COLOMBIA", "AUSTRALIA", 
        "MEXICO", "INDIA", "SUDAFRICA", "EGIPTO", "PERU", "CHILE", "CUBA", "COREA","INDIA"
    ]

    palabra_secreta=random.choice(base)
    tablero=tablero_init(palabra_secreta)
    letras_adivinadas=[]
    num_letras_adivinadas=0
    intentos=7
    while True:
        cls()
        tablero=mostrar_tablero(palabra_secreta,letras_adivinadas)
        num_letras_adivinadas=contar_letras(tablero)
        #print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
        marco(20,2,60,4)
        gotoxy(33,3)
        print("Juego Ahorcado")
        gotoxy(1,10)
        print(dibujar_soga(intentos))
        marco(4,9,25,22)
        gotoxy(6,20)
        print(f"Quedan {intentos} intentos")
    
        # Dibujar Tablero
        marco(30,9,70,16)
        gotoxy(40,11)
        print(tablero)
        gotoxy(33,13)
        print(f"Haz adivinado {num_letras_adivinadas} letras de {len(palabra_secreta)}")
        marco(30,18,70,20)

        # Verifica si aun quedan intentos
        if intentos==0:
            gotoxy(32,19)
            print("¡No tienes mas intentos!")
            gotoxy(1,24)
            marco(30,22,70,24)
            gotoxy(32,23)
            print(f"¡Fin del Juego! - {palabra_secreta}")
            gotoxy(1,26)
            break
        
        # Verifica si ya se ha adivinado la palabra
        if tablero==palabra_secreta:
            gotoxy(32,19)
            print("Haz Adivinado la Palabra")
            gotoxy(1,24)
            marco(30,22,70,24)
            gotoxy(32,23)
            print("¡Fin del Juego!")
            gotoxy(1,26)
            break

        gotoxy(32,19)
        intento_letra=input("Introduzca una letra: ").upper()
        
        if intento_letra in letras_adivinadas:
            marco(30,22,70,24)
            gotoxy(32,23)
            print("Ya has intentado esa letra.")
            pause=input()
            continue
        elif len(intento_letra) != 1 or not intento_letra.isalpha():
            marco(30,22,70,24)
            gotoxy(32,23)
            print("Ingresa una sola letra válida.")
            pause=input()
            continue
        
        letras_adivinadas.append(intento_letra)

        if intento_letra in palabra_secreta:
            marco(30,22,70,24)
            gotoxy(32,23)
            print("¡Bien! Has adivinado una letra.")
            pause=input()
        else:
            marco(30,22,70,24)
            gotoxy(32,23)
            print("Esa letra no está en la palabra.")
            intentos = intentos-1
            pause=input()
