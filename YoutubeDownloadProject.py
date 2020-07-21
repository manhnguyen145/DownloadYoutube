from pytube import YouTube
from pytube import Playlist

# grab the list link from youtube
# split the list link and put indivdual video link in a list/array
# print out report that shows the list of first 100 songs + song names 
# allow user to select the music they want to download
# if the video has sectors, split the video in sectors and name them based on 
# their section name, see thishttps://www.youtube.com/watch?v=aFBiYwI3pVY
# if music already exist (same length, same name, Advanced: same sound wave), 
# then skipn

# grab the link from internet

plistLink = input('Please paste the link that you want to download')

if plistLink in ['https://www.youtube.com/playlist?list=']:
    print('link is correct')
else:
    print('link is incorrect')
    
pl = Playlist('https://www.youtube.com/playlist?list=PLlJefS-Tmt6_CbDXAOKmALQcHyAQhgqhQ')
#pl = Playlist('https://www.youtube.com/playlist?list=PLu1S36l0eVs3uxzUk38MiXL9PMRhlB2-w')

print('The playlist name that will be download is %s:'% pl.playlist_url)
print('Number of videos in this playlist: %s' % len(pl.video_urls))


download = input('Do you want to download the videos? Y/N?')

if download.lower() in ['y', 'Y']:
    for video_url in pl.video_urls:
        yt = YouTube(str(video_url))
        stream = yt.streams.get_audio_only()
        # stream = yt.streams.filter(only_audio=True)
        filepath = stream.download('/home/manh/Programming/YoutubeDownload/downloaded/', yt.streams[0].title)  # only mp4 files so far
        print(yt.streams[0].title + ' downloaded')
    print('Download complete')
else:
    print('Cancel download.')

