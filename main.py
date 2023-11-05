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
    link = argv[1]
except:
    print("Please pass the link of the video as argument")
    exit()

path = "./Downloads/Youtube_downloads"


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

if os.path.exists(path+video_title) is True:
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