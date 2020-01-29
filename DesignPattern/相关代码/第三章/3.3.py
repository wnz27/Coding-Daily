from abc import ABCMeta, abstractmethod

# Product
class Section(metaclass = ABCMeta):
    @abstractmethod
    def describe(self):
        pass

# ConcreteProduct
class PersonalSection(Section):
    def describe(self):
        print("Personal Section!!!")

# ConcreteProduct
class AlbumSection(Section):
    def describe(self):
        print("Album Section!!!")

# ConcreteProduct
class PatentSection(Section):
    def describe(self):
        print("Patent Section!!!")

# ConcreteProduct
class PublicationSection(Section):
    def describe(self):
        print("Publication Section!!!")

# Creator
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)

# ConcreteCreator
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

# ConcreteCreator
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

# client
if __name__ == "__main__":
    profile_type = input("Which Profile you'd like to create? [LinkedIn or Facebook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile...", type(profile).__name__)
    print("Profile has sections --", profile.getSections())




    