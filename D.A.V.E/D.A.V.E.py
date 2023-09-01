from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import tqdm
from pytube import YouTube as YT

# Configure browser
options = Options()
options.add_argument("--mute-audio")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def watch_videos():
    #Replace these URLs with your own videos
    videos = [
    "https://www.youtube.com/shorts/jMRrvcYAPgI",
    "https://www.youtube.com/shorts/Y4u_HcRDpcs",
    "https://www.youtube.com/shorts/XCSGQsG_lBw",
    "https://www.youtube.com/watch?v=mqIMugPY4u0&t=10s"
    
    ]
    for url in videos:
      video = YT(url, use_oauth=True, allow_oauth_cache=True)
      print(video.title)
      driver.get(url)
      if videos.index(url) == 0:
        time.sleep(5)
      
      #Set up list for tqdm
      video_length_list = []
      for i in range(0, video.length):
        video_length_list.append(i)
        
      for i in tqdm.tqdm(video_length_list, desc="Progress:"):
          time.sleep(1)
      print("====================================================") 

#The amount of times you want the videos watched.
loop_times = 5
this_loop = 0

print("====================================================")

while this_loop < loop_times:
    watch_videos()
    print("Done", this_loop, "times")
    print("====================================================")
    this_loop += 1

print("Finished!")

