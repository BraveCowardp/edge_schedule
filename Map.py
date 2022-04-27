class Map:

    width=0
    length=0

    @classmethod
    def set_size(cls,width,length):
        cls.width=width
        cls.length=length

    @classmethod
    def generate(cls):
        