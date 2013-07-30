import sure
import tempfile
from contents import contents


def test_css():

    content = '''/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 16
        Buttons ......................................................... 25
            Buttons (Call to Action) .................................... 36
            Buttons (Sizes) ............................................. 46

============================================================================= */
/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    new_content = '''/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 16
        Buttons ......................................................... 25
            Buttons (Call to Action) .................................... 36
            Buttons (Sizes) ............................................. 46

============================================================================= */
/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    temp = tempfile.NamedTemporaryFile()
    try:
        temp.write(content)
        temp.seek(0)

        contents(temp.name)

        temp.seek(0)
        temp.read().should.be.equal(new_content)
    finally:
        temp.close()


def test_css_with_toc_mark():

    content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    new_content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 17
        Buttons ......................................................... 26
            Buttons (Call to Action) .................................... 37
            Buttons (Sizes) ............................................. 47

============================================================================= */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    temp = tempfile.NamedTemporaryFile()
    try:
        temp.write(content)
        temp.seek(0)

        contents(temp.name)

        temp.seek(0)
        temp.read().should.be.equal(new_content)
    finally:
        temp.close()


def test_css_with_incomplete_toc():

    content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 17
            Buttons (Sizes) ............................................. 47

============================================================================= */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    new_content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 17
        Buttons ......................................................... 26
            Buttons (Call to Action) .................................... 37
            Buttons (Sizes) ............................................. 47

============================================================================= */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    temp = tempfile.NamedTemporaryFile()
    try:
        temp.write(content)
        temp.seek(0)

        contents(temp.name)

        temp.seek(0)
        temp.read().should.be.equal(new_content)
    finally:
        temp.close()


def test_css_with_complete_toc():

    content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    HTML5 display-role reset for older browsers ......................... 17
        Buttons ......................................................... 26
            Buttons (Call to Action) .................................... 37
            Buttons (Sizes) ............................................. 47

============================================================================= */

/* > HTML5 display-role reset for older browsers */
button, input, select, textarea {
    width:auto;
    overflow:visible;
    margin:0;
    font-size:100%;
    vertical-align:baseline;
}

/* >> Buttons */
button,
a.button,
input[type='reset'],
input[type='button'],
input[type='submit'] {
    background-color:#eaeaea;
    border:1px solid #ccc;
    color:#555;
}

/* >>> Buttons (Call to Action) */
.call-to-action {
    text-align:center;
}

.call-to-action a.button {
    font-size:24px;
    padding:15px 35px;
}

/* >>> Buttons (Sizes) */
.small a.button {
    font-size:10px;
    padding:3px 6px;
}

.medium a.button {
    font-size:16px;
    padding:8px 16px;
}
'''

    temp = tempfile.NamedTemporaryFile()
    try:
        temp.write(content)
        temp.seek(0)

        contents(temp.name)

        temp.seek(0)
        temp.read().should.be.equal(content)
    finally:
        temp.close()
