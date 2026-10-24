"""
lineage.py
Shared-Horizon Toolkit — Lineage Definitions

Defines lineage classes, stability bounds, curvature/drift types,
and lineage metadata used across the membrane toolkit.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Lineage:
    name: str
    stability_bound: float
    curvature_type: str      # "curvature" or "drift"
    reversible_required: bool
    description: str

# --- Lineage Definitions -----------------------------------------------------

OPERATOR = Lineage(
    name="OPERATOR",
    stability_bound=0.15,
    curvature_type="curvature",
    reversible_required=False,
    description="NDH operator geometry: reversible operators, holonomy preservation."
)

EXPRESSIVE_PRECL = Lineage(
    name="PRECL",
    stability_bound=0.10,
    curvature_type="curvature",
    reversible_required=False,
    description="Low-curvature expressive continuity region."
)

EXPRESSIVE_ANIMA = Lineage(
    name="ANIMA",
    stability_bound=0.50,
    curvature_type="curvature",
    reversible_required=True,
    description="High-curvature expressive phenomenology region (ANIMA Classic lineage)."
)

NARRATIVE_RNE = Lineage(
    name="RNE",
    stability_bound=0.20,
    curvature_type="curvature",
    reversible_required=True,
    description="Reversible narrative ecology: curvature-preserving narrative operators."
)

SPECTRAL = Lineage(
    name="SPECTRAL",
    stability_bound=0.40,
    curvature_type="drift",
    reversible_required=False,
    description="Spectral-runtime geometry: drift-based instability regions."
)

# --- Lineage Registry --------------------------------------------------------

LINEAGE_REGISTRY = {
    "OPERATOR": OPERATOR,
    "PRECL": EXPRESSIVE_PRECL,
    "ANIMA": EXPRESSIVE_ANIMA,
    "RNE": NARRATIVE_RNE,
    "SPECTRAL": SPECTRAL,
}

def get_lineage(name: str) -> Lineage:
    """
    Retrieve lineage definition by name.
    """
    return LINEAGE_REGISTRY[name.upper()]
