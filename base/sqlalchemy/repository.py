
        
        
'Respoitory pattern example'
    # def get_all(self) -> List[Optional[Setup]]:
    #     setupLst = self.session.query(Setup).all()
    #     return [Setup(**setup.__dict__) for setup in setupLst]

    # def get_region(self, _id: UUID4) -> RegionOutput:
    #     region = self.session.query(Region).filter_by(id=_id).first()
    #     return RegionOutput(**region.__dict__)

    # def get_by_id(self, config_id: str) -> Type[Setup]:
    #     return self.session.query(Setup).filter_by(config_id=config_id).first()

    # def setup_exists_by_id(self, config_id: str) -> bool:
    #     setup = self.session.query(Setup).filter_by(config_id=config_id).first()
    #     return setup is not None

    # def region_exists_by_name(self, name: str) -> bool:
    #     region = self.session.query(Region).filter_by(name=name).first()
    #     return region is not None

    # def update(self, region: Type[Region], data: RegionInput) -> RegionInput:
    #     region.name = data.name
    #     self.session.commit()
    #     self.session.refresh(region)
    #     return RegionInput(**region.__dict__)

    # def delete(self, region: Type[Region]) -> bool:
    #     self.session.delete(region)
    #     self.session.commit()
    #     return True