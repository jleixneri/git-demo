# GIT Demo Project

Demo Repository, zum Kennenlernen von GIT. Test-Brances können gerne erstellt werden.

**GIT Cheatsheet**: https://ndpsoftware.com/git-cheatsheet.html#loc=workspace;

Verwendung von hello_world.py:

```bash
pip install -r .\requirements.txt
python .\hello_world.py 
```



## Neues Repository anlegen

Das Repository muss in der richtigen Gruppe angelegt werden. Die Gruppe MetalEngineering > DIA hat für jede BU eine separate Subgruppe.

<img src="./assets/2023-05-30 09_42_47-Clipboard.png" alt="2023-05-30 09_42_47-Clipboard" style="zoom: 67%;" />

DIA interne Projekte können in der Gruppe DIA direkte angelegt werden. 

<img src="./assets/2023-05-30 10_00_29-Clipboard.png" alt="2023-05-30 10_00_29-Clipboard" style="zoom: 67%;" />

<img src="./assets/2023-05-30 10_01_25-Clipboard.png" alt="2023-05-30 10_01_25-Clipboard" style="zoom:67%;" />

Nachdem das Repository angelegt wurde, kann es lokal geklont werden. Dafür ist der SSH Link geeignet, sofern der SSH-Key richtig angelegt wurde.

```bash
# define parent directory
cd local_code_folder
# clone repository
git clone git@git.voestalpine.net:MetalEngineering/dia/demo-git.git
# change directory
cd git-demo
# list files
ls 
```

<img src="./assets/2023-05-30 10_02_36-Clipboard.png" alt="2023-05-30 10_02_36-Clipboard" style="zoom:67%;" />

<img src="./assets/2023-05-30 10_06_15-Clipboard.png" alt="2023-05-30 10_06_15-Clipboard" style="zoom:67%;" />



## GIT & VS Code

GIT ist in VSCode integriert, und kann dafür einfach verwendet werden. 

```bash
# change directory to demo repository
cd git-demo
# you can open vscode from terminal
code . 
```

![2023-05-30 10_27_44-Clipboard](./assets/2023-05-30 10_27_44-Clipboard.png)

geänderte Dateien können ausgewählt und committed werden.

![2023-05-30 10_31_32-Clipboard](./assets/2023-05-30 10_31_32-Clipboard.png)

Synchronisieren vom lokalen Repository und dem Remote Repository

![2023-05-30 10_36_17-Clipboard](./assets/2023-05-30 10_36_17-Clipboard.png)

Vor dem Committen sollte man sich die Änderungen im Code anschauen. Dafür klickt man auf das File und kann im `Working Tree` die Änderungen zum vorherigen File begutachten.

![2023-05-30 10_40_12-Clipboard](./assets/2023-05-30 10_40_12-Clipboard.png)



## SSH Key anlegen und mit Gitlab verknüpfen

sadfsdf

![2023-05-30 10_47_31-Window](./assets/2023-05-30 10_47_31-Window.png)
