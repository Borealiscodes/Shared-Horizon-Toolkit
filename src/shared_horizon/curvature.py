"""
curvature.py
Shared-Horizon Toolkit — Curvature, Gradient & Drift

Defines the geometric Point object and lineage-specific curvature, gradient,
and drift functions. Implements curvature compatibility checks used in Stage 2
of the membrane evaluation pipeline.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Callable, Dict

from .lineage import Lineage, OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE, SPECTRAL


# ---------------------------------------------------------------------------
# Geometric Point Definition
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Point:
    """
    Canonical geometric point used throughout the Shared-Horizon architecture.

    Attributes
    ----------
    curvature : float
        Local curvature magnitude.
    gradient : float
        Curvature gradient magnitude.
    drift : float
        Spectral drift magnitude (SPECTRAL lineage only).
    """
    curvature: float
    gradient: float
    drift: float = 0.0


# ---------------------------------------------------------------------------
# Curvature Functions
# ---------------------------------------------------------------------------

def curvature_operator(p: Point) -> float:
    """Operator curvature: low curvature, low gradient."""
    return p.curvature


def curvature_precl(p: Point) -> float:
    """PRECL curvature: slightly higher sensitivity."""
    return 1.2 * p.curvature


def curvature_anima(p: Point) -> float:
    """ANIMA curvature: steep curvature amplification."""
    return 2.5 * p.curvature + 1.5 * p.gradient


def curvature_narrative(p: Point) -> float:
    """RNE curvature: moderate curvature + gradient."""
    return 1.8 * p.curvature + 1.0 * p.gradient


def drift_spectral(p: Point) -> float:
    """Spectral drift: drift dominates curvature."""
    return 3.0 * p.drift + 0.2 * p.curvature


# ---------------------------------------------------------------------------
# Curvature Registry
# ---------------------------------------------------------------------------

CURVATURE_REGISTRY: Dict[str, Callable[[Point], float]] = {
    "OPERATOR": curvature_operator,
    "PRECL": curvature_precl,
    "ANIMA": curvature_anima,
    "RNE": curvature_narrative,
    "SPECTRAL": drift_spectral,
}


def get_curvature_fn(lineage: Lineage) -> Callable[[Point], float]:
    """
    Retrieve the curvature function for a lineage.
    """
    name = lineage.name.upper()
    if name not in CURVATURE_REGISTRY:
        raise KeyError(f"No curvature function registered for lineage: {lineage.name}")
    return CURVATURE_REGISTRY[name]


# ---------------------------------------------------------------------------
# Curvature Gradient
# ---------------------------------------------------------------------------

def curvature_gradient(p: Point, q: Point) -> float:
    """
    Compute curvature gradient between two points.

    Defined as absolute difference in curvature plus gradient difference.
    """
    return abs(q.curvature - p.curvature) + abs(q.gradient - p.gradient)


# ---------------------------------------------------------------------------
# Curvature Compatibility
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CurvatureCompatibility:
    """Structured result for curvature compatibility evaluation."""
    compatible: bool
    delta: float
    threshold: float
    reason: str


def curvature_compatible(p: Point, q: Point, threshold: float = 0.20) -> CurvatureCompatibility:
    """
    Determine whether curvature transition p -> q is smooth enough for membrane evaluation.

    Parameters
    ----------
    p : Point
        Source point.
    q : Point
        Target point.
    threshold : float
        Maximum allowed curvature gradient for compatibility.

    Returns
    -------
    CurvatureCompatibility
        Structured result containing compatibility flag, delta, threshold, and reason.
    """
    delta = curvature_gradient(p, q)
    compatible = delta <= threshold

    reason = (
        "Curvature transition is smooth."
        if compatible else
        f"Curvature gradient {delta:.4f} exceeds threshold {threshold:.4f}."
    )

    return CurvatureCompatibility(
        compatible=compatible,
        delta=delta,
        threshold=threshold,
        reason=reason,
    )
