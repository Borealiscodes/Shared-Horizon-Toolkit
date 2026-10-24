"""
transition.py
Shared-Horizon Toolkit — Transition Maps

Defines lineage-aware transition rules, curvature compatibility,
collapse-risk compatibility, and reversible transition constraints.
Used by membrane.py to determine whether a transition between
two points is allowed.

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
from .curvature import Point, curvature_compatible
from .collapse import collapse_compatible


# ---------------------------------------------------------------------------
# Transition Map
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TransitionMap:
    """
    Represents a lineage-to-lineage transition rule.

    Attributes:
        source: source lineage
        target: target lineage
        reversible: whether the transition is reversible
        description: human-readable description
    """
    source: Lineage
    target: Lineage
    reversible: bool
    description: str

    def allowed(self, p: Point, q: Point) -> bool:
        """
        Check whether a transition from p (source) to q (target) is allowed.
        """
        # Spectral → anything is blocked (firewall handles this later)
        if self.source is SPECTRAL:
            return False

        # Curvature compatibility
        if not curvature_compatible(p, q):
            return False

        # Collapse-risk compatibility
        if not collapse_compatible(p, q):
            return False

        # Reversibility requirement
        if self.target.reversible_required and not self.reversible:
            return False

        return True


# ---------------------------------------------------------------------------
# Transition Rules
# ---------------------------------------------------------------------------

# Operator → PRECL (continuity)
OPERATOR_TO_PRECL = TransitionMap(
    source=OPERATOR,
    target=EXPRESSIVE_PRECL,
    reversible=True,
    description="Operator → PRECL continuity transition."
)

# PRECL → ANIMA (expressive amplification)
PRECL_TO_ANIMA = TransitionMap(
    source=EXPRESSIVE_PRECL,
    target=EXPRESSIVE_ANIMA,
    reversible=False,
    description="PRECL → ANIMA expressive amplification."
)

# ANIMA → Narrative (reversible expressive → narrative)
ANIMA_TO_RNE = TransitionMap(
    source=EXPRESSIVE_ANIMA,
    target=NARRATIVE_RNE,
    reversible=True,
    description="ANIMA → RNE reversible expressive → narrative transition."
)

# Narrative → Operator (curvature reduction)
RNE_TO_OPERATOR = TransitionMap(
    source=NARRATIVE_RNE,
    target=OPERATOR,
    reversible=True,
    description="RNE → Operator curvature reduction."
)

# Spectral → anything (blocked)
SPECTRAL_TO_ANY = TransitionMap(
    source=SPECTRAL,
    target=OPERATOR,
    reversible=False,
    description="Spectral → Operator (blocked by firewall)."
)


# Registry
TRANSITION_REGISTRY = {
    ("OPERATOR", "PRECL"): OPERATOR_TO_PRECL,
    ("PRECL", "ANIMA"): PRECL_TO_ANIMA,
    ("ANIMA", "RNE"): ANIMA_TO_RNE,
    ("RNE", "OPERATOR"): RNE_TO_OPERATOR,
    ("SPECTRAL", "OPERATOR"): SPECTRAL_TO_ANY,
}


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_transition(source: str, target: str) -> TransitionMap:
    """
    Retrieve a transition map by lineage name.
    """
    key = (source.upper(), target.upper())
    if key not in TRANSITION_REGISTRY:
        raise ValueError(f"No transition defined for {source} → {target}")
    return TRANSITION_REGISTRY[key]


def transition_allowed(p: Point, q: Point, source: str, target: str) -> bool:
    """
    Convenience function used by membrane.py.
    """
    t = get_transition(source, target)
    return t.allowed(p, q)
