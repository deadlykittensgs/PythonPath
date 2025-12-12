import webbrowser 
import os
from pathlib import Path


def runExe(x):
   dirName = x
#   This prints the current dir 
   smoke = Path.cwd()
#    This gets the parrent of the above dir
   corrcrDir = smoke.parent
#    this combines the parent dir with a name to give the new dir to be created
   finishedItem = f"{corrcrDir}/{dirName}"
# This creats the new dir
   os.mkdir(finishedItem)

# This rick rolls in to distract 
   url = "https://www.youtube.com/watch?v=QDia3e12czc&t=2s"
   webbrowser.open(url)
   print()

runExe("tester")

# if __name__ == "__main__":
#     runExe()