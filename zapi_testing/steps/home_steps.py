from behave import use_step_matcher, step

from zapi_testing.page_model.home_api import Home

use_step_matcher('re')


def home_instance(context):
    return Home(context, context.api_instance.username, context.api_instance.password)


@step('I get all homes, the amount of homes should be "(.*)"')
def step_impl(context, expected_num_homes):
    instance = home_instance(context)
    json, status = instance.all_homes
    assert len(json) == int(expected_num_homes), "The number of homes is '{}', expected '{}'".format(len(json), expected_num_homes)
