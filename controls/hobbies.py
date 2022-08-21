from selene import have, command, by
from selene.support.shared import browser


class Hobbies:
    def __init__(self, element):
        self.element = element

    def mark_by_element(self, hobby_names):
        self.element = hobby_names
        for hobby_name in hobby_names:
            browser.element(by.text(hobby_name)).perform(command.js.scroll_into_view).click()
