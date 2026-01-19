import os
import CheckName

DirPath : str = "F:/Perso/Python/FilesManagement_Automation/TestFiles"
Assets_List : list = os.listdir(DirPath)

WrongFileType : list = []
WrongAssetsName : list = []


if len(Assets_List) >= 1:
    for x in range(len(Assets_List)):

        NameTest : tuple = os.path.splitext(Assets_List[x])

        ## Check Extension for class creation
        if NameTest[1] == ".png" or NameTest[1] == ".jpeg" or NameTest[1] == ".jpg":
            NameTest = CheckName.TextureRenamer(NameTest)

        elif NameTest[1] == ".obj" or NameTest[1] == ".fbx":
            NameTest = CheckName.StaticMeshRenamer(NameTest)
        
        else:
            WrongFileType.append(Assets_List[x])
            continue


        ## Start Name Checks
        NameTest.CheckName()

        if NameTest.NameChecked == True:

            NameTest.Cleaning()
            NameTest.PrefixCheck()

            if NameTest.AssetName + NameTest.FileExtension != Assets_List[x]:
                os.rename(os.path.join(DirPath, Assets_List[x]) , os.path.join(DirPath, NameTest.AssetName + NameTest.FileExtension))

        else:
            WrongAssetsName.append(Assets_List[x])
    
    print("Name Correction is finished")

    if len(WrongFileType) > 0:
        print("Check the file type from this asset list")
        print(WrongFileType)

    if len(WrongAssetsName) > 0:
        print("Here's is the list of wrong asset names that needs to be corrected manually, to follow the naming convention or the tool use :")
        print(WrongAssetsName)

else:
    print("There are no files in the folder")