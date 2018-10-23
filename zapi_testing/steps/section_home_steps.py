from behave import use_step_matcher, step

from zapi_testing.page_model.home_api import Home
from zapi_testing.page_model.section_home_api import SectionHome

use_step_matcher('re')


def section_home_instance(context):
    return SectionHome(context, context.api_instance.username, context.api_instance.password)


@step('I get all section homes, the amount of sections should be "(.*)"')
def step_impl(context, expected_num_sections):
    instance = section_home_instance(context)
    json, status = instance.all_section_homes
    assert len(json) == int(expected_num_sections), "The number of sections is '{}', expected '{}'".format(len(json),
                                                                                                           expected_num_sections)
