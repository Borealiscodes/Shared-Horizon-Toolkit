"""
lineage.py
Shared-Horizon Toolkit — Lineage Definitions

Defines the five canonical lineages used throughout the geometric membrane
architecture. Each lineage specifies stability bounds, curvature/drift profiles,
and descriptive metadata. All membrane subsystems depend on these definitions.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Lineage:
    """
    Immutable lineage definition.

    Attributes
    ----------
    name : str
        Lineage identifier (e.g., "OPERATOR").
    stability_bound : float
        Maximum allowed envelope energy before instability.
    curvature_weight : float
        Weight applied to curvature differences in geodesics and diagnostics.
    drift_weight : float
        Weight applied to spectral drift (SPECTRAL lineage only).
    reversible_required : bool
        Whether transitions into/out of this lineage require reversibility.
    description : str
        Human-readable description of the lineage's geometric behavior.
    """

    name: str
    stability_bound: float
    curvature_weight: float
    drift_weight: float
    reversible_required: bool
    description: str


# ---------------------------------------------------------------------------
# Lineage Definitions
# ---------------------------------------------------------------------------

OPERATOR = Lineage(
    name="OPERATOR",
    stability_bound=0.15,
    curvature_weight=1.0,
    drift_weight=0.0,
    reversible_required=False,
    description=(
        "Low-curvature operator geometry. Stable, reversible operators with "
        "minimal drift. Forms the baseline region for membrane evaluation."
    ),
)

PRECL = Lineage(
    name="PRECL",
    stability_bound=0.10,
    curvature_weight=1.2,
    drift_weight=0.0,
    reversible_required=False,
    description=(
        "Low-curvature expressive continuity region. Smooth transitions from "
        "operator geometry with slightly higher curvature sensitivity."
    ),
)

EXPRESSIVE_ANIMA = Lineage(
    name="ANIMA",
    stability_bound=0.50,
    curvature_weight=2.5,
    drift_weight=0.0,
    reversible_required=True,
    description=(
        "High-curvature expressive phenomenology region. Strong curvature and "
        "gradient amplification. Requires reversible transitions."
    ),
)

RNE = Lineage(
    name="RNE",
    stability_bound=0.20,
    curvature_weight=1.8,
    drift_weight=0.0,
    reversible_required=True,
    description=(
        "Reversible narrative ecology. Moderate curvature and gradient behavior "
        "with reversible operator requirements."
    ),
)

SPECTRAL = Lineage(
    name="SPECTRAL",
    stability_bound=0.40,
    curvature_weight=0.0,
    drift_weight=3.0,
    reversible_required=False,
    description=(
        "Spectral-runtime geometry dominated by drift. Unstable for curvature-"
        "based transitions. Hard firewall blocks apply."
    ),
)


# ---------------------------------------------------------------------------
# Lineage Registry
# ---------------------------------------------------------------------------

LINEAGE_REGISTRY: Dict[str, Lineage] = {
    "OPERATOR": OPERATOR,
    "PRECL": PRECL,
    "ANIMA": EXPRESSIVE_ANIMA,
    "RNE": RNE,
    "SPECTRAL": SPECTRAL,
}


def get_lineage(name: str) -> Lineage:
    """
    Retrieve a lineage definition by name.

    Parameters
    ----------
    name : str
        Lineage name (case-insensitive).

    Returns
    -------
    Lineage
        The corresponding lineage object.

    Raises
    ------
    KeyError
        If the lineage name is not recognized.
    """
    key = name.upper()
    if key not in LINEAGE_REGISTRY:
        raise KeyError(f"Unknown lineage: {name}")
    return LINEAGE_REGISTRY[key]
