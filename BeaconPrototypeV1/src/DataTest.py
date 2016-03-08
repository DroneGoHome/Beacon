import sys, subprocess
sys.path.append(r"C:\Users\Taylor\AppData\Local\Programs\Python\Python35-32\Lib\site-packages")


with open("C:\\Users\\Taylor\\Documents\\GitHub\\DataCollection\\test.csv",'a') as myfile:
    myfile.write("\nPost-Commit")
print("opened file, calling git")
    
p = subprocess.Popen([r"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "-ExecutionPolicy", "Unrestricted", "-File",
              "C:/Users/Taylor/Documents/LiClipse Workspace/BeaconPrototypeV1/src/Git.ps1"], 
              stdout=sys.stdout)
p.communicate()
print("finished")