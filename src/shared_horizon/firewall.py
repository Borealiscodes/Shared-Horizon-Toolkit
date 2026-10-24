"""
firewall.py
Shared-Horizon Toolkit — Mosaic Boundary Firewall

Enforces forbidden transitions between lineage regions. The firewall
is the hard boundary layer of the Shared-Horizon membrane architecture:
it blocks spectral → anything, expressive → operator jumps, ANIMA → OPERATOR
direct transitions, collapse-risk spikes, and Jacobian blowouts.

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
from .collapse import get_collapse_fn
from .jacobian import jacobian_safe


# ---------------------------------------------------------------------------
# Firewall Decision
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FirewallDecision:
    allowed: bool
    reason: str


# ---------------------------------------------------------------------------
# Firewall Rules
# ---------------------------------------------------------------------------

def firewall_block_spectral(source: Lineage, target: Lineage) -> FirewallDecision:
    """
    Spectral → anything is forbidden.
    """
    if source is SPECTRAL:
        return FirewallDecision(False, "Spectral → any transition is forbidden.")
    return FirewallDecision(True, "OK")


def firewall_block_anima_to_operator(source: Lineage, target: Lineage) -> FirewallDecision:
    """
    ANIMA expressive → OPERATOR is forbidden.
    Curvature jump is too large and violates membrane continuity.
    """
    if source is EXPRESSIVE_ANIMA and target is OPERATOR:
        return FirewallDecision(False, "ANIMA → OPERATOR is forbidden (expressive → operator jump).")
    return FirewallDecision(True, "OK")


def firewall_block_expressive_to_operator(source: Lineage, target: Lineage) -> FirewallDecision:
    """
    PRECL expressive → OPERATOR is forbidden unless curvature is extremely low.
    """
    if source is EXPRESSIVE_PRECL and target is OPERATOR:
        return FirewallDecision(False, "PRECL → OPERATOR is forbidden (expressive → operator jump).")
    return FirewallDecision(True, "OK")


def firewall_block_collapse_spike(p: Point, q: Point, source: Lineage, target: Lineage) -> FirewallDecision:
    """
    Collapse-risk spike: if collapse-risk increases by > 50%, block.
    """
    collapse_fn_src = get_collapse_fn(source)
    collapse_fn_tgt = get_collapse_fn(target)

    cp = collapse_fn_src(p).total
    cq = collapse_fn_tgt(q).total

    if cq > cp * 1.5:
        return FirewallDecision(False, "Collapse-risk spike > 50% detected.")
    return FirewallDecision(True, "OK")


def firewall_block_jacobian(p: Point, q: Point, target: Lineage) -> FirewallDecision:
    """
    Jacobian blowout: if Jacobian exceeds lineage smoothness bound, block.
    """
    if not jacobian_safe(p, q, target):
        return FirewallDecision(False, "Jacobian blowout: smoothness constraint violated.")
    return FirewallDecision(True, "OK")


# ---------------------------------------------------------------------------
# Unified Firewall
# ---------------------------------------------------------------------------

def firewall(source: Lineage, target: Lineage, p: Point, q: Point) -> FirewallDecision:
    """
    Unified firewall check combining all boundary rules.
    """

    # Spectral → anything
    d = firewall_block_spectral(source, target)
    if not d.allowed:
        return d

    # ANIMA → OPERATOR
    d = firewall_block_anima_to_operator(source, target)
    if not d.allowed:
        return d

    # PRECL → OPERATOR
    d = firewall_block_expressive_to_operator(source, target)
    if not d.allowed:
        return d

    # Collapse-risk spike
    d = firewall_block_collapse_spike(p, q, source, target)
    if not d.allowed:
        return d

    # Jacobian blowout
    d = firewall_block_jacobian(p, q, target)
    if not d.allowed:
        return d

    return FirewallDecision(True, "Transition allowed by firewall.")
