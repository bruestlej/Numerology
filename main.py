class Numerology:
    def __init__(self, sName, sDOB):
        self.__sName = sName
        self.__sDOB = sDOB

    def getName(self):
        return self.__sName

    def getBirthdate(self):
        return self.__sDOB

    def getAttitude(self):
        attitudeNum = self.__reduceNum(int(self.__sDOB[0:2] + self.__sDOB[3:5]))
        return attitudeNum

    def getBirthday(self):
        birthdayNum = self.__reduceNum(int(self.__sDOB[3:5]))
        return birthdayNum

    def getLifePath(self):
        lifePathNum = self.__reduceNum(int(self.__sDOB[0:2] + self.__sDOB[3:5] + self.__sDOB[6:]))
        return lifePathNum

    def getSoul(self):
        vowels = 'aeiouAEIOU'
        soulTotal = 0
        for char in self.__sName:
            if char in vowels:
                soulTotal += self.__convertCharToInt(char)
        return self.__reduceNum(soulTotal)

    def getPersonality(self):
        vowels = 'aeiouAEIOU'
        personalityTotal = 0
        for char in self.__sName:
            if char.isalpha() and char not in vowels:
                personalityTotal += self.__convertCharToInt(char)
        return self.__reduceNum(personalityTotal)

    def getPowerName(self):
        # Power number is typically: Soul Number + Personality Number
        soulNum = self.getSoul()
        personalityNum = self.getPersonality()
        return self.__reduceNum(soulNum + personalityNum)

    def __reduceNum(self, iNum):
        # Reduce until single-digit unless it's a Master Number (optional)
        while iNum > 9:
            digits = [int(d) for d in str(iNum)]
            iNum = sum(digits)
        return iNum

    def __convertCharToInt(self, sCharacter):
        if sCharacter.isalpha():
            return ((ord(sCharacter.upper()) - 65) % 9 + 1)
        return 0
