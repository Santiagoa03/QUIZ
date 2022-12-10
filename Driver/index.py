from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path= "Driver/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.viajesexito.com/")

paquetes = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a')
paquetes.click()

vueloHotel = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div/ul/li[1]/label')
vueloHotel.click()

origen = "Bogotá"
input = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/input')
input.click()
input.send_keys(origen)
inputSelect = driver.find_element(By.XPATH,'/html/body/ul[20]/li/a/table/tbody/tr/td[2]')
inputSelect.click()

destino = "Punta Cana"
inputDestino = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input')
inputDestino.click()
inputDestino.send_keys(destino)
inputSelectDestino = driver.find_element(By.XPATH,'/html/body/ul[21]/li/a/table/tbody/tr/td[2]')
inputSelectDestino.click()

FechaInicio = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/input')
FechaInicio.click()
FechaInicioSelect = driver.find_element(By.XPATH,'/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a')
FechaInicioSelect.click()

FechaRegreso = driver.find_element(By.XPATH,'/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a')
FechaRegreso.click()

habitacion = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p')
habitacion.click()

habitacion1 = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span')
habitacion1.click()

aplicar = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
aplicar.click()

buscar = driver.find_element(By.XPATH,'/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a/span')
buscar.click()

time.sleep(20)
precio = []
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/a/div/div[2]/span[2]'))
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/a/div/div[2]/span[2]'))
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[1]/div[4]/a/div/div[2]/span[2]'))
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[3]/a/div/div[2]/span[2]'))
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[3]/div[3]/a/div/div[2]/span[2]'))
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[4]/div[3]/a/div/div[2]/span[2]'))
precio.append(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[5]/div[3]/a/div/div[2]/span[2]'))



for p in precio:
    print(p.text)

aerolinea = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolinea.click()
busquedaAerolinea = "Latam"
aerolinea.send_keys(busquedaAerolinea)
aerolineaSelect = driver.find_element(By.XPATH,'/html/body/ul[3]/li[2]/a')
aerolineaSelect.click()

busquedaNueva = driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
busquedaNueva.click()

time.sleep(30)

driver.quit()


