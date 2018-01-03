from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'list team'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'lions'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'brothers'

    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'lamigo'

    def state1_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'lions'

    def state1_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'brothers'

    def state1_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'lamigo'

    def on_enter_state1(self, update):
        update.message.reply_text("you can search the official website of three baseball team.just input 'lions' or 'brothers' or 'lamigo'")
        

    def on_enter_state2(self, update):
        update.message.reply_text("here is the website of lions")
        update.message.reply_photo(open("img/lions.jpg","rb"))
        update.message.reply_text("https://www.uni-lions.com.tw/")
        self.go_back(update)

    def on_enter_state3(self, update):
        update.message.reply_text("here is the website of brothers")
        update.message.reply_text("https://www.brothers.tw/")
        self.go_back(update)

    def on_enter_state4(self, update):
        update.message.reply_text("here is the website of lamigo")
        update.message.reply_photo(open("img/lamigo.png","rb"))
        update.message.reply_text("http://www.lamigo-monkeys.com.tw/")
        self.go_back(update)
