# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 21:47:42 2019

@author: jotas
"""

import random
import pandas as pd
import operator
import copy


def Clasificatoria(p1,p2,p3,p4):
    
    global clasificado1
    global clasificado2
    
    grupo = [p1, p2, p3, p4]
    
    resultados = {"Resultados" : ["JJ", "G", "P", "E", "GF", "GC", "Puntos"]}
    
    for pais in grupo:
        
        resultados[pais] = []
   
    resultados = {"Primera Ronda " : copy.deepcopy(resultados),
                      "Segunda Ronda " : copy.deepcopy(resultados),
                      "Tercera Ronda " : copy.deepcopy(resultados)}
    
    def CajitaGoles(a,b,ronda):
    
        goles1 = random.choice(range(0,5))
        goles2 = random.choice(range(0,5))
    
        if goles1 == goles2:
            print('Empate',grupo[a],':',goles1,'vs',goles2,':',grupo[b])
                    
            resultados[ronda][grupo[a]] = [1,0,0,1,goles1,goles2,1]
            resultados[ronda][grupo[b]] = [1,0,0,1,goles2,goles1,1]
    
        elif goles1 > goles2:
            print('Ha ganado',grupo[a],':',goles1,'vs',goles2,':',grupo[b])
            
            resultados[ronda][grupo[a]] = [1,1,0,0,goles1,goles2,3]
            resultados[ronda][grupo[b]] = [1,0,1,0,goles2,goles1,0]
    
        else:
            print('Ha ganado',grupo[b],':',goles2,'vs',goles1,':',grupo[a])
            
            resultados[ronda][grupo[a]] = [1,0,1,0,goles1,goles2,0]
            resultados[ronda][grupo[b]] = [1,1,0,0,goles2,goles1,3]
    
    
    print('========== primera ronda ==========')
    CajitaGoles(0,1, "Primera Ronda ")
    CajitaGoles(2,3, "Primera Ronda ")
    
    print()
    print('========== segunda ronda ==========')
    CajitaGoles(1,2, "Segunda Ronda ")
    CajitaGoles(3,0, "Segunda Ronda ")
    
    print()
    print('========== tercera ronda ==========')
    CajitaGoles(0,2, "Tercera Ronda ")
    CajitaGoles(3,1, "Tercera Ronda ")
    
   
    ResultadoTotal = {"" : ["JJ", "G", "P", "E", "GF", "GC", "Puntos"]}
    
    for pais in grupo:
        ResultadoTotal[pais] = []
        for i in range(7):
            
            ResultadoTotal[pais].append(resultados["Primera Ronda "][pais][i] + 
                          resultados["Segunda Ronda "][pais][i] + 
                          resultados["Tercera Ronda "][pais][i])
    
    print()
    del ResultadoTotal[""]
    ResultadoTotal1 = pd.DataFrame(ResultadoTotal,  index = ['JJ', 'G', 'P', 'E', 'GF', 'GC', 'Puntos']).sort_values(by=['Puntos','GC','GF'], ascending=False, axis = 1)
    print((ResultadoTotal1).T)                               
                                    
    
    listapais = []
    
    for key in ResultadoTotal.keys():
        listapais.append(key)
    
    
    listaPuntos = []
    
    for values in ResultadoTotal.values():
        listaPuntos.append(values[6])
    
    
    listaGf = []
    
    for values in ResultadoTotal.values():
        listaGf.append(values[4])
    
    
    listaGc = []
    
    for values in ResultadoTotal.values():
        listaGc.append(values[5])
    
    
    D3={listapais[0]:listaPuntos[0],
        listapais[1]:listaPuntos[1],
        listapais[2]:listaPuntos[2],
        listapais[3]:listaPuntos[3]}
    
    
    D4={listapais[0]:listaGc[0],
        listapais[1]:listaGc[1],
        listapais[2]:listaGc[2],
        listapais[3]:listaGc[3]}
    
    
    D5={listapais[0]:listaGf[0],
        listapais[1]:listaGf[1],
        listapais[2]:listaGf[2],
        listapais[3]:listaGf[3]}
    
    
    ordD3values = sorted(D3.items(),
                         key = operator.itemgetter(1),
                         reverse = True)
    
    
    if ordD3values[0][1] != ordD3values[1][1]:
        
        clasificado1 = ordD3values[0][0]
        
        if ordD3values[1][1] != ordD3values[2][1]:
            
            clasificado2=ordD3values[1][0]
        
        elif ordD3values[1][1] == ordD3values[2][1]:
        
            if D4[ordD3values[1][0]] > D4[ordD3values[2][0]]:
                
                clasificado2 = ordD3values[2][0]
                
            elif D4[ordD3values[1][0]] < D4[ordD3values[2][0]]:
                
                clasificado2 = ordD3values[1][0]
                    
            else:
                        
                if D5[ordD3values[1][0]] > D5[ordD3values[2][0]]:
                
                    clasificado2 = ordD3values[1][0]
                            
                elif D5[ordD3values[1][0]] < D5[ordD3values[2][0]]:
                
                    clasificado2 = ordD3values[2][0]
        
    if ordD3values[0][1] == ordD3values[1][1] and ordD3values[1][1] != ordD3values[2][1]:
        
        if D4[ordD3values[0][0]] > D4[ordD3values[1][0]]:
            
            clasificado1 = ordD3values[1][0]
            clasificado2 = ordD3values[0][0]
            
            
        elif D4[ordD3values[0][0]] < D4[ordD3values[1][0]]:
            
            clasificado1 = ordD3values[0][0]
            clasificado2 = ordD3values[1][0]
            
            
        else:       
            if D5[ordD3values[0][0]] > D5[ordD3values[1][0]]:
                
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[1][0]
                
            elif D5[ordD3values[0][0]] < D5[ordD3values[1][0]]:
                
                clasificado1 = ordD3values[1][0]
                clasificado2 = ordD3values[0][0]
                
    
    if ordD3values[0][1] == ordD3values[1][1] == ordD3values[2][1]:
        
        if D4[ordD3values[2][0]] > D4[ordD3values[1][0]] >  D4[ordD3values[0][0]]:
            
            clasificado1 = ordD3values[0][0]
            clasificado2 = ordD3values[1][0]
            
        if D4[ordD3values[0][0]] > D4[ordD3values[2][0]] >  D4[ordD3values[1][0]]:
            
            clasificado1 = ordD3values[1][0]
            clasificado2 = ordD3values[2][0]
            
        if D4[ordD3values[1][0]] > D4[ordD3values[0][0]] >  D4[ordD3values[2][0]]:
            
            clasificado1 = ordD3values[2][0]
            clasificado2 = ordD3values[0][0]
            
        
        if D4[ordD3values[0][0]] > D4[ordD3values[1][0]] >  D4[ordD3values[2][0]]:
            
            clasificado1 = ordD3values[2][0]
            clasificado2 = ordD3values[1][0]
            
        elif D4[ordD3values[1][0]] > D4[ordD3values[2][0]] >  D4[ordD3values[0][0]]:
            
            clasificado1 = ordD3values[0][0]
            clasificado2 = ordD3values[2][0]
            
        elif D4[ordD3values[2][0]] > D4[ordD3values[0][0]] >  D4[ordD3values[1][0]]:
            
            clasificado1 = ordD3values[1][0]
            clasificado2 = ordD3values[0][0]
            
        elif D4[ordD3values[0][0]] > D4[ordD3values[1][0]] ==  D4[ordD3values[2][0]]:
            
            if D5[ordD3values[1][0]] > D5[ordD3values[2][0]]:
                
                clasificado1 = ordD3values[1][0]
                clasificado2 = ordD3values[2][0]
                
            elif D5[ordD3values[1][0]] < D5[ordD3values[2][0]]:
                
                clasificado1 = ordD3values[2][0]
                clasificado2 = ordD3values[1][0]
                
            else:
                
                print('esto hay que mejorarlo, por resultados entre estos equipos')
                clasificado1 = ordD3values[2][0]
                clasificado2 = ordD3values[1][0]
                
        elif D4[ordD3values[1][0]] > D4[ordD3values[2][0]] ==  D4[ordD3values[0][0]]:
            
            if D5[ordD3values[2][0]] > D5[ordD3values[0][0]]:
                
                clasificado1 = ordD3values[2][0]
                clasificado2 = ordD3values[0][0]
                
            elif D5[ordD3values[2][0]] < D5[ordD3values[0][0]]:
                
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[2][0]
                
            else:
                
                print('esto hay que mejorarlo, por resultados entre estos equipos')
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[2][0]
                
        elif D4[ordD3values[2][0]] > D4[ordD3values[0][0]] ==  D4[ordD3values[1][0]]:
            
            if D5[ordD3values[0][0]] > D5[ordD3values[1][0]]:
                
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[1][0]
                
            elif D5[ordD3values[0][0]] < D5[ordD3values[1][0]]:
                
                clasificado1 = ordD3values[1][0]
                clasificado2 = ordD3values[0][0]
                
            else:
                
                print('esto hay que mejorarlo, por resultados entre estos equipos')
                clasificado1 = ordD3values[1][0]
                clasificado2 = ordD3values[0][0]
                
        elif D4[ordD3values[0][0]] < D4[ordD3values[1][0]] ==  D4[ordD3values[2][0]]:
                
            clasificado1 = ordD3values[0][0]
                
            if D5[ordD3values[1][0]] > D5[ordD3values[2][0]]:
                
                clasificado2 = ordD3values[1][0]
                
            elif D5[ordD3values[1][0]] < D5[ordD3values[2][0]]:
                
                clasificado2 = ordD3values[2][0]
                
            else:
                
                print('esto hay que mejorarlo, por resultados entre estos equipos')
                
                clasificado2 = ordD3values[1][0]
                
        elif D4[ordD3values[1][0]] < D4[ordD3values[2][0]] ==  D4[ordD3values[0][0]]:
                
            clasificado1 = ordD3values[1][0]
                
            if D5[ordD3values[2][0]] > D5[ordD3values[0][0]]:
                
                clasificado2 = ordD3values[2][0]
                
            elif D5[ordD3values[0][0]] > D5[ordD3values[2][0]]:
                
                clasificado2 = ordD3values[0][0]
                
            else:
                
                print('esto hay que mejorarlo, por resultados entre estos equipos')
                
                clasificado2 = ordD3values[0][0]
                
        elif D4[ordD3values[2][0]] < D4[ordD3values[0][0]] ==  D4[ordD3values[1][0]]:
                
            clasificado1 = ordD3values[2][0]
                
            if D5[ordD3values[0][0]] > D5[ordD3values[1][0]]:
                
                clasificado2 = ordD3values[0][0]
                
            elif D5[ordD3values[1][0]] > D5[ordD3values[0][0]]:
                
                clasificado2 = ordD3values[1][0]
                
            else:
                
                print('esto hay que mejorarlo, por resultados entre estos equipos')
                
                clasificado2 = ordD3values[1][0]
                
        elif D4[ordD3values[0][0]] == D4[ordD3values[1][0]] ==  D4[ordD3values[2][0]]:
            
            if D5[ordD3values[0][0]] > D5[ordD3values[1][0]] > D5[ordD3values[2][0]]:
                
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[1][0]
                
            elif D5[ordD3values[1][0]] > D5[ordD3values[2][0]] > D5[ordD3values[0][0]]:
                
                clasificado1 = ordD3values[1][0]
                clasificado2 = ordD3values[2][0]
                
            elif D5[ordD3values[2][0]] > D5[ordD3values[0][0]] > D5[ordD3values[1][0]]:
                
                clasificado1 = D5[ordD3values[2][0]]
                clasificado2 = D5[ordD3values[0][0]]
                
            elif D5[ordD3values[0][0]] > D5[ordD3values[1][0]] == D5[ordD3values[2][0]]:
                
                clasificado1 = ordD3values[0][0]
                
                print('esto hay que mejorarlo')
                
                clasificado2 = ordD3values[1][0]
                
            elif D5[ordD3values[1][0]] > D5[ordD3values[2][0]] == D5[ordD3values[0][0]]:
                
                clasificado1 = ordD3values[1][0]
                
                print('esto hay que mejorarlo')
                
                clasificado2 = ordD3values[2][0]
                
            elif D5[ordD3values[2][0]] > D5[ordD3values[0][0]] == D5[ordD3values[1][0]]:
                
                clasificado1 = ordD3values[2][0]
                
                print('esto hay que mejorarlo')
                
                clasificado2 = ordD3values[0][0]
                
            elif D5[ordD3values[0][0]] > D5[ordD3values[2][0]] > D5[ordD3values[1][0]]:
                
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[2][0]
                
            elif D5[ordD3values[1][0]] > D5[ordD3values[0][0]] > D5[ordD3values[2][0]]:
                
                clasificado1 = ordD3values[1][0]
                clasificado2 = ordD3values[0][0]
                
            elif D5[ordD3values[2][0]] > D5[ordD3values[1][0]] > D5[ordD3values[0][0]]:
                
                clasificado1 = ordD3values[2][0]
                clasificado2 = ordD3values[1][0]
            else:
                
                print('todos tienen los goles en contra y los a favor iguales')
                print('hay que ver los resultados individuales entre los equipos')
                print('o algun otro metodo')
                
                clasificado1 = ordD3values[0][0]
                clasificado2 = ordD3values[1][0]

    print()           
 
    
print('GRUPO A')
Clasificatoria('Rusia', 'Egipto', 'Arabia Saudí', 'Uruguay')
clasGrupoA1 = clasificado1
clasGrupoA2 = clasificado2
print('El primer clasificado del Grupo A es: ',clasGrupoA1)
print('El segundo clasificado del Grupo A es: ',clasGrupoA2)
print()

print('GRUPO B')
Clasificatoria('Portugal', 'España', 'Marruecos', 'Irán')
clasGrupoB1 = clasificado1
clasGrupoB2 = clasificado2
print('El primer clasificado del Grupo B es: ',clasGrupoB1)
print('El segundo clasificado del Grupo B es: ',clasGrupoB2)
print()

print('GRUPO C')
Clasificatoria('Francia', 'Australia', 'Perú', 'Dinamarca')
clasGrupoC1 = clasificado1
clasGrupoC2 = clasificado2
print('El primer clasificado del Grupo C es: ',clasGrupoC1)
print('El segundo clasificado del Grupo C es: ',clasGrupoC2)
print()

print('GRUPO D')
Clasificatoria('Argentina', 'Islandia', 'Croacia', 'Nigeria')
clasGrupoD1 = clasificado1
clasGrupoD2 = clasificado2
print('El primer clasificado del Grupo D es: ',clasGrupoD1)
print('El segundo clasificado del Grupo D es: ',clasGrupoD2)
print()

print('GRUPO E')
Clasificatoria('Brasil', 'Suiza', 'Costa Rica','Serbia')
clasGrupoE1 = clasificado1
clasGrupoE2 = clasificado2
print('El primer clasificado del Grupo E es: ',clasGrupoE1)
print('El segundo clasificado del Grupo E es: ',clasGrupoE2)
print()

print('GRUPO F')
Clasificatoria('Alemania', 'México', 'Suecia', 'Corea del Sur')
clasGrupoF1 = clasificado1
clasGrupoF2 = clasificado2
print('El primer clasificado del Grupo F es: ',clasGrupoF1)
print('El segundo clasificado del Grupo F es: ',clasGrupoF2)
print()

print('GRUPO G')
Clasificatoria('Bélgica', 'Panamá', 'Túnez', 'Inglaterra')
clasGrupoG1 = clasificado1
clasGrupoG2 = clasificado2
print('El primer clasificado del Grupo G es: ',clasGrupoG1)
print('El segundo clasificado del Grupo G es: ',clasGrupoG2)
print()

print('GRUPO H')
Clasificatoria('Polonia', 'Senegal', 'Colombia', 'Japón')
clasGrupoH1 = clasificado1
clasGrupoH2 = clasificado2
print('El primer clasificado del Grupo H es: ',clasGrupoH1)
print('El segundo clasificado del Grupo H es: ',clasGrupoH2)

##################################
##################################
##################################
##################################
##################################
##################################
print()
print('***  Octavos de Final  ***')

def Octavos(p1,p2):
    
    global ResultadoTotal
    
    
    print()
    
    grupo = [p1, p2]
    
    resultados = {"" : ["JJ", "G", "P", "E", "GF", "GC", "Puntos"]}
    
    for pais in grupo:
        
        for pais in grupo:
            
            resultados[pais] = []
   
    def CajitaGoles(a,b):
        
        global clasifOctavos
        global clasifOctavos2
    
        goles1 = random.choice(range(0,5))
        goles2 = random.choice(range(0,5))
        
        print('=============================================')
        print()
        if goles1 == goles2:
            
            print('Empate',grupo[a],':',goles1,'vs',goles2,':',grupo[b])
                    
            resultados[grupo[a]] = [1,0,0,1,goles1,goles2,1]
            resultados[grupo[b]] = [1,0,0,1,goles2,goles1,1]
            
            penales = {1:'1-0',2:'2-0',3:'2-1',4:'3-0',5:'3-1',
                       6:'3-2',7:'4-0',8:'4-1',9:'4-2',10:'4-3',
                       11:'5-3',12:'5-4',13:'6-5',14:'7-6',15:'8-7',
                       16:'9-8',17:'10-9'}
            
            ganadorPenales = {1:grupo[a],2:grupo[b]}
            
            penalesRandom = random.choice(range(1,18))
            
            ganadorPenalesRandom = random.choice(range(1,3))
            
            print()
            print('El ganador es', ganadorPenales[ganadorPenalesRandom],
                  'con el resultado: ',penales[penalesRandom],'en penales')
            
            clasifOctavos = ganadorPenales[ganadorPenalesRandom]
            
            if grupo[a] == ganadorPenales[ganadorPenalesRandom]:
                
                clasifOctavos2 = grupo[b]
                
            else:
                
                clasifOctavos2 = grupo[a]
                

        elif goles1 > goles2:
            
            print('Ha ganado',grupo[a],':',goles1,'vs',goles2,':',grupo[b])
            
            resultados[grupo[a]] = [1,1,0,0,goles1,goles2,3]
            resultados[grupo[b]] = [1,0,1,0,goles2,goles1,0]
            
            clasifOctavos = grupo[a]
            clasifOctavos2 = grupo[b]
            
    
        else:
            
            print('Ha ganado',grupo[b],':',goles2,'vs',goles1,':',grupo[a])
            
            resultados[grupo[a]] = [1,0,1,0,goles1,goles2,0]
            resultados[grupo[b]] = [1,1,0,0,goles2,goles1,3]
            
            clasifOctavos = grupo[b]
            clasifOctavos2 = grupo[a]
    
        
        ResultadoTotal = { grupo[a]:resultados[grupo[a]], grupo[b]:resultados[grupo[b]]}
           
        ResultadoTotal1 = pd.DataFrame(ResultadoTotal,  index = ['JJ', 'G', 'P', 'E', 'GF', 'GC', 'Puntos']).sort_values(by=['Puntos','GC','GF'], ascending=False, axis = 1)
        print()
        print((ResultadoTotal1).T)
        print()
    
    CajitaGoles(0,1)
       
Octavos(clasGrupoA1, clasGrupoB2)
print()
clasifOct1 = clasifOctavos
print('El primer clasificado a Cuartos de Final es:', clasifOct1)

Octavos(clasGrupoA2, clasGrupoB1)
print()
clasifOct2 = clasifOctavos
print('El segundo clasificado a Cuartos de Final es:',clasifOct2)

Octavos(clasGrupoC1, clasGrupoD2)
print()
clasifOct3 = clasifOctavos
print('El tercer clasificado a Cuartos de Final es:',clasifOct3)

Octavos(clasGrupoC2, clasGrupoD1)
print()
clasifOct4 = clasifOctavos
print('El cuarto clasificado a Cuartos de Final es:',clasifOct4)

Octavos(clasGrupoE1, clasGrupoF2)
print()
clasifOct5 = clasifOctavos
print('El quinto clasificado a Cuartos de Final es:',clasifOct5)

Octavos(clasGrupoE2, clasGrupoF1)
print()
clasifOct6 = clasifOctavos
print('El sexto clasificado a Cuartos de Final es:',clasifOct6)

Octavos(clasGrupoG1, clasGrupoH2)
print()
clasifOct7 = clasifOctavos
print('El septimo clasificado a Cuartos de Final es:',clasifOct7)

Octavos(clasGrupoG2, clasGrupoH1)
print()
clasifOct8 = clasifOctavos
print('El octavo clasificado a Cuartos de Final es:',clasifOct8)

##################################
##################################
##################################
##################################

print()
print('***  Cuartos de Final  ***')

Octavos(clasifOct1,clasifOct2)
print()
clasifCuartos1 = clasifOctavos
print('El primer clasificado a **La Semifinal**  es:',clasifCuartos1)

Octavos(clasifOct3,clasifOct4)
print()
clasifCuartos2 = clasifOctavos
print('El segundo clasificado a **La Semifinal**  es:',clasifCuartos2)

Octavos(clasifOct5,clasifOct6)
print()
clasifCuartos3 = clasifOctavos
print('El tercer clasificado a **La Semifinal**  es:',clasifCuartos3)

Octavos(clasifOct7,clasifOct8)
print()
clasifCuartos4 = clasifOctavos
print('El cuarto clasificado a **La Semifinal**  es:',clasifCuartos4)

##################################
##################################
##################################

print()
print('***  La Semifinal  ***')

Octavos(clasifCuartos1,clasifCuartos2)
print()
clasifsemiFinal1 = clasifOctavos
clasifBronce1 = clasifOctavos2
print('El primer equipo que ira a ** La FINAL ** es:',clasifsemiFinal1)
print()
print('El primer equipo que discutirá el TERCER LUGAR es:',clasifBronce1)

Octavos(clasifCuartos3,clasifCuartos4)
print()
clasifsemiFinal2 = clasifOctavos
clasifBronce2 = clasifOctavos2
print('El segundo equipo que ira a ** La FINAL ** es:',clasifsemiFinal2)
print()
print('El segundo equipo que discutirá el TERCER LUGAR es:',clasifBronce2)

##################################
##################################
print()
print('***  Discusión por el Tercer Lugar  ***')
Octavos(clasifBronce1,clasifBronce2)
print()
print('El 4to LUGAR es para:',clasifOctavos2)
print()
print('El 3er LUGAR es para:',clasifOctavos)

##################################
print()
print('***  Discusión por el Primer Lugar  ***')
Octavos(clasifsemiFinal1,clasifsemiFinal2)
print()
print('El 2do LUGAR es para:',clasifOctavos2)
print()
print('El 1er LUGAR es para:',clasifOctavos)

