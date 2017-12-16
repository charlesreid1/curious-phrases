import glob

print("WARNING:")
print("This will permanently modify the .md files.")
print("Make sure you have backups!")
print("\n\n\n")

# Don't bother asking for user input...
# but if you did you'd say, if raw_input=='y', then go.
if(True):

    for md in glob.glob("*.md"):

        print("Processing %s..."%(md))
       
        # read the lines of the file
        with open(md,'r') as f:
            lines = f.readlines()
        
        # purge lines of empty lines and of only-uppercase lines
        purged = [j for j in lines if len(j)>3 and j.upper()!=j]
    
        with open(md,'w') as f:
            f.write("\n".join(purged))

        print("Done with %s.\n"%(md))
