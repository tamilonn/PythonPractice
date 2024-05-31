class UserInfo:
    def __init__(self, name: str, profession: str, age: int):
        self.name = name
        self.profession = profession
        self.age = age

class PublicUserInfo:
    def __init__(self, name: str, profession: str):
        self.name = name
        self.profession = profession

user_info = UserInfo("John Malkovich", "engineer", 35)

from automapper import mapper

public_user_info = mapper.to(PublicUserInfo).map(user_info)

print(vars(public_user_info))
{'name': 'John Malkovich', 'profession': 'engineer'}
'-----------------------------------------------------------------------------------------------'


# Register
# mapper.add(UserInfo, PublicUserInfo)

# public_user_info = mapper.map(user_info)

# print(vars(public_user_info))
# {'name': 'John Malkovich', 'profession': 'engineer'}

'----------------------------------------------------------------------------------------------------'

##Map dictionary source to target object
source = {
    "name": "John Carter",
    "profession": "hero"
}
public_info = mapper.to(PublicUserInfo).map(source)

print(vars(public_info))
# {'name': 'John Carter', 'profession': 'hero'}

'---------------------------------------------------------------------------------------'

#Different field names
#If your target class field name is different from source class.

class PublicUserInfo:
    def __init__(self, full_name: str, profession: str):
        self.full_name = full_name       # UserInfo has `name` instead
        self.profession = profession

public_user_info = mapper.to(PublicUserInfo).map(user_info, fields_mapping={"full_name": user_info.name})

mapper.add(UserInfo, PublicUserInfo, fields_mapping={"full_name": "UserInfo.name"})
public_user_info = mapper.map(user_info)

print(vars(public_user_info))
# {'full_name': 'John Malkovich', 'profession': 'engineer'}

