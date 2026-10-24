"""
transition.py
Shared-Horizon Toolkit — Lineage Transition Maps

Implements lineage transition rules, reversibility constraints, and forbidden
transitions. Transition logic is Stage 4 of the membrane evaluation pipeline,
following envelope safety, curvature compatibility, and collapse-risk checks.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass
from typing import Dict, Tuple

from .lineage import (
    Lineage,
    OPERATOR,
    PRECL,
    EXPRESSIVE_ANIMA,
    RNE,
    SPECTRAL,
)


# ---------------------------------------------------------------------------
# Transition Definition
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Transition:
    """
    Immutable lineage transition rule.

    Attributes
    ----------
    source : str
        Source lineage name.
    target : str
        Target lineage name.
    reversible : bool
        Whether the transition must be reversible.
    allowed : bool
        Whether the transition is permitted.
    reason : str
        Diagnostic explanation.
    """
    source: str
    target: str
    reversible: bool
    allowed: bool
    reason: str


# ---------------------------------------------------------------------------
# Transition Rules
# ---------------------------------------------------------------------------
# These rules encode the geometric constraints described in your notebook series.

TRANSITION_RULES: Dict[Tuple[str, str], Transition] = {}

def _add(source: Lineage, target: Lineage, allowed: bool, reason: str):
    """Internal helper to populate the transition registry."""
    reversible = target.reversible_required or source.reversible_required
    TRANSITION_RULES[(source.name, target.name)] = Transition(
        source=source.name,
        target=target.name,
        reversible=reversible,
        allowed=allowed,
        reason=reason,
    )


# ---------------------------------------------------------------------------
# Allowed Transitions
# ---------------------------------------------------------------------------

# OPERATOR → PRECL (smooth expressive continuity)
_add(OPERATOR, PRECL, True, "Smooth expressive continuity transition.")

# PRECL → OPERATOR (reversible return)
_add(PRECL, OPERATOR, True, "Reversible return to operator geometry.")

# PRECL → ANIMA (expressive ascent)
_add(PRECL, EXPRESSIVE_ANIMA, True, "Expressive ascent into ANIMA geometry.")

# ANIMA → PRECL (reversible descent)
_add(EXPRESSIVE_ANIMA, PRECL, True, "Reversible descent from ANIMA.")

# RNE ↔ PRECL (narrative ↔ expressive reversible)
_add(RNE, PRECL, True, "Reversible narrative → expressive transition.")
_add(PRECL, RNE, True, "Reversible expressive → narrative transition.")

# RNE ↔ ANIMA (reversible expressive-narrative)
_add(RNE, EXPRESSIVE_ANIMA, True, "Reversible narrative → ANIMA transition.")
_add(EXPRESSIVE_ANIMA, RNE, True, "Reversible ANIMA → narrative transition.")


# ---------------------------------------------------------------------------
# Forbidden Transitions
# ---------------------------------------------------------------------------

# OPERATOR → ANIMA (too steep curvature)
_add(OPERATOR, EXPRESSIVE_ANIMA, False, "Forbidden: curvature amplification too steep.")

# OPERATOR → RNE (requires reversible operator, not satisfied)
_add(OPERATOR, RNE, False, "Forbidden: RNE requires reversible operator geometry.")

# OPERATOR → SPECTRAL (hard firewall block)
_add(OPERATOR, SPECTRAL, False, "Forbidden: spectral drift incompatible with operator geometry.")

# PRECL → SPECTRAL (hard firewall block)
_add(PRECL, SPECTRAL, False, "Forbidden: spectral drift incompatible with expressive continuity.")

# ANIMA → SPECTRAL (hard firewall block)
_add(EXPRESSIVE_ANIMA, SPECTRAL, False, "Forbidden: spectral drift incompatible with ANIMA geometry.")

# RNE → SPECTRAL (hard firewall block)
_add(RNE, SPECTRAL, False, "Forbidden: spectral drift incompatible with narrative geometry.")

# SPECTRAL → any (spectral cannot transition out)
for target in [OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE]:
    _add(SPECTRAL, target, False, "Forbidden: spectral geometry cannot transition out.")


# ---------------------------------------------------------------------------
# Transition Lookup
# ---------------------------------------------------------------------------

def get_transition(source: str | Lineage, target: str | Lineage) -> Transition:
    """
    Retrieve the transition rule between two lineages.

    Parameters
    ----------
    source : str or Lineage
    target : str or Lineage

    Returns
    -------
    Transition
        The corresponding transition rule.

    Raises
    ------
    KeyError
        If the transition is not defined.
    """
    if isinstance(source, Lineage):
        source = source.name
    if isinstance(target, Lineage):
        target = target.name

    key = (source, target)
    if key not in TRANSITION_RULES:
        raise KeyError(f"No transition rule defined for {source} → {target}")
    return TRANSITION_RULES[key]


# ---------------------------------------------------------------------------
# Transition Permission Check
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TransitionDecision:
    """Structured result for transition permission evaluation."""
    allowed: bool
    reversible: bool
    reason: str
    source: str
    target: str


def transition_allowed(source: str | Lineage, target: str | Lineage) -> TransitionDecision:
    """
    Determine whether a lineage transition is allowed.

    Returns
    -------
    TransitionDecision
        Structured result containing permission flag, reversibility requirement,
        and diagnostic reason.
    """
    rule = get_transition(source, target)

    return TransitionDecision(
        allowed=rule.allowed,
        reversible=rule.reversible,
        reason=rule.reason,
        source=rule.source,
        target=rule.target,
    )
