import os
import shutil

path = "folder"

try:
    #os.remove(path)        # deletes a file
    #os.rmdir(path)         # deletes an empty directory
    #shutil.rmtree(path)     # delete a directory containing files

except FileNotFoundError:
    print("The file was already deleted")

except PermissionError:
    print("You don't have permission to delete")

except OSError:
    print("You cannot delete that using that fucntion")

else:
    print("{} was deleted".format(path))
