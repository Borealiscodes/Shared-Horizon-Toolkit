# 06 — Membrane Notebook

Shared‑Horizon Toolkit — Full Membrane Evaluator

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
notebooks/06-Membrane-Notebook.md
`

4. Add src/ to the Python path:

`python
import sys
sys.path.append("../src")
`

5. Validate:

`python
from shared_horizon.membrane import MembraneEvaluator
MembraneEvaluator()
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
notebooks/06-Membrane-Notebook.md
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
from shared_horizon.membrane import MembraneEvaluator
MembraneEvaluator()
`

---

1. Conceptual Layer — What the Membrane Is

The membrane is the unified evaluator that determines whether a transition between two geometric points is allowed.

It integrates:

- envelope safety  
- curvature compatibility  
- collapse‑risk compatibility  
- Jacobian smoothness  
- transition logic  
- firewall enforcement  
- lineage geometry  
- geodesic behavior  

The membrane is the final arbiter of geometric safety in the Shared‑Horizon architecture.

---

2. Diagnostic Layer — Inspecting the Membrane Evaluator

`python
from shared_horizon.membrane import MembraneEvaluator

evaluator = MembraneEvaluator()
evaluator
`

Inspect the evaluate() method:

`python
import inspect
print(inspect.getsource(MembraneEvaluator.evaluate))
`

This shows the full evaluation pipeline.

---

3. Mathematical Layer — Membrane Evaluation Pipeline

A transition \(p \rightarrow q\) from lineage \(Ls\) to \(Lt\) is allowed only if:

1. Envelope Safety

\[
E{Ls}(p) \leq B{Ls}
\]
\[
E{Lt}(q) \leq B{Lt}
\]

2. Curvature Compatibility

\[
\kappa(p) \rightarrow \kappa(q) \text{ is smooth}
\]

3. Collapse‑Risk Compatibility

\[
C(q) \leq 1.2 \cdot C(p)
\]

4. Jacobian Smoothness

\[
|J(p, q)| \leq 2 \cdot B{Lt}
\]

5. Firewall Enforcement

Hard blocks:

- Spectral → anything  
- PRECL → OPERATOR  
- ANIMA → OPERATOR  
- Collapse‑risk spike > 50%  
- Jacobian blowout  

6. Final Decision

\[
\text{allowed} = \text{True/False}
\]

---

4. Practical Layer — Running the Membrane Evaluator

Create points

`python
from shared_horizon.curvature import Point

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
q = Point(curvature=0.12, gradient=0.03, drift=0.0)
`

Run evaluation

`python
from shared_horizon.membrane import MembraneEvaluator

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision
`

Expected:

`
MembraneDecision(
    allowed=True,
    reason="Transition allowed by membrane.",
    lineage_source="OPERATOR",
    lineage_target="PRECL"
)
`

---

5. Envelope Stage

`python
from sharedhorizon.envelopes import envelopesafe

envelopesafe(p, "OPERATOR"), envelopesafe(q, "PRECL")
`

---

6. Curvature Stage

`python
from sharedhorizon.curvature import curvaturecompatible

curvature_compatible(p, q)
`

---

7. Collapse‑Risk Stage

`python
from sharedhorizon.collapse import collapsecompatible

collapse_compatible(p, q)
`

---

8. Jacobian Stage

`python
from sharedhorizon.jacobian import jacobiansafe
from sharedhorizon.lineage import getlineage

jacobiansafe(p, q, getlineage("PRECL"))
`

---

9. Firewall Stage

`python
from shared_horizon.firewall import firewall
from sharedhorizon.lineage import getlineage

source = get_lineage("OPERATOR")
target = get_lineage("PRECL")

firewall(source, target, p, q)
`

---

10. Geodesic Integration

`python
from shared_horizon.geodesics import GeodesicSolver
from sharedhorizon.lineage import getlineage

solver = GeodesicSolver()
segment = solver.transitiongeodesic(p, q, getlineage("OPERATOR"), get_lineage("PRECL"))

segment.total
`

---

11. Full Pipeline Visualization

`python
{
    "envelopesource": envelopesafe(p, "OPERATOR"),
    "envelopetarget": envelopesafe(q, "PRECL"),
    "curvature": curvature_compatible(p, q),
    "collapse": collapse_compatible(p, q),
    "jacobian": jacobiansafe(p, q, getlineage("PRECL")),
    "firewall": firewall(source, target, p, q),
    "geodesic_total": segment.total,
    "membrane_decision": decision
}
`

---

12. Summary

This notebook introduced:

- the full membrane evaluator  
- envelope → curvature → collapse → Jacobian → firewall pipeline  
- lineage‑specific behavior  
- transition safety  
- geodesic integration  
- diagnostic inspection  
- Jupyter + VS Code execution instructions  

It forms the foundation for:

- 07 — Geodesics Notebook  
- 08 — Worked Examples Notebook  

---

