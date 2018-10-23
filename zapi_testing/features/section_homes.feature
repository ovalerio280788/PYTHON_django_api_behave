Feature: This feature file will test all related to the homes section of the application

  Background:
    Given As user "ovalerio" with password "admin123" log into the application

  @wip
  Scenario: tcid-8
  [Homes] - Check that there is no home sections in a fresh installation
    When I get all section homes, the amount of sections should be "0"