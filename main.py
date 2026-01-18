import os
import CheckName

DirPath : str = "F:/Perso/Python/FilesManagement_Automation/TestFiles"
Assets_List : list = os.listdir(DirPath)

WrongAssetsName : list = []

if len(Assets_List) >= 1:
    for x in range(len(Assets_List)):

        NameTest = CheckName.AssetRenamer(Assets_List[x])
        NameTest.CheckName()

        if NameTest.NameChecked == True:
            NameTest.Cleaning()

            if NameTest.AssetName != Assets_List[x]:
                os.rename(os.path.join(DirPath, Assets_List[x]) , os.path.join(DirPath, NameTest.AssetName))

        else:
            WrongAssetsName.append(Assets_List[x])
    
    print("Name Correction is finished")

    if len(WrongAssetsName) > 0:
        print("Here's is the list of wrong asset names that needs to be corrected manually, to follow the naming convention or the tool use :")
        print(WrongAssetsName)

else:
    print("There are no files in the folder")