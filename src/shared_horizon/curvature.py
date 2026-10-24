"""
curvature.py
Shared-Horizon Toolkit — Curvature & Drift Geometry

Defines curvature, drift, and curvature-gradient functions used across
the membrane evaluator. Provides lineage-specific curvature behavior
for operator, expressive, narrative, and spectral systems.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from .lineage import (
    Lineage,
    OPERATOR,
    EXPRESSIVE_PRECL,
    EXPRESSIVE_ANIMA,
    NARRATIVE_RNE,
    SPECTRAL
)


# ---------------------------------------------------------------------------
# Point Geometry
# ---------------------------------------------------------------------------

@dataclass
class Point:
    """
    Minimal geometric point representation used by curvature, drift,
    envelope, collapse-risk, and transition modules.

    Attributes:
        curvature: scalar curvature at the point
        gradient: curvature gradient magnitude
        drift: spectral drift magnitude
    """
    curvature: float
    gradient: float
    drift: float


# ---------------------------------------------------------------------------
# Curvature Functions
# ---------------------------------------------------------------------------

def curvature_operator(p: Point) -> float:
    """
    NDH operator curvature.
    Typically small, smooth, and reversible.
    """
    return p.curvature


def curvature_precl(p: Point) -> float:
    """
    PRECL expressive continuity curvature.
    Low curvature, smooth gradients.
    """
    return p.curvature


def curvature_anima(p: Point) -> float:
    """
    ANIMA expressive phenomenology curvature.
    High curvature with steep gradients.
    """
    return p.curvature


def curvature_narrative(p: Point) -> float:
    """
    RNE narrative curvature.
    Moderate curvature with reversibility constraints.
    """
    return p.curvature


# ---------------------------------------------------------------------------
# Drift Functions (Spectral)
# ---------------------------------------------------------------------------

def drift_spectral(p: Point) -> float:
    """
    Spectral drift replaces curvature as the dominant instability measure.
    """
    return p.drift


# ---------------------------------------------------------------------------
# Curvature Gradient Functions
# ---------------------------------------------------------------------------

def curvature_gradient(p: Point) -> float:
    """
    Curvature gradient magnitude.
    Used for collapse-risk and expressive curvature behavior.
    """
    return p.gradient


# ---------------------------------------------------------------------------
# Compatibility Checks
# ---------------------------------------------------------------------------

def curvature_compatible(p: Point, q: Point) -> bool:
    """
    Check curvature compatibility between source point p and target q.

    Operator → PRECL: low curvature required
    ANIMA → Narrative: curvature must match (reversible expressive → narrative)
    Spectral → anything: generally incompatible (handled by firewall)
    """
    # Operator → PRECL
    if p.curvature <= OPERATOR.stability_bound and q.curvature <= EXPRESSIVE_PRECL.stability_bound:
        return True

    # ANIMA → Narrative (reversible expressive → narrative)
    if abs(p.curvature - q.curvature) <= NARRATIVE_RNE.stability_bound:
        return True

    # Spectral → anything: curvature compatibility is not meaningful
    if p.drift > 0:
        return False

    # Default: allow if curvature does not increase dramatically
    return abs(q.curvature) <= abs(p.curvature) + 0.05


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_curvature_fn(lineage: Lineage):
    """
    Retrieve curvature or drift function for a lineage.
    """
    if lineage is OPERATOR:
        return curvature_operator
    if lineage is EXPRESSIVE_PRECL:
        return curvature_precl
    if lineage is EXPRESSIVE_ANIMA:
        return curvature_anima
    if lineage is NARRATIVE_RNE:
        return curvature_narrative
    if lineage is SPECTRAL:
        return drift_spectral

    raise ValueError(f"Unknown lineage: {lineage.name}")
