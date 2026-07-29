# Apertus Data Transparency

This is a repository containing versioned snapshots of key documentation from the Apertus releases.

## The central dataset repository

`Apertus dataset repository.tsv` is the single source of truth for the datasets that go into the
main Apertus training run. It lists every dataset we use, together with its modalities, licenses,
versions, storage paths and processing scripts.

The repository defines the workflow for contributing data to a training run:

1. **Declare** the datasets you want to use by adding them to the catalogue (see below).
2. **Validation** — the data and legal teams review each entry to confirm the dataset's
   licensing, PII handling and robots filtering are acceptable.
3. **Use only validated datasets** — once an entry has been reviewed and merged, it is cleared for
   use in the training run. Datasets that are not in the catalogue must not be used.

## Adding a dataset

There are two ways to add a dataset to the catalogue. Both end with a pull request that the data
and legal teams review before it is merged.

### Option A — Open a "New Dataset" issue (recommended)

1. Go to the repository's **Issues** tab and open a new issue using the
   [**➕ New Dataset**](../../issues/new?template=new_dataset.yml) template.
2. Fill in the form fields (name, modalities, licenses, version, storage paths, processing
   scripts, etc.). Follow the format hints in each field's description.
3. On submit, a GitHub Action validates the required fields and, if everything checks out,
   automatically opens a pull request that appends your dataset as a new row to the TSV. It then
   links the PR back on the issue.
4. If validation fails, the bot comments on the issue listing what needs fixing. **Edit the
   issue** to correct it — the action re-runs automatically and refreshes the pull request.

This route is best if you are not comfortable editing a TSV by hand: the form guides the expected
format and the automation keeps the file consistent.

### Option B — Edit the TSV directly via a pull request

1. Create a branch.
2. Add one row per dataset to `Apertus dataset repository.tsv`, filling in every column
   (use the [**New Dataset** issue template](.github/ISSUE_TEMPLATE/new_dataset.yml) as a
   reference for what each column expects and how to format it).
3. Open a pull request against `main`.

This route is best for bulk additions or edits to existing rows.

In both cases the pull request is only merged once the data and legal teams have validated the
entry.
