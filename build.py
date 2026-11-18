#!/usr/bin/env python3
"""Build SAHAAYA into a single self-contained page.

Writes:
  index.html          full standalone document (open it directly, or serve with GitHub Pages)
  dist/artifact.html  body-only fragment for publishing as a claude.ai artifact (optional)

No dependencies beyond the Python standard library.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / 'src'


def read(name):
    return (SRC / name).read_text(encoding='utf-8')


def main():
    ui = "(function () {\n'use strict';\n" + read('ui-core.js') + read('ui-views.js') + read('ui-views-plan.js') + read('ui-actions.js') + "})();\n"
    scripts = '<script>\n' + read('engine.js') + '</script>\n<script>\n' + read('seed.js') + '</script>\n<script>\n' + ui + '</script>\n'
    if '</script>' in read('engine.js') + read('seed.js') + ui:
        raise SystemExit('A source file contains a literal </script>; split it before building.')

    head, body = read('head.html'), read('body.html')

    fragment = head + body + scripts
    (ROOT / 'dist').mkdir(exist_ok=True)
    (ROOT / 'dist' / 'artifact.html').write_text(fragment, encoding='utf-8')

    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<meta name="description" content="SAHAAYA: an outcome-financed platform for sustainable digital financial inclusion, '
            'measuring the moment a household no longer needs help.">\n'
            '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
            + head + '\n</head>\n<body>\n' + body + scripts + '</body>\n</html>\n')
    (ROOT / 'index.html').write_text(page, encoding='utf-8')
    print('built index.html', len(page), 'bytes; dist/artifact.html', len(fragment), 'bytes')


if __name__ == '__main__':
    main()
