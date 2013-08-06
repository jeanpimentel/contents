# Contents

> Put a table of contents in your files!


#### Note:
![](https://cdn1.iconfinder.com/data/icons/16x16-free-toolbar-icons/16/58.png) **Currently, only css/javascript files are supported. In fact, files of languages with __/* BlockComment */__ syntax. I'm working on it.**

## How it works

### Before:
```css
/* > HTML5 display-role reset for older browsers
============================================================================= */
button, input, select, textarea {
  width:auto;
  overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

textarea {
    overflow:auto;
    vertical-align:text-top;
}

/* >> Buttons
============================================================================= */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

button:hover,
a.button:hover,
input[type='reset']:hover,
input[type='button']:hover,
input[type='submit']:hover {
    background-color:#ececec;
    border:1px solid #bbb;
    color:#555;
}

/* >>> Buttons (Call to Action)
============================================================================= */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

.call-to-action a.button:hover {
    text-decoration:none;
}

.ie7 .call-to-action a.button {
    padding:15px 35px 18px 35px;
}

/* >>> Buttons (Sizes)
============================================================================= */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}

.large a.button {
    font-size:18px;
    padding:10px 35px;
}

.xlarge a.button {
    font-size:24px;
    padding:12px 55px;
}
```

### After:
```css
/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 10
        Buttons ......................................................... 25
            Buttons (Call to Action) .................................... 47
            Buttons (Sizes) ............................................. 66

============================================================================= */

/* > HTML5 display-role reset for older browsers
============================================================================= */
button, input, select, textarea {
  width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

textarea {
    overflow:auto;
    vertical-align:text-top;
}

/* >> Buttons
============================================================================= */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

button:hover,
a.button:hover,
input[type='reset']:hover,
input[type='button']:hover,
input[type='submit']:hover {
    background-color:#ececec;
    border:1px solid #bbb;
    color:#555;
}

/* >>> Buttons (Call to Action)
============================================================================= */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

.call-to-action a.button:hover {
    text-decoration:none;
}

.ie7 .call-to-action a.button {
    padding:15px 35px 18px 35px;
}

/* >>> Buttons (Sizes)
============================================================================= */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}

.large a.button {
    font-size:18px;
    padding:10px 35px;
}

.xlarge a.button {
    font-size:24px;
    padding:12px 55px;
}
```


## Installation

- Simple, using PyPI:

```
user@machine:~$ [sudo] pip install contents
```

- or download the source and:

```
user@machine:~$ [sudo] python setup.py install
```


## Usage

- Command line:

```
user@machine:~$ contents my-file.css
```


## License

Copyright (C) 2013  Jean Pimentel <contato@jeanpimentel.com.br>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.