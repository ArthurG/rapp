from pydub import AudioSegment
'''
def main(file, array):
   
    sound = AudioSegment.from_file(file)
    
    section=0
    names=[]
    choppedFileName = file[:-4]
    
    fractionals=[]
    
    i = 0 
    fractionals.append(0)
    for j in range(1, len(array)):
        fractionals.append((array[j]-array[i])/len(sound))
        i += 1

    fractionals.append(1)

    for j in fractionals:
        print(j)

    i=0
    for j in fractionals:
        if(j==0):
            continue
        print(i, " and the ", j);
        print(len(sound))
        next_part = sound[len(sound)*i: len(sound)*j]
        i = j
        section += 1
        next_part.export(choppedFileName + "_%d" % section + ".3gp")
        print (choppedFileName + "we splitted out section %d" % section + ".3gp")
        names.append(choppedFileName + "_%d" % section + ".3gp")

    return names
'''
    



'''
def merge(fileArr, fileNameUserWantsMergedFileToBe):
    mergedFile = AudioSegment.from_file(fileArr[0], "3gp")
    for file in fileArr:
        if(file == fileArr[0]):
            continue
        sound = AudioSegment.from_file(file, "3gp")
        mergedFile += sound
    
    mergedFile.export(fileNameUserWantsMergedFileToBe)

 '''   

#main("rapp4.3gp", [30000,31000,35000])

#merge(["poop.mp3", "reverse.mp3", "1486231725915.3gp" ,    "1486235464774.3gp"     ,
#"1486236990831.3gp"     ,
#"1486238870432.3gp"   ,  
#"1486249802936.3gp",
#], "fartypants.mp3")

#merge(["1486266684133.3gp","1486266684133.3gp"], "potty.3gp")

file=AudioSegment.from_mp3("reverse.mp3")
file.reverse()
file.export("gay.mp3", format="mp3")



