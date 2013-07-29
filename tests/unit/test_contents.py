import sure
import tempfile
import contents


def test_read_file_as_dict():

    temp = tempfile.NamedTemporaryFile()
    try:
        temp.write('this\ntests\n\rread\nfile\n\ras\ndict')
        temp.seek(0)

        expected = {
            1: 'this',
            2: 'tests',
            3: 'read',
            4: 'file',
            5: 'as',
            6: 'dict'
        }

        contents.read_file_as_dict(temp.name).should.be.equals(expected)

    finally:
        temp.close()


def test_find_level():

    first_level = {'text': 'First Level',  'line': 1, 'level': 1}
    second_level = {'text': 'Second Level', 'line': 1, 'level': 2}
    third_level = {'text': 'Third Level',  'line': 1, 'level': 3}
    fourth_level = {'text': 'Fourth Level', 'line': 1, 'level': 4}
    fifth_level = {'text': 'Fifth Level',  'line': 1, 'level': 5}
    sixth_level = {'text': 'Sixth Level',  'line': 1, 'level': 6}

    provider = [
        [['''/* > First Level''', 1],                    first_level],
        [['''/* > =First Level''', 1],                   first_level],
        [['''/* > First Level <''', 1],                  first_level],
        [['''/* > =First Level <''', 1],                 first_level],
        [['''/* > First Level < */''', 1],               first_level],
        [['''/* > =First Level < */''', 1],              first_level],
        [['''/* >> Second Level <<''', 1],               second_level],
        [['''/* ===>> =Second Level <<====''', 1],       second_level],
        [['''/* ===>> =Second Level <==== */''', 1],     second_level],
        [['''/* >>> Third Level <<<''', 1],              third_level],
        [['''/* ===>>> =Third Level ====''', 1],         third_level],
        [['''/* ===>>> Third Level <<<==== */''', 1],    third_level],
        [['''/* >>>> Fourth Level <''', 1],              fourth_level],
        [['''/* ===>>>> =Fourth Level <<<==''', 1],      fourth_level],
        [['''/* ===>>>> Fourth Level <<<<==== */''', 1], fourth_level],
        [['''/* >>>>> Fifth Level''', 1],                fifth_level],
        [['''/* =>>>>> Fifth Level ====''', 1],          fifth_level],
        [['''/* ===>>>>> Fifth Level <<==== */''', 1],   fifth_level],
        [['''/* >>>>>> Sixth Level <''', 1],             sixth_level],
        [['''/* >>>>>> =Sixth Level <<<<<<''', 1],       sixth_level],
        [['''/* ===>>>>>> Sixth Level <<<= */''', 1],    sixth_level],
    ]

    for call in provider:
        contents.find_level(call[0][0], call[0][1]).should.be.equal(call[1])


def test_find_level_invalid():

    provider = [
        ['''/* >>>>>>> Seventh Level? */''', 1],
        ['''/* None Level? */''', 1],
        ['''/* >< Invalid */''', 1],
        ['''/* > */''', 1],
    ]

    for call in provider:
        contents.find_level(call[0], call[1]).should.be.equal(None)


def test_sort_lines_unordered():
    lines = {25: 'b', 10: 'a', 66: 'd', 47: 'c'}
    contents.sort_lines(lines).should.be.equal(['a', 'b', 'c', 'd'])


def test_sort_lines_ordered():
    lines = {10: 'a', 25: 'b', 47: 'c', 66: 'd'}
    contents.sort_lines(lines).should.be.equal(['a', 'b', 'c', 'd'])


def test_sort_lines_empty():
    contents.sort_lines({}).should.be.equal([])


def test_find_toc_with_toc():

    with_toc = {
        1: '/**',
        2: ' * Project X',
        3: ' * Author: Jean Pimentel',
        4: ' * Date: August, 2012',
        5: ' */',
        6: '',
        7: '/* Table of Contents',
        8: '',
        9: '    Item A .................................... 15',
        10: '        Item B ................................ 25',
        11: '            Item C ............................. 48',
        12: '        Item D ................................. 62',
        13: '',
        14: '====================================================== */',
        15: '',
        16: 'Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!'
    }

    contents.find_toc(with_toc).should.be.equal({'start': 7, 'end': 14})


def test_find_toc_without_toc():

    without_toc = {
        1: '/**',
        2: ' * Project X',
        3: ' * Author: Jean Pimentel',
        4: ' * Date: August, 2012',
        5: ' */',
        6: '',
        7: 'Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!'
    }

    contents.find_toc(without_toc).should.be.equal({'start': 1, 'end': 1})


def test_update_lines_with_zero():

    old = {
        1: '/**',
        2: ' * Project X',
        3: ' * Date: August, 2012',
        4: ' */'
    }
    contents.update_lines(old, 0, 0).should.be.equal(old)
    contents.update_lines(old, 10, 0).should.be.equal(old)


def test_update_lines_with_negative():

    old = {
        4: '/**',
        5: ' * Project X',
        6: ' * Date: August, 2012',
        7: ' */'
    }
    new = {
        1: '/**',
        2: ' * Project X',
        3: ' * Date: August, 2012',
        4: ' */'
    }
    contents.update_lines(old, 4, -3).should.be.equal(new)


def test_update_lines_with_positive():

    old = {
        1: '/**',
        2: ' * Project X',
        3: ' * Date: August, 2012',
        4: ' */'
    }
    new = {
        9: '/**',
        10: ' * Project X',
        11: ' * Date: August, 2012',
        12: ' */'
    }
    contents.update_lines(old, 1, 8).should.be.equal(new)


def test_update_lines_starting_from_middle():

    old = {1: '/**', 2: ' * Project X', 3: ' * Date: August, 2012', 4: ' */'}
    new = {1: '/**', 2: ' * Project X', 11: ' * Date: August, 2012', 12: ' */'}
    contents.update_lines(old, 3, 8).should.be.equal(new)


def test_update_lines_starting_after_end():

    old = {1: '/**', 2: ' * Project X', 3: ' * Date: August, 2012', 4: ' */'}
    contents.update_lines(old, 10, 1).should.be.equal(old)


def test_update_toc_with_zero():

    old = {
        41: {'text': 'Item C', 'line': 41, 'level': 3},
        19: {'text': 'Item B', 'line': 19, 'level': 2},
        4: {'text': 'Item A', 'line': 4, 'level': 1},
        60: {'text': 'Item D', 'line': 60, 'level': 3}
    }

    contents.update_toc(old, 0).should.be.equal(old)


def test_update_toc_with_negative():

    old = {
        41: {'text': 'Item C', 'line': 41, 'level': 3},
        19: {'text': 'Item B', 'line': 19, 'level': 2},
        4: {'text': 'Item A', 'line': 4, 'level': 1},
        60: {'text': 'Item D', 'line': 60, 'level': 3}
    }

    new = {
        39: {'text': 'Item C', 'line': 39, 'level': 3},
        17: {'text': 'Item B', 'line': 17, 'level': 2},
        2: {'text': 'Item A', 'line': 2, 'level': 1},
        58: {'text': 'Item D', 'line': 58, 'level': 3}
    }

    contents.update_toc(old, -2).should.be.equal(new)


def test_update_toc_with_positive():

    old = {
        41: {'text': 'Item C', 'line': 41, 'level': 3},
        19: {'text': 'Item B', 'line': 19, 'level': 2},
        4: {'text': 'Item A', 'line': 4, 'level': 1},
        60: {'text': 'Item D', 'line': 60, 'level': 3}
    }

    new = {
        50: {'text': 'Item C', 'line': 50, 'level': 3},
        28: {'text': 'Item B', 'line': 28, 'level': 2},
        13: {'text': 'Item A', 'line': 13, 'level': 1},
        69: {'text': 'Item D', 'line': 69, 'level': 3}
    }

    contents.update_toc(old, 9).should.be.equal(new)


def test_build_toc_from_start():

    itens = {
        80: {'text': 'Item G', 'line': 80, 'level': 6},
        41: {'text': 'Item C', 'line': 41, 'level': 3},
        19: {'text': 'Item B', 'line': 19, 'level': 2},
        73: {'text': 'Item F', 'line': 73, 'level': 5},
        4: {'text': 'Item A', 'line': 4, 'level': 1},
        60: {'text': 'Item D', 'line': 60, 'level': 3},
        66: {'text': 'Item E', 'line': 66, 'level': 4}
    }

    result = {
        0: '/* TABLE OF CONTENTS',
        1: '',
        2: '    Item A ............................................................... 4',
        3: '        Item B .......................................................... 19',
        4: '            Item C ...................................................... 41',
        5: '            Item D ...................................................... 60',
        6: '                Item E .................................................. 66',
        7: '                    Item F .............................................. 73',
        8: '                        Item G .......................................... 80',
        9: '',
        10: '============================================================================= */'
    }

    contents.build_toc(itens, 0).should.be.equal(result)


def test_build_toc_from_middle():

    itens = {
        80: {'text': 'Item G', 'line': 80, 'level': 6},
        41: {'text': 'Item C', 'line': 41, 'level': 3},
        19: {'text': 'Item B', 'line': 19, 'level': 2},
        73: {'text': 'Item F', 'line': 73, 'level': 5},
        4: {'text': 'Item A', 'line': 4, 'level': 1},
        60: {'text': 'Item D', 'line': 60, 'level': 3},
        66: {'text': 'Item E', 'line': 66, 'level': 4}
    }

    result = {
        15: '/* TABLE OF CONTENTS',
        16: '',
        17: '    Item A ............................................................... 4',
        18: '        Item B .......................................................... 19',
        19: '            Item C ...................................................... 41',
        20: '            Item D ...................................................... 60',
        21: '                Item E .................................................. 66',
        22: '                    Item F .............................................. 73',
        23: '                        Item G .......................................... 80',
        24: '',
        25: '============================================================================= */'
    }

    contents.build_toc(itens, 15).should.be.equal(result)


def test_save_file():

    temp = tempfile.NamedTemporaryFile()
    try:

        lines = {
            1: '/**',
            2: ' * Project X',
            3: ' * Author: Jean Pimentel',
            4: ' * Date: August, 2012',
            5: ' */',
            6: '',
            7: 'Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!'
        }

        contents.save_file(temp.name, lines)

        content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2012
 */

Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!
'''
        temp.seek(0)
        temp.read().should.be.equal(content)

    finally:
        temp.close()
