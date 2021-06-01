## Julie's workflow notes

Our book is published to **<https://nasa-openscapes.github.io/openscapes_jupyterbook_test>**.

All code is Bash from the Command Line, no Python needed. (I use Terminal from within RStudio because that is my comfort zone).

### Setup 

Following documentation from: 

- <https://jupyterbook.org/intro.html>
- <https://jupyterbook.org/publish/gh-pages.html#option-2-automatically-push-your-build-files-with-ghp-import>
- <https://pypi.org/project/ghp-import>

First install two Python libraries: `jupyter-book`, which will structure and build the book, and `ghp-import`, which will publish the book to the `gh-pages` branch.
```{bash}
pip install -U jupyter-book
pip install ghp-import
```

Next, clone the repository and set it as the current directory (below is the Bash code; I did this clicking from RStudio)
```{bash}
git clone https://github.com/NASA-Openscapes/openscapes_jupyterbook_test/
cd openscapes_jupyterbook_test
```
### Building locally

To build the book:
```{bash}
jupyter-book build ./book
```
You can paste the url into your browser to see the local build. 


If there are updates online you want locally, first pull from GitHub.com and then bebuild: 
```{bash}
git pull
jupyter-book build ./book
```

You'll want to commit your changes to GitHub (I do this from the RStudio GUI):

```{bash}
git add --all
git commit -m "rebuilding book with TOC disabling in _config.yml"
git pull # just to be safe
git push
```


### Publishing as github.io

To publish the book to your `gh-pages` branch and then view on nasa-openscapes.github.io/<our book>, you need to run the following with the `ghp-import` package:
```{bash}
ghp-import -n -p -f ./book/_build/html
```

Note: the default commit message will then be "Update documentation" as seen [here](https://github.com/NASA-Openscapes/openscapes_jupyterbook_test/commits/gh-pages). 


