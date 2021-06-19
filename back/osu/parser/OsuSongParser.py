class OsuSongParser:
    songFile = None

    videoFileName = None
    audioFileName = "audioFileName"

    def openSongFile(self, filePath):
        self.songFile = open(filePath).readlines()

    def getBlockLine(self, phrase):
        for num, line in enumerate(self.songFile, 0):
            if phrase in line:
                return num


class Block:
    class __Base:
        blockLine = -1
        blockName = "blockName"

    class General(__Base):
        def __init__(self):
            self.blockName = "[General]"

    class Metadata(__Base):
        def __init__(self):
            self.blockName = "[Metadata]"

    class Difficulty(__Base):
        def __init__(self):
            self.blockName = "[Difficulty]"

    class Events(__Base):
        def __init__(self):
            self.blockName = "[Events]"
