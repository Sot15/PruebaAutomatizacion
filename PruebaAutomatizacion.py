#Librerias
import select
from selenium import webdriver
import time
import pandas as pd


#Opciones de navegador

driver = webdriver.Chrome()
driver.set_window_size(1024, 600)
driver.maximize_window()


#iniciamos el navegador

driver.get('https://utest.com/')
time.sleep(4)
#Al entrar a la url ubicamos el boton de registro y damos click
driver.find_element_by_class_name('unauthenticated-nav-bar__sign-up').click()
time.sleep(3)
#Despues del click al boton damos espera de la paginma de 3 segundos y completamos los campos requeridos como primer nombre
driver.find_element_by_name('firstName').send_keys('jhoan')
#primer Apellido
driver.find_element_by_id('lastName').send_keys('sandoval')
#Correo Electronico
driver.find_element_by_id('email').send_keys('jsebastiansandovalsoto@gmail.com')
#Seleccionamos nuestra fecha de cumpleaños y damos una espera de 1 segundo en cada opcion para evitar colapso del sistema
driver.find_element_by_id('birthMonth').click()
driver.find_element_by_id('birthMonth').send_keys('November')
time.sleep(0.5)
driver.find_element_by_id('birthDay').click()
driver.find_element_by_id('birthDay').send_keys('15')
time.sleep(0.5)
driver.find_element_by_id('birthYear').click()
driver.find_element_by_id('birthYear').send_keys('1997')
#luego damos click en el boton de ubicacion para continuar y damos una espera de 5 segundos para que cargue por completo la pagina
driver.find_element_by_class_name('btn.btn-blue').click()
time.sleep(3)
driver.find_element_by_class_name('btn.btn-blue.pull-right').click()
time.sleep(3)
#Generamos click en el botonb para continuar de pagina y damos 2 segundos de carga de la pagina
driver.find_element_by_class_name('btn.btn-blue.pull-right').click()
time.sleep(2)
driver.find_element_by_id('password').send_keys('Choucair.2022')
driver.find_element_by_id('confirmPassword').send_keys('Choucair.2022')
driver.find_element_by_class_name('checkmark.signup-consent__checkbox.signup-consent__checkbox--highlight').click()
driver.find_element_by_id('termOfUse').click()
driver.find_element_by_id('privacySetting').click()
driver.find_elements_by_class_name('pull-right.next-step').click()
time.sleep(6)
driver.close()







