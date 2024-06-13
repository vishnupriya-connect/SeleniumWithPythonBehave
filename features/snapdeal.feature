Feature: Snap Deal Website

  @tc-2001
  Scenario: Verify Snap Deal Title
    Given I open the Snap Deal website "https://www.snapdeal.com"
    Then I should see the Snap Deal title

  @tc-2002
  Scenario: Verify Snap Deal Title2
    Given I open the Snap Deal website "https://www.snapdeal.in"
    Then I should see the Snap Deal title