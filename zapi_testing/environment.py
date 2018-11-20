import logging

import sys


###########################################################################################################################################
# https://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls  official information about hooks
###########################################################################################################################################

def before_all(context):
    context.logger = setup_custom_logger("Api automation demo")
    context.logger.info("************************************************************************************************")
    context.logger.info("* Starting execution of Automation..".upper())
    context.logger.info("************************************************************************************************")
    context.logger.info("Before all execution configurations -- setting environment..")
    context.base_url = context.config.userdata.get('base_api_url')


def before_feature(context, feature):
    context.logger.info("Execution the before feature '{}' section".format(feature))


def before_tag(context, tag):
    context.logger.info("Execution the before tage '{}' section".format(tag))


def after_tag(context, tag):
    if tag == "add_country":
        context.execute_steps("""
                When Add countries "{}"
            """.format(context.scenario.name))


def after_scenario(context, scenario):
    print("\n")
    context.logger.info("******************************************************************************")
    context.logger.info("* Test case '{}' ---------------> '{}'".format(scenario.name, scenario.status))
    context.logger.info("******************************************************************************\n\n\n\n")


def after_feature(context, feature):
    context.username = None
    context.password = None


def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger
