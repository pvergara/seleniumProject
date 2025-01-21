from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('https://dummyflight.com/booking/')

driver.find_element(By.ID, 'sourceInput').send_keys("Madang Airport (MAG)")
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sourceAirportList')))
# els = driver.find_element(By.ID, 'sourceAirportList')


driver.find_element(By.ID, 'destinationInput').send_keys("Los Angeles International Airport (LAX)")
# driver.find_element(By.ID, 'destinationAirportList').find_elements(By.CLASS_NAME,"airport-item")[0].click()
driver.find_element(By.ID, 'departure_date').click()
WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.datepicker-day-button')))

els = driver.find_elements(By.CSS_SELECTOR, 'button.datepicker-day-button')
els[len(els) - 1].click()

driver.find_element(By.CSS_SELECTOR, 'button.datepicker-done').click()

driver.find_element(By.CSS_SELECTOR, 'button.next-step').click()

WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//*/label[@for="passenger-title-1"]')))

driver.quit()