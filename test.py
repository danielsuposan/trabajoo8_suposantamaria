import libreria

#1
assert(libreria.verifica_marcas_gaseosas("FANTA") == "SI")
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
assert(libreria.estaciones_año("ENERO") ==False)
print("estaciones_año OK")

#14.
assert(libreria.convertir_minuscula("CADENA") == "cadena")
assert(libreria.convertir_minuscula("TELEVISION") == "television")
print("convertir_minuscula OK")

#15
assert(libreria.validar_fin("muebleria","eria") == True)
print("validar_fin OK")

#16
assert(libreria.verificar_edad(20) == True)
assert(libreria.verificar_edad(35) == True)
print("verificar_edad OK")

#17
assert(libreria.pago_mensual(1300) == True)
assert(libreria.pago_mensual(100) == False)
print("pago_mensual OK")

#18
assert(libreria.reemplazar_cadena("Hola mundo", "mundo", "a todos") == "Hola a todos")
print("reeplazar_cadena OK")

#19
assert(libreria.eliminar_espacios("    Hola   ") == "Hola")
print("eliminar_espacios OK")

#20
assert(libreria.contar_caracteres("bienvenidos") == 11)
print("contar_caracteres OK")

#21
assert ( libreria.es_respuesta_validad("Z") == False)
assert ( libreria.es_respuesta_validad("A") == True)
assert ( libreria.es_respuesta_validad("E") == True)
assert ( libreria.es_respuesta_validad("J") == False)
assert ( libreria.es_respuesta_validad("I") == True)
assert ( libreria.es_respuesta_validad("G") == False)
assert ( libreria.es_respuesta_validad("O") == True)
assert ( libreria.es_respuesta_validad("X") == False)
assert ( libreria.es_respuesta_validad("U") == True)
assert ( libreria.es_respuesta_validad("M") == False)
print("es_respuesta_valida OK")

#22
assert (libreria.es_letra_valida("A") == False)
assert (libreria.es_letra_valida("B") == True)
assert (libreria.es_letra_valida("I") == True)
assert (libreria.es_letra_valida("Z") == False)
assert (libreria.es_letra_valida("O") == True)
print("es_letra_valida OK")

#23
assert (libreria.es_cancion_valida("X") == False)
assert (libreria.es_cancion_valida("C") == True)
assert (libreria.es_cancion_valida("A") == True)
assert (libreria.es_cancion_valida("Z") == False)
assert (libreria.es_cancion_valida("C") == True)
assert (libreria.es_cancion_valida("I") == True)
print("es_Cancion_valida OK")

#24
assert (libreria.es_Alto(160) == True)
assert (libreria.es_Alto(150) == False)
assert (libreria.es_Alto(158) == False)
assert (libreria.es_Alto(159) == False)
assert (libreria.es_Alto(180) == True)
print("X_persona_es_Alta OK")

#25
assert (libreria.mayor_de_edad(18) == True)
assert (libreria.mayor_de_edad(21) == False)
assert (libreria.mayor_de_edad(59) == False)
assert (libreria.mayor_de_edad(19) == False)
assert (libreria.mayor_de_edad(58) == True)
print("X_Mayor_de_edad Ok")

#26
assert (libreria.gane_un_premio("A") == False)
assert (libreria.gane_un_premio("I") == True)
assert (libreria.gane_un_premio("P") == True)
assert (libreria.gane_un_premio("Z") == False)
assert (libreria.gane_un_premio("H") == True)
assert (libreria.gane_un_premio("O") == True)
assert (libreria.gane_un_premio("L") == False)
assert (libreria.gane_un_premio("N") == True)
print("GANE UN PREMIO OK")

#27
assert (libreria.es_Bueno_OK(12) == True)
assert (libreria.es_Bueno_OK(10) == False)
assert (libreria.es_Bueno_OK(8) == False)
assert (libreria.es_Bueno_OK(6) == False)
assert (libreria.es_Bueno_OK(18) == True)
print("X_persona_es_buena OK")

#28
assert (libreria.es_impar_con_ltr("2") == False)
assert (libreria.es_impar_con_ltr("4") == False)
assert (libreria.es_impar_con_ltr("AA") == False)
assert (libreria.es_impar_con_ltr("1") == True)
assert (libreria.es_impar_con_ltr("F") == True)
assert (libreria.es_impar_con_ltr("l") == False)
print("es_Impar_con_ltr OK")

#29
assert (libreria.descuento_valido("A", 300) == 0)
assert (libreria.descuento_valido("Preferencial", 100) == 10.0)
assert (libreria.descuento_valido("PREFERENCIAL", 100) == 10.0)
assert (libreria.descuento_valido("PrEfErEnCiAl", 100) == 10.0)
assert (libreria.descuento_valido("", 100) == 0)
print("descuento_valido OK")