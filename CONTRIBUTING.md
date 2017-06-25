# CONTRIBUTING

Standard GitHub procedure applies.  Make a fork and submit a PR.  

If there's a feature you would like, feel free to write an issue for it.

All code must have accompanying unit tests and documentation changes.  

You can execute `make test` to run the tests (this will also check pep8 compliance.)

## Versioning Scheme

Versioning is X.Y.Z.  

* X is the major revision; this will change if backwards compatibility is broken (messages change or deleted)
* Y is the minor revision; this will change as items are added (new buttons or new fields on existing buttons).  An API using an older minor version should not change behaviour with a server of older minor version.
* Z is the bugfix revision; this will change for non-behavior affecting changes

This also reflects the API versioning.