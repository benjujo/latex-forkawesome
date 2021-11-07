latex-forkawesome
=================

Based on [posquit0's latex-fontawesome](https://github.com/posquit0/latex-fontawesome) which is based on [furl's latex-fontawesome](https://github.com/furl/latex-fontawesome).
This project provides to use latest [ForkAwesome](https://forkaweso.me/) icons in XeLaTeX.

The current version of ForkAwesome icons used is 1.2.0. 

How to Use
----------

### Requirements
* You must have the ForkAwesome font installed on your machine (you need the `forkawesome-webfont.ttf` file that is contained [here](https://github.com/ForkAwesome/Fork-Awesome/archive/1.2.0.zip). It's on the `fonts` folder.).
* You must be using XeLaTeX and have the `fontspec` package installed.

### Usage
1. Download the `forkawesome.sty` file and put it in the same directory as the LaTeX file using the icons.
2. Include the package as normal (in the preamble of the `.tex` file, add the line `\usepackage{forkawesome}`).
3. Use an icon by typing `\faIconName`. For example, to use the `fa-quote-left` icon, convert it to camelcase and prepend the slash: `\faQuoteLeft`.

Make Latest forkawesome.sty
---------------------------

### Requirements
It uses `BeautifulSoup` and `requests` libraries. Just run (preferably on a virtual enviroment):
```bash
$ pip install -r requirements.txt
```

### Usage
```bash
$ python makesty.py
```
This should result in the creation of latest ``forkawesome.sty``


Notice
------
* You still cannot use the icons which include a digit(0~9) in the name. Those are (v1.2.0):
  - `500px`
  - `battery-0`
  - `battery-1`
  - `battery-2`
  - `battery-3`
  - `battery-4`
  - `css3`
  - `hourglass-1`
  - `hourglass-2`
  - `hourglass-3`
  - `html5`
  - `s15`
  - `thermometer-0`
  - `thermometer-1`
  - `thermometer-2`
  - `thermometer-3`
  - `thermometer-4`

