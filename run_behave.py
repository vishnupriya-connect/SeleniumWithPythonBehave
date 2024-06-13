from behave import __main__ as behave_main

if __name__ == '__main__':
    # Run scenarios with the @smoke tag
    # behave_main.main(['features', '--tags=smoke'])

    # Run scenarios with the @amazon_com tag
    # behave_main.main(['features', '--tags=amazon_com'])

    # behave_main.main(['features', '--tags=tc-2002,wip'])
    # behave_main.main(['features', '--tags=wip'])

    # Run scenarios excluding    @ignore tags
    # behave_main.main(['features', '--tags=-ignore'])
    behave_main.main(['features/amazon.feature', '--tags=-ignore'])

