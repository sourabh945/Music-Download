from sys import argv
import os
import subprocess

try: 
    from pytube import YouTube 
except:
    print("\nYou doesn't have pytube installed in python")
    if input("\nEnter 'y' to conform the installation of pytube in python :: ").lower() != 'y': exit()
    try : 
        subprocess.run(['python3','-m','pip','install','pytube'])
    except Exception as error: 
        print(error)
        exit()
    from pytube import YouTube

try: 
    from moviepy.editor import *
except:
    print("\nYou doesn't have moviepy installed in python")
    if input("\nEnter 'y' to conform the installation of moviepy in python :: ").lower() != 'y': exit()
    try : 
        subprocess.run(['python3','-m','pip','install','moviepy'])
    except Exception as error: 
        print(error)
        exit()
    from moviepy.editor import *

try: 
    link = argv[1]
except:
    print("Please pass the link of the video as argument")
    exit()

path = "./Downloads/Youtube_downloads/"


if os.path.exists(path) is False :
    if os.path.exists("./Downloads") is False:
        os.mkdir("./Downloads")
    os.mkdir(path)


video = YouTube(link,use_oauth=False,allow_oauth_cache=True)

if video.check_availability() is False:
    print("\n Sorry video is not available on Youtube")
    exit()

video_title = video.title

print("\n Title :: ", video_title)

if os.path.isfile(path+video_title+'.mp4') is True:
    print("\nFile is already exits")
    if input("You wanna to replace it , enter 'y' to conform :: ").lower() != 'y': exit()
    

streams = video.streams

try:
    downloader = streams.get_by_itag("140")
    print(f"\nThe Size of file :: {downloader.filesize_mb} MB")
    if input("\nEnter 'y' to conform :: ").lower() != 'y': exit()
    print(f"\nDownloading start ... \n")
    downloader.download(output_path=path,skip_existing=False)
    print(f"Download complete ")
except Exception as error:
    print(f"Unable to download due to error : {error}")

try:
    print("Converting video into the audio")
    video_ed = AudioFileClip(os.path.join(path+video_title+".mp4"))
    video_ed.write_audiofile(os.path.join(path+video_title+".mp3"))
    os.remove(path+video_title+".mp4")
    print("Convertion is complete")
except Exception as error:
    print(f"Unable to convert due to error :: {error}")