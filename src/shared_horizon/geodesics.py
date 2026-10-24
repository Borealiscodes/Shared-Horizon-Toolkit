"""
geodesics.py
Shared-Horizon Toolkit — Lineage & Transition Geodesics

Implements geometric geodesics for lineage diagnostics. Geodesics provide
curvature-weighted, gradient-weighted, drift-weighted, and collapse-risk
weighted paths between geometric points.

This subsystem is used for visualization, debugging, and membrane analysis.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Callable, Dict, List

from .curvature import Point, curvature_gradient
from .collapse import collapse_spectral, collapse_anima, collapse_operator, collapse_precl, collapse_narrative
from .lineage import Lineage, OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE, SPECTRAL


# ---------------------------------------------------------------------------
# Geodesic Segment
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class GeodesicSegment:
    """
    A single segment of a geodesic path.

    Attributes
    ----------
    start : Point
        Starting geometric point.
    end : Point
        Ending geometric point.
    cost : float
        Geodesic cost for this segment.
    lineage : str
        Lineage used for weighting.
    """
    start: Point
    end: Point
    cost: float
    lineage: str


# ---------------------------------------------------------------------------
# Lineage-Specific Geodesic Functions
# ---------------------------------------------------------------------------

def geodesic_operator(p: Point, q: Point) -> float:
    """
    Operator geodesic: curvature-weighted, minimal drift.
    Cost = |Δcurvature| + 0.5 * |Δgradient|
    """
    return abs(q.curvature - p.curvature) + 0.5 * abs(q.gradient - p.gradient)


def geodesic_precl(p: Point, q: Point) -> float:
    """
    PRECL geodesic: expressive continuity.
    Cost = 1.2 * |Δcurvature| + 0.5 * |Δgradient|
    """
    return 1.2 * abs(q.curvature - p.curvature) + 0.5 * abs(q.gradient - p.gradient)


def geodesic_anima(p: Point, q: Point) -> float:
    """
    ANIMA geodesic: steep expressive curvature.
    Cost = 2.5 * |Δcurvature| + 1.5 * |Δgradient|
    """
    return 2.5 * abs(q.curvature - p.curvature) + 1.5 * abs(q.gradient - p.gradient)


def geodesic_narrative(p: Point, q: Point) -> float:
    """
    RNE geodesic: moderate curvature + gradient.
    Cost = 1.8 * |Δcurvature| + 1.0 * |Δgradient|
    """
    return 1.8 * abs(q.curvature - p.curvature) + 1.0 * abs(q.gradient - p.gradient)


def geodesic_spectral(p: Point, q: Point) -> float:
    """
    Spectral geodesic: drift-dominated geometry.
    Cost = 3.0 * |Δdrift| + 0.2 * |Δcurvature|
    """
    return 3.0 * abs(q.drift - p.drift) + 0.2 * abs(q.curvature - p.curvature)


# ---------------------------------------------------------------------------
# Geodesic Registry
# ---------------------------------------------------------------------------

GEODESIC_REGISTRY: Dict[str, Callable[[Point, Point], float]] = {
    "OPERATOR": geodesic_operator,
    "PRECL": geodesic_precl,
    "ANIMA": geodesic_anima,
    "RNE": geodesic_narrative,
    "SPECTRAL": geodesic_spectral,
}


def get_geodesic_fn(lineage: Lineage) -> Callable[[Point, Point], float]:
    """
    Retrieve the geodesic function for a lineage.
    """
    name = lineage.name.upper()
    if name not in GEODESIC_REGISTRY:
        raise KeyError(f"No geodesic function registered for lineage: {lineage.name}")
    return GEODESIC_REGISTRY[name]


# ---------------------------------------------------------------------------
# Geodesic Solver
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class GeodesicPath:
    """
    Full geodesic path between two points.

    Attributes
    ----------
    segments : List[GeodesicSegment]
        List of geodesic segments.
    total_cost : float
        Sum of segment costs.
    lineage : str
        Lineage used for weighting.
    """
    segments: List[GeodesicSegment]
    total_cost: float
    lineage: str


class GeodesicSolver:
    """
    Compute geodesics between geometric points.

    Usage
    -----
    solver = GeodesicSolver()
    path = solver.compute(p, q, "PRECL")
    """

    def compute(self, p: Point, q: Point, lineage: Lineage | str) -> GeodesicPath:
        """
        Compute geodesic path between two points.

        Parameters
        ----------
        p : Point
            Starting point.
        q : Point
            Ending point.
        lineage : Lineage or str
            Lineage used for weighting.

        Returns
        -------
        GeodesicPath
            Structured geodesic path.
        """
        if isinstance(lineage, str):
            from .lineage import get_lineage
            lineage = get_lineage(lineage)

        fn = get_geodesic_fn(lineage)
        cost = fn(p, q)

        segment = GeodesicSegment(
            start=p,
            end=q,
            cost=cost,
            lineage=lineage.name,
        )

        return GeodesicPath(
            segments=[segment],
            total_cost=cost,
            lineage=lineage.name,
        )
