## Julie's workflow notes

Our book is published to [**https://nasa-openscapes.github.io/openscapes_jupyterbook_test**](https://nasa-openscapes.github.io/openscapes_jupyterbook_test){.uri}.

All code is Bash from the Command Line, no Python needed. (I use Terminal from within RStudio because that is my comfort zone).

### Setup

Following documentation from:

-   <https://jupyterbook.org/intro.html>
-   <https://jupyterbook.org/publish/gh-pages.html#option-2-automatically-push-your-build-files-with-ghp-import>
-   <https://pypi.org/project/ghp-import>

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

### Commit, push, and publishing as gh-pages (github.io)

To publish the book to your `gh-pages` branch and then view on nasa-openscapes.github.io/<our book>, you need to run the following with the `ghp-import` package:

You'll need to also commit your changes to GitHub:

```{bash}
## git commands to pus to main/master branch
git add --all
git commit -m "commit message here"
git pull # just to be safe
git push

# publish to gh-pages
ghp-import -n -p -f ./book/_build/html
```

Note: the default commit message will then be "Update documentation" as seen [here](https://github.com/NASA-Openscapes/openscapes_jupyterbook_test/commits/gh-pages).

## Workflow - GitHub

Return to the project: navigate to it in the command line/Terminal, or open it in RStudio/Visual Studio, etc.

Pull most recent updates:

```{bash}
git pull 
```

Create a new branch, then switch to that branch to work in

```{bash}
git branch branch-name
git checkout branch-name

# Julie's example
git branch jsl-dev
git checkout jsl-dev
```

Check which branch you're on anytime by not specifying a branch name:

```{bash}
git branch
```

Make edits and build (see this workflow below)... Then when you're ready, push back to GitHub

\<with these steps\>

## Workflow - Jupyterbook

To build the book, run the following from Terminal

```{bash}
jupyter-book build ./book
```

Paste the url from the console into your browser to see your updates.

## Benefits of Quarto

-   Rendered build updates automatically (rather than having to re-run the build command each time)

-   YML table of contents includes file extension so easier to navigate

-   

## Quarto notes
