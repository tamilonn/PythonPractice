from dataclasses import dataclass
from typing import Optional
from mapper.object_mapper import ObjectMapper
# from collections import MutableMapping
# import collections.abc
# collections.MutableMapping = collections.abc.MutableMapping

# @dataclass
# class UserEntity:

#     first_name: Optional[str] = None
#     last_name: Optional[str] = None
#     email: Optional[str] = None
#     password: Optional[str] = None



# @dataclass
# class UserDTO:

#     name: Optional[str] = None
#     emailId: Optional[str] = None




# define mappings
# mapping = {
#  "name":     lambda entity: entity.first_name,
#  'emailId':  lambda entity: entity.email
# }

# mapper = ObjectMapper()
# mapper.create_map(UserEntity, UserDTO, mapping)

# user_entity = UserEntity("Yusuf", "Malkan", "yusuf.aziz@gmail.com", 'xyz123')
# # get a instance of UserDTO
# user_dto = mapper.map(user_entity, UserDTO)

# if __name__ == '__main__':
#     mapper = ObjectMapper()
#     mapper.create_map(UserEntity, UserDTO, mapping)

#     user_entity = UserEntity("Yusuf", "Malkan", "yusuf.aziz@gmail.com", 'xyz123')
#     # get a instance of UserDTO
#     user_dto = mapper.map(user_entity, UserDTO)

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

class UserDTO:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

class ObjectMapper:
    @staticmethod
    def map_user_to_user_dto(user):
        return UserDTO(user.id, user.username, user.email)

# Example usage
user = User(1, "john_doe", "john@example.com")
user_dto = ObjectMapper.map_user_to_user_dto(user)

print(user_dto.id, user_dto.username, user_dto.email)