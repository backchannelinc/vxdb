# vxdb

## [Installation ⚙️](#getting-started) | [Docs 📚](https://mwdblib.readthedocs.io/en/latest/) | [Guide 📕](https://mwdb.readthedocs.io/en/latest/user-guide/8-REST-and-mwdblib.html)

---

API bindings for [virus.exchange](https://virus.exchange), which is [VX Underground](https://www.vx-underground.org/)'s malware repository based on [mwdb.cert.pl](https://mwdb.cert.pl).

Latest version requires Python >= 3.7.

## Getting started

```console
$ pip install vxdb

or with CLI

$ pip install vxdb[cli]
$ vxdb version
```

The main interface is the VXDB object that provides various methods to interact with virus.exchange.

```python
>>> from vxdb import VXDB
>>> vx = VXDB()
>>> vx.login()
Username: eripley
Password:

>>> files = vx.recent_files()
>>> file = next(files)
>>> file.name
'400000_1973838fc27536e6'
>>> file.tags
['dump:win32:exe', 'avemaria']
>>> file.children
[<mwdblib.file.VXDBConfig at ...>]
```

`vxdb` provides also optional command line interface (CLI).

```console
$ vxdb --help

Usage: mwdb [OPTIONS] COMMAND [ARGS]...

  VXDB Core API client

Options:
  --help  Show this message and exit.

Commands:
  comment  Add comment to object
  fetch    Download object contents
  get      Get information about object
  link     Set relationship for objects
  list     List recent objects
  login    Store credentials for MWDB authentication
  logout   Reset stored credentials
  metakey  Add metakey to object
  search   Search objects using Lucene query
  server   Prints current server URL and version
  share    Share object with another group
  tag      Add/remove tags for objects
  upload   Upload object into MWDB
  version  Prints mwdblib version

$ vxdb login
Username: eripley
Password:
```

If you log in via CLI, your credentials will be stored in configuration file (`~/.vxdb`) and keyring. These are used by
default by `MWDB()` objects, so you don't have to login each time when you use e.g. IPython session to interact
with MWDB Core API.

## More information

Complete `mwdblib` API docs can be found here: https://mwdblib.readthedocs.io/en/latest/

Additional guidelines regarding MWDB REST API and automation can be found in MWDB Core documentation: https://mwdb.readthedocs.io/en/latest/user-guide/8-REST-and-mwdblib.html