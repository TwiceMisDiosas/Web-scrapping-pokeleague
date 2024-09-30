from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Lista de XPaths para los Pokémon (GREAT LEAGUE)
poke_xpaths = {
    "pokemon1": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[1]/div[2]/span[1]', 'posicion'),  # Posición
        ('/html/body/div[1]/div/div[2]/div[9]/div[1]/div[2]/span[2] ', 'nombre'),    # Nombre
        ('/html/body/div[1]/div/div[2]/div[9]/div[1]/div[3]/div[1]', 'score'),      # Score
    ],
    "pokemon2": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[2]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[2]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[2]/div[3]/div[1]', 'score'),      
    ],
    "pokemon3": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[3]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[3]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[3]/div[3]/div[1]', 'score'),      
    ],
    "pokemon4": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[4]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[4]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[4]/div[3]/div[1]', 'score'),      
    ],
    "pokemon5": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[5]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[5]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[5]/div[3]/div[1]', 'score'),      
    ],
    
}
# Lista de XPaths para los Pokémon (ULTRA LEAGUE)
poke2_xpaths = {
    "pokemon1": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[1]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[1]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[1]/div[3]/div[1]', 'score'),      
    ],
    "pokemon2": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[2]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[2]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[2]/div[3]/div[1]', 'score'),     
    ],
    "pokemon3": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[3]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[3]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[3]/div[3]/div[1]', 'score'),      
    ],
    "pokemon4": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[4]/div[2]/span[1]', 'posicion'), 
        ('/html/body/div[1]/div/div[2]/div[9]/div[4]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[4]/div[3]/div[1]', 'score'),      
    ],
    "pokemon5": [
        ('/html/body/div[1]/div/div[2]/div[9]/div[5]/div[2]/span[1]', 'posicion'),  
        ('/html/body/div[1]/div/div[2]/div[9]/div[5]/div[2]/span[2]', 'nombre'),    
        ('/html/body/div[1]/div/div[2]/div[9]/div[5]/div[3]/div[1]', 'score'),      
    ],
    
}
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def main():
    print("MEJORES POKEMON POR LIGA")
    abrir_navegador()
    ranking_boton()
    print("GREAT LEAGUE")
    informacion()
    click_lista_desplegable()
    print("ULTRA LEAGUE")
    informacion2()
    #input()
    driver.quit()

def abrir_navegador():  
    driver.get("https://pvpoke.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[2]/a[2]'))) 
    #print("Boton encontrado")

def ranking_boton(): 
    click_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/a[2]')
    #print("Click")
    click_button.click()

def informacion():
    
    datos_pokemon = []

    try:
        
        for poke_name, xpaths in poke_xpaths.items():
            pokemon_data = {}  
            
            for xpath, clave in xpaths:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                texto = element.text
                pokemon_data[clave] = texto  

            datos_pokemon.append(pokemon_data)  

        
        for pokemon in datos_pokemon:
            print(f"Posicion: {pokemon['posicion']}  Nombre: {pokemon['nombre']}  Score: {pokemon['score']}")
    except Exception as e:
        print(f"Error al obtener la información: {e}")

def click_lista_desplegable():
    click_button_lista = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/select')
    click_button_lista.click()
    click_button_Ultra= driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/select/option[2]')
    click_button_Ultra.click()
    click_button_lista = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div[1]/select')
    click_button_lista.click()


def informacion2():
    
    datos_pokemon = []

    try:
        
        for poke_name, xpaths in poke2_xpaths.items():
            pokemon_data = {}  
            
            for xpath, clave in xpaths:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                texto = element.text
                pokemon_data[clave] = texto 

            datos_pokemon.append(pokemon_data)  

        for pokemon in datos_pokemon:
            print(f"Posicion: {pokemon['posicion']}  Nombre: {pokemon['nombre']}  Score: {pokemon['score']}")
    except Exception as e:
        print(f"Error al obtener la información: {e}")

if __name__ == "__main__":
    main()
