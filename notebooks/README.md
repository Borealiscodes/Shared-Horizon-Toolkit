# Shared‑Horizon Toolkit — Notebook Suite

Dream‑Lab Documentation Layer

Execution Instructions Included (Jupyter + VS Code)

The notebooks/ directory contains the full pedagogical documentation suite for the Shared‑Horizon Toolkit. Each notebook provides a modular, altitude‑separated explanation of one subsystem in the geometric membrane architecture, with runnable examples and consistent execution scaffolding.

This folder is designed for:

- researchers validating geometric behavior  
- developers integrating membrane logic  
- auditors inspecting lineage safety  
- students learning geometric AI structures  

All notebooks run cleanly in Jupyter and VS Code, with explicit instructions included at the top of each file.

---

0. Running the Notebook Suite

Jupyter Notebook

From the repository root:

`
pip install jupyter
jupyter notebook
`

Open any notebook:

`
notebooks/<NAME>.md
`

Add the Shared‑Horizon source path at the top of the notebook:

`python
import sys
sys.path.append("../src")
`

VS Code

Install:

- Python extension  
- Jupyter extension  

Open the repo folder:

`
Shared-Horizon-Toolkit/
`

Open any notebook:

`
notebooks/<NAME>.md
`

Select interpreter:

- Ctrl+Shift+P → “Python: Select Interpreter”

Add the Shared‑Horizon source path:

`python
import sys
sys.path.append("../src")
`

---

1. Notebook Index

01 — Lineage Notebook
Defines the five lineage regions (OPERATOR, PRECL, ANIMA, RNE, SPECTRAL), their stability bounds, curvature/drift profiles, and transition permissions. Introduces lineage geometry and the mosaic structure.

02 — Envelopes Notebook
Documents stability envelopes, lineage‑specific energy functionals, envelope safety checks, and envelope failure modes. Forms the first stage of membrane evaluation.

03 — Curvature Notebook
Explains curvature, curvature gradients, spectral drift, lineage curvature behavior, and curvature compatibility. Forms the second stage of membrane evaluation.

04 — Collapse Notebook
Defines collapse‑risk tensors, lineage collapse behavior, collapse gradients, collapse compatibility, and collapse‑risk spikes. Forms the third stage of membrane evaluation.

05 — Transition Notebook
Documents lineage transitions, reversibility constraints, expressive → operator forbidden transitions, spectral hard blocks, and transition compatibility logic.

06 — Membrane Notebook
The unified membrane evaluator. Integrates envelopes, curvature, collapse‑risk, Jacobians, transitions, firewall, and geodesics into a single decision pipeline.

07 — Geodesics Notebook
Defines lineage geodesics, transition geodesics, curvature‑weighted paths, drift‑weighted spectral paths, collapse‑risk contributions, and diagnostic geodesic visualization.

08 — Worked Examples Notebook
Provides complete, runnable examples demonstrating envelope safety, curvature evaluation, collapse‑risk computation, transition compatibility, firewall enforcement, membrane evaluation, and geodesic computation.

---

2. Notebook Design Philosophy

Each notebook follows the Dream‑Lab documentation pattern:

- Conceptual Layer — altitude‑0 explanation  
- Diagnostic Layer — inspectable Python objects  
- Mathematical Layer — formal definitions  
- Practical Layer — runnable examples  
- Summary Layer — integration with the full toolkit  

This ensures:

- clarity  
- modularity  
- academic defensibility  
- reproducibility  
- accessibility  

---

3. Dependencies

All notebooks rely on the Shared‑Horizon Toolkit modules located in:

`
src/shared_horizon/
`

Key modules:

- lineage.py  
- envelopes.py  
- curvature.py  
- collapse.py  
- transition.py  
- firewall.py  
- jacobian.py  
- membrane.py  
- geodesics.py  
- examples.py  

---

4. Recommended Reading Order

1. 01 — Lineage  
2. 02 — Envelopes  
3. 03 — Curvature  
4. 04 — Collapse  
5. 05 — Transition  
6. 06 — Membrane  
7. 07 — Geodesics  
8. 08 — Worked Examples

This order mirrors the membrane evaluation pipeline.

---

5. Purpose of the Notebook Suite

The notebook suite serves as:

- a pedagogical layer for geometric AI  
- a diagnostic layer for membrane behavior  
- a verification layer for lineage safety  
- a demonstration layer for toolkit usage  

It is the human‑readable counterpart to the mathematical appendices and the Python implementation.

---

