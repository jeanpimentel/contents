import sure
import tempfile
from contents import contents


def test_empty_file():

    temp = tempfile.NamedTemporaryFile()
    try:
        contents(temp.name)

        temp.seek(0)
        temp.read().should.be.equal('')
    finally:
        temp.close()
