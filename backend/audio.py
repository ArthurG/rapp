from pydub import AudioSegment
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


   # final_file=sound[fractionals[-1]*len(sound) : len(sound)]
   # section += 1;
   # final_file.export(choppedFileName+ "_%d" % section + ".3gp")
   # print (choppedFileName+ "we splitted out section %d" % section + ".3gp")
   # names.append(choppedFileName + "_%d" % section + ".3gp")
    
    # sound = AudioSegment.from_3gp("/path/to/file.3gp")
    # len() and slicing are in milliseconds 
    #halfway_point = len(sound) / 2
    
    half1 = sound[0: len(sound)/2]
    half2 = sound[len(sound)/2 : len(sound)]

    backwards = sound.reverse()
    backwards.export("reverse.3gp")
    
    half1.export("half1.3gp")
    half2.export("half2.3gp")
    
    print (names)
    return names
    
   # next_part = sound[halfway_point:]

    # Concatenation is just adding
    #second_half_3_times = second_half + second_half + second_half

    # writing 3gp files is a one liner
    #second_half_3_times.export("/path/to/new/file.3gp", format="3gp")




"""
def main(speech_file):
    Transcribe the given audio file.
    Args:
        speech_file: the name of the audio file.
    
    # [START construct_request]
    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                # There are a bunch of config options you can specify. See
                # https://goo.gl/KPZn97 for the full list.
                'encoding': 'AMR_WB',  # raw 16-bit signed LE samples
                'sampleRate': 16000,  # 16 khz
                # See http://g.co/cloud/speech/docs/languages for a list of
                # supported languages.
                'languageCode': 'en-US',  # a BCP-47 language tag
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    # [END construct_request]
    # [START send_request]
    response = service_request.execute()

    # First print the raw json response
    print(json.dumps(response, indent=2))

    # Now print the actual transcriptions
    for result in response.get('results', []):
        print('Result:')
        for alternative in result['alternatives']:
            print(u'  Alternative: {}'.format(alternative['transcript']))
    # [END send_request]
if __name__ == "__main__":
   main(sys.argv[1:])
if __name__ == "__main__":
   main(sys.argv[1:])
   
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'speech_file', help='Full path of audio file to be recognized')
    args = parser.parse_args()
    main(args.speech_file)

"""

main("rapp4.3gp", [30000,31000,35000])

