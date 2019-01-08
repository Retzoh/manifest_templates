Sr ht build manifest templates
==============================

This repository is a collection of language-specific CI setups for
[sr.ht](https://meta.sr.ht/).

Its purpose is to let you quickly setup new CI pipelines for your
programming language by copying the appropriate manifest template.

Each language support comes with a "hello world" project on which the
pipelines run.

Subscribe to updates by sending a mail to
~retzoh/manifest-templates-updates+subscribe@lists.sr.ht

#### git.sh.ht repository
https://git.sr.ht/~retzoh/manifest_templates
#### github repository
https://github.com/Retzoh/manifest_templates

The master branches on sr.ht and github are synchronized through this
[manifest](https://git.sr.ht/~retzoh/manifest_templates/tree/master/.build.yml)
at each commit on master

#### Index
- [Setup a pipeline](#setup-a-pipeline)
  - [Supported languages](#supported-languages)
- [Basic CI pipeline structure](#basic-ci-pipeline-structure)
- [Repository structure](#repository-structure)
- [Future work](#future-work)
- [Discussion](#discussion)

## Setup a pipeline
- Pick your language in the
[repository tree](https://git.sr.ht/~retzoh/manifest_templates/tree),
open the `.builds` folder and choose yml file named after the
architecture ([man](https://man.sr.ht/builds.sr.ht/compatibility.md))
you will be working on.
- Put it under `.builds/` in your repository
- Adapt the `source` and `environment` lists to match your needs

### Supported languages
- [python (with anaconda)](https://git.sr.ht/~retzoh/manifest_templates/tree/master/python_anaconda/.builds)

## Basic CI pipeline structure
- install dependencies
- build the project (if needed)
- install the project (if needed)
- run project tests
- run the project

## Repository structure
- `[languages]`
    - `.builds`
        - `[architectures].yml`
    - `src`
        - minimal source code to test the CI pipelines on
    - `tests`
        - minimal testing utilities to test the CI on
    - language-specific build/setup files

## Contributing
Notes on how to contribute can be found in CONTRIBUTING.md
[(sr.ht link)](https://git.sr.ht/~retzoh/manifest_templates/tree/master/CONTRIBUTING.md)
, [(github link)](https://git.sr.ht/~retzoh/manifest_templates/tree/master/CONTRIBUTING.md).

## Future work
- Include freeBSD support for [python (with anaconda)](https://git.sr.ht/~retzoh/manifest_templates/tree/master/python_anaconda/.builds)

## Discussion
Have an issue or something to discuss about the project ?
[This tracker](https://todo.sr.ht/~retzoh/manifest-templates-discussions)
is the appropriate place to bring it up.
