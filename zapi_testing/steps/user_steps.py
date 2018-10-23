from behave import use_step_matcher, step

from zapi_testing.page_model.user_api import Users

use_step_matcher('re')


def user_instance(context):
    return Users(context, context.api_instance.username, context.api_instance.password)


@step('I get all users I should have a status code "(.*)"')
def step_impl(context, status_code):
    instance = user_instance(context)
    json, status = instance.all_users
    assert int(status) == int(status_code), "Actual status code '{}', expected '{}'".format(status, status_code)


@step('I get all users the amount of users should be at least "(.*)"')
def step_impl(context, expected_num_users):
    instance = user_instance(context)
    json, status = instance.all_users
    assert len(json) >= int(expected_num_users), "The number of users is '{}', expected '{}'".format(len(json), expected_num_users)


@step('I create a new user with data')
def step_impl(context):
    instance = user_instance(context)
    json, status = instance.create_user(context.table[0]['username'], context.table[0]['email'])
    assert int(status) == int(context.table[0]['status_code']), "Actual status code '{}', expected '{}'".format(status, context.table[0][
        'status_code'])

    if context.table[0]['field'] and context.table[0]['error_message']:
        assert json[context.table[0]['field']][0] == context.table[0]['error_message']
    else:
        assert json['username'] == context.table[0]['username'], "The returned username is not the one we tried to create"
        assert json['email'] == context.table[0]['email'], "The returned email is not the one we tried to create"


@step('I update existing user with data')
def step_impl(context):
    instance = user_instance(context)
    user_id = user_with_id(instance, context.table[0]['username'])
    json, status = instance.update_user(user_id=user_id, username=context.table[0]['newusername'] or None,
                                        email=context.table[0]['email'] or None)
    assert int(status) == int(context.table[0]['status_code']), "Actual status code '{}', expected '{}'".format(status, context.table[0][
        'status_code'])
    assert json['url'].split('/')[-2] == user_id, "The id of the user should be the same after the update process."
    assert json['username'] == context.table[0]['newusername'], "The returned username is not the one we tried to update"
    assert json['email'] == context.table[0]['email'], "The returned email is not the one we tried to update"


@step('Delete users "(.*)"')
def step_impl(context, users):
    users = users.split(",")
    instance = user_instance(context)
    json, status = instance.all_users

    for user in users:
        for json_user in json:
            if user in json_user['username']:
                user_id = json_user['url'].split("/")[-2]
                instance.delete_user(user_id)


def user_with_id(instance, user_name):
    json, status = instance.all_users
    return [json_user for json_user in json if json_user['username'] == user_name][0]['url'].split('/')[-2]
