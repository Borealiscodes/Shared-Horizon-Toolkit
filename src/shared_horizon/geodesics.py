"""
geodesics.py
Shared-Horizon Toolkit — Lineage & Transition Geodesics

Defines geodesic computation across lineage regions. Geodesics are
curvature-weighted or drift-weighted shortest paths between points
in the Shared-Horizon membrane architecture.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from math import sqrt
from .lineage import (
    Lineage,
    OPERATOR,
    EXPRESSIVE_PRECL,
    EXPRESSIVE_ANIMA,
    NARRATIVE_RNE,
    SPECTRAL
)
from .curvature import Point, curvature_gradient, get_curvature_fn
from .collapse import get_collapse_fn


# ---------------------------------------------------------------------------
# Geodesic Segment
# ---------------------------------------------------------------------------

@dataclass
class GeodesicSegment:
    """
    Represents a geodesic segment between two points.

    Attributes:
        length: geodesic length
        curvature_cost: curvature contribution
        drift_cost: drift contribution
        collapse_cost: collapse-risk contribution
    """
    length: float
    curvature_cost: float
    drift_cost: float
    collapse_cost: float

    @property
    def total(self) -> float:
        return self.length + self.curvature_cost + self.drift_cost + self.collapse_cost


# ---------------------------------------------------------------------------
# Lineage-Specific Geodesic Behavior
# ---------------------------------------------------------------------------

def geodesic_operator(p: Point, q: Point) -> GeodesicSegment:
    """
    NDH operator geodesic.
    Smooth, low curvature, low collapse-risk.
    """
    base = sqrt((q.curvature - p.curvature)**2)
    return GeodesicSegment(
        length=base,
        curvature_cost=base * 0.5,
        drift_cost=0.0,
        collapse_cost=abs(q.curvature - p.curvature) * 0.2
    )


def geodesic_precl(p: Point, q: Point) -> GeodesicSegment:
    """
    PRECL expressive continuity geodesic.
    Low curvature, smooth gradients.
    """
    base = sqrt((q.curvature - p.curvature)**2)
    return GeodesicSegment(
        length=base,
        curvature_cost=base * 0.7,
        drift_cost=0.0,
        collapse_cost=abs(q.gradient - p.gradient) * 0.3
    )


def geodesic_anima(p: Point, q: Point) -> GeodesicSegment:
    """
    ANIMA expressive phenomenology geodesic.
    High curvature and steep gradients dominate.
    """
    base = sqrt((q.curvature - p.curvature)**2 + (q.gradient - p.gradient)**2)
    return GeodesicSegment(
        length=base,
        curvature_cost=base * 1.5,
        drift_cost=0.0,
        collapse_cost=abs(q.gradient - p.gradient) * 1.0
    )


def geodesic_narrative(p: Point, q: Point) -> GeodesicSegment:
    """
    RNE narrative geodesic.
    Moderate curvature, moderate gradient.
    """
    base = sqrt((q.curvature - p.curvature)**2 + (q.gradient - p.gradient)**2)
    return GeodesicSegment(
        length=base,
        curvature_cost=base * 1.0,
        drift_cost=0.0,
        collapse_cost=abs(q.gradient - p.gradient) * 0.6
    )


def geodesic_spectral(p: Point, q: Point) -> GeodesicSegment:
    """
    Spectral geodesic.
    Drift dominates geodesic behavior.
    """
    base = abs(q.drift - p.drift)
    return GeodesicSegment(
        length=base,
        curvature_cost=0.0,
        drift_cost=base * 2.0,
        collapse_cost=abs(q.drift - p.drift) * 1.5
    )


# ---------------------------------------------------------------------------
# Geodesic Dispatch
# ---------------------------------------------------------------------------

def get_geodesic_fn(lineage: Lineage):
    """
    Retrieve geodesic function for a lineage.
    """
    if lineage is OPERATOR:
        return geodesic_operator
    if lineage is EXPRESSIVE_PRECL:
        return geodesic_precl
    if lineage is EXPRESSIVE_ANIMA:
        return geodesic_anima
    if lineage is NARRATIVE_RNE:
        return geodesic_narrative
    if lineage is SPECTRAL:
        return geodesic_spectral

    raise ValueError(f"Unknown lineage: {lineage.name}")


# ---------------------------------------------------------------------------
# Geodesic Solver
# ---------------------------------------------------------------------------

class GeodesicSolver:
    """
    Computes lineage-specific geodesics and transition geodesics.
    """

    def __init__(self):
        pass

    def geodesic(self, p: Point, q: Point, lineage: Lineage) -> GeodesicSegment:
        """
        Compute geodesic segment for a single lineage.
        """
        fn = get_geodesic_fn(lineage)
        return fn(p, q)

    def transition_geodesic(self, p: Point, q: Point, source: Lineage, target: Lineage) -> GeodesicSegment:
        """
        Compute geodesic across a lineage transition.

        Rule:
            - Compute geodesic in source lineage
            - Compute geodesic in target lineage
            - Combine costs
        """
        gs_src = self.geodesic(p, q, source)
        gs_tgt = self.geodesic(p, q, target)

        return GeodesicSegment(
            length=(gs_src.length + gs_tgt.length) / 2,
            curvature_cost=(gs_src.curvature_cost + gs_tgt.curvature_cost),
            drift_cost=(gs_src.drift_cost + gs_tgt.drift_cost),
            collapse_cost=(gs_src.collapse_cost + gs_tgt.collapse_cost)
        )
