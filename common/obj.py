import datetime
import json
import jsonpickle

from common.util import Team, HouTeam

team=Team(12,"Houston")
print(team.team_name)
print(team.team_id)

team2=Team("12id","Houston")
print(team2.team_name)
print(team2.team_id)

team2.show_team_name()

print(team2.public_var)
#print(team2.__private_var)

hou=HouTeam(12,"Houston")
hou.show_team_name()

print(datetime.datetime.now())



#import doctest
#doctest.testmod()

data={
    'id': 1,
    'name': 'hou',
    'url': 'https://hou.nba.com'
}

data_json=json.dumps(data)
print(data_json)

data2=json.loads(data_json)
print(type(data2))
print(data2)

json_string = jsonpickle.encode(team, indent=4)
print(json_string)

team_from_json=jsonpickle.decode(json_string)
print(team_from_json.show_team_name())