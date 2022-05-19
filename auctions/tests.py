from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class Auction_Testing(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Chrome()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/1')
    #find the elements you need to submit form
    active_listing_user = selenium.find_element_by_id('user_id')
    active_listing_title = selenium.find_element_by_id('active_listing_title')
    active_listing_desc = selenium.find_element_by_id('active_listing_desc')
    active_listing_price = selenium.find_element_by_id('active_listing_price')
    active_listing_starting_bid = selenium.find_element_by_id('active_listing_starting_bid')
    active_listing_category = selenium.find_element_by_id('active_listing_category')
    active_listing_image_url = selenium.find_element_by_id('active_listing_image_url')
    active_listing_bid_counter = selenium.find_element_by_id('active_listing_bid_counter')
    active_listing_created_at = selenium.find_element_by_id('active_listing_created_at')
    active_listing_active = selenium.find_element_by_id('active_listing_active')
    active_listing_winner = selenium.find_element_by_id('active_listing_winner')



    

    submit = selenium.find_element_by_id('submit_button')

   
    active_listing_active_author.send_keys('waseem')
    active_listing_user.send_keys('Test')
    active_listing_title.send_keys('This is for testing purpose')
    active_listing_desc.send_keys('Test')
    active_listing_price.send_keys('$50')
    active_listing_starting_bid.send_keys('$50')
    active_listing_category.send_keys('Test')
    active_listing_image_url.send_keys('')
    active_listing_bid_counter.send_keys('0')
    active_listing_created_at.send_keys('Test')
    active_listing_active.send_keys('True')
    active_listing_winner.send_keys('None')

    #submit form
    submit.send_keys(Keys.RETURN)

    #check result; page source looks at entire html document
    assert 'Test' in selenium.page_source
