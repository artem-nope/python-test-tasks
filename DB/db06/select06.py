from create06 import Pupil, Group, session
from sqlalchemy import func


if __name__ == '__main__':
    for item in session.query(Pupil).order_by(Pupil.mark.desc()):
        print(item, item.mark, item.weight, item.group)

    print('* * * ' * 10)

    for item in session.query(Group).all():
        print(item)
        print(item.pupils)

    print('* * * ' * 10)

    for p, g in session.query(Pupil, Group).select_from(Group).join(Pupil.group).all():
        print(p.name, g.name)

    print('* * * ' * 10)

    for item in session.query(Group.name, func.avg(Pupil.mark)).select_from(Group)\
            .join(Pupil.group).group_by(Group.id).order_by(Group.name):
        print(item)
