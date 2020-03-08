def songparser():
    textf = input("input songtext file")+ ".txt"
    tf = open(textf,"r")
    lines= tf.readlines()
    lines1=[]
    for i in range (0, len(lines)):
        if lines[i]!="\n":
            lines1.append(lines[i])
    tf.close()
    global wordlist
    wordlist=[]
    for i in range (0,len(lines1)):
        line = lines1[i]
        z=0
        for j in range (0,len(line)):
            if line[j]==" " or j == len(line)-1:
                 word = line[z:j]
                 wordlist.append(word)
                 z=j+1
    for i in range ( len(wordlist)):
        word2 = wordlist[i]
        length = len(word2)
        word3=""
        for j in range (0, length):
            if word2[j].isalpha()== True:
                word3 = word3 + word2[j]
                wordlist[i]=word3.upper()
    print(wordlist)
def getlength(filename):
    import wave
    import contextlib
    fname = filename
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / int(rate)
    return duration
def frames():
    import wave
    global filename,x
    x=0
    filename=input("input filename")+".wav"
    w = wave.open(filename, 'r')
    from pydub import AudioSegment
    song = AudioSegment.from_wav(filename)
    t1,t2,k=0,100,0
    l=0
    for i in range(w.getnframes()):
        frames = w.readframes(i)
        for j in range(len(frames)):
            if frames[j] >0:
                l+=1
            if l> 100000:
                chunk = song[t1:t2]
                outfile='.//splitAudio//chunk{0}.wav'.format(k)
                print(outfile)
                chunk.export(outfile, format="wav")
                k+=1
                t1=t2
                l=0
                x+=1
        t2+=5
def sr(x):
    import speech_recognition as sr
    r = sr.Recognizer()
    global words
    words=["the"]*x
    for i in range (x):
       chunk= ".//splitAudio//chunk{0}.wav".format(i)
       harvard = sr.AudioFile(chunk)
       with harvard as source:
            audio = r.record(source)
            try:
                text=r.recognize_google(audio)
                print(text)
                words[i]=text.upper()
            except:
                print("unknown")
    print(words)

def splitter():
    from pydub import AudioSegment
    from pydub.silence import split_on_silence
    global x
    x=0
    song=input("songname")+".wav"
    sound_file = AudioSegment.from_wav(song)
    audio_chunks = split_on_silence(sound_file,300,-20)
    for i, chunk in enumerate(audio_chunks):
         out_file = ".//splitAudio//chunk{0}.wav".format(i)
         print ("exporting", out_file)
         chunk.export(out_file, format="wav")
         x+=1
def remove(x):
    import os
    for i in  range (x):
        os.remove(".//splitAudio//chunk{0}.wav".format(i))
def wordfinder(wordlist,words):
    reorder=[0]*len(wordlist)
    from pydub import AudioSegment
    print(wordlist,words)
    for i in range (len(wordlist)):
        for j in range (len(words)):
            if wordlist[i]== words[j]:
                reorder[i]=".//splitAudio//chunk{0}.wav".format(j)
    print(reorder)
    files = list(filter(lambda x : x != 0, reorder))
    full = AudioSegment.from_wav(files[0])
    for i in range (1,len(files)):
        full = full+ AudioSegment.from_wav(files[i])
    print(files)
    full.export(".//full//full.wav", format="wav")
    
                
songparser()
splitter()
sr(1000)
wordfinder(wordlist,words)
remove(1000)



















                    
        
