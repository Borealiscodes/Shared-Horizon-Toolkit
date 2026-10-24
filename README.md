# 🌌 Shared‑Horizon Toolkit

Modular Python implementation of the Shared‑Horizon membrane architecture (2026)

The Shared‑Horizon Toolkit is the canonical Python implementation of the membrane architecture described in the Shared‑Horizon Unified Preprint (2026).  
It provides modular, inspectable components for:

- lineage geometry  
- stability envelopes  
- curvature & drift operators  
- collapse‑risk tensors  
- transition maps  
- membrane evaluation  
- geodesic computation  
- worked examples  

This repository is the operational companion to the mathematical preprint.

---

🧩 Color‑Tile Lineage Map

Each module corresponds to one or more tiles in the Shared‑Horizon mosaic:

| Tile | Emoji | Lineage | Description |
|------|-------|---------|-------------|
| 🔵 Blue | 🔵 | Operator Geometry (NDH) | Reversible operators, holonomy preservation |
| 🟧 Orange | 🟧 | PRECL Continuity Systems | Low‑curvature expressive continuity |
| 🟪 Violet | 🟪 | ANIMA Phenomenology | High‑curvature expressive phenomenology |
| 🟩 Green | 🟩 | Reversible Narrative Ecology (RNE) | Curvature‑preserving narrative operators |
| ⬛ Black | ⬛ | Spectral Runtime Systems | Drift‑based spectral instability |

These tiles appear throughout the toolkit to indicate lineage‑specific logic.

---

🟪 ANIMA Classic (External Expressive Lineage)

High‑curvature expressive phenomenology system (Stell, 2026)

The Shared‑Horizon expressive lineage is historically grounded in ANIMA Classic, Stell’s original high‑curvature expressive system.

🔗 ANIMA Classic Repository:  
https://github.com/stell2026/Anima

ANIMA Classic provides the expressive curvature profile that informed:

- ANIMA manifold definition  
- expressive collapse‑risk geometry  
- expressive → operator firewall boundaries  
- expressive → narrative reversibility constraints  

All expressive geometry in the Toolkit is original to Shared‑Horizon but acknowledges ANIMA Classic as its lineage predecessor.

---

🗂️ Repository Structure (src‑based layout)

`
<pre> 

Shared-Horizon-Toolkit/
│
├── README.md
├── LICENSE
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── shared_horizon/
│       ├── init.py
│       ├── lineage.py          🔵🟧🟪🟩⬛
│       ├── envelopes.py        🔵🟧🟪🟩⬛
│       ├── curvature.py        🔵🟧🟪🟩
│       ├── collapse.py         🔵🟧🟪🟩⬛
│       ├── transition.py       🔵🟧🟪🟩⬛
│       ├── jacobian.py         🔵🟧🟪🟩⬛
│       ├── firewall.py         🔵🟧🟪🟩⬛
│       ├── membrane.py         🔵🟧🟪🟩⬛
│       ├── geodesics.py        🔵🟧🟪🟩⬛
│       └── examples.py         🔵🟧🟪🟩⬛
│
├── notebooks/
│   ├── 01-Lineage-Notebook.md
│   ├── 02-Envelopes-Notebook.md
│   ├── 03-Curvature-Notebook.md
│   ├── 04-Collapse-Notebook.md
│   ├── 05-Transition-Notebook.md
│   ├── 06-Membrane-Notebook.md
│   ├── 07-Geodesics-Notebook.md
│   └── 08-Worked-Examples.md
│
├── tests/
│   ├── test_lineage.py
│   ├── test_envelopes.py
│   ├── test_curvature.py
│   ├── test_collapse.py
│   ├── test_transition.py
│   ├── test_firewall.py
│   ├── test_membrane.py
│   └── test_geodesics.py
│
└── docs/
    ├── architecture.md
    ├── membrane-state-machine.md
    ├── mosaic-specification.md
    └── provenance.md

</pre>

`

This layout follows modern Python packaging standards and ensures clean imports:

`
from shared_horizon.lineage import OPERATOR
`

---

📦 Installation

Install via pip:

`
pip install shared-horizon-toolkit
`

Or clone the repository:

`
git clone https://github.com/<your-username>/Shared-Horizon-Toolkit.git
`

---

🔧 Modules Overview

🔵🟧🟪🟩⬛ lineage.py
Canonical lineage definitions: OPERATOR, PRECL, ANIMA, RNE, SPECTRAL.

🔵🟧🟪🟩⬛ envelopes.py
Stability envelopes, energy functionals, lineage‑specific envelope logic.

🔵🟧🟪🟩 curvature.py
Curvature, drift, divergence, curvature‑gradient operators.

🔵🟧🟪🟩⬛ collapse.py
Collapse‑risk tensors, gradients, envelopes, drift‑risk evaluation.

🔵🟧🟪🟩⬛ transition.py
Transition maps, curvature compatibility, collapse‑risk preservation.

🔵🟧🟪🟩⬛ jacobian.py
Jacobian bound evaluation for smoothness constraints.

🔵🟧🟪🟩⬛ firewall.py
Mosaic boundary enforcement (forbidden lineage transitions).

🔵🟧🟪🟩⬛ membrane.py
Full membrane evaluator: envelope → curvature → collapse → Jacobian → reversibility → firewall.

🔵🟧🟪🟩⬛ geodesics.py
Lineage geodesics and transition geodesics.

🔵🟧🟪🟩⬛ examples.py
Worked membrane evaluations (Appendix M logic).

---

📘 Notebooks (Dream‑Lab Style)

The /notebooks/ directory contains .md notebooks with:

- conceptual intros  
- runnable Python cells  
- diagrams  
- membrane evaluation walkthroughs  
- lineage‑specific examples  
- collapse‑risk visualizations  
- provenance footers  

These notebooks mirror the Dream Lab format and serve as the pedagogical layer of the toolkit.

---

🧬 Relationship to the Unified Preprint

This toolkit implements the mathematical spine described in:

Shared‑Horizon Unified Preprint (2026)  
including Appendices A–M:

- operator geometry  
- expressive manifolds  
- narrative curvature  
- spectral drift  
- stability envelopes  
- collapse‑risk tensors  
- transition maps  
- membrane algorithms  
- state machine  
- worked examples  

The toolkit is the operational counterpart to the preprint.

---

🏛️ Provenance

Authored by Borealis S. Hedling (2026).  
All lineage definitions, membrane constraints, curvature/drift structures, and collapse‑risk geometry originate from the Shared‑Horizon research corpus.

This repository provides the canonical Python implementation of the membrane architecture.

---

