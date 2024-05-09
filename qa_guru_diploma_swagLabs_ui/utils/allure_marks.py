import allure


def feature(name):
    return allure.label('feature', name)


def owner(name):
    return allure.label('owner', name)
