import sure
import tempfile
from contents import contents


def test_javascript():

    content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
'''

    new_content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    Common Variables .................................................... 25
    Call Plugins ........................................................ 39
        Accordion ....................................................... 42
        Modal ........................................................... 54
        Dropdown ........................................................ 73
    Loading third-party scripts ......................................... 83
        Facebook SDK .................................................... 98
        Twitter SDK .................................................... 101

============================================================================= */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
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


def test_javascript_with_toc_mark():

    content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
'''

    new_content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    Common Variables .................................................... 25
    Call Plugins ........................................................ 39
        Accordion ....................................................... 42
        Modal ........................................................... 54
        Dropdown ........................................................ 73
    Loading third-party scripts ......................................... 83
        Facebook SDK .................................................... 98
        Twitter SDK .................................................... 101

============================================================================= */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
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


def test_javascript_with_incomplete_toc():

    content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    Common Variables .................................................... 25
    Call Plugins ........................................................ 39
    Loading third-party scripts ......................................... 83

============================================================================= */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
'''

    new_content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    Common Variables .................................................... 25
    Call Plugins ........................................................ 39
        Accordion ....................................................... 42
        Modal ........................................................... 54
        Dropdown ........................................................ 73
    Loading third-party scripts ......................................... 83
        Facebook SDK .................................................... 98
        Twitter SDK .................................................... 101

============================================================================= */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
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


def test_javascript_with_complete_toc():

    content = '''/**
 * Project X
 * Author: Marcos Moura
 * Date: August, 2013
 * Version: 1.0
 */

/* TABLE OF CONTENTS

    Common Variables .................................................... 25
    Call Plugins ........................................................ 39
        Accordion ....................................................... 42
        Modal ........................................................... 54
        Dropdown ........................................................ 73
    Loading third-party scripts ......................................... 83
        Facebook SDK .................................................... 98
        Twitter SDK .................................................... 101

============================================================================= */

/* ==========================================================================
    Main scripts
   ========================================================================== */

/* > Common Variables
============================================================================= */

var SITEURL  = window.location.protocol + '//' + window.location.host,
    PATHNAME = window.location.pathname,
    stopEvent = function(event) {
        (event.preventDefault) ? event.preventDefault() : event.returnValue = false;

        if(event.stopPropagation) {
            event.stopPropagation();
        }
    };


/* > Call Plugins
   ========================================================================== */

/* ===>> Accordion <<=== */

$('.accordion').accordion({
    wrapContent: '.accordion-item',
    titleElement: '.accordion-title',
    contentElement: '.accordion-content',
    effect: 'show',
    duration: 200,
    hideOthers: false
});


/* ===>> Modal <<=== */

$('.button.alert').modal({
    appendTo: '.container',
    overlayClass: 'alert-overlay',
    closeClass: 'close-alert',
    duration: 400,
    css: {
        width: 400,
        height: 'auto',
        marginTop: 0,
        position: 'fixed',
        top: 100,
        background: '#fff'
    },
    centered: true
});


/* ===>> Dropdown <<=== */

$('.dropdown').dropdown({
    dropdownButton: '.button',
    dropdownContent: '.dropdown-content',
    effect: 'slideDown',
    duration: 200
});


/* > Loading third-party scripts
   ========================================================================== */

(function(doc, script) {
    var js,
        fjs = doc.getElementsByTagName(script)[0],
        frag = doc.createDocumentFragment(),
        add = function(url, id) {
            if (doc.getElementById(id)) {return;}
            js = doc.createElement(script);
            js.src = url;
            id && (js.id = id);
            frag.appendChild( js );
        };

    /* >> Facebook SDK */
    add('//connect.facebook.net/pt_BR/all.js#xfbml=1&status=0', 'facebook-jssdk');

    /* >> Twitter SDK */
    add('//platform.twitter.com/widgets.js');

    fjs.parentNode.insertBefore(frag, fjs);
}(document, 'script'));
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
