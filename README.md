# Numpy taak - Stijn Van Vlaenderen 
## 1 setup
### 1. 1 docker image  
Docker image gebruikt om deze code te runnen is te vinden op:  
```console
docker pull stijnvanvl/taaknumpy:latest
```
Indien u pycharm pro edition gebruikt kan u dit doen via:  
- > Ctrl+Alt+s 
- > Add:interpreter (dropdown) 
- > Select: On Docker...  
- > Select: Pull or use existing  
- > use image tag: "stijnvanvl/taaknumpy:latest"

Indien niet gebruik volgend command in de shell:

```console
docker run -it -v .:/taak_numpy stijnvanvl/taaknumpy:latest python /taak_numpy/main.py
```
### 1.2 Maintaining Docker image 
### 1.2 Maintaining Github project

- git add <file> # files die je wilt toevoegen waar je veranderingen hebt gedaan  
- git commit -m "Message." #berichtje erbij vb datum/important changes  
- git push origin main pushed naar de github link  