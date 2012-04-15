Zope Interfaces
===============

Presented at ChiPy on 4/12/2012

Zope Interfaces provide a way for Python objects to promise to provide certain attributes and methods.  Without losing the benefits of duck-typing this can add a bit of structure and also doubles as runnable documentation.  For example, an application developer might point to an interface that can be implemented to create a plugin, and the plugin developer can verify at runtime that he or she has properly implemented this interface.  Furthermore, the metadata about what interfaces an object provides can be used to wire up dependencies between objects at runtime or configuration time with confidence that the relationships are compatible.

For a simple example of the mechanics of creating and implementing interfaces, see `expression.py <https://github.com/thatmattbone/zope-chipy/blob/master/expression.py>`_.  Zope interfaces can also specify invariants, and `binary_search.py <https://github.com/thatmattbone/zope-chipy/blob/master/binary_search.py>`_ shows this in action.  Finally to discover what metadata zope interfaces are adding to objects to provide all of this behavior, check out `class_diff.py <https://github.com/thatmattbone/zope-chipy/blob/master/class_diff.py>`_.  Some of these slides have strange strings in them that I used to generate the original set of slides, so just ignore that.

The full set of slides as presented are available `here <http://static.thatmattbone.com/zope-chipy/>`_ but they probably aren't terribly useful.

More Information
++++++++++++++++

* `zope.interface documentation <http://docs.zope.org/zope.interface>`_
* `What are interfaces? -- Zope Documentation <http://wiki.zope.org/zope3/WhatAreInterfaces>`_
* `Purpose of Zope Interfaces? -- stackoverflow <http://stackoverflow.com/questions/2521189/purpose-of-zope-interfaces>`_
* `PEP 3119: Introducing Abstract Base Classes <http://www.python.org/dev/peps/pep-3119/>`_
* `What Bothers Me About The Component Architecture -- Ian Bicking <http://www.coactivate.org/projects/topp-engineering/blog/2008/10/20/what-bothers-me-about-the-component-architecture>`_


Other projects sharing ideas with zope.interface
++++++++++++++++++++++++++++++++++++++++++++++++

* `abc <http://docs.python.org/library/abc.html>`_
* `traits from enthought <http://code.enthought.com/projects/traits/>`_
* `colander <http://docs.pylonsproject.org/projects/colander/en/latest/>`_
* django/sqlaclhemy models


