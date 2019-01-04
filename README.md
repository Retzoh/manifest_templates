Manifest templates
==================

This repository is a collection of language-specific CI setups for
[sr.ht](https://meta.sr.ht/).

Its purpose is to let you quickly setup new CI pipelines for your
programming language by copying the appropriate manifest template.

Send a mail to ~retzoh/manifest-templates-updates+subscribe@lists.sr.ht
to be informed of updates.

- [Pick a template](#pick-a-template)
  - [Supported languages](#supported-languages)
- [Basic CI pipeline structure](#basic-ci-pipeline-structure)
- [Repository structure](#repository-structure)
- [Future work](#future-work)

## Pick a template
Pick your language in the
[repository tree](https://git.sr.ht/~retzoh/manifest_templates/tree),
open the `.builds` folder and choose yml file named after the
architecture ([man](https://man.sr.ht/builds.sr.ht/compatibility.md))
you will be working on.

### Supported languages
- [python (with anaconda)](https://git.sr.ht/~retzoh/manifest_templates/tree/master/python_anaconda/.builds)

## Basic CI pipeline structure
- install dependencies
- build the project (if needed)
- install the project (if needed)
- run project tests
- run the project

Each language comes with a "hello world" project which the CI
pipelines tests.

## Repository structure
- `[languages]`
    - `.builds`
        - `[architectures].yml`
    - `src`
        - minimal source code to test the CI pipelines on
    - `tests`
        - minimal testing utilities to test the CI on
    - language-specific build/setup files
- [CONTRIBUTING.md](https://git.sr.ht/~retzoh/manifest_templates/tree/master/CONTRIBUTING.md)
- [README.md](https://git.sr.ht/~retzoh/manifest_templates/tree/master/README.md)

## Contributing
Notes on how to contribute can be found in [CONTRIBUTING.md](https://git.sr.ht/~retzoh/manifest_templates/tree/master/CONTRIBUTING.md).

## Future work
- complete support for all images for [python (with anaconda)](https://git.sr.ht/~retzoh/manifest_templates/tree/master/python_anaconda/.builds)
- enable github-based contribution (see [CONTRIBUTING.md](https://git.sr.ht/~retzoh/manifest_templates/tree/master/CONTRIBUTING.md)
for details)
