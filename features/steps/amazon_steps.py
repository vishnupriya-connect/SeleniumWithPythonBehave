import logging
from tests import common_methods  # as cm
from behave import given, then
from tests import assertions
import yaml

with open("locators.yml", "r") as file:
    locators = yaml.safe_load(file)


@given('I open the Amazon website "{url}"')
def step_i_open_the_amazon_website(context, url):
    context.driver = common_methods.open_browser()
    common_methods.maximize_browser(context.driver)
    common_methods.open_url(context.driver, url)


@then("I should see the Amazon title")
def step_i_should_see_the_amazon_title(context):
    common_methods.sleep(2)
    assertions.assert_amazon_title(context.driver)


@then("close the browser")
def step_close_the_browser(context):
    common_methods.close_browser(context.driver)


@then('Enter product name "{product}" in search bar')
def step_enter_product_name_in_search_bar(context, product):
    search_bar_text_box_element = common_methods.find_element_by_id(context.driver, locators['search_bar_text_box_element']['id'])
    common_methods.clear(search_bar_text_box_element)
    common_methods.send_keys(search_bar_text_box_element,product)
    search_bar_submit_element = common_methods.find_element_by_id(context.driver,locators['search_bar_submit_element']['id'])
    common_methods.click(search_bar_submit_element)

