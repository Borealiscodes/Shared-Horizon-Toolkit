# 05 — Transition Notebook

Shared‑Horizon Toolkit — Lineage Transition Maps

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
notebooks/05-Transition-Notebook.md
`

4. Add src/ to the Python path:

`python
import sys
sys.path.append("../src")
`

5. Validate:

`python
from sharedhorizon.transition import TRANSITIONREGISTRY
TRANSITION_REGISTRY
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
notebooks/05-Transition-Notebook.md
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
from sharedhorizon.transition import gettransition
get_transition("OPERATOR", "PRECL")
`

---

1. Conceptual Layer — What Transitions Are

A transition is a lineage‑to‑lineage mapping:

\[
\text{source} \rightarrow \text{target}
\]

Transitions define how geometric states move across the Shared‑Horizon mosaic.

Each transition has:

- a source lineage  
- a target lineage  
- a reversibility flag  
- a description  
- compatibility constraints  
- firewall constraints  

Transitions are the logical rules; the firewall is the hard boundary.

---

2. Diagnostic Layer — Inspecting Transition Maps

`python
from sharedhorizon.transition import TRANSITIONREGISTRY

for (src, tgt), t in TRANSITION_REGISTRY.items():
    print(f"{src} → {tgt}")
    print("  reversible =", t.reversible)
    print("  description =", t.description)
    print()
`

Expected transitions:

- OPERATOR → PRECL  
- PRECL → ANIMA  
- ANIMA → RNE  
- RNE → OPERATOR  
- SPECTRAL → any (blocked)  

---

3. Mathematical Layer — Transition Constraints

A transition is allowed only if:

\[
\text{curvature\_compatible}(p, q) = \text{True}
\]

\[
\text{collapse\_compatible}(p, q) = \text{True}
\]

\[
\text{Jacobian}(p, q) \leq B_{\text{lineage}}
\]

\[
\text{firewall}(p, q) = \text{allowed}
\]

Additionally:

- Spectral → anything is always forbidden  
- PRECL → OPERATOR forbidden  
- ANIMA → OPERATOR forbidden  
- Reversibility required for some transitions  

---

4. Practical Layer — Using Transitions in Code

Create points

`python
from shared_horizon.curvature import Point

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
q = Point(curvature=0.12, gradient=0.03, drift=0.0)
`

Retrieve a transition

`python
from sharedhorizon.transition import gettransition

t = get_transition("OPERATOR", "PRECL")
t
`

Check transition compatibility

`python
from sharedhorizon.transition import transitionallowed

transition_allowed(p, q, "OPERATOR", "PRECL")
`

---

5. Transition Behavior Across Lineages

Allowed (pre‑firewall)

| Source | Target | Notes |
|--------|--------|-------|
| OPERATOR | PRECL | continuity |
| PRECL | ANIMA | expressive amplification |
| ANIMA | RNE | reversible expressive → narrative |
| RNE | OPERATOR | curvature reduction |

Forbidden (firewall)

| Source | Target | Reason |
|--------|--------|--------|
| SPECTRAL | any | drift → curvature forbidden |
| ANIMA | OPERATOR | expressive → operator jump |
| PRECL | OPERATOR | expressive → operator jump |

---

6. Transition + Firewall Example

`python
from shared_horizon.firewall import firewall
from sharedhorizon.lineage import getlineage

source = get_lineage("OPERATOR")
target = get_lineage("PRECL")

firewall(source, target, p, q)
`

Expected:

`
FirewallDecision(allowed=True, reason="Transition allowed by firewall.")
`

---

7. Transition in the Membrane Evaluator

`python
from shared_horizon.membrane import MembraneEvaluator

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision
`

This integrates:

- envelope safety  
- curvature compatibility  
- collapse‑risk compatibility  
- Jacobian smoothness  
- firewall enforcement  

---

8. Transition Geodesics

`python
from shared_horizon.geodesics import GeodesicSolver
from sharedhorizon.lineage import getlineage

solver = GeodesicSolver()
segment = solver.transitiongeodesic(p, q, getlineage("OPERATOR"), get_lineage("PRECL"))

segment.total
`

Transition geodesics combine:

- source geodesic  
- target geodesic  
- collapse‑risk contributions  
- curvature contributions  

---

9. Summary

This notebook introduced:

- transition maps  
- reversibility constraints  
- curvature + collapse compatibility  
- spectral hard blocks  
- expressive → operator forbidden transitions  
- transition registry  
- membrane integration  
- transition geodesics  
- Jupyter + VS Code execution instructions  

It forms the foundation for:

- 06 — Membrane Notebook  
- 07 — Geodesics Notebook  
- 08 — Worked Examples  

---

