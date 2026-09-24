# Road Operator Perspective

METR adds a digital operational tool to existing road-management practices. It works with, rather than replaces, established processes for traffic control, signing, maintenance, construction, incident management and regulatory decision-making. For a road operator, METR serves as the digital link between the rules governing the road and the people, vehicles and systems that operate on it. The road operator helps ensure that authorized road rules are accurately represented, operationally maintained, communicated to users, and convey the relevant situation actually present on the roadway. This includes the trustworthy, machine-interpretable road rules—including both relatively static rules and dynamic rules—so that vehicles and other users can obtain authoritative information relevant to their location, time and circumstances. At the core, the road operator's METR role is to keep the digital representation of the road aligned with the authorized rules and the physical roadway—using trusted electronic rules, reliable roadside systems and a disciplined discrepancy-response process to keep road users informed. METR provides the trusted digital representation and distribution of that information.

## Road Operator Responsibilities

A road operator should establish clear responsibilities for three connected activities:

1.  Connecting operational rules to the authorized rule maker

2.  Managing the roadside equipment and systems that support METR

3.  Responding when the electronic representation does not match the physical roadway

## Operational Rule Makers

The road operator should maintain a clear and traceable relationship with the authorized rule maker(s) responsible for establishing the legal or operational rules applicable to the roadway. Operational rule makers might include transportation agencies, municipalities, toll-road authorities, campus authorities, emergency-management authorities or other entities legally empowered to establish or modify traffic rules.

The operator should:

-   Identify which organization has authority for each category of rule

-   Ensure that authorized rules are entered into, or made available to, the appropriate METR regulation system

-   Establish procedures for planned, temporary and emergency rules

-   Ensure that changes to physical signs, markings, lane controls, parking restrictions, work zones and other regulated conditions are coordinated with their electronic representation

-   Define who is authorized to approve, verify and digitally sign rules

-   Maintain traceability between the legal/operational source, the electronic rule and the field implementation

-   Establish appropriate rule freshness and activation procedures, particularly for temporary and emergent rules

The operator should not, however, independently create a legal rule merely because a roadway condition has changed. Where the operator has delegated authority to establish an operational restriction; for example, an emergency lane closure, the operator should follow the applicable authority and approval process and then ensure that the resulting rule is represented and distributed through METR.

For practical guidance, the operator should use the applicable materials here (see [ISO/TC 204 METR repository and implementation materials](https://github.com/ISO-TC204/iso24315?utm_source=chatgpt.com)) and coordinate with the regional METR policy framework (insert link to Regional Body Perspective/Regional Guidance 5.2).

## RSE Management

Roadside equipment (RSE) provides an important operational connection between the digital METR environment and conditions observed or controlled on the roadway.

Depending on the deployment, RSE might support:

-   Distribution of emergent or locally relevant rules

-   Communication where normal network connectivity is unavailable or unreliable

-   Detection or confirmation of roadway conditions

-   Work-zone and lane-control operations

-   Dynamic restrictions or zone status

-   Collection of information that can support discrepancy reporting

The road operator should establish procedures to ensure that RSE is:

-   **Available and operational** when required for safety-critical functions

-   **Correctly located and associated** with the roadway element or zone it serves

-   **Securely connected** to authorized METR systems

-   **Maintained, monitored and periodically tested**

-   Protected against unauthorized modification

-   Supported by backup or alternative communication arrangements where loss of connectivity could delay an emergent rule

RSE should not become a separate source of uncontrolled "truth." Where an RSE-originated message represents a regulation, the deployment should clearly identify the authority and verification process behind that message. For emergent situations, the operational objective is particularly important since a rule that becomes effective immediately must reach affected users no later than the point at which the rule takes effect. Where connectivity is intermittent, METR deployments should support resilient distribution paths, including appropriate local or roadside mechanisms.

## Road Maintenance and Discrepancy Response

Road maintenance is where the METR digital environment most directly meets the physical roadway.

A discrepancy occurs when there is a potential conflict between:

-   an electronic METR rule and a physical sign or marking;

-   two electronic rules;

-   two physical signs or markings; or

-   an electronic rule and the actual roadway condition

Examples include a missing, damaged, obscured or incorrect sign, an electronic speed limit that does not match the posted speed limit, a lane closure that is physically in place but absent electronically, or a temporary restriction that remains electronically active after the physical restriction has been removed. The road operator should establish a simple workflow that will reliably:

### Detect → Validate → Prioritize → Correct → Confirm

#### 1. Detect
Receive a discrepancy report from a METR consumer, field employee, inspection system, RSE or another authorized source.

#### 2. Validate
Determine whether the reported discrepancy is real. A single report may be incorrect; for example, a sign might have been temporarily obscured by a vehicle. Reports should be assessed according to locally defined procedures.

#### 3. Prioritize
Safety-critical discrepancies should receive the fastest response. Priority should consider risk, traffic exposure, regulatory significance and whether or not the discrepancy could cause an automated or human road user to take an unsafe or unlawful action.

#### 4. Correct
Repair, replace, uncover or reposition the physical asset; correct the electronic rule; or refer the matter to the authorized rule maker when the underlying rule itself requires clarification or change.

#### 5. Confirm and close
Verify that the physical and electronic states now agree, update the relevant METR record, and retain an audit trail of the report, investigation, action and resolution.

Where immediate physical correction is not possible, the operator should use the appropriate operational process to provide a temporary warning, restriction or other authorized response.

More broadly, the road operator should treat METR as part of the roadway lifecycle:

### Plan → Authorize → Encode → Sign/Deploy → Distribute → Operate → Monitor → Report discrepancy → Correct → Verify

This means that a new sign, lane restriction, work zone, parking restriction or emergency closure should ideally generate both the physical/operational change and the corresponding electronic METR change. As well, the road operator should employ a practical checklist tool to ensure successful METR deployment:

## Minimum Road-Operator Implementation Checklist

A deployment should, at minimum, define:

-   **Authority:** Who is legally authorized to create or change each rule?

-   **Ownership:** Who owns and maintains the physical roadway asset?

-   **METR responsibility:** Who enters, verifies, signs and maintains the electronic rule?

-   **RSE responsibility:** Who operates and maintains roadside communications/equipment?

-   **Discrepancy workflow:** Who receives, validates, prioritizes and resolves reports?

-   **Response times:** What service levels apply to safety-critical versus routine discrepancies?

-   **Emergent rules:** How are urgent restrictions distributed when normal connectivity is unavailable?

-   **Auditability:** What records demonstrate when a rule changed, who authorized it, when it was distributed and when the physical roadway was updated?

-   **Fallback:** What happens when METR connectivity, RSE or another digital component is unavailable?

-   **Coordination:** How do maintenance, construction, traffic management, emergency response and regulatory staff coordinate changes?

## Related pages

- [Roadway environment](roadway-environment.md)
- [Physical view](physical-view.md)
- [Jurisdictional management perspective](jurisdictional-management-perspective.md)
- [Rule maker perspective](rule-maker-perspective.md)
- [TRO installation and implementation](tro-installation-and-implementation.md)
