# 03 — Curvature Notebook

Shared‑Horizon Toolkit — Curvature, Gradient & Drift Geometry

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
notebooks/03-Curvature-Notebook.md
`

4. Add src/ to the Python path:

`python
import sys
sys.path.append("../src")
`

5. Validate:

`python
from shared_horizon.curvature import Point
Point(curvature=0.1, gradient=0.02, drift=0.0)
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
notebooks/03-Curvature-Notebook.md
`

4. Select interpreter:

- Ctrl+Shift+P  
- “Python: Select Interpreter”  
- Choose your environment.

5. Add the src/ path:

`python
import sys
sys.path.append("../src")
`

6. Validate:

`python
from sharedhorizon.curvature import getcurvature_fn
from shared_horizon.lineage import OPERATOR

getcurvaturefn(OPERATOR)
`

---

1. Conceptual Layer — Curvature in Shared‑Horizon

Curvature is the primary geometric quantity for four of the five lineages:

- OPERATOR (🔵) — low curvature, reversible  
- PRECL (🟧) — low curvature, smooth continuity  
- ANIMA (🟪) — high curvature, steep expressive gradients  
- RNE (🟩) — moderate curvature, reversible narrative  
- SPECTRAL (⬛) — drift replaces curvature  

Curvature determines:

- envelope energy  
- collapse‑risk  
- transition compatibility  
- Jacobian smoothness  
- geodesic length  

This notebook introduces curvature functions, gradients, drift, and compatibility logic.

---

2. Diagnostic Layer — Inspecting Curvature Functions

`python
from shared_horizon.curvature import (
    curvature_operator,
    curvature_precl,
    curvature_anima,
    curvature_narrative,
    drift_spectral
)

curvatureoperator, curvatureprecl, curvatureanima, curvaturenarrative, drift_spectral
`

---

3. Mathematical Layer — Curvature & Gradient Definitions

Curvature

For a point \(p\):

\[
\kappa(p) = p.\text{curvature}
\]

Gradient

\[
\nabla \kappa(p) = p.\text{gradient}
\]

Spectral Drift

\[
D(p) = p.\text{drift}
\]

Lineage‑specific curvature behavior

| Lineage | Curvature | Gradient | Drift |
|--------|-----------|----------|-------|
| OPERATOR | ✓ | ✓ | ✗ |
| PRECL | ✓ | ✓ | ✗ |
| ANIMA | ✓ | ✓ | ✗ |
| RNE | ✓ | ✓ | ✗ |
| SPECTRAL | ✗ | ✗ | ✓ |

---

4. Practical Layer — Using Curvature in Code

Create a point

`python
from shared_horizon.curvature import Point

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
`

Evaluate curvature

`python
from sharedhorizon.curvature import getcurvature_fn
from shared_horizon.lineage import OPERATOR

fn = getcurvaturefn(OPERATOR)
fn(p)
`

Evaluate gradient

`python
from sharedhorizon.curvature import curvaturegradient

curvature_gradient(p)
`

Evaluate spectral drift

`python
from sharedhorizon.curvature import driftspectral

drift_spectral(p)
`

---

5. Curvature Compatibility

Curvature compatibility determines whether a transition is geometrically safe:

`python
from sharedhorizon.curvature import curvaturecompatible

q = Point(curvature=0.12, gradient=0.03, drift=0.0)
curvature_compatible(p, q)
`

Rules:

- Operator → PRECL: low curvature required  
- ANIMA → RNE: curvature must match  
- Spectral → anything: incompatible  
- Default: curvature cannot increase sharply  

---

6. Curvature in the Membrane Evaluator

Curvature is used in:

- envelope energy  
- collapse‑risk tensors  
- Jacobian smoothness  
- transition compatibility  
- firewall checks  
- geodesic computation  

Example: membrane evaluation

`python
from shared_horizon.membrane import MembraneEvaluator

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision
`

---

7. Curvature in Geodesics

Curvature contributes to geodesic length:

`python
from shared_horizon.geodesics import GeodesicSolver
from sharedhorizon.lineage import getlineage

solver = GeodesicSolver()
segment = solver.geodesic(p, q, get_lineage("OPERATOR"))

segment.total
`

---

8. Summary

This notebook introduced:

- curvature functions  
- curvature gradients  
- spectral drift  
- lineage‑specific curvature behavior  
- curvature compatibility  
- curvature in membrane evaluation  
- curvature in geodesics  
- Jupyter + VS Code execution instructions  

It forms the foundation for:

- 04 — Collapse Notebook  
- 05 — Transition Notebook  
- 06 — Membrane Notebook  
- 07 — Geodesics Notebook  
- 08 — Worked Examples  

---

