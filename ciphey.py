import os,webbrowser, time, subprocess


enc=input("Enter Value") 
subprocess.run("ciphey " + "-t " + " \"" + enc + "\"", shell=True)
#str="ciphey " + "-t " + " \"" + enc + "\""
#print(str)