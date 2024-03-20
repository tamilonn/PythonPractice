import os
from dotenv import dotenv_values , load_dotenv


#os
path = os.environ["PATH"]
# print(path)

os.environ["DATABASE_URL"] = "new_database_url"
print(os.environ.get("DATABASE_URL"))

load_dotenv(override=True)

#.env_dev
config = dotenv_values(".env_dev")
print(config)

#.env_uat
config = dotenv_values(".env_uat")
print(config)

