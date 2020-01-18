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
def colores (strcolores):
    """
    verifica si strcolores coinciden con los colores mencionados en lista
    :param strcolores:
    :return: str
    """
    if (strcolores == "NEGRO" or strcolores == "BLANCO"):
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
    if (estaciones != "PRIMAVERA" or estaciones != "VERANO" or estaciones != "OTOÑO" or estaciones != "INVIERNO" ):
        return False
    else:
        return True
#fin_estaciones_año




