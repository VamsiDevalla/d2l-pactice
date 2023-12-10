# D2L setup

## 1. Install miniconda

### Mac os

```bash
sh Miniconda3-py39_4.12.0-MacOSX-x86_64.sh -b
```

### Linux os

```bash
sh Miniconda3-py39_4.12.0-Linux-x86_64.sh -b
```

### Windows os

[Follow the directions on website](https://docs.conda.io/projects/miniconda/en/latest)

## 2. Add a profile for conda3 for windows terminal

Add the following to list of profiles in terminal settings.json

```json
{
    "commandline": "cmd.exe /K C:\\Users\\vamsi\\miniconda3\\Scripts\\activate.bat",
    "guid": "{e6b718fc-b480-4708-b5e4-5187130e9030}",
    "hidden": false,
    "icon": "C:/Program Files/Git/mingw64/share/git/git-for-windows.ico",
    "name": "miniconda3",
    "startingDirectory": "%USERPROFILE%"
}
```

## 3. Initialize the shell so we can run conda directly

open miniconda3 profile and run the following command

```bash
init
```

## 4. Create conda env for d2l

```bash
# create a d2l env for d2l book
conda create --name d2l python=3.9 -y
# create a d2l-practice env for your practice
conda create --name d2l-practice python=3.9 -y 
```

## 5. Activate conda env for d2l

```bash
conda activate {package-name d2l/d2l-practice}
```

## 6. Install PyTorch

PyTorch (the specified versions are tested at the time of writing) with either
CPU or GPU support as follows:

```bash
pip install torch==2.0.0 torchvision==0.15.1
```

## 7. Install the d2l package 

Encapsulates frequently used functions and classes found throughout this book

```bash
# only needed for d2l env
pip install d2l==1.0.3
```

## 8. Downloading and running code

```bash
# only needed for d2l env
mkdir d2l-en && cd d2l-en
curl https://d2l.ai/d2l-en-1.0.3.zip -o d2l-en.zip
unzip d2l-en.zip && rm d2l-en.zip
cd pytorch
jupyter notebook
```

## 9. Required extensions for vscode

1. Python

2. code runner

## 10. Useful links

1. [adding miniconda profile in windows terminal](https://dev.to/azure/easily-add-anaconda-prompt-in-windows-terminal-to-make-life-better-3p6j)

2. [setting up conda in vscode](https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d)

## 11. Useful Commands

1. List conda envs

   ```bash
   conda info --envs
   ```

2. Activate env

   ```bash
   conda activate {package_name}
   ```

3. List installed packages in an env

   ```bash
   conda list
   ```
