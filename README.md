# an_tdc_errors

In this repository are the sources from which the application note available at
[docs.cronologic.de/app_notes/tdc_errors](https://docs.cronologic.de/app_notes/tdc_errors)

## Building the application note

## Prerequisites

Python is necessary for creating the HTML output.

Optionally, create and activate a virtual environment

```shell
python -m venv .venv
. .\.venv\Scripts\activate
```

Depending on your operating system, you may need to run a different activation script.

The requirements are listed in `requirements.txt`, `requirements-frozen.txt`, and
`requirements-dev.txt`.

If you want to guarantee the output to be the same as hosted at
[docs.cronologic.de](https://docs.cronologic.de/app_notes/tdc_errors), install the
packages listed in `requirements-frozen.txt`, that is, run

```shell
pip install -r requirements-frozen.txt
```

If you want to install the most up-to-date versions of the prerequisites, use
`requirements.txt`.

If you want to install the most up-to-date versions and also install plotting libraries
(e.g., to run Python scripts in [source/_code/](source/_code)), use
`requirements-dev.txt`.

## Building

Run

```shell
cd app_note
make html
```

to compile the project as HTML. The HTML output is in `build/html/`.

## License

![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

This documentation is licensed under the
[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) license. You are free to
copy and redistribute the material in any medium or format for any purpose, even
commercially unchanged if you give appropriate credit to cronologic GmbH & Co. KG. A
link to [this repository](https://github.com/cronologic-de/an_tdc_errors) or the
[application note](https://docs.cronologic.de/app_notes/tdc_errors) is sufficient. If you
decide to contribute to this repository, you transfer non-exclusive but unlimited rights
to your edit to cronologic GmbH & Co. KG.
