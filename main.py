import os
import urllib.request
import json

def directory_and_textures():
    # Creating directory
    dir_name = ""
    dir_created = False
    while not dir_created:
        dir_name = input("\nEnter what you want to name your mod folder: ") + " Mod"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print("\nFolder created successfully")
            dir_created = True
        else:
            print("\nTry using a different name since that folder already exists")

    # Downloading files to directory
    print("\nDownloading texture files to folder...")
    links = ["https://raw.githubusercontent.com/mestiez/ppg-snippets/master/Human%20textures/bone%20layer.png", 
             "https://raw.githubusercontent.com/mestiez/ppg-snippets/master/Human%20textures/flesh%20layer.png",
             "https://raw.githubusercontent.com/mestiez/ppg-snippets/master/Human%20textures/skin%20layer.png"]
    files = ["bone.png", "flesh.png", "skin.png"]
    for i in range(3):
        filename = os.path.join(dir_name, files[i])
        urllib.request.urlretrieve(links[i], filename)
    print("\nFiles successfully downloaded for you to edit")

def cs_maker():
    # User input
    name = input("\nEnter what you want your mod to be called: ")
    description = input("\nEnter what you want your mod's description to be: ")
    thumbnail = input("\nEnter the name of the file, including the file extension, that you want to be the thumbnail for your mod (you need to add this yourself): ")

    # Writing the file
    filename = "script.cs"
    print("\nCreating script.cs...")
    with open(filename, 'w') as file:
        file.write("using UnityEngine;\n\n")
        file.write("namespace Mod {\n\n")
        file.write("\tpublic class Mod {\n\n")
        file.write("\t\tpublic static void Main() {\n")
        file.write("\t\t\tModAPI.Register(\n")
        file.write("\t\t\t\tnew Modification() {\n")
        file.write('\t\t\t\t\tOriginalItem = ModAPI.FindSpawnable("Human"),\n')
        file.write('\t\t\t\t\tNameOverride = "' + name + '",\n')
        file.write('\t\t\t\t\tDescriptionOverride = "' + description + '",\n')
        file.write('\t\t\t\t\tCategoryOverride = ModAPI.FindCategory("Entities"),\n')
        file.write('\t\t\t\t\tThumbnailOverride = ModAPI.LoadSprite("' + thumbnail + '"),\n')
        file.write("\t\t\t\t\tAfterSpawn = (Instance) => {\n")
        file.write('\t\t\t\t\t\tvar skin = ModAPI.LoadTexture("skin.png");\n')
        file.write('\t\t\t\t\t\tvar flesh = ModAPI.LoadTexture("flesh.png");\n')
        file.write('\t\t\t\t\t\tvar bone = ModAPI.LoadTexture("bone.png");\n\n')
        file.write("\t\t\t\t\t\tvar person = Instance.GetComponent<PersonBehaviour>();\n")
        file.write("\t\t\t\t\t\tperson.SetBodyTextures(skin, flesh, bone, 1);\n")
        file.write("\t\t\t\t\t}\n")
        file.write("\t\t\t\t}\n")
        file.write("\t\t\t);\n")
        file.write("\t\t}\n")
        file.write("\t}\n")
        file.write("}")
        print("\nscript.cs created successfully")

def json_maker():
    # User input
    name = input("\nEnter what you want the mod's title to be: ")
    author = input("\nEnter what you want the mod's author to be: ")
    description = input("\nEnter what you want the mod's description to be: ")
    mod_version = input("\nEnter the version of the mod: ")
    game_version = input("\nEnter what version of the game this is for (current version is 1.26.6): ")
    thumbnail = input("\nEnter the name of the file, including the file extension, that you want to be the thumbnail for your mod (you need to add this yourself): ")
    print("\nCreating mod.json...")

    # Writing the file
    mod = {
        "Name": name,
        "Author": author,
        "Description": description,
        "ModVersion": mod_version,
        "GameVersion": game_version,
        "ThumbnailPath": thumbnail,
        "EntryPoint": "Mod.Mod",
        "Tags": [
            "Fun"
        ],
        "Scripts": [
            "script.cs"
        ]
    }
    with open("mod.json", 'w') as f:
        json.dump(mod, f)
    print("\nmod.json successfully created")

def main():
    print("Welcome to the PPG Human Texture Maker!")
    done = False
    while not done:
        make_stuff = input("\nEnter d to create the mod folder and download the textures, c to create the C# file, j to create the JSON file, or q to quit: ")
        if make_stuff == 'd':
            directory_and_textures()
        elif make_stuff == 'c':
            cs_maker()
        elif make_stuff == 'j':
            json_maker()
        elif make_stuff == 'q':
            done = True
            print("\nThanks for using this silly little program!")
        else:
            print("\nNot a recognized input")

main()
