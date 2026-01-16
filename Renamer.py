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

        ## Remove space character at start
        while self.AssetName[0] == " ":
            self.AssetName = self.AssetName[1 : len(self.AssetName)]

        ## Remove Space character at end
        while self.AssetName[len(self.AssetName) - 1] == " ":
            self.AssetName = self.AssetName[0 : len(self.AssetName) - 1]
        
        ## Replace space character inside Naming
        while " " in self.AssetName:
            self.AssetName = self.AssetName[0 : self.AssetName.index(" ")] + "_" + self.AssetName[self.AssetName.index(" ") + 1 : len(self.AssetName)]

        ## Check and replace Uppercase with lowercase
        for i in range(len(self.AssetName)):
            if self.AssetName[i].isupper():
                self.AssetName = self.AssetName[0 : i] + self.AssetName[i].lower() + self.AssetName[i + 1 : len(self.AssetName)]

        ## Add Prefix if it's not already added
        self.FileExtension = self.AssetName[self.AssetName.index(".") : len(self.AssetName)]

        if self.FileExtension == ".png" or self.FileExtension == ".jpg" or self.FileExtension == ".jpeg":

            if self.AssetName[0 : 1] != "T_":
                self.AssetName = "T_" + self.AssetName
        



liste_assets = [
    "  MonHero_FINAL.jpg ",
    "Mur de Pierre.png",
    "   ", 
    None, 
    "INTERFACE_USER.png",
    12345,
    "decor_rocher.fbx"
]

Wrong_assets : list = []

for x in range(len(liste_assets)):

    NameTest = Renamer(liste_assets[x])
    NameTest.CheckName()

    if NameTest.NameChecked == True:
        NameTest.Cleaning()

        if NameTest.AssetName != liste_assets[x]:
            liste_assets[x] = NameTest.AssetName
    
    else:
        Wrong_assets.append(liste_assets[x])

print("Here's the asset list with corrected name :")
print(liste_assets)

print("Here's is the list of wrong asset names that needs to be corrected manually, to follow the naming convention or the tool use :")
print(Wrong_assets)