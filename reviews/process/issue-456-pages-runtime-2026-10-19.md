# Pages runtime assessment for issue 456

Inspected base: `a272f29d32ad36fa0bb398ed866aeb0ab1b3cd8b`.
[Issue 456](https://github.com/CultureBotAI/CMMMech/issues/456) is a maintenance
assessment, not a demonstrated deployment failure. This branch prepares explicit
Node 24 action versions and records the remaining hosted verification.

## Evidence and version choices

The [reported run](https://github.com/CultureBotAI/CMMMech/actions/runs/38849343402)
at `6a43774bf15a206b04e59c7525e93fdb334325d6` succeeded, including upload and
deployment. Freshly acquired job metadata and annotations confirm that GitHub
forced four Node-20-declared actions onto Node 24. The warning alone does not
establish that an upgrade was required to restore service.

Official release references and action definitions acquired on 2026-10-19 support
these deliberately pinned choices in the repository-owned Pages workflow:

| Action | Selected release and exact source | Declared runtime |
|---|---|---|
| Checkout | [7.0.1, `3d3c42e`](https://github.com/actions/checkout/tree/3d3c42e5aac5ba805825da76410c181273ba90b1) | Node 24 |
| Configure Pages | [6.0.0, `45bfe01`](https://github.com/actions/configure-pages/tree/45bfe0192ca1faeb007ade9deae92b16b8254a0d) | Node 24 |
| Upload Pages artifact | [5.0.0, `fc324d3`](https://github.com/actions/upload-pages-artifact/tree/fc324d3547104276b827a68afc52ff2a11cc49c9) | Composite |
| Deploy Pages | [5.0.1, `368f825`](https://github.com/actions/deploy-pages/tree/368f82528645a54fb793d4d04e342629a3f51346) | Node 24 |

The upload composite pins [upload-artifact 7.0.0](https://github.com/actions/upload-artifact/blob/bbbca2ddaa5d8feaa63e36b76fdaad77386f024f/action.yml),
also declaring Node 24. It does not use the separately inspected latest uploader
7.0.2. Full commit pins make the inspected source choice reproducible; explicit
runtime declarations avoid relying on GitHub's forced runtime substitution.

The [complete canonical manifest](https://github.com/CultureBotAI/culturebotai-claw/blob/a5d562962c75a2ad9efd8160b548df5944315422/src/kg_microbe_governance/vendored_artifacts.json)
enumerates 22 governed CMMMech artifacts and excludes `.github/workflows/pages.yaml`.
The native workflow is therefore the correct edit location. No governed copy is
edited.

## Preserved behavior and runner assessment

Triggers, permissions, concurrency, environment, runner label, step order, site
layout and staging commands stay the same. Checkout disables persisted Git
credentials; later steps do not perform authenticated Git operations. Configure
and deploy retain their documented token inputs. Deploy 5.0.1 includes its
documented polling backoff/jitter behavior; an unchanged input contract does not
mean identical action internals.

Uploader 5 defaults to excluding hidden files. Explicit `include-hidden-files:
true` preserves the previous selection, including root `.nojekyll` and
`pages/.nojekyll`. With that expression resolved, its Linux archive command
matches version 3 after whitespace normalization. Both versions exclude `.git`
and `.github`. Only the existing staged site is uploaded, not the repository root.

GitHub's [migration notice](https://github.blog/changelog/2026-09-17-ubuntu-26-generally-available-and-latest-migration/)
places the gradual `ubuntu-latest` move between October 19 and November 19, 2026.
The [pinned Ubuntu 26.04 inventory](https://github.com/actions/runner-images/blob/ee1ff4569e381a9649b400338bdc8ceb7e18a80e/images/ubuntu/Ubuntu2604-Readme.md)
describes image `20261012.163.1`, Bash 5.3.9 and GNU tar 1.35, the shell/archive
tools needed here. Checkout documents runner 2.327.1 or later for Node 24.
The image's Node installation on PATH is distinct from the runner-supplied
JavaScript action runtime. These sources support compatibility assessment;
they do not prove execution on the new image. `ubuntu-latest` is retained.

## Executed checks and outstanding acceptance

An independent reviewer executed the exact YAML staging command under Bash on
macOS in a new temporary `RUNNER_TEMP`. All **627 output files** matched the
expected paths and SHA-256 values: 626 tracked site inputs plus the generated
root `.nojekyll`. There were no extra files or symlinks; hidden-file traversal
was included. Static verification checked all configured action inputs and
pins, transitive runtime, complete manifest and deployment boundaries.

`uv run --no-sync just check` exited 0: **327 tests passed, three empty-parameter
skips, 602 records with zero failures and 730 histories with zero errors**.
`bash scripts/check_vendored_sync.sh` exited 0 for all 22 governed artifacts.
Local Python was 3.14.7; strict hosted CI uses Python 3.13. No existing failure
was waived. This maintenance assessment introduces no claimed bug regression
or synthetic test that equates a version string with platform support.

The [paired receipt](issue-456-pages-runtime-2026-10-19-evidence.json) records
source pins, hashes, the staged inventory digest, independent review and gate
results. Raw responses and the complete replay script remain in temporary
scratch; their paths are not promised as durable published artifacts.

**Hosted acceptance remains open.** GNU tar was unavailable in the checked
local locations, and the configured Docker endpoint was unavailable. No new
action JavaScript, Linux archive, artifact upload or deployment was executed.
Ordinary PR CI does not exercise this Pages workflow, whose triggers are main
pushes and manual dispatch. A future authorized hosted run must retain its
actual runner image, action revisions, archive/upload and deployment results
before issue 456's complete acceptance can be claimed. No deployment or merge
was performed for this assessment.
