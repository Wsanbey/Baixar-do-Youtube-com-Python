import pytube

link = input("Entre com a URL do youtube: ")

yt = pytube.YouTube(link)

yt.streams.first().download()

print(f"O dowload do site YouTube {link} foi realizado com sucesso!")
