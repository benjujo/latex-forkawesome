#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import sys

CHEATSHEET_URL = 'https://forkaweso.me/Fork-Awesome/cheatsheet/'
OUTPUT_FILE = 'forkawesome.sty'

OUTPUT_HEADER = r'''
%% Based on posquit0 latex-fontawesome, which is
%% based on furl's latex-fontawesome project.

% Identify this package.
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{forkawesome}[2021/11/04 v1.2.0 fork awesome icons]

% Requirements to use.
\usepackage{fontspec}

% Define shortcut to load the Fork Awesome font.
\newfontfamily{\FA}{ForkAwesome}
% Generic command displaying an icon by its name.
\newcommand*{\faicon}[1]{{
  \FA\csname faicon@#1\endcsname
}}

'''.lstrip()

OUTPUT_LINE = '\expandafter\def\csname faicon@%(name)s\endcsname '
OUTPUT_LINE += '{\symbol{"%(symbol)s}} \def\%(camel_name)s '
OUTPUT_LINE += '{{\FA\csname faicon@%(name)s\endcsname}}\n'

response = requests.get(CHEATSHEET_URL)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
cheatsheet = soup.select('div.row > div')

with open(OUTPUT_FILE, 'w') as w:
    w.write(OUTPUT_HEADER)
    for line in cheatsheet:
        data = line.text
        if 'fa' not in data:
            print(f"Unexpected data: {data}")
            continue

        data = ' '.join(data.split())
        # Expects to find 'fa-NAME' ending with " " (single space)
        name = re.findall(r'fa-(\S+)', data)[0]
        # Expects to find 'xfSYMBOL' ending with ;
        symbol = re.findall(r'xf[^;]*', data)[0][1:].upper()

        camel_case = [s.capitalize() for s in name.split('-')]
        camel_name = 'fa' + ''.join(camel_case)

        if re.findall('[0-9]', name):
            print(f"Cannot handle icon: {name}")
            continue

        w.write(
            OUTPUT_LINE % {
                'name': name, 'camel_name': camel_name, 'symbol': symbol
            }
        )
    w.write(r'\endinput')
