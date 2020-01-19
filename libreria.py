#ejercicio 1
def verifica_marcas_gaseosas(strgaseosas):
    """
    Verifica si su strgaseosas coinciden con la lista de gaseosas mencionads
    :param strgaseosas:
    :return: str
    """
    if (strgaseosas == "CASINELLI" or strgaseosas == "INKA KOLA" or strgaseosas == "FANTA"):
        return "SI"
    else:
        return "NO"
#2
def es_mayor(intedad):
    """
    Verifica su intedad si es mayor o igual que 40
    :param intedad:
    :return: str
    """
    if (intedad >= 40):
        return "MAYOR"
    else:
        return "MENOR"
    #fin_es_mayor
#3
def es_animal(stranimal):
    """
    Verifica si stranimal coinciden con los animales invertebrados o vertebrados de lista
    :param stranimal:
    :return: str
    """
    if (stranimal == "LEON" or stranimal == "JIRAFA" or stranimal == "ELEFANTE"):
        return "VERTEBRADO"
    else:
        return "INVERTEBRADO"
    #fin_es_animal
#4
def deportes(strdeportes):
    """
    Verificar su strdeportes si coinciden con los deportes de la siguiente lista
    :param strdeportes:
    :return: str
    """
    if (strdeportes == "NATACION" or strdeportes == "VOLEY" or strdeportes == "TENNIS"):
        return "SI"
    else:
        return "NO"
    #fin_deportes
#5
def sexo(strsexo):
    """
    Verifica si strsexo si so masculino o femenino en la siguiente lista.
    :param strsexo:
    :return: str
    """
    if (strsexo == "DANIEL" or strsexo == "DIEGO" or strsexo == "JAVIER"):
        return "MASCULINO"
    else:
        return "FEMENINO"
    #fin_sexo
#6
def verifica_marca_zapatillas(strzapatillas):
    """
    verifica si strzapatillas si coinciden con las marcas dela lista
    :param strzapatillas:
    :return: str
    """
    if (strzapatillas == "ADIDAS" or strzapatillas == "PUMA"):
        return "SI"
    else:
        return "NO"
    #fin_zapatillas

#7
def es_dias(strdias):
    """
    verifica si strdias coinciden con los dias mencionados
    :param strdias:
    :return: str
    """
    if (strdias == "LUNES" or strdias == "MIERCOLES"):
        return "SI"
    else:
        return "NO"
    #fin_dias
#8
def colores (color):
    """
    verifica si strcolores coinciden con los colores mencionados en lista
    :param strcolores:
    :return: str
    """
    if (color == "NEGRO" or color == "BLANCO"):
        return "SI"
    else:
        return "NO"
    #fin_colores
#9
def instituciones_educativas (strinstituciones):
    """
    verifica si strinstitucones coinciden con los mencionados
    :param strinstituciones:
    :return: str
    """
    if (strinstituciones == "BASADRE" or strinstituciones == "PERUANO ESPAÑOL"):
        return "MUJERES"
    else:
        return "HOMBRES"
    #fin_instituciones
#10
def pescados (strpescados):
    """
    verifica si strpescados coiciden con los mencionados
    :param strpescados:
    :return: str
    """
    if (strpescados == "CABALLA" or strpescados == "TOLLO"):
        return "SI"
    else:
        return "NO"
    #fin_pescados
#11
def utensilios_cocina (strutensilios):
    """
    verifica si strutensilios coinciden con los mencionados
    :param strutensilios:
    :return: str
    """
    if (strutensilios == "OLLA" or strutensilios == "CUCHARAS"):
        return "SI"
    else:
        return "NO"
    #fin_utensilios

#12
def juguetes (strjuguetes):
    """
    verifica si strjuguetes coinciden con los de la lista mencionados
    :param strjuguetes:
    :return: str
    """
    if (strjuguetes == "CARRO" ):
        return "NIÑO"
    else:
        return "NIÑA"
    #fin_juguetes

#13.
def estaciones_año (estaciones):
    """
    verifica  que sea una estacion del año
    :param estaciones:
    :return: bool
    """
    if (estaciones == "PRIMAVERA" and estaciones == "VERANO" and estaciones == "OTOÑO" and estaciones == "INVIERNO" ):
        return True
    else:
        return False
#fin_estaciones_año


#14
def convertir_minuscula(cadena):
    """
    verifica que sea letra minuscula
    :param cadena:
    :return: cadena
    """
    if (isinstance(cadena, str)):
        return cadena.lower()
    else:
        return False
#fin_convetir_minuscula

#15
def validar_fin(cadena,busqueda):
    """
    Valida que una cadena inicie con un valor ingresado
    :param cadena:
             busqueda:
    :return: bool
      """
    if(isinstance(cadena,str) and isinstance(busqueda,str)):
        return cadena.endswith(busqueda)
    else:
        return False


#16
def verificar_edad(edad):
    """
    comprobar si edad es un digito
    Param: edad
    Retorna: bool
        """
    if(isinstance(edad,int)):
        return True
    else:
        return False

#17
def pago_mensual(pago):
    """
    Muestra el ciclo de vida de una persona segun la edad ingresada
    Param: edad
    Retorna: cadena
        """
    if(pago >= 1200 and pago <= 2000):
        return True
    else:
        return False

#18
def reemplazar_cadena(cadena, busqueda, reemplazo):
    """
    reemplaza una cadena por otra
    Param: cadena => cadena a corregir
			   busqueda => cadena a buscar
			   reemplazo => cadena que reemplaza
    Retorna: str
        """
    if(isinstance(cadena, str)):
        return cadena.replace(busqueda, reemplazo)
    else:
        return False

#19
def eliminar_espacios(cadena):
    """
    Elimina los espacios en blanco al inicio y final de la cadena
    :Param: cadena => cadena a corregir
    Retorna: str
        """
    if(isinstance(cadena, str)):
        return cadena.strip()
    else:
        return False
#Fin eliminar_espacios

#20
def contar_caracteres(cadena):
    """
    Cuenta los caracteres de una cadena
    Param: cadena => cadena a contar
    Retorna: int
        """
    if(isinstance(cadena, str)):
        return len(cadena)
    else:
        return False
#Fin contar_cadena

#21
def es_respuesta_validad(strRspta):
# verifique si la respuespuesta es valida. puede ser A,E,I,O o U
# Parametro strRspta (Respuesta Utilizada en el examen)
#retornar: bool

#1. si la longitud de strRspta es 1
    if( len(strRspta) == 1 ):
#1.1.si la strRspta no es A o E o I o O o U, devolver False, sino retornar  True
        if( strRspta!= "A" and strRspta!= "E" and strRspta!= "I" and strRspta!= "O" and strRspta!= "U"):
            return False
        else:
             return  True
#2. si no retornar False
    return False
#Fin_es_respuesta_valida

#22
def es_letra_valida(strletra):
    """
    Verifica si strletraes una letra valida del Bingo.Pueden ser B, I , N ,G ,O
    :param strletra:
    :return: bool
    """
    #1
    if (len(strletra) == 1):

    #1.1
        if (strletra != "B" and strletra != "I" and strletra != "N" and strletra != "G" and strletra != "O"):
            return False

    #2
        else:
            return True
        #fin_es_letra_valida

#23
def es_cancion_valida(strCancion):
    """
    Verifica si strletraes una letra valida de la cancion .Pueden ser C, A, N , C ,I,O,N
    :param strletra:
    :return: bool
    """
    #1
    if (len(strCancion) == 1):

    #1.1
        if (strCancion != "C" and strCancion != "A" and strCancion != "N" and strCancion != "C" and strCancion != "I" and
            strCancion != "O" and strCancion != "N" ):
            return False

    #2
        else:
            return True
#fin_es_cancion_valida

#24
def es_Alto(intAlto):
    """
    Verifica si X persona es persona alta si esta  entre 160cm y 180cm es par
    :param intAño: Entero positivo
    :return: int
    """
    if ( intAlto == 160 or intAlto ==164 or intAlto == 168 or intAlto == 172 or
         intAlto == 174 or intAlto ==176 or intAlto == 180 ):
        return True
    else:
        return False

#fin_Persona_alta

#25
def mayor_de_edad(intMayor):
    """
    Verifica si X persona es persona es mayor de edad si esta  entre 18 y 60 años es par
    :param intAño: Entero positivo
    :return: int
    """
    if ( intMayor == 18 or intMayor == 24 or intMayor == 26 or intMayor == 32 or
         intMayor ==  36 or intMayor == 40 or intMayor == 58 ):
        return True
    else:
        return False

#fin_Mayor_de_edad

#26
def gane_un_premio(strPremio):
    """
    Verifica si strletraes una letra valida del Premio.Pueden ser I, P , H ,O,N
    :param strletra:
    :return: bool
    """
    #1
    if (len(strPremio) == 1):

    #1.1
        if (strPremio != "I" and  strPremio != "P" and strPremio != "H" and strPremio != "O" and
                strPremio != "N"):
            return False

    #2
        else:
            return True
#fin_gane_un_premio

#27
def es_Bueno_OK(intBueno):
    """
    Verifica si X persona es Bueno, si x persona saca notas  entre 12 y  20 es par
    :param intAño: Entero positivo
    :return: int
    """
    if ( intBueno == 12 or intBueno == 14 or intBueno == 16 or intBueno == 18 or
         intBueno == 20 ):
        return True
    else:
        return False

#fin_es_bueno_Ok

#28
def es_impar_con_ltr(strImpar):
    # 1. strNum puede ser un numero impar de 1-19 o letras de B-G
    if ( strImpar == "1" or strImpar == "3" or strImpar == "5" or
         strImpar == "7" or strImpar == "9" or strImpar == "11" or
         strImpar == "13" or strImpar == "15" or strImpar == "17" or
         strImpar == "19" or strImpar == "B" or strImpar == "C" or
         strImpar == "D" or strImpar == "E" or strImpar == "F" or
         strImpar == "G"):
        return True
    else:
        # Si no es ningun numero 1-19 ni letras de a-z
        return False
#fin_es_impar_con_ltr

#29
def descuento_valido(tipo, prestamo):
    # Si el tipo de cliente es PREFERENCIAL
    # Aqui se usa la funcion upper()
    if ( tipo.upper() == "PREFERENCIAL" ):
        return 0.10 * prestamo
    else:
        return 0
#fin_descuento

