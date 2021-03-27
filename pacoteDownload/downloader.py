import pytube

url = 'https://www.youtube.com/watch?v=hBP-NzOadL0'
youtube = pytube.YouTube(url)

#streams = youtube.streams.filter(progressive=True, file_extension='mp4')
#progressive download se refere aos arquivos que contem tanto o vídeo quanto o audio
#for i in streams:
#    print(i)

video = youtube.streams.get_by_itag(22)
video.download()
print('Feito')

