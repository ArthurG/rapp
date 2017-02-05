from pydub import AudioSegment

def main(file, array):
   
    sound = AudioSegment.from_file(file)
    
    section=0
    names=[]
    choppedFileName = file[:-4]
    


    for j in (0, len(array)-1):
        print("The", j,"was at time click time for ", array[j])


    initTime = array[0]
    print("Init Time is, ", initTime)
    for j in range(0, len(array)-1):
        array[j] -= initTime
        print (array[j])

    previous = 0
    
    i=0
    print("Length of audio is ", len(sound))

    for j in range(1, len(array)):
         next_part = sound[previous : array[j]]
         print("Length of audioseg is ", len(next_part))
         previous = array[j]
         section += 1
         next_part.export(choppedFileName + "_%d" % section + ".3gp")
         names.append(choppedFileName + "_%d" % section + ".3gp")

    section += 1     
    next_part = sound[array[-1] : len(sound)-1]
    next_part.export(choppedFileName + "_%d" % section + ".3gp")    
    return names


#main("1486276797127.3gp", [1486276797127, 1486276908227, 1486276909370, 1486276911176])    

'''
    for j in range(1,len(array)):
        print(i, " and the ", j)

        print(len(sound));
        print(len(sound)*i,":left time mine right time:", len(sound)*j)
     
        next_part = sound[len(sound)*array[j]: len(sound)*j]
        i = j
        fractionals[j+1] = fractionals[j+1]+j
        
'''
    




def merge(fileArr, fileNameUserWantsMergedFileToBe):
    mergedFile = AudioSegment.from_file(fileArr[0])
    for file in fileArr:
        if(file == fileArr[0]):
            continue
        sound = AudioSegment.from_file(file)
        mergedFile += sound
    
    mergedFile.export(fileNameUserWantsMergedFileToBe, format="mp3")

    

#main("rapp4.3gp", [30000,31000,35000])

#merge(["poop.mp3", "reverse.mp3", "1486231725915.3gp" ,    "1486235464774.3gp"     ,
#"1486236990831.3gp"     ,
#"1486238870432.3gp"   ,  
#"1486249802936.3gp",
#], "fartypants.mp3")

#merge(["1486266684133.3gp","1486266684133.3gp"], "potty.mp3")






