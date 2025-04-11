import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "Ponerse o esta agresivo/enojado",
            "ALGARETE": "algo que esta o se esta haciendo mal o erroniamente",
            "PICHEA": "es como decir olvidate",
            "JANGUEO": "salir a pasear o a una fiesta, usualmente en grupo"
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
        print("---------------------------------------------------")
        time.sleep(0.5)
    else:
        print("Perdon, esa palabra no esta :(")
        print("---------------------------------------------------")
        time.sleep(0.5)
