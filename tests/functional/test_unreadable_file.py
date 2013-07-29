import sure
import tempfile
import os
from nose.tools import raises
from contents import contents


@raises(Exception)
def test_unreadable_file():

    temp = tempfile.NamedTemporaryFile(mode='w+b')
    os.chmod(temp.name, 0000)
    try:
        contents(temp.name)

        temp.seek(0)
        temp.read().should.be.equal('')
    finally:
        temp.close()
