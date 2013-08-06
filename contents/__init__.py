#!/usr/bin/env python
# coding: utf-8
#
# <contents - Put a table of contents in your files!>
# Copyright (C) 2013  Jean Pimentel <contato@jeanpimentel.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__version__ = '0.1.0'

import sys
import os
import re

RE_FIND_LEVELS = ur'''\/\*(?:[^>|^#]*)(>+|#+)\W*([a-zA-Z0-9_\-():;,' ]+)'''
RE_EXIST_TABLE_BEGIN = ur'''(TABLE OF CONTENTS)$'''
RE_EXIST_TABLE_END = ur'''^=* \*\/$'''
RE_EXIST_TABLE_MARK = ur'''\/\* (TABLE OF CONTENTS) \*\/'''


def contents(input_file):

    if not os.access(input_file, os.R_OK):
        raise Exception('Input file is not readable')

    lines = read_file_as_dict(input_file)
    if len(lines) == 0:
        return

    actual = find_toc(lines)

    new = {}
    for line in lines:
        level = find_level(lines[line], line)
        if level is not None:
            new[line] = level

    if len(new) == 0:
        return

    if actual['start'] == 1 and actual['start'] == actual['end']:
        difference = (len(new) + 4)
        lines = update_lines(lines, actual['start'], difference)
    else:
        difference = (len(new) + 4) - (actual['end'] - actual['start'] + 1)
        lines = update_lines(lines, actual['start'], difference)

    new = update_toc(new, difference)
    new = build_toc(new, actual['start'])
    for line in new:
        lines[line] = new[line]

    save_file(input_file, lines)


def read_file_as_dict(filename):
    lines = {}
    i = 1
    f = open(filename)
    for line in f:
        lines[i] = line.strip('\n').strip('\r')
        i += 1
    f.close()
    return lines


def find_level(line, lineno):
    matches = re.compile(RE_FIND_LEVELS, re.M).findall(line)
    if len(matches) > 0:
        match = matches.pop()
        level = len(match[0])
        text = match[1].strip()
        if 0 < level < 7 and len(text):
            return {
                'level': level,
                'text': text,
                'line': lineno
            }


def sort_lines(d):
    keys = d.keys()
    keys.sort()
    return [d.get(k) for k in keys]


def find_toc(lines):
    start = -1
    end = -1

    for line in lines:
        # check for table of contents mark
        matches = re.compile(RE_EXIST_TABLE_MARK, re.M | re.IGNORECASE) \
                    .findall(lines[line])
        if len(matches) > 0:
            start = end = line
            break

        if start == -1:
            matches = re.compile(RE_EXIST_TABLE_BEGIN, re.M | re.IGNORECASE) \
                        .findall(lines[line])
            if len(matches) > 0:
                start = line
        elif end == -1:
            matches = re.compile(RE_EXIST_TABLE_END, re.M).findall(lines[line])
            if len(matches) > 0:
                end = line
        else:
            break

    if(start == -1 or end == -1):
        return {'start': 1, 'end': 1}

    return {'start': start, 'end': end}


def update_lines(lines, start, difference):
    new = {}
    for line in lines:
        if line < start:
            new[line] = lines[line]
        else:
            new[line + difference] = lines[line]
    return new


def update_toc(toc, difference):
    new = {}
    for line in toc:
        new[line + difference] = toc[line]
        new[line + difference]['line'] += difference
    return new


def build_toc(toc, start):

    new = {start: '/* TABLE OF CONTENTS'}
    start += 1
    new[start] = ''
    start += 1

    for entry in sort_lines(toc):
        line = ' ' * 4 * entry['level'] + entry['text']
        line_len = len(line.decode('utf-8'))
        if line_len > 70:
            line = line[:65] + '[...]'
            line_len = 70
        line += ' ' + ((74 - line_len - len(str(entry['line']))) * '.')
        line += ' ' + str(entry['line'])
        new[start] = line
        start += 1

    new[start] = ''
    start += 1
    new[start] = '=' * 77 + ' */'
    return new


def save_file(filename, lines):
    f = open(filename, 'w')
    for line in lines:
        f.write('%s\n' % lines[line])
    f.close()


def main():
    if len(sys.argv) > 1:
        contents(sys.argv[1])
    else:
        sys.exit('Usage: contents FILE')


if __name__ == "__main__":
    main()
