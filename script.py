# my_name = "Temuulen"
# print("Hello and welcome " + my_name + "!")
# gg = input("what is your name?")
# print("hello" + gg)
# birth_year = input("Enter your birth year:")
# age = 2023 - int(birth_year)
# # print("birth_year", age)
# course = "Python for beginners"
# print(course.replace("g", "5"))
# temprature = 25
# if temprature >= 30:
#     print("hot temprature")
#     print("Drink plenty of water")
# elif temprature > 20:
#     print("it's a nice day")
# else:
# print("cold temprature")
# i =1
# while i <= 20:
#     print(i * "*" )
#     i+=1
# numbers = [1, 2, 3, 4, 5]

# for item in numbers:
#     print(item)

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1


# def func():
#     print("gg")


# func()

# x = None
# print(x)

# import random

# print(random.randrange(0, 10))

# import camelcase

# c = camelcase.CamelCase()

# txt = "lorem ipsum dolor sit amet"

# print(c.hump(txt))

# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_eight_components():
#     driver = webdriver.Chrome()

#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")

#     title = driver.title
#     assert title == "Web form"

#     driver.implicitly_wait(0.5)

#     text_box = driver.find_element(by=By.NAME, value="my-text")
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    
#     text_box = driver.find_element(by=By.NAME, value="my-password")
    
#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     value = message.text
#     assert value == "Received!"
    

#     driver.quit()
# test_eight_components()

# from selenium import webdriver


# driver = webdriver.Chrome()

# driver.get("http://youtube.com")

# driver.quit()
 
 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""    
print(a)