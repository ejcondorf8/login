import logging as log
log.basicConfig(level=log.DEBUG,format='INFORMACION  %(levelname)s %(asctime)s  CARPETA[ %(filename)s %(message)s ]',handlers=[log.StreamHandler(),log.FileHandler('capa.log')])