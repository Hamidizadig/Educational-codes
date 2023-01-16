from abc import ABC, abstractmethod
from datetime import datetime
import enum
class BookStatus(enum.Enum):
    UnSelected = 1
    Selected = 2
    Translate = 3
class Text(ABC):
    def __init__(self, lang, numberOfDay):
        self.lang = lang
        self.unmberOfDay = numberOfDay
        self.staus = BookStatus.UnSelected
        self.registerDate = datetime.now()
    def getLang(self):
        return self.lang
    @abstractmethod
    def getFee(self):
        pass
    def changeStatus(self, newStatus):
        self.staus = newStatus
    def __str__(self):
        return f"{self.lang}\t{self.numberOfDay}\t{self.registerDate}\t{self.staus}"
class PlainText(Text):
    def __init__(self, lang, numberOfDay, numberWord, numberLongWord):
        super().__init__(lang, numberOfDay)
        self.__numberWord = numberWord
        self.__numberLongWord = numberLongWord
    def getFee(self):
        return self.__numberWord*500+self.__numberLongWord*600
class SciText(Text):
    def __init__(self, lang, numberOfDay, numberSciWord, numberGeneralWord):
        super().__init__(lang, numberOfDay)
        self.__nunberSciWord = numberSciWord
        self.__numberGeneralWord = numberGeneralWord
    def getFee(self):
        return self.__numberGeneralWord*600+self.__nunberSciWord*100
class HumorosText(Text):
    def __init__(self, lang, numberOfDay, numberImage):
        super().__init__(lang, numberOfDay)
        self.__numberImage = numberImage
    def getFee(self):
        return self.__numberImage*300000
class Book(Text):
    def __init__(self, lang, numberOfDay):
        super().__init__(lang, numberOfDay)
        self.__textList = []
    def addText(self, text):
        self.__textList.append(text)
    def getFee(self):
        sum = 0
        for text in self.__textList:
            sum += text.getFee()
        return sum
class Translator:
    def __init__(self, name, family, mobile):
        self.__name = name
        self.__family = family
        self.__mobile = mobile
        self.__isActive = False
        self.__langList = []
    def addLang(self, lang):
        self.__langList.append(lang)
    def __str__(self):
        temp = self.__name+"\t"+self.__family+"\t" + \
            self.__mobile+"\t"+str(self.__isActive)+"\n"
        for lang in self.__langList:
            temp += lang+"\n"
        return temp
    def selectText(self, text):
        if self.__isActive == False:
            if text.status == BookStatus.UnSelected:
                text.changeStatus(BookStatus.Selected)
                self.__isActive = True
            else:
                print('This text is selected')
        else:
            print("Can not more text select")
    def afterTranslate(self, text):
        text.changeStatus(BookStatus.Translate)
motarjem1 = Translator('alix', 'rizax', '0977777777')
motarjem1.addLang('EN')
motarjem1.addLang('FR')
print(motarjem1)
motarjem2 = Translator('samek', 'saklis', '0977848484877')
motarjem2.addLang('EN')
print(motarjem2)
book1 = Book('EN', 40)
book1.addText(PlainText('EN', 12, 1200, 250))
book1.addText(SciText('EN', 28, 3000, 1500))
motarjem2.selectText(book1)
print(book1.getFee())
print(motarjem2)
print(book1)
