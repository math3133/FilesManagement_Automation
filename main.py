import os
import CheckName

def run_renamer(target_path):
    DirPath : str = target_path
    FilesUnaccessible : list = []
    WrongFileType : list = []
    WrongAssetsName : list = []


    for root, dirs, files in os.walk(DirPath, topdown=True):
        for x in range(len(files)):

            NameTest : tuple = os.path.splitext(files[x])

            ## Check Extension for class creation
            if NameTest[1] == ".png" or NameTest[1] == ".jpeg" or NameTest[1] == ".jpg":
                NameTest = CheckName.TextureRenamer(NameTest)

            elif NameTest[1] == ".obj" or NameTest[1] == ".fbx":
                NameTest = CheckName.StaticMeshRenamer(NameTest)
            
            else:
                WrongFileType.append(os.path.join(root, files[x]))
                continue


            ## Start Name Checks
            NameTest.CheckName()

            if NameTest.NameChecked == True:

                NameTest.Cleaning()
                NameTest.PrefixCheck()

                if NameTest.AssetName + NameTest.FileExtension != files[x]:

                    ## Try renaming the files if it doesn't works print the error prompt, and add to a list
                    try :
                        os.rename(os.path.join(root, files[x]) , os.path.join(root, NameTest.AssetName + NameTest.FileExtension))

                    except Exception as ErrorPrompt:
                        FilesUnaccessible.append(os.path.join(root, files[x]))
                        print(ErrorPrompt)

            else:
                WrongAssetsName.append(os.path.join(root, files[x]))

    print("Name Correction is finished")

    if len(WrongFileType) > 0:
        print("Check the file type from this asset list")
        print(WrongFileType)

    if len(WrongAssetsName) > 0:
        print("Here's is the list of wrong asset names that needs to be corrected manually, to follow the naming convention or the tool use :")
        print(WrongAssetsName)

    if len(FilesUnaccessible) > 0:
        print("These files were not accessible by the script, please check if they were open or their access was restricted")
        print(FilesUnaccessible)

if __name__ == "__main__":
    path_to_clean : str = "F:\\Perso\\Python\\FilesManagement_Automation\\TestFiles"
    run_renamer(path_to_clean)