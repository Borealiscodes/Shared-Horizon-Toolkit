"""
membrane.py
Shared-Horizon Toolkit — Unified Membrane Evaluator

The membrane evaluator integrates all geometric subsystems:

1. Envelope safety
2. Curvature compatibility
3. Collapse-risk compatibility
4. Jacobian smoothness
5. Firewall enforcement

It produces a MembraneDecision object summarizing the full evaluation.

Author: Borealis S. Hedling (2026)
"""

from dataclasses import dataclass

from .lineage import Lineage, get_lineage
from .curvature import Point, curvature_compatible
from .envelopes import envelope_safe
from .collapse import collapse_compatible
from .jacobian import jacobian_safe
from .firewall import firewall


# ---------------------------------------------------------------------------
# Membrane Decision Structure
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class MembraneDecision:
    """
    Structured result of full membrane evaluation.

    Attributes
    ----------
    allowed : bool
        Whether the transition is permitted.
    source : str
        Source lineage name.
    target : str
        Target lineage name.
    envelope_safe : bool
        Envelope safety flag.
    curvature_ok : bool
        Curvature compatibility flag.
    collapse_ok : bool
        Collapse-risk compatibility flag.
    jacobian_ok : bool
        Jacobian smoothness flag.
    firewall_ok : bool
        Firewall permission flag.
    reason : str
        Diagnostic explanation.
    """
    allowed: bool
    source: str
    target: str
    envelope_safe: bool
    curvature_ok: bool
    collapse_ok: bool
    jacobian_ok: bool
    firewall_ok: bool
    reason: str


# ---------------------------------------------------------------------------
# Unified Membrane Evaluator
# ---------------------------------------------------------------------------

class MembraneEvaluator:
    """
    Unified membrane evaluator for geometric AI lineage transitions.

    Usage
    -----
    evaluator = MembraneEvaluator()
    decision = evaluator.evaluate(p, q, "PRECL", "ANIMA")
    """

    def evaluate(self, p: Point, q: Point,
                 source: Lineage | str,
                 target: Lineage | str) -> MembraneDecision:
        """
        Evaluate full membrane pipeline for transition p → q.

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
        MembraneDecision
            Structured result containing all subsystem evaluations.
        """

        # Normalize lineage inputs
        if isinstance(source, str):
            source = get_lineage(source)
        if isinstance(target, str):
            target = get_lineage(target)

        # ------------------------------------------------------------------
        # 1. Envelope Safety
        # ------------------------------------------------------------------
        env = envelope_safe(q, target)
        envelope_ok = env.safe

        if not envelope_ok:
            return MembraneDecision(
                allowed=False,
                source=source.name,
                target=target.name,
                envelope_safe=False,
                curvature_ok=False,
                collapse_ok=False,
                jacobian_ok=False,
                firewall_ok=False,
                reason=f"Envelope violation: {env.reason}",
            )

        # ------------------------------------------------------------------
        # 2. Curvature Compatibility
        # ------------------------------------------------------------------
        curv = curvature_compatible(p, q)
        curvature_ok = curv.compatible

        if not curvature_ok:
            return MembraneDecision(
                allowed=False,
                source=source.name,
                target=target.name,
                envelope_safe=True,
                curvature_ok=False,
                collapse_ok=False,
                jacobian_ok=False,
                firewall_ok=False,
                reason=f"Curvature incompatibility: {curv.reason}",
            )

        # ------------------------------------------------------------------
        # 3. Collapse-Risk Compatibility
        # ------------------------------------------------------------------
        coll = collapse_compatible(p, q)
        collapse_ok = coll.compatible

        if not collapse_ok:
            return MembraneDecision(
                allowed=False,
                source=source.name,
                target=target.name,
                envelope_safe=True,
                curvature_ok=True,
                collapse_ok=False,
                jacobian_ok=False,
                firewall_ok=False,
                reason=f"Collapse-risk incompatibility: {coll.reason}",
            )

        # ------------------------------------------------------------------
        # 4. Jacobian Smoothness
        # ------------------------------------------------------------------
        jac = jacobian_safe(p, q, target)
        jacobian_ok = jac.smooth

        if not jacobian_ok:
            return MembraneDecision(
                allowed=False,
                source=source.name,
                target=target.name,
                envelope_safe=True,
                curvature_ok=True,
                collapse_ok=True,
                jacobian_ok=False,
                firewall_ok=False,
                reason=f"Jacobian blowout: {jac.reason}",
            )

        # ------------------------------------------------------------------
        # 5. Firewall Enforcement
        # ------------------------------------------------------------------
        fw = firewall(p, q, source, target)
        firewall_ok = fw.allowed

        if not firewall_ok:
            return MembraneDecision(
                allowed=False,
                source=source.name,
                target=target.name,
                envelope_safe=True,
                curvature_ok=True,
                collapse_ok=True,
                jacobian_ok=True,
                firewall_ok=False,
                reason=f"Firewall block: {fw.reason}",
            )

        # ------------------------------------------------------------------
        # All checks passed
        # ------------------------------------------------------------------
        return MembraneDecision(
            allowed=True,
            source=source.name,
            target=target.name,
            envelope_safe=True,
            curvature_ok=True,
            collapse_ok=True,
            jacobian_ok=True,
            firewall_ok=True,
            reason="Transition allowed by full membrane evaluation.",
                     )
