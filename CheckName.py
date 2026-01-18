import os

class AssetRenamer:
    def __init__(self, AssetName : str):
        self.SplitAssetName : list = list(os.path.splitext(AssetName))
        self.FileExtension : str = ""
        self.NameChecked : bool = False
        self.AssetName : str = ""

    def CheckName(self):

        ## Check if it's a list
        if not isinstance(self.SplitAssetName, list):
            return

        ## Check if AssetName is empty
        if len(self.SplitAssetName[0]) < 1:
            return
        
        ## Check if it has an extension
        if len(self.SplitAssetName[1]) < 1:
            return

        ## Check if it contains a letter or digit
        name = self.SplitAssetName[0]
        for n in range(len(name)):
            
            if name[n] >= "A" and name[n] <= "Z":
                self.NameChecked = True
                return
            
            if name[n] >= "a" and name[n] <= "z":
                self.NameChecked = True
                return
            
            if name[n] >= "0" and name[n] <= "9":
                self.NameChecked = True
                return


    def Cleaning(self):

        if self.NameChecked == False:
            return print("Please check name before cleaning it")

        ## Remove space character at start and end
        self.SplitAssetName[0] = self.SplitAssetName[0].strip()

        ## Replace space character inside Naming
        self.SplitAssetName[0] = self.SplitAssetName[0].replace(" ","_")

        ## Check and replace Uppercase with lowercase
        self.SplitAssetName[0] = self.SplitAssetName[0].lower()

        ## Reconstruct Name
        self.AssetName = self.SplitAssetName[0] + self.SplitAssetName[1]