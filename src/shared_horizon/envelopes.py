"""
envelopes.py
Shared-Horizon Toolkit — Stability Envelopes

Implements lineage-specific stability envelopes. Each envelope is an energy
functional that determines whether a geometric point lies within the safe
operating region of a lineage.

Envelope safety is Stage 1 of the membrane evaluation pipeline.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Callable, Dict

from .lineage import Lineage, OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE, SPECTRAL
from .curvature import Point


# ---------------------------------------------------------------------------
# Envelope Energy Functional
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class EnvelopeResult:
    """Structured result for envelope evaluation."""
    safe: bool
    energy: float
    bound: float
    lineage: str
    reason: str


# ---------------------------------------------------------------------------
# Envelope Functions
# ---------------------------------------------------------------------------

def envelope_operator(p: Point) -> float:
    """
    Operator envelope: low curvature, low gradient, no drift.
    Energy = curvature + 0.5 * gradient
    """
    return p.curvature + 0.5 * p.gradient


def envelope_precl(p: Point) -> float:
    """
    PRECL envelope: expressive continuity, slightly higher curvature sensitivity.
    Energy = 1.2 * curvature + 0.5 * gradient
    """
    return 1.2 * p.curvature + 0.5 * p.gradient


def envelope_anima(p: Point) -> float:
    """
    ANIMA envelope: high curvature, high gradient.
    Energy = 2.5 * curvature + 1.5 * gradient
    """
    return 2.5 * p.curvature + 1.5 * p.gradient


def envelope_rne(p: Point) -> float:
    """
    RNE envelope: moderate curvature + gradient.
    Energy = 1.8 * curvature + 1.0 * gradient
    """
    return 1.8 * p.curvature + 1.0 * p.gradient


def envelope_spectral(p: Point) -> float:
    """
    Spectral envelope: drift-dominated geometry.
    Energy = 3.0 * drift + 0.2 * curvature
    """
    return 3.0 * p.drift + 0.2 * p.curvature


# ---------------------------------------------------------------------------
# Envelope Registry
# ---------------------------------------------------------------------------

ENVELOPE_REGISTRY: Dict[str, Callable[[Point], float]] = {
    "OPERATOR": envelope_operator,
    "PRECL": envelope_precl,
    "ANIMA": envelope_anima,
    "RNE": envelope_rne,
    "SPECTRAL": envelope_spectral,
}


def get_envelope_fn(lineage: Lineage) -> Callable[[Point], float]:
    """
    Retrieve the envelope function for a lineage.
    """
    name = lineage.name.upper()
    if name not in ENVELOPE_REGISTRY:
        raise KeyError(f"No envelope function registered for lineage: {lineage.name}")
    return ENVELOPE_REGISTRY[name]


# ---------------------------------------------------------------------------
# Envelope Safety Check
# ---------------------------------------------------------------------------

def envelope_safe(p: Point, lineage: Lineage | str) -> EnvelopeResult:
    """
    Determine whether a point lies within the stability envelope of a lineage.

    Parameters
    ----------
    p : Point
        Geometric point with curvature, gradient, drift.
    lineage : Lineage or str
        Lineage object or lineage name.

    Returns
    -------
    EnvelopeResult
        Structured result containing safety flag, energy, bound, lineage name,
        and diagnostic reason.
    """
    if isinstance(lineage, str):
        from .lineage import get_lineage
        lineage = get_lineage(lineage)

    fn = get_envelope_fn(lineage)
    energy = fn(p)
    bound = lineage.stability_bound
    safe = energy <= bound

    reason = (
        "Energy within stability bound."
        if safe else
        f"Energy {energy:.4f} exceeds stability bound {bound:.4f}."
    )

    return EnvelopeResult(
        safe=safe,
        energy=energy,
        bound=bound,
        lineage=lineage.name,
        reason=reason,
    )
