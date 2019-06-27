from mycroft import MycroftSkill, intent_file_handler


class CurrencyConverter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('converter.currency.intent')
    def handle_converter_currency(self, message):
        self.speak_dialog('converter.currency')


def create_skill():
    return CurrencyConverter()

