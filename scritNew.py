import argparse

parse = argparse.ArgumentParser()
parse.add_argument("nombre del archivo csv")
parse.add_argument("DNI del cliente donde se filtrar")
parse.add_argument("salida: PANTALLA o CSV")
parse.add_argument("tipo de cheque: EMITIDO o DEPOSITADO")
parse.add_argument("estado de cheque: PENDIENTE, APROBADO, RECHAZADO")
parse.add_argument("rango de fecha")
args = parse.parse_args()