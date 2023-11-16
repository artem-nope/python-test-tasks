class NewsSite:
    def __init__(self, name):
        self.name = name
        self.news = []
        self.subscribers = []

    def __str__(self):
        return f'{self.name}: {self.subscribers}'

    def create_news(self, txt):
        self.news.append(txt)
        for s in self.subscribers:
            s.add_message(f'{self.name}: {txt}')

    def add_subscriber(self, subs):
        self.subscribers.append(subs)

    def remove_subscriber(self, subs):
        self.subscribers.remove(subs)

    def show_subscribers(self):
        print(f'{self.name}: ')
        for s in self.subscribers:
            print(s)


class Subscriber:
    def __init__(self, name):
        self.name = name
        self.sites = []
        self.messages = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def subscribe(self, site):
        if site not in self.sites:
            self.sites.append(site)
            site.add_subscriber(self)

    def add_message(self, message):
        self.messages.append(message)

    def show_news(self):
        print(self)
        for m in self.messages:
            print(m)

    def unsubscribe(self, site: NewsSite):
        if site in self.sites:
            # self.sites.remove(site)
            self.sites.pop(self.sites.index(site))
            site.remove_subscriber(self)


if __name__ == '__main__':
    user1 = Subscriber('John')
    user2 = Subscriber('Peter')
    newsSite1 = NewsSite('Pravda.com')
    newsSite2 = NewsSite('Chip.com')
    user1.subscribe(newsSite1)
    user1.subscribe(newsSite2)
    user2.subscribe(newsSite1)
    newsSite1.create_news('Shock NEWS!!! There is a new version of Python!!!')
    newsSite2.create_news('Shock NEWS!!! There is a new version of Java!!!')
    user1.unsubscribe(newsSite1)
    newsSite1.create_news('Shock NEWS!!! There is a new version of C++!!!')
    newsSite1.show_subscribers()
    newsSite2.show_subscribers()
    user1.show_news()
    user2.show_news()
    print()
    print(newsSite1)
    print(newsSite2)






