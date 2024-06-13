Feature: Amazon Website

  @tc-1101 @smoke
  Scenario: Verify Amazon Title and Search a Product in amazon.in
    Given I open the Amazon website "https://www.amazon.in"
    Then I should see the Amazon title
    Then Enter product name "Laptop" in search bar
    Then Enter product name "Sarees" in search bar
    And close the browser


  @wip
  @tc-1102
  Scenario Outline: Verify Amazon Title and Search a Product in amazon.in
    Given I open the Amazon website "<url>"
    Then I should see the Amazon title
    Then Enter product name "<product>" in search bar
    And close the browser

    Examples:
      | url                    | product |
      | https://www.amazon.in  | Sarees  |
      | https://www.amazon.in  | Laptop  |
#      | https://www.amazon.in  | Mobiles  |
#      | https://www.amazon.in  | Watches  |
#      | https://www.amazon.in  | Headphones  |
#      | https://www.amazon.in  | Python programming books  |

  @smoke
  @tc-1103 @amazon_com
  Scenario: Verify Amazon Title in amazon.com
    Given I open the Amazon website "https://www.amazon.com"
    Then I should see the Amazon title
    And close the browser

  @ignore
  Scenario: Verify Amazon Title - duplicate - ignore
    Given I open the Amazon website "https://www.amazon.com"
    Then I should see the Amazon title
    And close the browser
