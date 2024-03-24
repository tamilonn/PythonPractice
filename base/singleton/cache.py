#THis is singleton class with only one instance creation

class Cache(object):

    _values = {} # private dict


    #Make a singleton object creation
    def __new__(cls):
        print('...inside new()...')
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cache, cls).__new__(cls)

        return cls.instance
    

    def __init__(self) -> None:

        print('.... inside init()...')
        self._values = self.__load()


    def __load(self):
        print('.....inside load()...')
        print(self._values)

        if (self._values == {}):
            print('Adding values....')
            return {"1": "one",  "2" : "two"} 
        else: 
            print('Returning cache values....')
            return self._values
      
        
        


    # @property
    # def values(self):
    #     print('..... inside GET values()....')
    #     return self._values
    




if __name__ == '__main__':
    cache = Cache()

    print(cache._values)

    cache2 = Cache()
    print(cache2._values)

    cache2._values = {} # This does not empty dict, since we use private attribute with __

    print('After reseting {} to cache2....')
    print(cache._values)
    print(cache2._values)




    print (cache is cache2)


