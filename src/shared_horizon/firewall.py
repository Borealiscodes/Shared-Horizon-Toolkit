"""
firewall.py
Shared-Horizon Toolkit — Firewall Enforcement

Implements hard safety boundaries for lineage transitions. The firewall is
Stage 5 of the membrane pipeline, following envelope safety, curvature
compatibility, collapse-risk evaluation, and Jacobian smoothness checks.

The firewall enforces:
- spectral hard blocks
- expressive → operator forbidden transitions
- collapse-risk spikes
- Jacobian blowouts

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass

from .lineage import Lineage, OPERATOR, PRECL, EXPRESSIVE_ANIMA, RNE, SPECTRAL
from .collapse import collapse_spike
from .jacobian import jacobian_safe
from .curvature import Point
from .transition import transition_allowed


# ---------------------------------------------------------------------------
# Firewall Decision Structure
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FirewallDecision:
    """
    Structured firewall evaluation.

    Attributes
    ----------
    allowed : bool
        Whether the transition is permitted.
    reason : str
        Diagnostic explanation.
    source : str
        Source lineage name.
    target : str
        Target lineage name.
    collapse_safe : bool
        Whether collapse-risk is within bounds.
    jacobian_safe : bool
        Whether Jacobian is within smoothness bounds.
    """
    allowed: bool
    reason: str
    source: str
    target: str
    collapse_safe: bool
    jacobian_safe: bool


# ---------------------------------------------------------------------------
# Firewall Enforcement Logic
# ---------------------------------------------------------------------------

def firewall(p: Point, q: Point, source: Lineage | str, target: Lineage | str) -> FirewallDecision:
    """
    Enforce hard safety boundaries for lineage transitions.

    Parameters
    ----------
    p : Point
        Source geometric point.
    q : Point
        Target geometric point.
    source : Lineage or str
        Source lineage.
    target : Lineage or str
        Target lineage.

    Returns
    -------
    FirewallDecision
        Structured result containing permission flag, diagnostics, and safety checks.
    """
    # Normalize lineage inputs
    if isinstance(source, str):
        from .lineage import get_lineage
        source = get_lineage(source)
    if isinstance(target, str):
        from .lineage import get_lineage
        target = get_lineage(target)

    # ----------------------------------------------------------------------
    # 1. Spectral Hard Block
    # ----------------------------------------------------------------------
    if source.name == "SPECTRAL":
        return FirewallDecision(
            allowed=False,
            reason="Hard block: spectral geometry cannot transition out.",
            source=source.name,
            target=target.name,
            collapse_safe=False,
            jacobian_safe=False,
        )

    if target.name == "SPECTRAL":
        return FirewallDecision(
            allowed=False,
            reason="Hard block: spectral drift incompatible with target lineage.",
            source=source.name,
            target=target.name,
            collapse_safe=False,
            jacobian_safe=False,
        )

    # ----------------------------------------------------------------------
    # 2. Expressive → Operator Hard Block
    # ----------------------------------------------------------------------
    if source.name == "ANIMA" and target.name == "OPERATOR":
        return FirewallDecision(
            allowed=False,
            reason="Hard block: expressive → operator transition forbidden.",
            source=source.name,
            target=target.name,
            collapse_safe=False,
            jacobian_safe=False,
        )

    # ----------------------------------------------------------------------
    # 3. Collapse-Risk Spike Check
    # ----------------------------------------------------------------------
    collapse_result = collapse_spike(q, target)
    if not collapse_result.safe:
        return FirewallDecision(
            allowed=False,
            reason=f"Collapse-risk spike: {collapse_result.reason}",
            source=source.name,
            target=target.name,
            collapse_safe=False,
            jacobian_safe=True,
        )

    # ----------------------------------------------------------------------
    # 4. Jacobian Blowout Check
    # ----------------------------------------------------------------------
    jac_result = jacobian_safe(p, q, target)
    if not jac_result.smooth:
        return FirewallDecision(
            allowed=False,
            reason=f"Jacobian blowout: {jac_result.reason}",
            source=source.name,
            target=target.name,
            collapse_safe=True,
            jacobian_safe=False,
        )

    # ----------------------------------------------------------------------
    # 5. Transition Rule Check
    # ----------------------------------------------------------------------
    t = transition_allowed(source, target)
    if not t.allowed:
        return FirewallDecision(
            allowed=False,
            reason=f"Transition rule violation: {t.reason}",
            source=source.name,
            target=target.name,
            collapse_safe=True,
            jacobian_safe=True,
        )

    # ----------------------------------------------------------------------
    # All checks passed
    # ----------------------------------------------------------------------
    return FirewallDecision(
        allowed=True,
        reason="Transition allowed by firewall.",
        source=source.name,
        target=target.name,
        collapse_safe=True,
        jacobian_safe=True,
    )
