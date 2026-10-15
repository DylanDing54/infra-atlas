# Classification review

The published snapshot contains 1,133 papers, including 24 papers under Technique → Speculative Decoding. It includes subsequent workload and architecture refinements. Current tag counts are stored in `data/library.json`; the architecture review is summarized in [architecture-audit.md](architecture-audit.md).

The review checked catalogue structure, tag/count/coverage consistency, and ambiguous keywords, with targeted abstract and PDF reading for speculative decoding and boundary cases. It was not a complete manual reading of every paper.

Speculative Decoding includes token drafting and verification/sampling, self-speculation, hybrid diffusion drafting, and explicitly evaluated integrations, kernel support or diagnostic case studies. Speculation remains the broader parent tag. Protocol Buffer decoding, speculative prefetching or encryption, context-sparsity prediction, background citations and future work alone do not qualify.

Corrections distinguish AR from autoregressive decoding, rendering as a general verb, MOE institutional names from mixture-of-experts models, and PIM/Parallel Iterative Matching from processing-in-memory. They also address transaction serialization, model/expert routing, training-free stages, code/specification inference, and serving-as phrasing. SPEC CPU no longer implies a managed-language runtime.

Architecture/Resource overlap is intentional. Evaluated hardware and workloads are useful retrieval labels and should not automatically be treated as the main contribution. Some extracted abstracts contain front matter or are incomplete; consult the paper and quoted evidence.
