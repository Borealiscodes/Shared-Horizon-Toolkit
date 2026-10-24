"""
jacobian.py
Shared-Horizon Toolkit — Jacobian Smoothness Checks

Implements lineage-specific Jacobian smoothness evaluation. The Jacobian
constraint is Stage 4.5 of the membrane pipeline, positioned between collapse-
risk evaluation and firewall enforcement.

The Jacobian captures local differential stability: how rapidly curvature and
gradient change between two geometric points.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Dict

from .curvature import Point, curvature_gradient
from .lineage import Lineage, OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE, SPECTRAL


# ---------------------------------------------------------------------------
# Jacobian Smoothness Thresholds
# ---------------------------------------------------------------------------
# These thresholds define how much local differential change is allowed
# before the membrane flags instability.

JACOBIAN_THRESHOLDS: Dict[str, float] = {
    "OPERATOR": 0.15,   # very smooth required
    "PRECL": 0.20,      # smooth expressive continuity
    "ANIMA": 0.35,      # expressive curvature amplification
    "RNE": 0.30,        # narrative curvature
    "SPECTRAL": 0.50,   # drift-dominated, less curvature sensitivity
}


# ---------------------------------------------------------------------------
# Jacobian Structured Result
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class JacobianResult:
    """
    Structured Jacobian evaluation.

    Attributes
    ----------
    smooth : bool
        Whether the Jacobian is within lineage-specific bounds.
    delta : float
        Local differential change between points.
    threshold : float
        Maximum allowed Jacobian magnitude.
    lineage : str
        Lineage name.
    reason : str
        Diagnostic explanation.
    """
    smooth: bool
    delta: float
    threshold: float
    lineage: str
    reason: str


# ---------------------------------------------------------------------------
# Jacobian Estimator
# ---------------------------------------------------------------------------

def estimate_jacobian(p: Point, q: Point) -> float:
    """
    Estimate the Jacobian magnitude between two points.

    For the Shared-Horizon architecture, the Jacobian is approximated by
    curvature-gradient difference, which captures local differential change.

    J = |Δcurvature| + |Δgradient|
    """
    return curvature_gradient(p, q)


# ---------------------------------------------------------------------------
# Jacobian Smoothness Check
# ---------------------------------------------------------------------------

def jacobian_safe(p: Point, q: Point, lineage: Lineage | str) -> JacobianResult:
    """
    Determine whether the Jacobian between two points is smooth enough for
    membrane evaluation.

    Parameters
    ----------
    p : Point
        Source geometric point.
    q : Point
        Target geometric point.
    lineage : Lineage or str
        Lineage object or lineage name.

    Returns
    -------
    JacobianResult
        Structured result containing smoothness flag, delta, threshold,
        lineage name, and diagnostic reason.
    """
    if isinstance(lineage, str):
        from .lineage import get_lineage
        lineage = get_lineage(lineage)

    threshold = JACOBIAN_THRESHOLDS[lineage.name]
    delta = estimate_jacobian(p, q)
    smooth = delta <= threshold

    reason = (
        "Jacobian within smoothness bound."
        if smooth else
        f"Jacobian {delta:.4f} exceeds smoothness bound {threshold:.4f}."
    )

    return JacobianResult(
        smooth=smooth,
        delta=delta,
        threshold=threshold,
        lineage=lineage.name,
        reason=reason,
    )
