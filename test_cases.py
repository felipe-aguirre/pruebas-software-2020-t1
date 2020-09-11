from function import compareString
import logging
logger = logging.getLogger('Tarea 1')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# cases: Listado de pruebas: usar formato tupla (String1, String2)
# ejemplo: case = [("Sol", "Luna"), ("Dia", "NOCHE")...] 

cases = [("Sol", "Luna"), ("Dia", "NOCHE"), (3,"test"), ("Buenas", 5), (6,8)]
for entrada in cases:
    output = compareString(entrada[0],entrada[1])
    if type(output) == list:
        log = str()
        for i in range(2):
            if output[i] == 0:
                print(i)
                print(entrada[i])
                log+= "Entrada {} no permitida ".format(entrada[i])
        logger.debug(log)
    else:
        logger.debug("Entrada a: {} Entrada b: {} Salida: {}".format(entrada[0],entrada[1],output))
        
    

    
