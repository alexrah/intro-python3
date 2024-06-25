## Introduction to the Python 3 Programming Language

* this repo follows along the tutorials found here: [Introduction to the Python 3 Programming Language](https://egghead.io/courses/introduction-to-the-python-3-programming-language)
* repo URL: [https://github.com/alexrah/intro-python3](https://github.com/alexrah/intro-python3) 

### Install Python
* I decide to manage multiple Python version through [pyenv](https://github.com/pyenv/pyenv)
* install pyenv using Homebrew
```bash
brew update
brew install pyenv
```
* then added a few lines to .zshrc to initialize auto-completion and config
```bash
# initialize pyenv Python Version Manager
if (command -v "pyenv" &> /dev/null)
then
  export PYENV_ROOT="$HOME/.pyenv"
  eval "$(pyenv init -)"
fi
```

