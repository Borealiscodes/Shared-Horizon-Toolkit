# 08 — Worked Examples Notebook

Shared‑Horizon Toolkit — Complete Worked Examples

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
notebooks/08-Worked-Examples-Notebook.md
`

4. Add src/ to the Python path:

`python
import sys
sys.path.append("../src")
`

5. Validate:

`python
from sharedhorizon.examples import allexamples
all_examples()
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
notebooks/08-Worked-Examples-Notebook.md
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
from sharedhorizon.examples import exampleenvelope
example_envelope()
`

---

1. Conceptual Layer — Purpose of Worked Examples

This notebook provides end‑to‑end demonstrations of the Shared‑Horizon Toolkit:

- envelope safety  
- curvature evaluation  
- collapse‑risk evaluation  
- transition compatibility  
- firewall enforcement  
- membrane evaluation  
- lineage geodesics  
- transition geodesics  

Each example uses the canonical points:

`python
p = Point(curvature=0.05, gradient=0.01, drift=0.0)
q = Point(curvature=0.12, gradient=0.03, drift=0.0)
`

These represent:

- p — operator‑safe  
- q — expressive‑safe (PRECL)  

---

2. Diagnostic Layer — Import Examples

`python
from shared_horizon.examples import (
    example_points,
    example_envelope,
    example_curvature,
    example_collapse,
    example_transition,
    example_firewall,
    example_geodesic,
    all_examples
)

p, q = example_points()
p, q
`

---

3. Envelope Example

`python
example_envelope()
`

Expected:

`
{
  "example": "Envelope Safety",
  "lineage": "OPERATOR",
  "point": Point(...),
  "safe": True
}
`

This verifies that p lies within the OPERATOR stability envelope.

---

4. Curvature Example

`python
example_curvature()
`

Expected:

`
{
  "example": "Curvature Evaluation",
  "lineage": "OPERATOR",
  "point": Point(...),
  "curvature": 0.05
}
`

---

5. Collapse‑Risk Example

`python
example_collapse()
`

Expected:

`
{
  "example": "Collapse-Risk Evaluation",
  "lineage": "OPERATOR",
  "point": Point(...),
  "collapse_risk": <small value>
}
`

---

6. Transition Example

`python
example_transition()
`

Expected:

`
{
  "example": "Transition Safety",
  "source": "OPERATOR",
  "target": "PRECL",
  "safe": True
}
`

This demonstrates that OPERATOR → PRECL is a valid expressive continuity transition.

---

7. Firewall Example

`python
example_firewall()
`

Expected:

`
{
  "example": "Firewall + Membrane Evaluation",
  "source": "OPERATOR",
  "target": "PRECL",
  "allowed": True,
  "reason": "Transition allowed by membrane."
}
`

This shows the full firewall + membrane pipeline.

---

8. Geodesic Example

`python
example_geodesic()
`

Expected:

`
{
  "example": "Geodesic Computation",
  "lineage": "OPERATOR",
  "segment_total": <value>,
  "segment": GeodesicSegment(...)
}
`

This computes the curvature‑weighted geodesic between p and q inside the OPERATOR lineage.

---

9. Full Example Suite

`python
all_examples()
`

This runs:

- envelope  
- curvature  
- collapse  
- transition  
- firewall  
- geodesic  

and returns a single dictionary containing all results.

---

10. Visualizing Example Results (Optional)

If running in Jupyter:

`python
import matplotlib.pyplot as plt

results = all_examples()

labels = ["envelope", "curvature", "collapse", "transition", "firewall", "geodesic"]
values = [
    int(results["envelope"]["safe"]),
    results["curvature"]["curvature"],
    results["collapse"]["collapse_risk"],
    int(results["transition"]["safe"]),
    int(results["firewall"]["allowed"]),
    results["geodesic"]["segment_total"]
]

plt.bar(labels, values)
plt.title("Worked Example Outputs")
plt.xticks(rotation=45)
plt.show()
`

---

11. Summary

This notebook provides:

- complete worked examples  
- envelope safety  
- curvature evaluation  
- collapse‑risk evaluation  
- transition compatibility  
- firewall enforcement  
- membrane evaluation  
- lineage geodesics  
- transition geodesics  
- optional visualization  
- Jupyter + VS Code execution instructions  

This completes the Shared‑Horizon Toolkit Notebook Series:

1. Lineage  
2. Envelopes  
3. Curvature  
4. Collapse  
5. Transition  
6. Membrane  
7. Geodesics  
8. Worked Examples  

---

