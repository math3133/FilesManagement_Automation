import os
import CheckName

def Run_NameCheck(target_path):
    DirPath : str = target_path
    WrongFileType : list = []
    WrongAssetsName : list = []
    MissingPrefix : list = []

    ExtensionMap= {
        ".png" : CheckName.TextureChecker,
        ".jpeg" : CheckName.TextureChecker,
        ".jpg" : CheckName.TextureChecker,
        ".tga" : CheckName.TextureChecker,

        ".obj" : CheckName.StaticMeshChecker,
        ".fbx" : CheckName.StaticMeshChecker,
    }

    for root, dirs, files in os.walk(DirPath, topdown=True):
        for x in range(len(files)):

            NameTested : tuple = os.path.splitext(files[x])
            FilePath : str = os.path.join(root, files[x])

            ## Check Extension for class creation
            if NameTested[1] not in ExtensionMap:
                WrongFileType.append(FilePath)
                continue

            NameTested = ExtensionMap[NameTested[1]](NameTested)

            ## Start Name Checks
            NameTested.CheckName()

            if NameTested.NameValid == True:

                NameTested.PrefixCheck()

                if NameTested.PrefixValid != True:
                    MissingPrefix.append(FilePath)

            else:
                WrongAssetsName.append(FilePath)

    print("Name Correction is finished")

    if len(WrongFileType) > 0:
        print("Check the file type from this asset list :")
        for i in range(len(WrongFileType)):
            print(WrongFileType[i])

    if len(WrongAssetsName) > 0:
        print("Here's is the list of wrong asset names that needs to be corrected, to follow the naming convention or the tool use :")
        for i in range(len(WrongAssetsName)):
            print(WrongAssetsName[i])

    if len(MissingPrefix) > 0:
        print("These files were not accessible by the script, please check if they were open or their access was restricted")
        for i in range(len(MissingPrefix)):
            print(MissingPrefix[i])




if __name__ == "__main__":
    path_to_clean : str = "F:\\Perso\\Python\\FilesManagement_Automation\\TestFiles"
    Run_NameCheck(path_to_clean)