# Regulation States

Every regulation moves through a lifecycle. METR and TRO practice need shared language for those states so legal documents, roadside devices, and electronic catalogues stay consistent.

!!! note
    Draft ISO/TR 24315-5 extends and revises some state definitions relative to ISO 24315-1:2025; the series is expected to be harmonized in a future edition.

## Core states

| State | Meaning | Practical notes |
| --- | --- | --- |
| **proposed** | Not yet approved by the rule maker | Still in drafting / consultation |
| **approved** | Approved with a future inception time | May not yet be installed on the road |
| **beingImplemented** | Installation / authorization of associated TCDs is under way | Typical for posted regulations after approval |
| **dormant** | Approved but needs additional legal action to engage | Often used for rare emergency preparedness scenarios |
| **implemented** | Inception time is in the past; termination is undefined or in the future | May be active, inactive, or overridden |
| **active** | Implemented and presently in effect | Enforceable when conditions are met; posted regulations need TCDs installed and enabled |
| **inactive** | Implemented but not presently in effect | e.g., time-of-day restriction outside its hours |
| **overridden / suspended** | Implemented but temporarily nullified or replaced by another regulation | Overriding regulation is expected to terminate eventually |
| **terminated** | Previously in effect; no longer enforceable | Ended by termination time, cancellation, annulment, or replacement |
| **annulled** | Declared invalid or unenforceable as if it never existed | Typically because it was improperly made or unlawful |

## Useful distinctions

**Implemented vs active.** A school-zone speed limit can be *implemented* year-round but *active* only during posted hours. Enforcement applies only while active.

**Approved vs beingImplemented.** Approval creates legal authority to proceed; posted regulations still need field work before they can be active.

**Dormant.** Evacuation, avalanche, or similar plans may be approved and even partly prepared, yet remain disengaged until a rule maker formally announces engagement.

**Overridden.** Temporary work-zone or emergency regulations may suspend a permanent regulation without terminating it.

## Why rule makers care

Electronic METR records must carry enough state and timing information that user systems know whether a regulation is merely approved, already implemented, currently active, or overridden. Mis-stating state is a common source of [physical–digital discrepancy](roadway-environment.md).

Continue with [TRO states](tro-states.md) for the lifecycle of the order that packages one or more regulations.
