# 02 — Envelopes Notebook

Shared‑Horizon Toolkit — Stability Envelopes

Includes Jupyter + VS Code Execution Instructions

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
notebooks/02-Envelopes-Notebook.md
`

4. Add src/ to the Python path at the top of the notebook:

`python
import sys
sys.path.append("../src")
`

5. Validate imports:

`python
from sharedhorizon.envelopes import ENVELOPEREGISTRY
ENVELOPE_REGISTRY
`

If the registry prints, your environment is correct.

---

0.2 — Running in VS Code

1. Install the Python and Jupyter extensions.

2. Open the repo folder:

`
Shared-Horizon-Toolkit/
`

3. Open:

`
notebooks/02-Envelopes-Notebook.md
`

4. VS Code will show Run Cell buttons above each code block.

5. Select the correct Python interpreter:

- Ctrl+Shift+P  
- “Python: Select Interpreter”  
- Choose the environment with your toolkit dependencies.

6. Add the src/ path:

`python
import sys
sys.path.append("../src")
`

7. Validate:

`python
from sharedhorizon.envelopes import getenvelope
get_envelope("OPERATOR")
`

If it prints the envelope object, VS Code is configured correctly.

---

1. Conceptual Layer — What Stability Envelopes Are

A stability envelope defines the allowable geometric region for a lineage.

Each envelope is defined by:

- an energy functional  
- a stability bound  
- lineage‑specific curvature/drift behavior  

The envelope determines whether a point \(p\) is safe:

\[
E{\text{lineage}}(p) \leq B{\text{lineage}}
\]

Where:

- \(E_{\text{lineage}}(p)\) is the lineage’s energy functional  
- \(B_{\text{lineage}}\) is the lineage’s stability bound  

Envelopes are the first gate in the membrane evaluator.

---

2. Diagnostic Layer — Inspecting Envelope Definitions

`python
from sharedhorizon.envelopes import ENVELOPEREGISTRY

for name, env in ENVELOPE_REGISTRY.items():
    print(name)
    print("  bound =", env.bound)
    print("  lineage =", env.lineage.name)
    print("  energyfn =", env.energyfn.name)
    print()
`

This prints all envelope definitions:

- OPERATOR  
- PRECL  
- ANIMA  
- RNE  
- SPECTRAL  

---

3. Mathematical Layer — Energy Functionals

Each lineage defines its own energy functional:

Operator (NDH)

\[
E_{\text{op}}(p) = |p.\text{curvature}|
\]

PRECL (Expressive Continuity)

\[
E_{\text{precl}}(p) = |p.\text{curvature}|
\]

ANIMA (Expressive Phenomenology)

\[
E_{\text{anima}}(p) = |p.\text{curvature}| + |p.\text{gradient}|
\]

RNE (Narrative Ecology)

\[
E_{\text{rne}}(p) = |p.\text{curvature}|
\]

Spectral Runtime

\[
E_{\text{spectral}}(p) = |p.\text{drift}|
\]

These are implemented in:

`
src/shared_horizon/envelopes.py
`

---

4. Practical Layer — Using Envelopes in Code

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

Retrieve an envelope

`python
from sharedhorizon.envelopes import getenvelope

env = get_envelope("ANIMA")
env.bound
`

Compute energy manually

`python
energy = env.energy_fn(p)
energy
`

---

5. Envelope Behavior Across Lineages

Operator Envelope (🔵)
Low curvature, strict bound.

PRECL Envelope (🟧)
Low curvature, slightly flexible.

ANIMA Envelope (🟪)
High curvature + gradient allowed.

RNE Envelope (🟩)
Moderate curvature, reversible.

Spectral Envelope (⬛)
Drift‑dominated.

---

6. Envelope Failure Example

`python
bad_point = Point(curvature=0.9, gradient=0.4, drift=0.0)

envelopesafe(badpoint, "OPERATOR")
`

Expected:

`
False
`

Because operator geometry cannot support high curvature.

---

7. Envelope + Membrane Example

`python
from shared_horizon.membrane import MembraneEvaluator

p = Point(curvature=0.05, gradient=0.01, drift=0.0)
q = Point(curvature=0.12, gradient=0.03, drift=0.0)

evaluator = MembraneEvaluator()
decision = evaluator.evaluate(p, q, "OPERATOR", "PRECL")

decision
`

This demonstrates how envelope safety integrates into the full membrane evaluator.

---

8. Summary

This notebook introduced:

- stability envelopes  
- energy functionals  
- lineage‑specific envelope behavior  
- envelope safety checks  
- envelope failure modes  
- envelope integration into membrane evaluation  
- Jupyter + VS Code execution instructions  

It forms the foundation for:

- 03 — Curvature Notebook  
- 04 — Collapse Notebook  
- 05 — Transition Notebook  
- 06 — Membrane Notebook  
- 07 — Geodesics Notebook  
- 08 — Worked Examples  

---

