# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException,NoSuchElementException, TimeoutException  # Import both NoSuchElementException and TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import time as t
# %%

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome()

# Set up an explicit wait with a timeout of 100 seconds
wait = WebDriverWait(driver, 1)

# Maximize the browser window
driver.maximize_window()
# %%

# Open the DispatchTrack URL
driver.get('https://rtg.dispatchtrack.com/')
# %%

# Sign in to DispatchTrack via SSO Link
sso_button = driver.find_element(By.XPATH, '//*[@id="btn-azure-sign-in"]')
sso_button.click()

# Wait for the notification button to become visible and clickable
wait = WebDriverWait(driver, 60)  # Extend the timeout value
try:
    notification_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pre-routing-nav-link"]/a[1]/span')))
    print("Notification button is now visible and clickable. Continuing with the next steps.")
    
    # Click the Notification Button using JavaScript
    driver.execute_script("arguments[0].click();", notification_button)
except TimeoutException:
    print("Notification button did not become clickable within the specified timeout.")

# %%

# Click the Schedule Call button using JavaScript
schedule_call_button = driver.find_element(By.XPATH, '//*[@id="notificationSideMenu"]/ul/li[2]/a')
driver.execute_script("arguments[0].click();", schedule_call_button)

# Wait for the page to load after clicking Schedule Call 5 Seconds
t.sleep(5)  # Adjust the sleep time as needed

# %%

# Click the Scheduled Date button using JavaScript
scheduled_date_button = driver.find_element(By.XPATH, '//*[@id="order_scheduled_date_icon"]')
driver.execute_script("arguments[0].click();", scheduled_date_button)

# Wait for the action to take effect (you can adjust the sleep time if needed)2 Seconds
t.sleep(75)  # Adjust the sleep time as needed

# %%

# Click the Day Number using JavaScript 1:15 Minutes
day_number = driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/form/app-notification-filter/div/div[1]/div[5]/div/ngb-datepicker/div[2]/div/ngb-datepicker-month/div[3]/div[7]/div')
driver.execute_script("arguments[0].click();", day_number)

# Wait for the action to take effect 
t.sleep(5)  # Adjust the sleep time as needed

# %%

# Click the Call Status button
call_status_button = driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/form/app-notification-filter/div/div[1]/div[9]/ng-select/div/div/div[2]')
call_status_button.click()
t.sleep(1)
# %%

# Click the Not Called button
not_called_button = driver.find_element(By.XPATH, "//span[text() = 'Not Called']")
not_called_button.click()

# %%

# Click the Email Status button
email_status_button = driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/form/app-notification-filter/div/div[1]/div[10]/ng-select/div/span')
email_status_button.click()
# %%

# Click the Not Emailed button
not_emailed_button = driver.find_element(By.XPATH, "//span[text() = 'Not Emailed']")
not_emailed_button.click()
# %%

# Click the Text Status Button
text_status_button = driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/form/app-notification-filter/div/div[1]/div[11]/ng-select/div/span')
text_status_button.click()
# %%

# Click the Not Texted Button
not_texted_button = driver.find_element(By.XPATH, "//span[text() = 'Not Texted']")
not_texted_button.click()
# %%

# Click the Go Button 1:15 Seconds
go_button = driver.find_element(By.XPATH, '//*[@id="go"]')
go_button.click()
t.sleep(75)

# Wait until the target element appears or timeout is reached
wait = WebDriverWait(driver, 1)  # Adjust the timeout value as needed
try:
    target_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/div[2]/div')))
    print("Target element has appeared. Loop completed.")
except TimeoutException:
    print("Target element did not appear within the specified timeout.")

        
# %%
# Click the 25 / Per Page Button
driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/app-paginator/div/div/span[1]/ng-select/div/div/div[3]').click()
t.sleep(1)

# %%
# Click the 400 / Per Page 2:25 Minutes

# # Define a flag for the while loop
clicked_400_per_page = False

# # # Click 400
while not clicked_400_per_page:
    try:
        driver.find_element(By.XPATH, "//span[text() = '400 / page']").click()
        clicked_400_per_page = True
    except ElementClickInterceptedException:
        # If clicking using regular method fails, try using JavaScript to click
        try:
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//span[text() = '400 / page']"))
            clicked_400_per_page = True
        except NoSuchElementException:
            print("Failed to click the 400 / Per Page button. Retrying...")
            t.sleep(2)  # Wait for a moment before retrying

t.sleep(145)  # Wait after clicking the button
# %%
# Loop through the process of selecting all, clicking text, email, and call buttons
first_iteration = True  # Flag to indicate the first iteration

while True:
    try:
        if first_iteration:
            select_all_box = driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/div[2]/table/thead/tr/th[1]/input')
            select_all_box.click()
            first_iteration = False  # Update the flag after the first iteration
        else:
            # Double-click behavior
            select_all_box = driver.find_element(By.XPATH, '/html/body/app-root/app-notification/div/div[2]/div/div/app-schedule-call/div[2]/table/thead/tr/th[1]/input')
            if not select_all_box.is_selected():
                select_all_box.click()
            else:
                # Wait for a brief moment before double clicking
                t.sleep(1)
                driver.execute_script("arguments[0].click();", select_all_box)
                driver.execute_script("arguments[0].click();", select_all_box)

        sms_all_button = driver.find_element(By.XPATH, '//*[@id="sms_all"]')
        actions = ActionChains(driver)
        actions.click(sms_all_button).perform()
        t.sleep(1)

        ok_button = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/div[3]/button[2]')
        ok_button.click()
        t.sleep(100)

        email_all_button = driver.find_element(By.XPATH, '//*[@id="email_all"]')
        actions = ActionChains(driver)
        actions.click(email_all_button).perform()
        t.sleep(1)

        ok_button = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/div[3]/button[2]')
        ok_button.click()
        t.sleep(125)

        call_all_button = driver.find_element(By.XPATH, '//*[@id="call_all"]')
        actions = ActionChains(driver)
        actions.click(call_all_button).perform()
        t.sleep(1)

        ok_button = driver.find_element(By.XPATH, '/html/body/ngb-modal-window/div/div/div[3]/button[2]')
        ok_button.click()
        t.sleep(150)

        go_button = driver.find_element(By.XPATH, '//*[@id="go"]')
        go_button.click()
        t.sleep(100)

    except ElementClickInterceptedException:
        print("ElementClickInterceptedException occurred. Retrying...")
        t.sleep(5)  # Wait for a moment before retrying

    except NoSuchElementException:
        print("No orders found. Continuing with the next steps.")
        break



# %%
