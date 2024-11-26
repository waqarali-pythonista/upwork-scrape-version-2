# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os 

# class ScrapingService:
#     """
#     A service class to handle web scraping of job details using Selenium.
#     """

#     @staticmethod
#     def scrape_job_details(url):
#         """
#         Scrapes job details from a given URL.
        
#         Args:
#             url (str): The URL of the job post to scrape.

#         Returns:    
#             dict: A dictionary containing the scraped job details.
#         """
#         driver = webdriver.Chrome()  # Replace with the path to your ChromeDriver if necessary
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#         chrome_options.add_argument("--headless")
#         chrome_options.add_argument("--disable-dev-shm-usage")
#         chrome_options.add_argument("--no-sandbox")
#         driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    

#         try:
#             driver.get(url)

#             # Extract job details
#             job_title = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div[1]/div/div/header/h4"))
#             ).text

#             description = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[1]/div/p"))
#             ).text

#             post_time = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/header/div/div[1]"))
#             ).text

#             location = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/header/div/div[2]/span"))
#             ).text

#             # Extract additional fields
#             clock_hourly = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[1]").text
#             duration = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[2]").text
#             experience_level = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[3]").text
#             clock_timelog = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[4]").text
#             local = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[5]").text
#             project_type = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[6]").text

#             # Extract client details
#             client_contract_date = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/div").text
#             client_location = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[1]").text
#             client_spend = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[2]/strong").text
#             client_hires = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[2]/div").text
#             client_hours = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[3]/div").text
#             client_company_profile = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[4]").text

#             # Return all scraped data as a dictionary
#             return {
#                 "job_title": job_title,
#                 "description": description,
#                 "post_time": post_time,
#                 "location": location,
#                 "clock_hourly": clock_hourly,
#                 "duration": duration,
#                 "experience_level": experience_level,
#                 "clock_timelog": clock_timelog,
#                 "local": local,
#                 "project_type": project_type,
#                 "client_contract_date": client_contract_date,
#                 "client_location": client_location,
#                 "client_spend": client_spend,
#                 "client_hires": client_hires,
#                 "client_hours": client_hours,
#                 "client_company_profile": client_company_profile
#             }

#         except Exception as e:
#             raise Exception(f"Error occurred while scraping: {e}")

#         finally:
#             driver.quit()

# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class ScrapingService:
#     """
#     A service class to handle web scraping of job details using Selenium.
#     """

#     @staticmethod
#     def scrape_job_details(url):
#         """
#         Scrapes job details from a given URL.
        
#         Args:
#             url (str): The URL of the job post to scrape.

#         Returns:    
#             dict: A dictionary containing the scraped job details.
#         """
#         # Set up Chrome options for headless mode
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")  # Path to your Chrome binary (useful for Heroku)
#         chrome_options.add_argument("--headless")  # Run in headless mode
#         chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
#         chrome_options.add_argument("--no-sandbox")  # Necessary for running in Docker or certain restricted environments

#         # Initialize the WebDriver with the specified options and path to ChromeDriver
#         driver = webdriver.Chrome(
#             executable_path=os.environ.get("CHROMEDRIVER_PATH"),  # Path to ChromeDriver (ensure this is set in your environment)
#             options=chrome_options
#         )

#         try:
#             driver.get(url)

#             # Extract job details
#             job_title = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div[1]/div/div/header/h4"))
#             ).text

#             description = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[1]/div/p"))
#             ).text

#             post_time = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/header/div/div[1]"))
#             ).text

#             location = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/header/div/div[2]/span"))
#             ).text

#             # Extract additional fields
#             clock_hourly = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[1]").text
#             duration = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[2]").text
#             experience_level = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[3]").text
#             clock_timelog = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[4]").text
#             local = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[5]").text
#             project_type = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[6]").text

#             # Extract client details
#             client_contract_date = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/div").text
#             client_location = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[1]").text
#             client_spend = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[2]/strong").text
#             client_hires = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[2]/div").text
#             client_hours = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[3]/div").text
#             client_company_profile = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[4]").text

#             # Return all scraped data as a dictionary
#             return {
#                 "job_title": job_title,
#                 "description": description,
#                 "post_time": post_time,
#                 "location": location,
#                 "clock_hourly": clock_hourly,
#                 "duration": duration,
#                 "experience_level": experience_level,
#                 "clock_timelog": clock_timelog,
#                 "local": local,
#                 "project_type": project_type,
#                 "client_contract_date": client_contract_date,
#                 "client_location": client_location,
#                 "client_spend": client_spend,
#                 "client_hires": client_hires,
#                 "client_hours": client_hours,
#                 "client_company_profile": client_company_profile
#             }

#         except Exception as e:
#             raise Exception(f"Error occurred while scraping: {e}")

#         finally:
#             driver.quit()

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome  import ChromeDriverManager

class ScrapingService:
    """
    A service class to handle web scraping of job details using Selenium.
    """

    @staticmethod
    def scrape_job_details(url, proxy=None):
        """
        Scrapes job details from a given URL.

        Args:
            url (str): The URL of the job post to scrape.
            proxy (str, optional): Proxy server address (e.g., 'http://proxy-server:port').

        Returns:
            dict: A dictionary containing the scraped job details.
        """
        # Set up Chrome options for headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')  # Path to Chrome binary
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration in headless mode
        chrome_options.add_argument('--no-sandbox')  # Required for restricted environments
        chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
        chrome_options.add_argument('--remote-debugging-port=9222')  # Enable remote debugging

        # Add proxy configuration if provided
        if proxy:
            chrome_options.add_argument(f'--proxy-server={proxy}')

        # Initialize WebDriver with the configured options
        try:
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager.install()),  # Path to Chromedriver
                options=chrome_options
            )
        except Exception as e:
            raise RuntimeError(f"Error initializing the WebDriver: {e}")

        try:
            driver.get(url)

            # Extract job details
            job_title = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div[1]/div/div/header/h4"))
            ).text

            description = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[1]/div/p"))
            ).text

            post_time = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/header/div/div[1]"))
            ).text

            location = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/header/div/div[2]/span"))
            ).text

            # Extract additional fields
            clock_hourly = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[1]").text
            duration = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[2]").text
            experience_level = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[3]").text
            clock_timelog = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[4]").text
            local = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[5]").text
            project_type = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/section[2]/ul/li[6]").text

            # Extract client details
            client_contract_date = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/div").text
            client_location = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[1]").text
            client_spend = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[2]/strong").text
            client_hires = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[2]/div").text
            client_hours = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[3]/div").text
            client_company_profile = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/main/div/div/div/div/div[1]/div[1]/ul/li[4]").text

            # Return all scraped data as a dictionary
            return {
                "job_title": job_title,
                "description": description,
                "post_time": post_time,
                "location": location,
                "clock_hourly": clock_hourly,
                "duration": duration,
                "experience_level": experience_level,
                "clock_timelog": clock_timelog,
                "local": local,
                "project_type": project_type,
                "client_contract_date": client_contract_date,
                "client_location": client_location,
                "client_spend": client_spend,
                "client_hires": client_hires,
                "client_hours": client_hours,
                "client_company_profile": client_company_profile
            }

        except Exception as e:
            raise Exception(f"Error occurred while scraping: {e}")

        finally:
            driver.quit()

