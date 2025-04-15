import os


class Util:
    def print_message(self, message):
        print(message)


def pt():
    print("hello in pt")


def read_file_by_line(filepath):
    f=open(filepath,"r")
    for line in f:
        print(line)
    f.close()


def listdir(filepath):
    return os.listdir(filepath)

class Team:
    public_var=''
    # 私有化属性，不能对外访问
    __private_var=''
    def __init__(self,team_id,team_name):
        print(f"team instance is init now {team_id} {team_name}")
        self.team_id=team_id
        self.team_name=team_name
        self.public_var=team_name
        self.__private_var=team_name

    def show_team_name(self):
        print(f"TEAM NAME IS {self.team_name}")
        print(self)
        print(self.__class__)

class HouTeam(Team):
    def __init__(self,team_id,team_name):
        Team.__init__(self,team_id,team_name)
        self.city="Houston"

    def show_team_name(self):
        print(f"TEAM NAME IS {self.team_name} IN CITY {self.city}")