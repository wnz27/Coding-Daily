class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, ** kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print(super(),cls,'+',cls._instances)
        return cls._instances[cls]
    
class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)