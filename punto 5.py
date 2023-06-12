import requests

# Función para obtener el JSON de una API y mostrar los pares de llave-valor
def obtener_datos(api_url):
    response = requests.get(api_url)
    json_data = response.json()
    
    # Imprimir el JSON completo
    print("JSON:")
    print(json_data)
    print()
    
    # Extraer y mostrar los pares de llave-valor
    print("Pares de llave-valor:")
    for key, value in json_data.items():
        print(f"Llave: {key}, Valor: {value}")
    print()

# Ejemplo 
obtener_datos("https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY")
obtener_datos("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
obtener_datos("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
