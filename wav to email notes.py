import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import speech_recognition as sr
import os
from os import path
import pydub
pydub.AudioSegment.ffmpeg = "C:/ffmpeg"
from pydub import AudioSegment
import sys
import time
now = time.strftime("%c")
def get_filename_datetime():
   return "upload/" + time.strftime("%c") + ".txt"
name = get_filename_datetime()
#toaddr = sys.argv[0]
toaddr = ('reciever.gmail.com')

#sending the mail to client

print(toaddr)  
# obtain audio from the microphone  
r = sr.Recognizer()  

#print("asdfg")

#mic=sr.Microphone()
#sr.Microphone.list_microphone_names()

# files                                                                        
src = "C:/xampp/htdocs/img/upload/videoplayback.mp3"
dst = "C:/xampp/htdocs/img/upload/videoplayback.wav"

# convert wav to mp3      
import subprocess
cmds = ['c:/ffmpeg/bin/ffmpeg', '-i', src, dst]
subprocess.Popen(cmds)
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")
audio=dst;
with sr.AudioFile(audio) as source:  
   #print("Please wait. Calibrating microphone...")  
   # listen for 5 seconds and create the ambient noise energy level  
   r.adjust_for_ambient_noise(source, duration=0)  
   #print("Say something!")  
   audio = r.record(source)  
   
#with open("audio1.txt","rb") as f:
     # f.write(audio.get_raw_data)
   
 # recognize speech using Sphinx
now = time.strftime("%c")
timestr = time.strftime("%Y%m%d-%H%M%S")
import codecs
from io import open
name =  "C:/xampp/htdocs/img/upload/sample" + timestr + ".txt"    
try:
     txt = r.recognize_google(audio,language='ta-IN')
       
     with open(name,"a", encoding="utf-8") as f:
         f.write('\n'+ txt )
         f.close()
         print("hii")
         fromaddr = "sender.gmail.com"
         print(toaddr)
         msg = MIMEMultipart()
         msg['From'] = fromaddr
         msg['To'] = toaddr
         msg['Subject'] = "converting into text"
         body = "Thanks for using our service..."
         msg.attach(MIMEText(body, 'plain'))
         filename = 'audio.txt'
         attachment = open(name,"rb")
         p = MIMEBase('application', 'octet-stream')
         p.set_payload((attachment).read())
         encoders.encode_base64(p)
         p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
         msg.attach(p)
         s = smtplib.SMTP('smtp.gmail.com', 587)
         s.starttls()
         s.login(fromaddr, "sender@123")
         text = msg.as_string()
         s.sendmail(fromaddr, toaddr, text)
         #os.remove(src)
         os.remove(dst)
         s.quit()
         
except sr.UnknownValueError:  
   print("Sorry could not understand audio")  
except sr.RequestError as e:  
   print("Error; {0}".format(e)) 

