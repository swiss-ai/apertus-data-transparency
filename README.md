# Apertus Data Transparency

This repository contains the single source of truth for datasets that go into the
main Apertus training run, for each Apertus version. 

For a general overview of the datasets and methods, see the Public Summary published in [@swiss-ai/apertus-legal](https://github.com/swiss-ai/apertus-legal).

## Usage

The table (TSV file) here, and for historical reference in the `reports` folder, lists every dataset we use. 

This includes metadata about the dataset modalities, licenses,
versions, storage paths and processing scripts. The copy in this repository is the **published
snapshot** of the catalog.

## Contributing

Our workflow for contributing data to a training run is as follows:

1. **Declare** the datasets you want to use by adding them to the internal catalogue — in the
   [private repository](https://github.com/swiss-ai/apertus-data-transparency-private).
2. **Validation** — the data and legal teams review each entry to confirm the dataset's
   licensing, reproducibility, PII handling and robots filtering are acceptable.
3. **Use only validated datasets** — once an entry has been reviewed and merged, it is cleared for
   use in the training run. Datasets that are not in the catalogue must not be used.
4. **Sync the metadata** - at regular intervals, we share our catalogue with the public here: at latest, the complete information must be available at release time.

Please use the Issues here, or use the contacts on the [Apertus website](https://apertus-ai.org/contact), if you have questions.
