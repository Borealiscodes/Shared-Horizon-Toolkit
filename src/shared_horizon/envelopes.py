"""
envelopes.py
Shared-Horizon Toolkit — Stability Envelopes

Defines lineage-specific stability envelopes, energy functionals,
and envelope safety checks used by the membrane evaluator.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Callable
from .lineage import Lineage, OPERATOR, EXPRESSIVE_PRECL, EXPRESSIVE_ANIMA, NARRATIVE_RNE, SPECTRAL


# ---------------------------------------------------------------------------
# Energy Functionals
# ---------------------------------------------------------------------------

def operator_energy(p) -> float:
    """
    NDH operator energy functional.
    Typically small and curvature-based.
    """
    return abs(p.curvature)


def precl_energy(p) -> float:
    """
    PRECL expressive continuity energy.
    Low curvature, smooth gradients.
    """
    return abs(p.curvature)


def anima_energy(p) -> float:
    """
    ANIMA expressive phenomenology energy.
    High curvature, steep gradients.
    """
    return abs(p.curvature) + abs(p.gradient)


def narrative_energy(p) -> float:
    """
    RNE narrative curvature energy.
    Moderate curvature with reversibility constraints.
    """
    return abs(p.curvature)


def spectral_energy(p) -> float:
    """
    Spectral drift energy.
    Drift replaces curvature as the dominant instability measure.
    """
    return abs(p.drift)


# ---------------------------------------------------------------------------
# Envelope Definition
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Envelope:
    lineage: Lineage
    energy_fn: Callable
    bound: float

    def safe(self, p) -> bool:
        """
        Check whether a point p lies within the lineage's stability envelope.
        """
        return self.energy_fn(p) <= self.bound


# ---------------------------------------------------------------------------
# Envelope Instances
# ---------------------------------------------------------------------------

OPERATOR_ENVELOPE = Envelope(
    lineage=OPERATOR,
    energy_fn=operator_energy,
    bound=OPERATOR.stability_bound
)

PRECL_ENVELOPE = Envelope(
    lineage=EXPRESSIVE_PRECL,
    energy_fn=precl_energy,
    bound=EXPRESSIVE_PRECL.stability_bound
)

ANIMA_ENVELOPE = Envelope(
    lineage=EXPRESSIVE_ANIMA,
    energy_fn=anima_energy,
    bound=EXPRESSIVE_ANIMA.stability_bound
)

NARRATIVE_ENVELOPE = Envelope(
    lineage=NARRATIVE_RNE,
    energy_fn=narrative_energy,
    bound=NARRATIVE_RNE.stability_bound
)

SPECTRAL_ENVELOPE = Envelope(
    lineage=SPECTRAL,
    energy_fn=spectral_energy,
    bound=SPECTRAL.stability_bound
)


# Registry for lookup
ENVELOPE_REGISTRY = {
    "OPERATOR": OPERATOR_ENVELOPE,
    "PRECL": PRECL_ENVELOPE,
    "ANIMA": ANIMA_ENVELOPE,
    "RNE": NARRATIVE_ENVELOPE,
    "SPECTRAL": SPECTRAL_ENVELOPE,
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_envelope(lineage_name: str) -> Envelope:
    """
    Retrieve the stability envelope for a lineage.
    """
    return ENVELOPE_REGISTRY[lineage_name.upper()]


def envelope_safe(p, lineage_name: str) -> bool:
    """
    Convenience function used by membrane.py.
    """
    env = get_envelope(lineage_name)
    return env.safe(p)
