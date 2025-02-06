from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv


driver = webdriver.Firefox(service=Service(executable_path=r'E:\门户爬虫\geckodriver.exe'))
# driver = webdriver.Chrome()  # 创建一个谷歌浏览器对象

with open('extracted_results.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
print(lines[0])

driver.get('https://portal.pku.edu.cn/')  # 向浏览器发出访问请求
sleep(30)
with open("test.csv", 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for line in lines:
        driver.find_element(By.ID, 'deptText').clear()
        driver.find_element(By.ID, 'deptText').send_keys(line)    # send_keys()键入关键字
        driver.find_element(By.ID, 'deptText').send_keys(Keys.ENTER)
        # driver.find_element(By.XPATH, "//input[@type='button']").click()
        element = driver.find_element(By.XPATH, ".//span[@class='pku-red ng-scope']")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.invisibility_of_element(element))
        table = driver.find_element(By.CLASS_NAME, 'row-border-table')

        # 定位表格中的所有行
        rows = table.find_elements(By.XPATH, ".//tr[@class='a-tr-hand ng-scope']")

        # 遍历每一行，提取姓名、单位和身份信息
        for row in rows:
            # 假设姓名、单位和身份信息分别位于第二列、第三列和第四列
            name = row.find_element(By.XPATH, ".//td[1]").text
            department = row.find_element(By.XPATH, ".//td[2]").text
            identity = row.find_element(By.XPATH, ".//td[3]").text
            writer.writerow([name, department, identity])
