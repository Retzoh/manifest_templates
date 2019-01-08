# How to contribute

#### Issue tracker
https://todo.sr.ht/~retzoh/manifest-templates-discussions
#### Submit patches
Send your patches to
~retzoh/manifest-templates-contribution@lists.sr.ht
#### Reviewing
Submitted patches can be found there: https://lists.sr.ht/~retzoh/manifest-templates-contribution

Send a mail to
~retzoh/manifest-templates-contribution+subscribe@lists.sr.ht to be
notified of new patches.
#### General notes
Keep CI pipelines working. Run the ones concerning your language
once before submitting a patch.

The project attached to the language should be
tested/compiled/installed/run by the pipeline.

Keep placeholder projects minimals. A "hello world" will do.

In order to test manifests, you can create a 'manifest-test' branch
with a manifest that launches the builds for your language upon commit.
[Here](https://git.sr.ht/~retzoh/manifest_templates/tree/python_anaconda_builds/.build.yml)
is a sample manifest doing this for the python example.

## Contributing on sr ht
Please make sure you have read the
[sr.ht man](https://man.sr.ht/git.sr.ht/send-email.md) about
contributing and done the appropriate configuration.

The main repository is read-only for the general public. In order to
run builds on your commits, you will have to make a copy of the
repository and work on a local branch.

[This issue](https://todo.sr.ht/~sircmpwn/git.sr.ht/164) is about
making this easier.

Once you are done, send a patch to the contribution channel.

## Contributing on github
[dispatch.sr.ht does not support forked repositories for now.](https://todo.sr.ht/~sircmpwn/dispatch.sr.ht/19)

You will have to make a copy of the
[github repository](https://git.sr.ht/~retzoh/manifest_templates).

Then you can setup a [sr ht dispatch](https://dispatch.sr.ht/) to run
builds on your commits.

Once you are done, send a patch to the contribution channel.
