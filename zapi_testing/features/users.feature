Feature: This feature file will test all related to the users of the application

  Background:
    Given As user "ovalerio" with password "admin123" log into the application

  Scenario: tcid-1
  [Users] - Retrieving all users we should have a status code 200.
    When I get all users I should have a status code "200"


  Scenario: tcid-2
  [Users] - Retrieving all users should return at least 1 user.
    When I get all users the amount of users should be at least "1"


  @remove_user
  Scenario: tcid-3
  [Users] - Create new user
    When I create a new user with data
      | username         | email                     | field | error_message | status_code |
      | test_user_tcid-3 | test_user_tcid-3@test.com |       |               | 201         |


  Scenario: tcid-4
  [Users] - Create new user with bad email
    When I create a new user with data
      | username         | email     | field | error_message                | status_code |
      | test_user_tcid-4 | bad_email | email | Enter a valid email address. | 400         |


  Scenario: tcid-5
  [Users] - Create new user with bad username
    When I create a new user with data
      | username | email          | field    | error_message                                                                                   | status_code |
      | admin*   | admin@test.com | username | Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters. | 400         |


  @remove_user @wip
  Scenario: tcid-6
  [Users] - Update user
    # Pre-steps
    When I create a new user with data
      | username         | email                     | field | error_message | status_code |
      | test_user_tcid-6 | test_user_tcid-6@test.com |       |               | 201         |
    # Test case
    When I update existing user with data
      | username         | newusername              | email                             | status_code |
      | test_user_tcid-6 | test_user_tcid-6-updated | test_user_tcid-6-updated@test.com | 200         |