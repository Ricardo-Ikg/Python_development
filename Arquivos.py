# arquivo = open("my_archive.txt","r")

# linhas = arquivo.readlines()

# print(linhas)

# coding = 'UTF-8'
archive = open("My first archive.txt", "w")
archive = archive.write("Esse é o meu primeiro arquivo!" )


archive = open("My first archive.txt", "r")
archive = archive.read()
# print(archive)

archive = open("My first archive.txt","a")
archive = archive.write("\nEssa é a continuação do meu primeiro arquivo")

archive = open("My first archive.txt","r")
archive = archive.read()
print(archive)
