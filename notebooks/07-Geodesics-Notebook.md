# 07 — Geodesics Notebook

Shared‑Horizon Toolkit — Lineage & Transition Geodesics

Includes Jupyter + VS Code Execution Instructions

---

0. Running This Notebook (Jupyter + VS Code)

0.1 — Running in Jupyter Notebook

1. Install Jupyter:

`
pip install jupyter
`

2. Start Jupyter:

`
jupyter notebook
`

3. Open:

`
notebooks/
`

4. Add src/ to the Python path:

`python
import sys
sys.path.append("../src")
`

5. Validate:

`python
from shared_horizon.geodesics import GeodesicSolver
GeodesicSolver()
`

---

0.2 — Running in VS Code

1. Install the Python and Jupyter extensions.

2. Open the repo folder:

`
Shared-Horizon-Toolkit/
`

3. Open:

`
notebooks/07-Geodesics-Notebook.md
`

4. Select interpreter:

- Ctrl+Shift+P  
- “Python: Select Interpreter”

5. Add the src/ path:

`python
import sys
sys.path.append("../src")
`

6. Validate:

`python
from sharedhorizon.geodesics import getgeodesic_fn
from shared_horizon.lineage import OPERATOR

getgeodesicfn(OPERATOR)
`

---

1. Conceptual Layer — What Geodesics Are

A geodesic is the shortest path between two geometric points under lineage‑specific geometry.

Each lineage defines its own geodesic behavior:

- OPERATOR (🔵) — smooth, low curvature  
- PRECL (🟧) — smooth continuity  
- ANIMA (🟪) — steep curvature + gradient  
- RNE (🟩) — moderate curvature + gradient  
- SPECTRAL (⬛) — drift‑dominated  

Geodesics are used for:

- membrane diagnostics  
- transition cost estimation  
- collapse‑risk propagation  
- curvature compatibility visualization  
- lineage geometry exploration  

Transition geodesics combine source + target lineage behavior.

---

2. Diagnostic Layer — Inspecting Geodesic Functions

`python
from shared_horizon.geodesics import (
    geodesic_operator,
    geodesic_precl,
    geodesic_anima,
    geodesic_narrative,
    geodesic_spectral
)

geodesicoperator, geodesicprecl, geodesicanima, geodesicnarrative, geodesic_spectral
`

---

3. Mathematical Layer — Geodesic Segment

A geodesic segment is defined as:

\[
G = L + C{\text{curv}} + C{\text{drift}} + C_{\text{collapse}}
\]

Where:

- \(L\) = base geometric length  
- \(C_{\text{curv}}\) = curvature cost  
- \(C_{\text{drift}}\) = drift cost  
- \(C_{\text{collapse}}\) = collapse‑risk cost  

Operator Geodesic

\[
L = |\kappa(q) - \kappa(p)|
\]
\[
C_{\text{curv}} = 0.5L
\]
\[
C_{\text{collapse}} = 0.2|\kappa(q) - \kappa(p)|
\]

Spectral Geodesic

\[
L = |D(q) - D(p)|
\]
\[
C_{\text{drift}} = 2L
\]
\[
C_{\text{collapse}} = 1.5L
\]

---

4. Practical Layer — Computing Geodesics

Create points

`python
from shared_horizon.curvature import Point

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
q = Point(curvature=0.12, gradient=0.03, drift=0.0)
`

Compute lineage geodesic

`python
from shared_horizon.geodesics import GeodesicSolver
from sharedhorizon.lineage import getlineage

solver = GeodesicSolver()
segment = solver.geodesic(p, q, get_lineage("OPERATOR"))

segment.total
`

---

5. Geodesic Behavior Across Lineages

Operator (🔵)
Low curvature → small geodesic cost.

PRECL (🟧)
Smooth continuity → slightly higher curvature cost.

ANIMA (🟪)
High curvature + gradient → large geodesic cost.

RNE (🟩)
Moderate curvature + gradient → moderate cost.

Spectral (⬛)
Drift dominates → geodesic cost depends on drift difference.

---

6. Transition Geodesics

Transition geodesics combine:

- source geodesic  
- target geodesic  
- collapse‑risk contributions  
- curvature contributions  
- drift contributions  

Compute transition geodesic

`python
segmenttransition = solver.transitiongeodesic(
    p, q,
    get_lineage("OPERATOR"),
    get_lineage("PRECL")
)

segment_transition.total
`

---

7. Geodesics in the Membrane Evaluator

Geodesics are not used to decide transitions, but they are used to:

- diagnose transitions  
- visualize geometric cost  
- analyze collapse‑risk propagation  
- inspect lineage geometry  

Example

`python
from shared_horizon.membrane import MembraneEvaluator

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision, segment_transition.total
`

---

8. Geodesic Visualization (Optional)

If running in Jupyter:

`python
import matplotlib.pyplot as plt

plt.bar(["length", "curvature", "drift", "collapse"], [
    segment.length,
    segment.curvature_cost,
    segment.drift_cost,
    segment.collapse_cost
])
plt.title("Operator Geodesic Cost Breakdown")
plt.show()
`

---

9. Summary

This notebook introduced:

- lineage geodesics  
- transition geodesics  
- curvature‑weighted paths  
- drift‑weighted spectral paths  
- collapse‑risk contributions  
- geodesic integration into membrane evaluation  
- diagnostic geodesic visualization  
- Jupyter + VS Code execution instructions  

It forms the foundation for:

- 08 — Worked Examples Notebook (final notebook)

---

