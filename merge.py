from filesplit.merge import Merge

print("Enter the Location of data chunks you want to merge :")
inp=input()
print("Enter the destination of Merged file :")
out=input()
print("Enter the name of file Merged File :")
name=input()

try:
    merge=Merge(inp,out,name).merge(True)
    print("Files Merged Successfully. You can Locate file at"+out)
except:
    print("An Error occured during merging the files. Try again")
