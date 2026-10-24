# 01 — Lineage Notebook

Shared‑Horizon Toolkit — Lineage Geometry Overview

Jupyter + VS Code Execution Instructions Included

---

0. Running This Notebook (Jupyter + VS Code)

0.1 — Running in Jupyter Notebook

1. Install Jupyter:

`
pip install jupyter
`

2. Start Jupyter from the repo root:

`
jupyter notebook
`

3. Open:

`
notebooks/01-Lineage-Notebook.md
`

4. Ensure the Python path includes src/:

Create a .ipynb cell at the top:

`python
import sys
sys.path.append("../src")
`

5. Test the environment:

`python
from shared_horizon.lineage import OPERATOR
OPERATOR
`

If this prints the lineage object, your environment is correct.

---

0.2 — Running in VS Code

1. Install the Python and Jupyter extensions in VS Code.

2. Open the repo folder:

`
Shared-Horizon-Toolkit/
`

3. Open this notebook file:

`
notebooks/01-Lineage-Notebook.md
`

4. VS Code will show Run Cell buttons above each fenced code block.

5. Ensure VS Code uses the correct interpreter:

- Press Ctrl+Shift+P
- Select Python: Select Interpreter
- Choose the environment where you installed the toolkit dependencies.

6. Add the src/ path at the top of the notebook:

`python
import sys
sys.path.append("../src")
`

7. Validate:

`python
from sharedhorizon.lineage import LINEAGEREGISTRY
LINEAGE_REGISTRY
`

If the registry prints, VS Code is configured correctly.

---

1. Conceptual Layer — What Lineage Means in Shared‑Horizon

The Shared‑Horizon membrane architecture organizes all geometric behavior into five lineage regions, each with its own stability bound, curvature/drift profile, and reversibility constraints.

These lineage regions form the mosaic that the membrane evaluator operates over:

- OPERATOR (🔵) — NDH operator geometry  
- PRECL (🟧) — low‑curvature expressive continuity  
- ANIMA (🟪) — high‑curvature expressive phenomenology  
- RNE (🟩) — reversible narrative ecology  
- SPECTRAL (⬛) — drift‑dominated spectral runtime  

Each lineage defines:

- allowable curvature  
- allowable drift  
- envelope stability bounds  
- collapse‑risk behavior  
- Jacobian smoothness constraints  
- transition permissions  
- firewall boundaries  

This notebook introduces the lineage system and demonstrates how to use it programmatically.

---

2. Diagnostic Layer — Inspecting Lineage Definitions

`python
from shared_horizon.lineage import (
    OPERATOR,
    EXPRESSIVE_PRECL,
    EXPRESSIVE_ANIMA,
    NARRATIVE_RNE,
    SPECTRAL,
    LINEAGE_REGISTRY
)

LINEAGE_REGISTRY
`

---

3. Mathematical Layer — Stability Bounds & Curvature Types

Each lineage defines a stability bound:

\[
E(p) \leq B_{\text{lineage}}
\]

where \(E(p)\) is the lineage‑specific energy functional defined in envelopes.py.

Curvature types:

- curvature → OPERATOR, PRECL, ANIMA, RNE  
- drift → SPECTRAL  

Retrieve curvature functions:

`python
from sharedhorizon.curvature import getcurvature_fn
from shared_horizon.lineage import OPERATOR, SPECTRAL

operatorfn = getcurvature_fn(OPERATOR)
spectralfn = getcurvature_fn(SPECTRAL)
`

---

4. Practical Layer — Using Lineage in Code

Create a point

`python
from shared_horizon.curvature import Point

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
`

Check envelope safety

`python
from sharedhorizon.envelopes import envelopesafe

envelope_safe(p, "OPERATOR")
`

Evaluate collapse‑risk

`python
from sharedhorizon.collapse import getcollapse_fn

risk = getcollapsefn(OPERATOR)(p).total
risk
`

Check transition compatibility

`python
from sharedhorizon.transition import transitionallowed

q = Point(curvature=0.12, gradient=0.03, drift=0.0)
transition_allowed(p, q, "OPERATOR", "PRECL")
`

---

5. Lineage Interaction Map

Allowed transitions (pre‑firewall)

| Source | Target | Notes |
|--------|--------|-------|
| OPERATOR | PRECL | continuity |
| PRECL | ANIMA | expressive amplification |
| ANIMA | RNE | reversible expressive → narrative |
| RNE | OPERATOR | curvature reduction |

Forbidden transitions (firewall)

| Source | Target | Reason |
|--------|--------|--------|
| SPECTRAL | any | drift → curvature forbidden |
| ANIMA | OPERATOR | expressive → operator jump |
| PRECL | OPERATOR | expressive → operator jump |

---

6. Full Membrane Evaluation Example

`python
from shared_horizon.membrane import MembraneEvaluator

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
q = Point(curvature=0.12, gradient=0.03, drift=0.0)

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision
`

---

7. Geodesic Example

`python
from shared_horizon.geodesics import GeodesicSolver

solver = GeodesicSolver()
segment = solver.geodesic(p, q, get_lineage("OPERATOR"))

segment.total
`

---

8. Summary

This notebook introduced:

- lineage definitions  
- stability bounds  
- curvature/drift types  
- envelope safety  
- collapse‑risk behavior  
- transition compatibility  
- firewall boundaries  
- membrane evaluation  
- geodesic computation  
- Jupyter + VS Code execution instructions  

---

