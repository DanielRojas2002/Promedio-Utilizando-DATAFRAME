import matplotlib.pyplot as plt
import pandas as pd

def Promedio(lista_de_listas,materias):
    listapromedio=[]
    listanivel=[]
    
    print(separador)
    print("1=Quiero saber el promedio de todos los alumnos\n2=Quiero saber el promedio del grupo")
    menu=int(input(":"))
    print(separador)
    promedioFinal=0
    listaP=[]
    if menu==1:
        contadorAl=0
        for nivel in lista_de_listas:
            suma=0
            contadorAl+=1
            for elemento in nivel:
                suma=suma+elemento
            promedio=suma/materias
            listapromedio.append(promedio)
            diccionario["Promedio"]=listapromedio
            listaP.append(promedio)
            print(f"El promedio del alumno {contadorAl} es: {promedio}")
            print(separador)
           
        print("1=SI\n2=NO")
        submenu=int(input("Quieres Graficar lo promedio de todos los Alumnos : "))
        valores=[]
        alumnos2=[]
        print(separador)
            
        if submenu==1:
            
            colores=["red","green"]
            
            for promedio in listaP:
                valores.append(promedio)
            print(separador)
                
            for nombre in range(1,contadorAl+1):
                nom="alumno"
                alumnos=(f"{nom}{nombre}")
                alumnos2.append(alumnos)
            
            
            plt.grid(True)
            plt.xlabel("Alumnos:")
            plt.ylabel("Promedio de Alumno:")
            plt.title("PROMEDIO")    
            plt.bar(alumnos2,height=valores,color=colores,width=0.5)
            plt.show()
                
                
    
    elif menu==2:
        contadorAl=0
        for nivel in lista_de_listas:
            suma=0
            contadorAl+=1
            for elemento in nivel:
                suma=suma+elemento
            promedio=suma/materias
            listapromedio.append(promedio)
            diccionario["Promedio"]=listapromedio
            
            listaP.append(promedio)
            
            promedioFinal=promedioFinal+promedio
        promFinal=promedioFinal/contadorAl
        diccionario["Promedio Grupal"]=promFinal
        print(separador)
        print(f"Promedio Grupal :{promFinal}")
        print(separador)
        
        
        print("1=SI\n2=NO")
        submenu=int(input("Quieres Graficar el Promedio Grupal con el Promedio Individual : "))
        print(separador)
        valores=[promFinal]
        texto=["Promedio Grupal"]
            
        if submenu==1:
            colores=["yellow","orange","blue"]
            
            for promedio in listaP:
                valores.append(promedio)
            print(separador)
                
            for nombre in range(1,contadorAl+1):
                nom="alumno"
                alumnos=(f"{nom}{nombre}")
                texto.append(alumnos)
            
            plt.grid(True)
            plt.xlabel("Alumnos:")
            plt.ylabel("Promedio de Alumno:")
            plt.title("PROMEDIO")       
            plt.bar(texto,height=valores,color=colores,width=0.5)
            plt.show()


diccionario={}
opcion=1
listanombre=[]
notas=[]
contador=1
while opcion==1:
    separador=("*"*40)
    lista_de_listas=[]
    contadorMate=0
    contadorA=0
    listadelistas=[]
    print("*"*20,"Menu Principal","*"*20)
    alumnos=int(input("Cuantos alumnos son : "))
    materias=int(input("Cuantas Materias llevan : "))
    print(separador)
    for alumno in range(alumnos):
        contadorA+=1
        nombre=input("Nombre del Alumno: ")
        listanombre.append(nombre)
        listaNota=[]
        lista_de_listas.append(listaNota)
        contadorMate=0
        for materia in range(materias):
            contadorMate+=1
            nota=int(input(f"Calificacion {contadorMate} : "))
            print(separador)
            notas.append(nota)
            listaNota.append(nota)
            
           
    indice=0
    if alumnos==materias:
        for alumno in range (materias):
            diccionario[f"Calificacion{contador}"]=notas[indice::materias]
            contador=contador+1
            indice=indice+1
            
    elif alumnos<materias:
        for alumno in range (materias):
            diccionario[f"Calificacion{contador}"]=notas[indice::materias]
            contador=contador+1
            indice=indice+1
        
    elif alumnos>materias:
        for alumno in range (materias):
            diccionario[f"Calificacion{contador}"]=notas[indice::materias]
            contador=contador+1
            indice=indice+1
        
    Promedio(lista_de_listas,materias)
    print("1=SI\n2=NO")
    opcion=int(input("Quieres seguir con el programa : "))


dic=pd.DataFrame(diccionario)
dic.index=[listanombre]
print(dic)