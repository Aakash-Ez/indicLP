from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

supported = ["en","hi","ta"]
definition = {"en":sanscript.ITRANS,"ta":sanscript.TAMIL, "hi": sanscript.DEVANAGARI}

class Transliterate:
    def __init__(self, f = "en", t = "hi"):
        assert f in supported, "ERROR: From Language no supported. Supported languages are: " + str(supported)
        assert t in supported, "ERROR: To Language no supported. Supported languages are: " + str(supported)
        self.f = definition[f]
        self.t = definition[t]
    def convert(self, data):
        assert type(data) == str, "ERROR: Expected string as input, received "+type(data)
        return transliterate(data,self.f,self.t)
    def revert(self, data):
        assert type(data) == str, "ERROR: Expected string as input, received "+type(data)
        return transliterate(data,self.t,self.f)