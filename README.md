# Apertus Data Transparency

This is a repository containing versioned snapshots of key documentation from the Apertus releases.

## ⚠️ New datasets are declared in the private repository

Declaring a dataset means discussing its licensing, PII handling and robots filtering — a
discussion that belongs in a private setting rather than in public issues and pull requests. All of
that has therefore moved to
[`swiss-ai/apertus-data-transparency-private`](https://github.com/swiss-ai/apertus-data-transparency-private).

- **To add a dataset**, open a
  [**➕ New Dataset** issue](https://github.com/swiss-ai/apertus-data-transparency-private/issues/new?template=new_dataset.yml)
  in the private repository, or edit the TSV there directly via a pull request. See its README for
  the full instructions.
- **To discuss the compliance of a dataset**, open an issue in the private repository as well.
- Access to the private repository is granted to the data and legal teams — ping Sven if you need
  it.

Issues and pull requests opened here for new datasets will be redirected there.

## The central dataset repository

`Apertus dataset repository.tsv` is the single source of truth for the datasets that go into the
main Apertus training run. It lists every dataset we use, together with its modalities, licenses,
versions, storage paths and processing scripts. The copy in this repository is the **published
snapshot** of the catalogue; the working copy lives in the private repository and is mirrored here
automatically whenever it changes, so do not edit the TSV in this repository by hand.

The workflow for contributing data to a training run is unchanged:

1. **Declare** the datasets you want to use by adding them to the catalogue — in the
   [private repository](https://github.com/swiss-ai/apertus-data-transparency-private).
2. **Validation** — the data and legal teams review each entry to confirm the dataset's
   licensing, PII handling and robots filtering are acceptable.
3. **Use only validated datasets** — once an entry has been reviewed and merged, it is cleared for
   use in the training run. Datasets that are not in the catalogue must not be used.
