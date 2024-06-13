import logging

SNAP_DEAL_EXPECTED_TITLE = 'Shop Online for Men, Women & Kids Clothing, Shoes, Home Decor Items'
AMAZON_EXPECTED_TITLE = 'Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in'


def assert_amazon_title(driver):
    try:
        actual_title = driver.title
        logging.info(actual_title+" | "+AMAZON_EXPECTED_TITLE)
        assert actual_title == AMAZON_EXPECTED_TITLE
    except AssertionError as ae:
        logging.info("Amazon title assertion failed.")
        raise
    except Exception as e:
        logging.info("Amazon title test case failed.")
        raise
    else:
        logging.info("Amazon title assertion successful.")


def assert_snap_deal_title(driver):
    try:
        actual_title = driver.title
        assert actual_title == SNAP_DEAL_EXPECTED_TITLE
    except AssertionError as ae:
        logging.info("Snap deal title assertion failed.")
        raise
    except Exception as e:
        logging.info("Snap deal title test case failed.")
        raise
    else:
        logging.info("Snap deal title assertion successful.")