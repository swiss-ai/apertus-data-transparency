Apertus Data Transparency
---

This branch proposes a "static" version of `main`. Whereas `main` uses git tags to point to documents belonging to specific versions of Apertus, `static_folder_structure` keeps each version's document in a dedicated folder. 

The folder structure is thus the following: 

```
reports/ # Contains editable files
    |__ v1_0/
         |_some_v1_report.txt
         |_some_other_v1_report.docx
         |_...
    |__ v1_1/
         |_...
    |__ ...
         |_...
    |__ v2_0/
         |_...

# And the same goes for PDFs
pdfs/
    |__ v1_0/
    |__ v1_1/
    |__ ...
    |__ v2_0/
```
