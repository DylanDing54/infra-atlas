# Architecture review

This published snapshot contains 1,133 papers. Architecture has specific tags for 1,091 papers; 42 use Other. Tags can overlap.

## Scope and evidence

Architecture describes research/design targets, measured testbeds and explicitly simulated or synthesized platforms. Background references and comparator-only mentions are excluded. Each architecture evidence record identifies its quote, PDF page when available, platform role and review status. Source links open the publication; page numbers refer to the original PDF and do not imply direct navigation to that page.

The source review searched cached text from all 1,133 PDFs (15,486 pages), validated 1,965 evidence records against 629 PDF pages, and recorded 185 targeted decisions across 164 papers. These are reported results from the source review, not a new full-text audit performed for this upload. Keyword searches and quote validation do not establish the semantic correctness of every tag. Automatically inferred roles can still require review.

## Boundaries

- GPU requires execution or an explicit testbed; a vendor name, network adapter or comparison alone is insufficient.
- Custom accelerators include ASICs, NPUs, TPUs and wafer-scale processors. Evidence distinguishes measured hardware from simulation/synthesis.
- Near-Memory Computing, PIM / CIM and Near-Storage Computing are separate tags; ordinary caching or memory expansion does not imply PIM.
- Heterogeneous refers to hardware or memory/storage tiers, not diversity of workloads, models or service-level objectives.
- Distributed requires communicating independent workers, replicas or nodes. It does not automatically imply cloud or multiple physical machines.
- DRAM / DDR, SRAM / Scratchpad, Persistent Memory / NVM, HBM and HBF require explicit technology evidence.
- Language VMs and bytecode sandboxes use Runtime / Sandbox, separate from system/device virtualization.
- Resource can describe hardware involved or discussed, so its tags need not match Architecture exactly.

## Current tags

| Tag | Papers | Definition |
| --- | ---: | --- |
| CPU | 569 | A processor execution target or explicit experimental host. A CPU comparison alone is insufficient. |
| GPU | 502 | GPU execution or an explicit GPU testbed. Vendor names, GPU baselines and NVIDIA network adapters alone are insufficient. |
| FPGA | 39 | FPGA implementation, prototyping or synthesis target; not merely a compared accelerator. |
| Custom ASIC / NPU / TPU | 59 | Dedicated chip/accelerator designs, including synthesized ASICs, NPUs, TPUs and wafer-scale processors. The evidence states whether hardware is measured or simulated. |
| DSP | 1 | Digital signal processor execution or DSP-specific hardware/software research. |
| CGRA / Dataflow | 12 | Coarse-grained reconfigurable or spatial/handshake dataflow hardware. A software dataflow graph alone is insufficient. |
| Quantum | 25 | Quantum processors, qubits or quantum-machine organization, including simulated quantum systems. |
| Near-Memory Computing | 4 | Compute positioned close to memory, such as logic alongside memory devices. Ordinary caching or memory expansion alone is insufficient. |
| PIM / CIM | 16 | Processing/computation in memory as explicitly described by the paper. PIM as Parallel Iterative Matching is excluded. Author terminology may overlap near-memory designs. |
| Near-Storage Computing | 4 | Compute within or adjacent to storage devices, including computational storage and in-flash processing. |
| DRAM / DDR | 16 | Explicit DRAM/DDR design, memory organization or evaluated configuration; includes RowHammer defenses. Generic RAM does not determine the technology. |
| SRAM / Scratchpad | 4 | Explicit SRAM-based architecture or software-managed scratchpad. A generic cache does not establish SRAM technology. |
| Persistent Memory / NVM | 17 | Persistent/non-volatile hardware memory, such as Optane or byte-addressable NVM. Agent conversation memory and ordinary file persistence are excluded. |
| HBM | 26 | Explicit high-bandwidth memory evidence. Not inferred from generic DRAM or every GPU model. |
| HBF | 1 | Explicit high-bandwidth flash. Ordinary flash storage does not imply HBF. |
| CXL | 36 | A CXL design, supported architecture option, real testbed or explicit emulation. Related-work and comparator-only mentions are excluded. |
| SSD / Flash | 154 | SSD, NVMe, UFS or flash hardware used by the system. FlashAttention, Gemini Flash and similarly named software are excluded. |
| SmartNIC / DPU | 21 | Programmable network-interface or infrastructure offload processors. UPMEM DRAM processing units do not establish a network DPU. |
| Programmable Switch | 10 | Programmable switch/data-plane hardware or its explicit emulation, including P4/Tofino pipelines. |
| Disaggregation | 50 | Independently managed compute, memory, storage or service-stage resources. Can be within a node. Model refactoring, bit slicing and on-chip unit separation alone are excluded. |
| Heterogeneous | 93 | Explicitly different processor/device types, compute units or memory/storage tiers in the target design or testbed. Workload, model, graph, request and SLO diversity alone are excluded. |
| Distributed | 160 | Communicating independent workers, replicas or nodes, including explicit distributed GPU runtimes. Does not necessarily imply cloud or multiple physical machines. Statistical distributions, RAID placement and on-chip core distribution alone are excluded. |
| Serverless | 38 | Function/serverless execution as a design target or evaluated deployment. Replaying a serverless request trace alone is insufficient. |
| Virtualization | 53 | System, OS, device or network virtualization: VMs, hypervisors, virtual switches and virtual devices. Language VMs and bytecode sandboxes have a separate tag. |
| Runtime / Sandbox | 7 | Language/bytecode VMs, execution runtimes and software isolation compartments. Does not imply hardware virtualization. |
| Microservices | 8 | Decomposed communicating service applications or a measured microservice workload. Using Go alone is insufficient. |
| Federated | 14 | Federated/cross-domain computation or coordinated clients that retain local control, not just data with a statistical distribution. |
| TEE / Confidential Computing | 26 | A hardware-backed execution security boundary, including SGX, SEV, TDX, TrustZone and CCA. A trusted/authenticated device alone is insufficient. |
| Other | 42 | Insufficient evidence or outside the current categories. |

Current evidence statuses: automated: 1,833, reviewed: 132.
