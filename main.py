class Numerology:
    def _init_(self, sName, sDOB):
        self.__sName = sName
        self.__sDOB = sDOB
        

    def getName(self):
        return self.__sName

    def getBirthdate(self):
        return self.__sDOB

    def getAttitude(self):
      self.sAttitudeNum = self.__reduceNum(int(self.__sDOB[0:2] + self.__sDOB[3:5]))
      return self.__sAttitudeNum

    def getBirthday(self):
      self.sBirthdayNum = self.__reduceNum(int(sDOB[3:5]))
      return self.__sBirthdayNum

    def getLifePath(self):
        self.sLifePathNum = self.__reduceNum(int(self.__sDOB[0:2] + self.__sDOB[3:5] + self.__sDOB[6:]))
        return self.__sLifePathNum

    def getPersonality(self):
        lstVowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

        lstVowel2Num = []
        lstCon2Num = []
      
        for lstVowels not in sName:


    def getPowerName(self):
        sPowerNum = sSoulNum + sPersonalityNum

    def getSoul(self):
        for lstVowels in sName:



    def __reduceNum(self, iNum):

        iMultiDigit = int(iNum)

        while iMultiDigit > 9:
            iMultiDigit = iMultiDigit // 10 + iMultiDigit % 10
        return iMultiDigit

    def __convertCharToInt(self, sCharacter):

      iCharacterToNumberValue = 0

      if sCharacter.isalpha():

        iCharacterToNumberValue = (( ord(sCharacter.upper() ) - 65) % 9 + 1)

      return iCharacterToNumberValue