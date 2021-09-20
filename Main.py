print("Hola bienvenido")
print("Lista de comandos = /help")

while True:
    ComandoUser = input(">>> ")

    if ComandoUser == "/help":
        print("""Lista de Comandos:
        /vers --> Versión
        /help --> Lista de Comandos
        /exit --> Salir del programa""")
    elif ComandoUser == "/txt":
        NombreArchivo = input("Nombre del archivo >>> ")
        CuerpoArchivo = input(">>> ")
    elif ComandoUser == "/vers":
        print("Versión 1.0 by Ricardo Ocaña")
    
    elif ComandoUser == "/exit":
        break
    else:
        print("Syntax error")
print("Hasta luego")