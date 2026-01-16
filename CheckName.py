class Renamer:
    def __init__(self, AssetName : str):
        self.AssetName : str = AssetName
        self.FileExtension : str = ""
        self.NameChecked : bool = False

    def CheckName(self):

        ## Check if it's a string
        if not isinstance(self.AssetName, str):
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


    def Cleaning(self):

        if self.NameChecked == False:
            return print("Please check name before cleaning it")

        ## Remove space character at start and end
        self.AssetName = self.AssetName.strip()

        ## Replace space character inside Naming
        self.AssetName = self.AssetName.replace(" ","_")

        ## Check and replace Uppercase with lowercase
        self.AssetName = self.AssetName.lower()

        ## Add Prefix if it's not already added
        self.FileExtension = self.AssetName[self.AssetName.index(".") : len(self.AssetName)]

        if self.FileExtension == ".png" or self.FileExtension == ".jpg" or self.FileExtension == ".jpeg":

            if self.AssetName[0 : 1] != "T_":
                self.AssetName = "T_" + self.AssetName
