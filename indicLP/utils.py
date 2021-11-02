class SentenceIterator: 
    def __init__(self, filepath, delim = "\n"): 
        self.filepath = filepath 
        self.delim = delim
    def __iter__(self): 
        for txt in open(self.filepath, encoding="utf-8"): 
            for line in txt.split(self.delim):
                yield line