# Apertus Data Transparency

This is a repository contains the single source of truth for the datasets that go into the
main Apertus training run, for each Apertus version. 
It lists every dataset we use, together with its modalities, licenses,
versions, storage paths and processing scripts. The copy in this repository is the **published
snapshot** of the catalogu.

The workflow for contributing data to a training run is unchanged:

1. **Declare** the datasets you want to use by adding them to the catalogue — in the
   [private repository](https://github.com/swiss-ai/apertus-data-transparency-private).
2. **Validation** — the data and legal teams review each entry to confirm the dataset's
   licensing, reproducibility, PII handling and robots filtering are acceptable.
3. **Use only validated datasets** — once an entry has been reviewed and merged, it is cleared for
   use in the training run. Datasets that are not in the catalogue must not be used.
