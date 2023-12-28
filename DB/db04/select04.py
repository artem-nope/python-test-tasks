from create04 import Language, session


if __name__ == '__main__':
    for item in session.query(Language).all():
        print(item)
    print()
    for item in session.query(Language).order_by(Language.rating.desc()).all():
        print(item)
    print()
    for item in session.query(Language).filter(Language.year > 1990):
        print(item)
    print()
    for item in session.query(Language).filter(Language.year > 1990).order_by(Language.rating.desc()):
        print(item)
    print()

