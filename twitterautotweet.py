import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the tweets and their scheduled times
tweets = [
    {"content": "Tweet 1: Your first message here.", "schedule_time": "2023-10-01 10:00:00"},
    {"content": "Tweet 2: Your second message here.", "schedule_time": "2023-10-02 15:30:00"},
    # Add more tweets and schedule times as needed
]

# Function to send tweets at scheduled times
def send_tweet(tweet_content):
    # Create a WebDriver instance for Chrome (you can use other browsers)
    driver = webdriver.Chrome(executable_path="path_to_chromedriver.exe")  # Replace with your chromedriver path

    # Open Twitter login page
    driver.get("https://twitter.com/login")

    # Replace with your Twitter credentials
    username = "your_username"
    password = "your_password"

    # Locate and fill in the username and password fields, then submit
    driver.find_element_by_name("session[username_or_email]").send_keys(username)
    driver.find_element_by_name("session[password]").send_keys(password)
    driver.find_element_by_xpath('//span[text()="Log in"]').click()

    # Wait for the Twitter page to load
    time.sleep(3)

    # Locate and click the tweet button
    tweet_button = driver.find_element_by_xpath('//div[@aria-label="Tweet"]')
    tweet_button.click()

    # Write the tweet content and send
    tweet_input = driver.find_element_by_xpath('//div[@data-testid="tweetTextarea_0"]')
    tweet_input.send_keys(tweet_content)
    tweet_input.send_keys(Keys.CONTROL + Keys.ENTER)

    # Wait for the tweet to be posted
    time.sleep(5)

    # Close the browser
    driver.quit()

# Function to schedule and send tweets
def schedule_tweets(tweet_data):
    for tweet in tweet_data:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if current_time >= tweet["schedule_time"]:
            send_tweet(tweet["content"])
            tweet_data.remove(tweet)

# Continuously check and send scheduled tweets
while tweets:
    schedule_tweets(tweets)
    time.sleep(60)  # Adjust the time interval as needed
