"""
collapse.py
Shared-Horizon Toolkit — Collapse-Risk Tensors

Implements lineage-specific collapse-risk functions and compatibility checks.
Collapse-risk is Stage 3 of the membrane evaluation pipeline, following
envelope safety and curvature compatibility.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Callable, Dict

from .lineage import Lineage, OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE, SPECTRAL
from .curvature import Point, curvature_gradient


# ---------------------------------------------------------------------------
# Collapse-Risk Structured Result
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CollapseRisk:
    """
    Structured collapse-risk evaluation.

    Attributes
    ----------
    risk : float
        Collapse-risk energy.
    lineage : str
        Lineage name.
    safe : bool
        Whether collapse-risk is below lineage stability bound.
    reason : str
        Diagnostic explanation.
    """
    risk: float
    lineage: str
    safe: bool
    reason: str


# ---------------------------------------------------------------------------
# Collapse-Risk Functions
# ---------------------------------------------------------------------------

def collapse_operator(p: Point) -> float:
    """
    Operator collapse-risk: low curvature, low gradient.
    Risk = 0.2 * curvature + 0.1 * gradient
    """
    return 0.2 * p.curvature + 0.1 * p.gradient


def collapse_precl(p: Point) -> float:
    """
    PRECL collapse-risk: expressive continuity.
    Risk = 0.3 * curvature + 0.15 * gradient
    """
    return 0.3 * p.curvature + 0.15 * p.gradient


def collapse_anima(p: Point) -> float:
    """
    ANIMA collapse-risk: steep curvature + gradient amplification.
    Risk = 1.5 * curvature + 1.2 * gradient
    """
    return 1.5 * p.curvature + 1.2 * p.gradient


def collapse_narrative(p: Point) -> float:
    """
    RNE collapse-risk: moderate curvature + gradient.
    Risk = 0.8 * curvature + 0.6 * gradient
    """
    return 0.8 * p.curvature + 0.6 * p.gradient


def collapse_spectral(p: Point) -> float:
    """
    Spectral collapse-risk: drift-dominated geometry.
    Risk = 2.0 * drift + 0.3 * curvature
    """
    return 2.0 * p.drift + 0.3 * p.curvature


# ---------------------------------------------------------------------------
# Collapse Registry
# ---------------------------------------------------------------------------

COLLAPSE_REGISTRY: Dict[str, Callable[[Point], float]] = {
    "OPERATOR": collapse_operator,
    "PRECL": collapse_precl,
    "ANIMA": collapse_anima,
    "RNE": collapse_narrative,
    "SPECTRAL": collapse_spectral,
}


def get_collapse_fn(lineage: Lineage) -> Callable[[Point], float]:
    """
    Retrieve the collapse-risk function for a lineage.
    """
    name = lineage.name.upper()
    if name not in COLLAPSE_REGISTRY:
        raise KeyError(f"No collapse-risk function registered for lineage: {lineage.name}")
    return COLLAPSE_REGISTRY[name]


# ---------------------------------------------------------------------------
# Collapse Compatibility
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class CollapseCompatibility:
    """Structured result for collapse compatibility evaluation."""
    compatible: bool
    delta: float
    threshold: float
    reason: str


def collapse_compatible(p: Point, q: Point, threshold: float = 0.25) -> CollapseCompatibility:
    """
    Determine whether collapse-risk transition p -> q is smooth enough.

    Uses curvature-gradient as the underlying geometric signal.
    """
    delta = curvature_gradient(p, q)
    compatible = delta <= threshold

    reason = (
        "Collapse-risk transition is smooth."
        if compatible else
        f"Collapse gradient {delta:.4f} exceeds threshold {threshold:.4f}."
    )

    return CollapseCompatibility(
        compatible=compatible,
        delta=delta,
        threshold=threshold,
        reason=reason,
    )


# ---------------------------------------------------------------------------
# Collapse-Risk Spike Detection
# ---------------------------------------------------------------------------

def collapse_spike(p: Point, lineage: Lineage) -> CollapseRisk:
    """
    Detect collapse-risk spikes relative to lineage stability bounds.

    Returns
    -------
    CollapseRisk
        Structured result containing risk, safety flag, and diagnostic reason.
    """
    fn = get_collapse_fn(lineage)
    risk = fn(p)
    bound = lineage.stability_bound
    safe = risk <= bound

    reason = (
        "Collapse-risk within stability bound."
        if safe else
        f"Collapse-risk {risk:.4f} exceeds stability bound {bound:.4f}."
    )

    return CollapseRisk(
        risk=risk,
        lineage=lineage.name,
        safe=safe,
        reason=reason,
    )
