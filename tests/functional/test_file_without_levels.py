import sure
import tempfile
from contents import contents


def test_file_without_levels():

    content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 */

Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!
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
