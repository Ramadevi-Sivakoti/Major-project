import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import re

#Function to extract the required details from the entire text
# Function to extract the required details from the entire text
def data_slicing(l, loop_text):
    printed_elements.add(loop_text)
    accuracy = l[-2]
    print("Accuracy =", accuracy)
    max_score = max_score = re.search(r'\d+', l[-4].replace(",", "")).group()

    print("Max_Score =", max_score[:2])
    difficulty = l[-8]


    if difficulty == 'EasyProblem':
        difficulty = 1
    elif difficulty == 'MediumProblem':
        difficulty = 2
    else:
        difficulty = 3
    problem_status = l[-1]
    print("difficulty=",difficulty)
    print("problem_status =", problem_status)
    row_data = [accuracy, max_score[:2], difficulty, problem_status]

    # Adding the row data into CSV file
    writer.writerow(row_data)
def data_slicing2(l, loop_text):
    printed_elements.add(loop_text)
    if 'Try' in l:
     problem_status = 'TryAgain'

     if "MediumProblem" in l:
        Difficulty=2
     elif "EasyProblem" in l:
        Difficulty = 1
     elif "HardMax" in l:
        Difficulty = 3
     elif "ExpertMax" in l:
        Difficulty = 5
     else:
        Difficulty=4


     percentage_pattern = re.compile(r'\d+\.\d+%')

    # Find percentages in the list using regex
     accuracy= [match.group() for item in l for match in [percentage_pattern.search(item)] if match]

     pattern = re.compile(r'(.+?)Success')

    # Iterate through the list and find the text before "Success" using regex
     Max_Score = [match.group(1) for item in l for match in [pattern.search(item)] if match]
     print("Accuracy=", *accuracy)
     print("Max_Score=",*Max_Score)
     print("Difficulty=", Difficulty)
     print("problem_Status=", problem_status)
     row_data = [*accuracy, *Max_Score, Difficulty, problem_status]

    # Adding the row data into CSV file
     writer.writerow(row_data)

#Function to scroll upto end of the page ande load all problems
def scrolldown():
    # Check if there are new elements loaded
    if set(loop_elements) == set(printed_elements):
        new_elements_loaded = False

    # Iterate through loop elements and print the text content
    for loop_element in loop_elements:
        loop_text = loop_element.text
        l = list(loop_text.split())

        # Check if the element has already been printed
        if loop_text not in printed_elements:
            data_slicing(l, loop_text)

    # Scroll down to load more content
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    sleep(1)
def scrolldown2():
    # Check if there are new elements loaded
    if set(loop_elements) == set(printed_elements):
        new_elements_loaded = False

    # Iterate through loop elements and print the text content
    for loop_element in loop_elements:
        loop_text = loop_element.text
        l = list(loop_text.split())

        # Check if the element has already been printed
        if loop_text not in printed_elements:
            data_slicing2(l, loop_text)

    # Scroll down to load more   content
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    sleep(0.2)




# Open the website
driver = webdriver.Chrome()
driver.get("https://www.hackerrank.com/dashboard")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div/div/div[2]/div[1]/nav/div/div[2]/ul[2]/li[2]/button")))

# Click the login icon
driver.find_element(By.XPATH, "//*[@id='content']/div/div/div/div[2]/div[1]/nav/div/div[2]/ul[2]/li[2]/button").click()

# Wait for the login page to load
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='tab-1-item-1']")))

driver.find_element(By.XPATH, "//*[@id='tab-1-item-1']").click()

# Wait for the login form to load
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='input-1']")))

# Login page - Entering login credintials
driver.find_element(By.XPATH, "//*[@id='input-1']").send_keys("shahanawaz2804@gmail.com")
driver.find_element(By.XPATH, "//*[@id='input-2']").send_keys("shanu@2804")
driver.find_element(By.XPATH, "//*[@id='tab-1-content-1']/div[1]/form/div[4]/button").click()

# Wait for the next page to load
wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='base-card-4-link']/div")))

driver.find_element(By.XPATH, "//*[@id='base-card-4-link']/div").click()

# Wait for the challenges page to load
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@class = 'checkbox-input' and @value = 'unsolved']"))).click()
driver.find_element(By.XPATH,"//input[@class = 'checkbox-input' and @value = 'solved']").click()
sleep(4)


# Set to keep track of printed elements
printed_elements = set()

# Flag to check if new elements are loaded
new_elements_loaded = True

# Set maximum number of iterations to avoid infinite loop
max_iterations = 30  # Adjust as needed
iteration_count = 0


# Create a CSV file and write data to it
csv_filename = "HR_Result_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    header_data = ["Accuracy", "Max_Score", "Difficulty", "Problem_status"]
    writer.writerow(header_data)  #Adding header row in csv file

    # Perform smooth scroll
    while new_elements_loaded and iteration_count < max_iterations:
        # Wait for the loop elements to be present
        loop_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'content--list_body']")))
        scrolldown()

        iteration_count += 1
    driver.back()
    sleep(10)

    driver.find_element(By.XPATH, "//input[@class = 'checkbox-input' and @value = 'unsolved']").click()
    sleep(1)
    printed_elements = set()

    # Flag to check if new elements are loaded
    new_elements_loaded = True

    # Set maximum number of iterations to avoid infinite loop
    max_iterations = 30 # Adjust as needed
    iteration_count = 0

    # Create a CSV file and write data to it
      # Adding header row in csv file

        # Perform smooth scroll
    while new_elements_loaded and iteration_count < max_iterations:
            # Wait for the loop elements to be present
            loop_elements = wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "//div[@class = 'content--list_body']")))
            scrolldown2()

            iteration_count += 1
    driver.back()
    driver.back()
    # Close the browser
driver.quit()