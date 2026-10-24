"""
jacobian.py
Shared-Horizon Toolkit — Jacobian Smoothness Constraints

Defines Jacobian magnitude evaluation and lineage-specific smoothness
bounds. Used by membrane.py to ensure transitions do not violate
smoothness constraints required by the Shared-Horizon architecture.

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
from .curvature import Point


# ---------------------------------------------------------------------------
# Jacobian Representation
# ---------------------------------------------------------------------------

@dataclass
class Jacobian:
    """
    Jacobian magnitude representation.

    Attributes:
        magnitude: absolute Jacobian determinant or proxy measure
    """
    magnitude: float

    @property
    def abs(self) -> float:
        return abs(self.magnitude)


# ---------------------------------------------------------------------------
# Jacobian Evaluation
# ---------------------------------------------------------------------------

def jacobian_operator(p: Point, q: Point) -> Jacobian:
    """
    NDH operator Jacobian.
    Very smooth, low curvature → low Jacobian magnitude.
    """
    return Jacobian(
        magnitude=abs(q.curvature - p.curvature) * 0.5
    )


def jacobian_precl(p: Point, q: Point) -> Jacobian:
    """
    PRECL expressive continuity Jacobian.
    Smooth but slightly more flexible than operator geometry.
    """
    return Jacobian(
        magnitude=abs(q.curvature - p.curvature) * 0.7
    )


def jacobian_anima(p: Point, q: Point) -> Jacobian:
    """
    ANIMA expressive phenomenology Jacobian.
    High curvature and steep gradients → large Jacobian magnitudes.
    """
    return Jacobian(
        magnitude=abs(q.curvature - p.curvature) * 1.5 +
                  abs(q.gradient - p.gradient) * 1.2
    )


def jacobian_narrative(p: Point, q: Point) -> Jacobian:
    """
    RNE narrative Jacobian.
    Moderate curvature, moderate gradient.
    """
    return Jacobian(
        magnitude=abs(q.curvature - p.curvature) * 1.0 +
                  abs(q.gradient - p.gradient) * 0.6
    )


def jacobian_spectral(p: Point, q: Point) -> Jacobian:
    """
    Spectral Jacobian.
    Drift dominates smoothness behavior.
    """
    return Jacobian(
        magnitude=abs(q.drift - p.drift) * 2.0
    )


# ---------------------------------------------------------------------------
# Jacobian Dispatch
# ---------------------------------------------------------------------------

def get_jacobian_fn(lineage: Lineage):
    """
    Retrieve Jacobian evaluation function for a lineage.
    """
    if lineage is OPERATOR:
        return jacobian_operator
    if lineage is EXPRESSIVE_PRECL:
        return jacobian_precl
    if lineage is EXPRESSIVE_ANIMA:
        return jacobian_anima
    if lineage is NARRATIVE_RNE:
        return jacobian_narrative
    if lineage is SPECTRAL:
        return jacobian_spectral

    raise ValueError(f"Unknown lineage: {lineage.name}")


# ---------------------------------------------------------------------------
# Jacobian Safety Check
# ---------------------------------------------------------------------------

def jacobian_safe(p: Point, q: Point, lineage: Lineage) -> bool:
    """
    Check whether the Jacobian magnitude is within the lineage's smoothness bound.

    Rules:
        - Operator: extremely strict
        - PRECL: strict but flexible
        - ANIMA: large Jacobians allowed
        - Narrative: moderate Jacobians allowed
        - Spectral: drift-based Jacobians allowed but monitored
    """
    fn = get_jacobian_fn(lineage)
    J = fn(p, q)

    # Bound is lineage.stability_bound scaled for Jacobian behavior
    bound = lineage.stability_bound * 2.0

    return J.abs <= bound
