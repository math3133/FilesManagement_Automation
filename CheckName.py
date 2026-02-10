class AssetChecker:
    def __init__(self, SplitAssetName : tuple):
        self.AssetName : str = SplitAssetName[0]
        self.FileExtension : str = SplitAssetName[1]
        self.NameValid : bool = False
        self.PrefixValid : bool = False


    def CheckName(self):

        ## Check if it's a string
        if not isinstance(self.AssetName, str) and not isinstance(self.FileExtension, str):
            return

        ## Check if AssetName is empty
        if len(self.AssetName) < 1:
            return

        ## Check if it contains a letter, digit or underscore. no other character accepted
        validcharacter = False
        for n in range(len(self.AssetName)):
            if not self.AssetName[n].isalnum():
                    if self.AssetName[n] != "_":
                        return
            validcharacter = True

        if validcharacter == True:
            self.NameValid = True

class TextureChecker(AssetChecker):

    def PrefixCheck(self):

        if self.AssetName.startswith("T_"):
            self.PrefixValid = True
            return
        
class StaticMeshChecker(AssetChecker):

    def PrefixCheck(self):

        if self.AssetName.startswith("SM_"):
            self.PrefixValid = True
            return