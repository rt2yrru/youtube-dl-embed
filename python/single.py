from __future__ import unicode_literals
import os,json,sys
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    import youtube_dl

# line 1 to line 6 , successfully imports youtube-dl to the above code

# line 11 to 19 defines mylogger which will log youtube-dl result , we will pass it using youtube-dl dictionary object , named logger in line 33
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

# function my hooks attachs to youtube-dl , we will pass it using youtube-dl dictionary object , named progress_hooks in line 34

def my_hook(d):
	if d['status'] == 'finished':
		print('finished')
	else :
		os.system('clear')  # clears the screen from printing previous output
		print(d)

#dictionary object  to include youtube-dl options 
ydl_opts ={
    'format': '720p/best',      # either download 720p  or best whichever is possible
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

_url='https://www.youtube.com/watch?v=EjCLLChDlT0'   # pass on the link to be downloaded

# open youtube-dl and pass all the parameter ,  ydl acts as youtube-dl method

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	ydl.download([_url]) 
	# method ydl opens download function to download the provided string. Its the url of the link to be downloaded
	#NOTE : Not including [] in the parameter for ydl.download() will break the string into individual bytes

    
