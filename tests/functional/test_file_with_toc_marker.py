import sure
import tempfile
from contents import contents


def test_file_with_toc_marker():

    content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 */

/* TABLE OF CONTENTS
============================================================================= */

/* > Intro */
Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!

/* >> The Big Bang Theory << */
The Big Bang Theory is an American sitcom created by Chuck Lorre and Bill Prady.

/* ==>>> Characters ========================================================= */
Leonard Hofstadter, Sheldon Cooper, Howard Wolowitz, Rajesh Koothrappali, Penny

/* >>>> Production
============================================================================= */
Executive producer(s): Chuck Lorre, Bill Prady, Steven Molaro
Producer(s): Faye Oshima Belyeu

/* =>>>>> Info
============================================================================= */
No. of seasons: 5
No. of episodes: 111

/* =>>>>>> Quotes <========================================================== */
* Sheldon: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.
* Sheldon: I'm not insane, my mother had me tested!
'''

    new_content = '''/**
 * Project X
 * Author: Jean Pimentel
 * Date: August, 2013
 */

/* TABLE OF CONTENTS

    Intro ............................................................... 18
        The Big Bang Theory ............................................. 21
            Characters .................................................. 24
                Production .............................................. 27
                    Info ................................................ 32
                        Quotes .......................................... 37

============================================================================= */

/* > Intro */
Toc toc! Penny! Toc toc! Penny! Toc toc! Penny!

/* >> The Big Bang Theory << */
The Big Bang Theory is an American sitcom created by Chuck Lorre and Bill Prady.

/* ==>>> Characters ========================================================= */
Leonard Hofstadter, Sheldon Cooper, Howard Wolowitz, Rajesh Koothrappali, Penny

/* >>>> Production
============================================================================= */
Executive producer(s): Chuck Lorre, Bill Prady, Steven Molaro
Producer(s): Faye Oshima Belyeu

/* =>>>>> Info
============================================================================= */
No. of seasons: 5
No. of episodes: 111

/* =>>>>>> Quotes <========================================================== */
* Sheldon: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.
* Sheldon: I'm not insane, my mother had me tested!
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
