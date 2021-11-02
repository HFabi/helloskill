from mycroft import MycroftSkill, intent_file_handler


class Helloworld(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helloworld.intent')
    def handle_helloworld(self, message):
        skill = message.data.get('skill')

        self.speak_dialog('helloworld', data={
            'skill': skill
        })


def create_skill():
    return Helloworld()

