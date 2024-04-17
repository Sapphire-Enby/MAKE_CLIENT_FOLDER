# Makes a folder called datafolder in current directory
# fills datafolder with "client folders"

#   "client folders" contents:
#       - Data.txt
#       - ./cData
#   
#   - Data.txt formatting:
#   # [name, address, phone, mail,]
#   $ {Key}: {Value}
#
#   -./cData
#   Empty Directory to stuff client's files
#   Could be renamed to Entry Specific Files
#   To be hlinked to later in mains output
#
#
#
# TODO:NOW
# use  [name, address, phone, mail] to generate dict random entries
# write dict out to data.txt with below format 
# $ {Key}: {Value}
from faker import Faker
from pathlib import Path
#Startup: make keys, clientdir and faker
f = Faker()
keys = ["name", "address", "phone", "mail"]
clientDict = dict.fromkeys(keys)
clientRepo = Path("datafolder")

def genClient():
    #Generate new fake clientDict
    clientDict.update(f.profile(keys).items())
    clientDict["phone"] = f.phone_number()
    adrFix = clientDict["address"].replace("\n"," ")
    clientDict["address"] = adrFix

def writeClient():
    #write out to file
    with open("outfile.txt","w") as file:
        for k, v in clientDict.items():
            file.write(f"{k}: {v}\n")

def makeClientFolder():
    global clientRepo
    global clientFolder
    clientFolder = Path(clientRepo / clientDict["name"])
    clientFolder.mkdir(parents=True, exist_ok=True)
    #         write data.txt  
#make client data file, needs client folder to be up to date
def makeClientDataFile():
    clientDataFile = Path(clientFolder / "data.txt")
    with clientDataFile.open("w") as file:
        for k, v in clientDict.items():
            file.write(f"{k}: {v}\n")

def makeClientSpecificDataFolder():#         makedir cdata
    clientSpecificDataFolder = Path(clientFolder / "cData")
    clientSpecificDataFolder.mkdir(parents=True, exist_ok=True)
#Testing
def makeClient(count=1):
    for i in range(count):
        genClient()
        makeClientFolder()
        makeClientDataFile()
        makeClientSpecificDataFolder();
#TODO Cleanup main
def main():
    clientRepo.mkdir(parents=True, exist_ok=True)
    def intCheck(instr):
        try:
            int(instr)
            return True
        except ValueError:
            return False

    if len(sys.argv) > 1:
        first_arg = sys.argv[1]
        if intCheck(first_arg):
            first_arg = int(first_arg)
        if isinstance(first_arg, int) and first_arg >= 0:
            makeClient(first_arg)
        else:
            makeClient()
    else:
        makeClient()
if __name__ == "__main__":
    import sys
    main()
