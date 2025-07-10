lektor-gravatar
===============

A Lektor_ plugin providing a template filter that generates Gravatar_ URLs for
an email address.

The implementation is drawn from the `documentation on writing Lektor plugins`_;
this package is provided for the convenience of others.

Usage
-----

To add Gravatar support to your Lektor project, run::

    $ lektor plugins add lektor-gravatar

Then, in a template, you can reference::

    <img src="{{ object.email|gravatar }}" alt="gravatar">

where ``object.email`` is a variable in your context containing an email address.

Community
---------

lektor-gravatar is part of the `BeeWare suite <https://beeware.org>`__. You can talk to the
community through:

* `@beeware@fosstodon.org on Mastodon <https://fosstodon.org/@beeware>`__

* `Discord <https://beeware.org/bee/chat/>`__

We foster a welcoming and respectful community as described in our `BeeWare Community
Code of Conduct <https://beeware.org/community/behavior/>`__.

Contributing
------------

If you experience problems with lektor-gravatar, `log them on GitHub <https://github.com/beeware/lektor-gravatar/issues>`__.

If you want to contribute, please `fork the project <https://github.com/beeware/lektor-gravatar>`__ and `submit a pull request <https://github.com/beeware/lektor-gravatar/pulls>`__.


.. _Lektor: https://www.getlektor.com
.. _Gravatar: http://en.gravatar.com
.. _documentation on writing Lektor plugins: https://www.getlektor.com/docs/plugins/howto/
