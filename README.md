## Introduction

This tool is a simple word statistics extractor for [GNU gettext](https://www.gnu.org/software/gettext/) `.pot` (portable object template) [files](https://www.drupal.org/node/1814954).

## Prerequirements

- Python 2.7

## Usage

```bash
$ python pot-stat.py file1.pot <file2.pot> ... 
```

Extracted words and their respective statistic are dumped to `stdout` in comma separated format (CSV).

### Example Usage

```bash
$ python pot-stat.py wordpress-3.9.pot wordpress-admin-network.pot
wordpress-3.9.pot: 1520 messages, 1187 tokens
wordpress-admin-network.pot: 258 messages, 54 tokens
Total: 1778 messages, 1241 tokens
the, 224
to, 212
you, 175
not, 152
...
...

```

## License

- [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
