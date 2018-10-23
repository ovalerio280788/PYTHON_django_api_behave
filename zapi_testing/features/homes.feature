Feature: This feature file will test all related to the homes section of the application

  Background:
    Given As user "ovalerio" with password "admin123" log into the application

  @wip
  Scenario: tcid-7
  [Homes] - Check that there is no home in a fresh installation
    When I get all homes, the amount of homes should be "0"