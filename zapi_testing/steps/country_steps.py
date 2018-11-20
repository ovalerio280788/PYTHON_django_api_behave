from behave import use_step_matcher, step

from zapi_testing.page_model.country_api import Countries

use_step_matcher('re')


def country_instance(context):
    return Countries(context)


@step('I get all countries I should have a status code "(.*)"')
def step_impl(context, status_code):
    instance = country_instance(context)
    json, status = instance.all_countries
    assert int(status) == int(status_code), "Actual status code '{}', expected '{}'".format(status, status_code)


@step('I get all countries the list should include "(.*)"')
def step_impl(context, expected_country):
    instance = country_instance(context)
    json, status = instance.single_country(expected_country)
    assert int(status) == int(200), "Actual status code '{}', expected '{}'".format(status, 200)
    assert json['RestResponse']['result']['alpha2_code'] == expected_country, "The country '{}' was not retrieved".format(expected_country)


@step('I attempt to retrieve a non existing country "(.*)" response should include an Error Message')
def step_impl(context, expected_country):
    instance = country_instance(context)
    json, status = instance.single_country(expected_country)
    context.logger.info(json)
    assert int(status) == int(200), "Actual status code '{}', expected '{}'".format(status, 200)
    assert "No matching country" in json['RestResponse']['messages'][0], "The country was retrieved"


@step('I create a new country with data')
def step_impl(context):
    data = context.table[0]
    instance = country_instance(context)
    json, status = instance.create_country;status(data['name'], data['alpha2_code'], data['alpha3_code'])
    assert int(status) == 200, "Actual status code '{}', expected '{}'".format(status, 200)

