# Possible METR Deployment Scenarios

METR can be deployed incrementally. A jurisdiction does not need to implement the entire METR ecosystem or distribute regulations to external users to gain value. This page explains possible deployment scenarios for METR.

## Jurisdictional Management of Electronic Regulations

In this foundational scenario, a jurisdiction can start receiving benefits of METR through the management of electronic regulations throughout their lifecycle. Authorized personnel can create or amend regulations, translate them into a machine-readable form, verify that the electronic representation accurately reflects the governing regulation, and maintain the resulting regulatory data.

This scenario does not require regulations to be distributed to vehicles, navigation providers, or other external consumers. A single jurisdiction can deploy a METR regulation system purely as an internal regulation-management system, improving consistency, traceability, reuse, and quality control while continuing to publish regulations through existing channels.

Typical capabilities include:

- Regulation creation and approval
- Traceability to the Traffic Regulation Order (TRO)
- Translation into a standardized electronic representation
- Verification against the authoritative regulation
- Versioning, maintenance, and audit history
- Discrepancy identification and resolution

Distribution, vehicle integration, and real-time discovery can be introduced later as operational needs and ecosystem capabilities mature.

## Trip Planning

In the trip-planning scenario, METR regulations are made available to systems that evaluate a planned journey before it begins. A route-planning or fleet-management system can compare candidate routes with applicable regulations, vehicle characteristics, permits, intended movements, and anticipated travel times.

This allows the user or system to identify restrictions in advance, choose a compliant route, estimate operational constraints, or determine whether additional authorization is required. Examples include avoiding roads with vehicle weight or height limits, accounting for hazardous-material restrictions, and selecting routes that comply with time-dependent access regulations.

Trip planning extends the jurisdictional-management scenario by adding distribution and consumption capabilities, but it does not require continuous or real-time connectivity with  mobile devices or vehicles during a journey, thereby greatly reducing the complexity of the deployment.

## Pre-announced Regulations

Pre-announced regulations are regulations that are electronically published and distributed to all users with fresh data before they take effect. This includes most regulations issued by legislative and regulatory authorities (i.e., as opposed to emergent regulations that are typically issued by operational authorities and emergency services).

Because the effective location, conditions, and time period are known beforehand, the regulation can be verified, distributed, and loaded onto a user device or vehicle system using highly reliable communication channels before it becomes relevant to the user or vehicle. The receiving system can then apply the regulation at the appropriate time and place, including when network connectivity is unavailable.

This scenario supports a large percentage of regulations while notifying users that they still need to be prepared to respond to on-site variations (e.g., emergency services, local law enforcement, etc.). Regions allowing this type of deployment should define how authorities are to physically post emergent regulations to the public since they are not contained in the electronically published regulations.

## Emergent Regulations

Emergent regulations are introduced in response to an unplanned or rapidly changing situation. Examples include restrictions associated with a collision, extreme weather, an evacuation, infrastructure damage, or another immediate safety concern.

In this scenario, the interval between creating a regulation and applying it may be very short. METR must support rapid authorization, translation, verification, distribution, and receipt while still preserving the regulation's provenance and validity. Receiving systems can use this information to prioritize assess whether it affects an active trip, notify the user, or adapt system behaviour as appropriate.

Emergent regulation deployment places greater emphasis on timely distribution, freshness, revocation, and discrepancy handling than the earlier scenarios. It may also operate alongside existing traffic-management or emergency-notification mechanisms.

Deploying emergent regulations can be done before or after deploying pre-announced regulations; however, users must always be informed of which types of regulations are available electronically for a location and how to obtain them. For example, a jurisdiction can decide to deploy electronic emergent regulations within a work zone to improve compliance (especially for ADS) while still relying on posted regulations (and ADS databases) for other regulations.

## Regulation Discovery

Regulation discovery enables a specially authorized user or vehicle to identify posted regulations, generate or update a regulation record, and provide the record directly to a regulation system as a draft electronic regulation for further processing. For example, a specially equipped vehicle with can drive routes and identify all existing posted regulations rather than requiring an agency to manually enter this information into a database. Even if this information is already available in a database, the discovery process can be used to update the database with more accurate as-built information (e.g., a more accurate location of where an associated sign is actually posted).

The discovery process is conceptually similar to discrepancy handling, but uses an authorized user or vehicle to obtain the information rather than any METR user device.

Discovery can be deployed in any deployment scenario that includes a METR regulation system.