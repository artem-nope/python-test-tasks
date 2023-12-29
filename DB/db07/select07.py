from create07 import Pupil, Group, Section, session

if __name__ == '__main__':
    for item in session.query(Section, Pupil, Group) \
            .select_from(Pupil).join(Section.pupils).join(Group).all():
        print(item)

# avg weight, mark, count sex
