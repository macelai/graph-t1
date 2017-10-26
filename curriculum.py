from graph import Graph

class Course(object):

    def __init__(self, name, credits, semester, prereq):
        self.__name = name
        self.__credits = credits
        self.__semester = semester
        self.__prereq = prereq

    
    @property
    def name(self):
        return self.__name



class Curriculum(object):
    
    def __init__(self):
        self.__courses = [
            Course("eel5105", 5, 1, []),
            Course("ine5401", 2, 1, []),
            Course("ine5402", 6, 1, []),
            Course("ine5403", 6, 1, []),
            Course("mtm3101", 4, 1, []),
            Course("ine5404", 6, 2, ["ine5402"]),
            Course("ine5405", 5, 2, ["mtm3101"]),
            Course("ine5406", 5, 2, ["eel5105"]),
            Course("ine5407", 3, 2, []),
            Course("mtm5512", 4, 2, []),
            Course("mtm7174", 4, 2, ["mtm3101"]),
            Course("ine5408", 6, 3, ["ine5404"]),
            Course("ine5409", 4, 3, ["mtm5512", "mtm7174"]),
            Course("ine5410", 4, 3, ["ine5404"]),
            Course("ine5411", 6, 3, ["ine5406"]),
            Course("mtm5245", 4, 3, ["mtm5512"]),
            Course("ine5412", 4, 4, ["ine5410", "ine5411"]),
            Course("ine5413", 4, 4, ["ine5403", "ine5408"]),
            Course("ine5414", 4, 4, ["ine5404"]),
            Course("ine5415", 4, 4, ["ine5403", "ine5408"]),
            Course("ine5416", 5, 4, ["ine5408"]),
            Course("ine5417", 5, 4, ["ine5408"]),
            Course("ine5418", 4, 5, ["ine5412", "ine5414"]),
            Course("ine5419", 4, 5, ["ine5417"]),
            Course("ine5420", 4, 5, ["ine5408", "mtm5245", "mtm7174"]),
            Course("ine5421", 4, 5, ["ine5415"]),
            Course("ine5422", 4, 5, ["ine5414"]),
            Course("ine5423", 4, 5, ["ine5408"]),
            Course("ine5424", 4, 6, ["ine5412"]),
            Course("ine5425", 4, 6, ["ine5405"]),
            Course("ine5426", 4, 6, ["ine5421"]),
            Course("ine5427", 4, 6, ["ine5421"]),
            Course("ine5430", 4, 6, ["ine5405", "ine5413", "ine5416"]),
            Course("ine5453", 1, 6, ["ine5417"]),
            Course("ine5428", 4, 7, ["ine5407"]),
            Course("ine5429", 4, 7, ["ine5403", "ine5414"]),
            Course("ine5431", 4, 7, ["ine5414"]),
            Course("ine5432", 4, 7, ["ine5423"]),
            Course("ine5433", 6, 7, ["ine5427", "ine5453"]),
            Course("ine5434", 9, 8, ["ine5433"])
        ]
        self.g = Graph()
        

    def populate_graph(self):
        for course in self.__courses:
            self.g.add_vertex(course)
        for c in self.g.vertices():
            print c.name()
            

