class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
        s, s1 = Singleton(), Singleton()
        if s is not s1:
            raise Exception('Singleton doesn\'t work!')