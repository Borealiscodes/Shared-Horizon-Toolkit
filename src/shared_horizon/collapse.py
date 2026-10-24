"""
collapse.py
Shared-Horizon Toolkit — Collapse-Risk Geometry

Defines collapse-risk tensors, gradients, and lineage-specific
collapse behavior. Used by membrane.py and transition.py to
evaluate whether a point or transition is collapse-safe.

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
from .curvature import Point, curvature_gradient, drift_spectral


# ---------------------------------------------------------------------------
# Collapse-Risk Tensor
# ---------------------------------------------------------------------------

@dataclass
class CollapseRisk:
    """
    Collapse-risk tensor representation.

    Attributes:
        curvature_term: contribution from curvature magnitude
        gradient_term: contribution from curvature gradient
        drift_term: contribution from spectral drift
    """
    curvature_term: float
    gradient_term: float
    drift_term: float

    @property
    def total(self) -> float:
        """
        Total collapse-risk magnitude.
        """
        return self.curvature_term + self.gradient_term + self.drift_term


# ---------------------------------------------------------------------------
# Lineage-Specific Collapse Behavior
# ---------------------------------------------------------------------------

def collapse_operator(p: Point) -> CollapseRisk:
    """
    NDH operator collapse-risk.
    Very low curvature and gradient contributions.
    """
    return CollapseRisk(
        curvature_term=abs(p.curvature) * 0.5,
        gradient_term=abs(p.gradient) * 0.2,
        drift_term=0.0
    )


def collapse_precl(p: Point) -> CollapseRisk:
    """
    PRECL expressive continuity collapse-risk.
    Low curvature, low gradient.
    """
    return CollapseRisk(
        curvature_term=abs(p.curvature) * 0.6,
        gradient_term=abs(p.gradient) * 0.3,
        drift_term=0.0
    )


def collapse_anima(p: Point) -> CollapseRisk:
    """
    ANIMA expressive phenomenology collapse-risk.
    High curvature and steep gradients dominate.
    """
    return CollapseRisk(
        curvature_term=abs(p.curvature) * 1.2,
        gradient_term=abs(p.gradient) * 1.0,
        drift_term=0.0
    )


def collapse_narrative(p: Point) -> CollapseRisk:
    """
    RNE narrative collapse-risk.
    Moderate curvature, moderate gradient.
    """
    return CollapseRisk(
        curvature_term=abs(p.curvature) * 0.8,
        gradient_term=abs(p.gradient) * 0.5,
        drift_term=0.0
    )


def collapse_spectral(p: Point) -> CollapseRisk:
    """
    Spectral collapse-risk.
    Drift dominates collapse behavior.
    """
    drift = drift_spectral(p)
    return CollapseRisk(
        curvature_term=0.0,
        gradient_term=0.0,
        drift_term=abs(drift) * 1.5
    )


# ---------------------------------------------------------------------------
# Collapse-Risk Dispatch
# ---------------------------------------------------------------------------

def get_collapse_fn(lineage: Lineage):
    """
    Retrieve collapse-risk function for a lineage.
    """
    if lineage is OPERATOR:
        return collapse_operator
    if lineage is EXPRESSIVE_PRECL:
        return collapse_precl
    if lineage is EXPRESSIVE_ANIMA:
        return collapse_anima
    if lineage is NARRATIVE_RNE:
        return collapse_narrative
    if lineage is SPECTRAL:
        return collapse_spectral

    raise ValueError(f"Unknown lineage: {lineage.name}")


# ---------------------------------------------------------------------------
# Collapse Compatibility
# ---------------------------------------------------------------------------

def collapse_compatible(p: Point, q: Point) -> bool:
    """
    Check collapse-risk compatibility between source point p and target q.

    Rules:
        - Operator → PRECL: safe if collapse-risk does not increase sharply
        - ANIMA → Narrative: safe if gradient decreases
        - Spectral → anything: unsafe if drift increases
        - Default: safe if total collapse-risk does not increase by > 20%
    """
    # Compute collapse-risk tensors
    cp = collapse_operator(p) if p.drift == 0 else collapse_spectral(p)
    cq = collapse_operator(q) if q.drift == 0 else collapse_spectral(q)

    # Operator → PRECL
    if p.curvature <= OPERATOR.stability_bound and q.curvature <= EXPRESSIVE_PRECL.stability_bound:
        return cq.total <= cp.total + 0.05

    # ANIMA → Narrative
    if p.curvature > EXPRESSIVE_PRECL.stability_bound and q.curvature <= NARRATIVE_RNE.stability_bound:
        return q.gradient <= p.gradient

    # Spectral → anything
    if p.drift > 0:
        return q.drift <= p.drift

    # Default rule
    return cq.total <= cp.total * 1.2
