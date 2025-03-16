from email.policy import default
import json

def print_default_name(self) -> dict:
    name = "f_name"
    dictionary: dict = dict({
        name: "sinni"
    })
    return dictionary

class go_go():
    def print_name(self) -> None:
        res = json.dumps(self, skipkeys = True, default = print_default_name)
        if isinstance(res, str):
            print(res)
        else:
            print("400: Bad Request")

obj = go_go()
obj.print_name();

game_level = 0
if game_level == 0:
    hero = "me"

print(hero)