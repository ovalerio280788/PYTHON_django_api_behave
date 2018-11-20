Feature: This feature file will test all related to the country API of the application

  Background:
    Given As a user of the application

  @get_country
  Scenario: tcid-1
  [Countries] - Retrieving all countries we should have a status code 200.
    When I get all countries I should have a status code "200"

  Scenario: tcid-2
  [Countries] - Retrieving all countries should in include US.
    When I get all countries the list should include "US"

  Scenario: tcid-3
  [Countries] - Retrieving all countries should in include DE.
    When I get all countries the list should include "DE"

  Scenario: tcid-4
  [Countries] - Retrieving all countries should in include GB.
    When I get all countries the list should include "GB"

  Scenario: tcid-5
  [Countries] - Retrieving a non existing ZV country should return Error Message.
    When I attempt to retrieve a non existing country "ZV" response should include an Error Message

  Scenario: tcid-6
  [Countries] - Create new country
    When I create a new country with data
       | name         | alpha2_code     | alpha3_code |
       | TestCountry# | TC              | TCY         |