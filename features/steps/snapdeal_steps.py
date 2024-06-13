import logging

from behave import given, then

from tests import common_methods, assertions


@given('I open the Snap Deal website "{url}"')
def step_i_open_the_snap_deal_website(context,url):
    context.driver = common_methods.open_browser()
    common_methods.maximize_browser(context.driver)
    common_methods.open_url(context.driver, url)


@then("I should see the Snap Deal title")
def step_i_should_see_the_snap_deal_title(context):
    assertions.assert_snap_deal_title(context.driver)

