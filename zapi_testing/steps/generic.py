from behave import use_step_matcher, step

from zapi_testing.page_model.api_base import ApiBase

use_step_matcher('re')

@step('As a user of the application')
def step_impl(context):
    context.api_instance = ApiBase(context)