
from pydantic import BaseModel, UUID4, Field


class RegionInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    configno: int = 0


class RegionOutput(BaseModel):
    id: UUID4
    name: str


# if __name__ == '__main__':
#     region = RegionInput('Hi', 100)
#     region.name = 'Hello'
#     region.configno = 1234

#     region.model_dump(exclude_none=True)

#     # print(region.json)