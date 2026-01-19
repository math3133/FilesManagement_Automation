class AssetRenamer:
    def __init__(self, SplitAssetName : tuple):
        self.AssetName : str = SplitAssetName[0]
        self.FileExtension : str = SplitAssetName[1]
        self.NameChecked : bool = False


    def CheckName(self):

        ## Check if it's a string
        if not isinstance(self.AssetName, str) and not isinstance(self.FileExtension, str):
            return

        ## Check if AssetName is empty
        if len(self.AssetName) < 1:
            return
        
        ## Check if it contains a letter or digit
        for n in range(len(self.AssetName)):
            
            if self.AssetName[n] >= "A" and self.AssetName[n] <= "Z":
                self.NameChecked = True
                return
            
            if self.AssetName[n] >= "a" and self.AssetName[n] <= "z":
                self.NameChecked = True
                return
            
            if self.AssetName[n] >= "0" and self.AssetName[n] <= "9":
                self.NameChecked = True
                return


    def Cleaning(self):

        if self.NameChecked == False:
            print("Please check name before cleaning it")
            return

        ## Remove space character at start and end
        self.AssetName = self.AssetName.strip()

        ## Replace space character inside Naming
        self.AssetName = self.AssetName.replace(" ","_")

        ## Check and replace Uppercase with lowercase
        self.AssetName = self.AssetName.lower()

class TextureRenamer(AssetRenamer):

    def PrefixCheck(self):

        if self.NameChecked == False:
            print("Please check name before cleaning it")
            return

        if self.AssetName[0 : 2] == "T_":
            return

        if self.AssetName[0 : 2] == "t_":
            self.AssetName = "T_" + self.AssetName[2 : len(self.AssetName)]
            return

        self.AssetName = "T_" + self.AssetName

class StaticMeshRenamer(AssetRenamer):

    def PrefixCheck(self):

        if self.NameChecked == False:
            print("Please check name before cleaning it")
            return

        if self.AssetName[0 : 3] == "SM_":
            return
        
        if self.AssetName[0 : 3] == "Sm_" or self.AssetName[0 : 3] == "sM_" or self.AssetName[0 : 3] == "sm_":
            self.AssetName = "SM_" + self.AssetName[3 : len(self.AssetName)]
            return
        
        self.AssetName = "SM_" + self.AssetName