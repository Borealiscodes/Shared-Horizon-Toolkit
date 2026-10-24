# 04 — Collapse Notebook

Shared‑Horizon Toolkit — Collapse‑Risk Geometry

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
notebooks/04-Collapse-Notebook.md
`

4. Add src/ to the Python path:

`python
import sys
sys.path.append("../src")
`

5. Validate:

`python
from sharedhorizon.collapse import getcollapse_fn
from shared_horizon.lineage import OPERATOR

getcollapsefn(OPERATOR)
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
notebooks/04-Collapse-Notebook.md
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
from shared_horizon.collapse import CollapseRisk
CollapseRisk(0.1, 0.2, 0.0)
`

---

1. Conceptual Layer — What Collapse‑Risk Means

Collapse‑risk is the instability measure of a point in lineage geometry.

It is composed of:

- curvature term  
- gradient term  
- drift term (spectral only)  

Collapse‑risk determines:

- whether a transition is safe  
- whether a lineage can support a point  
- whether the firewall blocks a transition  
- whether the membrane evaluator allows the transition  

Collapse‑risk is lineage‑specific:

| Lineage | Curvature | Gradient | Drift |
|--------|-----------|----------|-------|
| OPERATOR | low | low | none |
| PRECL | low | low | none |
| ANIMA | high | high | none |
| RNE | moderate | moderate | none |
| SPECTRAL | none | none | drift‑dominated |

---

2. Diagnostic Layer — Inspecting Collapse Functions

`python
from shared_horizon.collapse import (
    collapse_operator,
    collapse_precl,
    collapse_anima,
    collapse_narrative,
    collapse_spectral
)

collapseoperator, collapseprecl, collapseanima, collapsenarrative, collapse_spectral
`

---

3. Mathematical Layer — Collapse‑Risk Tensor

A collapse‑risk tensor is defined as:

\[
C(p) = C{\text{curv}} + C{\text{grad}} + C_{\text{drift}}
\]

Where:

- \(C{\text{curv}} = |\kappa(p)| \cdot w{\text{curv}}\)  
- \(C{\text{grad}} = |\nabla \kappa(p)| \cdot w{\text{grad}}\)  
- \(C{\text{drift}} = |D(p)| \cdot w{\text{drift}}\)  

Weights are lineage‑specific.

Example (ANIMA):

\[
C_{\text{anima}}(p) = 1.2|\kappa(p)| + 1.0|\nabla\kappa(p)|
\]

Example (Spectral):

\[
C_{\text{spectral}}(p) = 1.5|D(p)|
\]

---

4. Practical Layer — Using Collapse‑Risk in Code

Create a point

`python
from shared_horizon.curvature import Point

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
`

Evaluate collapse‑risk

`python
from sharedhorizon.collapse import getcollapse_fn
from shared_horizon.lineage import OPERATOR

risk = getcollapsefn(OPERATOR)(p).total
risk
`

Compare collapse‑risk across lineages

`python
from sharedhorizon.lineage import EXPRESSIVEANIMA

riskanima = getcollapsefn(EXPRESSIVEANIMA)(p).total
risk_anima
`

---

5. Collapse Compatibility

Collapse compatibility determines whether a transition is safe:

`python
from sharedhorizon.collapse import collapsecompatible

q = Point(curvature=0.12, gradient=0.03, drift=0.0)
collapse_compatible(p, q)
`

Rules:

- Operator → PRECL: collapse‑risk must not increase sharply  
- ANIMA → RNE: gradient must decrease  
- Spectral → anything: drift must not increase  
- Default: collapse‑risk cannot increase by > 20%  

---

6. Collapse‑Risk in the Firewall

The firewall blocks transitions where collapse‑risk spikes:

`python
from shared_horizon.firewall import firewall
from sharedhorizon.lineage import getlineage

source = get_lineage("OPERATOR")
target = get_lineage("PRECL")

firewall(source, target, p, q)
`

A collapse‑risk spike is defined as:

\[
C(q) > 1.5 \cdot C(p)
\]

---

7. Collapse‑Risk in the Membrane Evaluator

Collapse‑risk is integrated into the membrane evaluator:

`python
from shared_horizon.membrane import MembraneEvaluator

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision
`

---

8. Collapse‑Risk in Geodesics

Collapse‑risk contributes to geodesic cost:

`python
from shared_horizon.geodesics import GeodesicSolver
from sharedhorizon.lineage import getlineage

solver = GeodesicSolver()
segment = solver.geodesic(p, q, get_lineage("ANIMA"))

segment.collapse_cost
`

---

9. Summary

This notebook introduced:

- collapse‑risk tensors  
- lineage‑specific collapse behavior  
- collapse‑risk gradients  
- collapse compatibility  
- collapse‑risk spikes  
- firewall collapse‑risk enforcement  
- membrane integration  
- geodesic collapse‑risk contributions  
- Jupyter + VS Code execution instructions  

It forms the foundation for:

- 05 — Transition Notebook  
- 06 — Membrane Notebook  
- 07 — Geodesics Notebook  
- 08 — Worked Examples  

---

