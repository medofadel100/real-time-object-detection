from gtts import gTTS 
  
# import Os module to start the audio file
import os 
  
mytext = 'اهلا'
  
# Language we want to use 
language = 'ar'
  

myobj = gTTS(text=mytext, lang=language, slow=False) 
  

myobj.save("temp.mp3") 
  
# Play the converted file 
os.system("start temp.mp3")
