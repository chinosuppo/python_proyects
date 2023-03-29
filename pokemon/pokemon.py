import requests

urlApi = "https://pokeapi.co/api/v2/pokemon/"

def main():
    nombre_pokemon = input("Indique el nombre del Pokemon: ")
    pokemon_data_url = urlApi + nombre_pokemon
    
    data = get_pokemon_data(pokemon_data_url)
    
    tipo_pokemon = [types['type']['name'] for types in data['types']]    
    print(data)
    print(",".join(tipo_pokemon))  


def get_pokemon_data(url_pokemon=""):
    pokemon_diccionario = {
        "nombre": "",
        "numero": "",
        "altura": "",
        "habilidades": "",
        "types": "",
        "peso": "",
    }
    
    respuesta = requests.get(url_pokemon)
    data = respuesta.json()
    
    pokemon_diccionario["nombre"] = data["name"]
    pokemon_diccionario["numero"] = data["order"]
    pokemon_diccionario["altura"] = data["height"]
    pokemon_diccionario["habilidades"] = len(data["abilities"])
    pokemon_diccionario["types"] = data["types"]
    pokemon_diccionario["peso"] = data["weight"]
    
    return pokemon_diccionario
    
        
if __name__ == '__main__':
    main()