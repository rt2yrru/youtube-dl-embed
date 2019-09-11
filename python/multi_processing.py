import youtube_dl

# importing the multiprocessing module 
import multiprocessing 
import os 

# line 1  , successfully imports youtube-dl to the above code 

# line 10 to 18 defines mylogger which will log youtube-dl result , we will pass it using youtube-dl dictionary object , named logger in line 33
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
		print(d)

#dictionary object  to include youtube-dl options 
ydl_opts ={
    'format': '720p/best',      # either download 720p  or best whichever is possible
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

# function to split the list into two half half list. 

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


path='./list/list.txt'    # path to the file
with open(path) as file_main:                # open the file   , remove spaces from the file and use it as a list
    lines = [line.strip() for line in file_main if line.strip()]

# worker 1   and worker 2 are part for multiprocessing
def worker1(_a_list): 
    # printing process id 
    print("ID of process running worker1: {}".format(os.getpid())) 

    # open youtube-dl and pass all the parameter ,  ydl acts as youtube-dl method

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for _url in _a_list:
        # method ydl opens download function to download the provided string. Its the url of the link to be downloaded
            ydl.download([_url]) 
    

def worker2(_b_list): 
    # printing process id 
    print("ID of process running worker2: {}".format(os.getpid())) 

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for _url in _b_list:
        # method ydl opens download function to download the provided string. Its the url of the link to be downloaded
            ydl.download([_url]) 

def processor(_a,_b):
    # Creating process p1 and p2  
    p1 = multiprocessing.Process(target=worker1(_a))  
    # process 1 is defined , will target worker1  and will provide the url
    p2 = multiprocessing.Process(target=worker2(_b)) 
    # process 2 is defined , will target worker1  and will provide the same url as process 1
    # starting processes 
    p1.start() 
    p2.start() 
    print("ID of process p1: {}".format(p1.pid)) 
    print("ID of process p2: {}".format(p2.pid)) 

    # wait until processes are finished 
    p1.join() 
    p2.join() 

    # both processes finished 
    print("Both processes finished execution!") 

    # check if processes are alive 
    print("Process p1 is alive: {}".format(p1.is_alive())) 
    print("Process p2 is alive: {}".format(p2.is_alive())) 




if __name__ == "__main__": 
    # printing main program process id 
    print("ID of main process: {}".format(os.getpid())) 
    if(len(lines)==0):
        print(' Empty ')
    elif(len(lines)==-1):
        print('error')
    elif(len(lines)==1):
        print(' only 1 url present')
        print(' running parallel process for faster download')  
        processor(lines,lines)
        # the processor function will receive the same url 
        # so it will parallel the download

    else :
        print(' Creating 2 process where first half will be completed by the first  process')  
        print(' and  second half will be completed by the second  process')  
        # split the list into half    
        _a1,_a2=split_list(lines)
        # send the half half list to processor so that two parallel process will  start and simulatneously download two url 
        processor(_a1,_a2)
