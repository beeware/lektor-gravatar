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

lektor-gravatar is part of the `BeeWare suite`_. You can talk to the community through:

* `@pybeeware on Twitter`_

* The `pybee/general`_ channel on Gitter.

Contributing
------------

If you experience problems with this backend, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _Lektor: https://www.getlektor.com
.. _Gravatar: http://en.gravatar.com
.. _documentation on writing Lektor plugins: https://www.getlektor.com/docs/plugins/howto/
.. _BeeWare suite: http://pybee.org
.. _@pybeeware on Twitter: https://twitter.com/pybeeware
.. _pybee/general: https://gitter.im/pybee/general
.. _log them on Github: https://github.com/pybee/lektor-gravatar/issues
.. _fork the code: https://github.com/pybee/lektor-gravatar
.. _submit a pull request: https://github.com/pybee/lektor-gravatar/pulls
