import libreria

#1
assert(libreria.verifica_marcas_gaseosas("INKA KOLA") == "SI")
print("verifica_marcas_gaseosa OK")

#2
assert (libreria.es_mayor(40) == "MAYOR")
print("es_mayor OK")

#3
assert (libreria.es_animal("LEON") == "VERTEBRADO")
print("es_animal OK")

#4
assert(libreria.deportes("TENNIS") == "SI")
print("deportes OK")

#5
assert(libreria.sexo("JAVIER") == "MASCULINO")
print("sexo OK")

#6
assert(libreria.verifica_marca_zapatillas("ADIDAS") == "SI")
print("zapatillas OK")

#7
assert(libreria.es_dias("LUNES") == "SI")
print("es_dias OK")

#8
assert(libreria.colores("NEGRO") == "SI")
print("colores OK")

#9
assert(libreria.instituciones_educativas("BASADRE") == "MUJERES")
print("instituciones_educativas OK")

#10
assert(libreria.pescados("CABALLA") == "SI")
print("pescados OK")

#11
assert(libreria.utensilios_cocina("OLLA") == "SI")
print("utensilios_cocina OK")

#12
assert(libreria.juguetes("CARRO") == "NIÑO")
print("juguetes OK")

#13.
assert(libreria.estaciones_año("ENERO") == False)
assert(libreria.estaciones_año("PRIMAVERA") == True)
print("estaciones_año OK")
