# Infra Atlas

An English catalogue of 1,133 systems-research papers, with conference navigation and eight parallel facets: Workload, Technique, Bottleneck, Deployment, Objective, Stage, Architecture and Resource.

## Browse

Open `index.html` directly or serve this directory as a static website. All classification data is embedded, so browsing needs no backend. Publication links open the original source. Six items without verified publication URLs use a clearly labeled title search. Full-text PDFs are not included.

Tags within a facet use OR; facets combine with AND. The FACETS overview always shows whole-library coverage. Individual tag counts respond to other active filters. Bookmarks remain in the visitor's browser. Filtered results can be exported as JSON.

## Classification

Tags combine title/abstract classification, evaluation-section evidence, and targeted review. Evidence includes PDF page numbers. Automated classification is provisional and does not imply a full manual review. Evaluation hardware and workloads may differ from a paper's central contribution. Other is excluded from specific-tag coverage.

## Update and build

- `data/library.json`: English paper records and taxonomy.
- `data/papers.json`: downloadable paper records, generated during build.
- `source/template.html`: catalogue template.
- `source/recovered-links.json`: publication links recovered from DOI statements in local PDFs.
- `source/build.py`: dependency-free Python 3 static build.
- `source/classification-audit.md` and `source/architecture-audit.md`: English review notes and classification boundaries.

```sh
python3 source/build.py
python3 -m http.server 8000
```

The static web version uses source links rather than local filesystem paths. Keep the data, source and README beside `index.html`.
