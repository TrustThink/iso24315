# METR website outline

Outline of published pages, headings, and section summaries.

## Home

**Management of Electronic Transport Regulations (METR):** METR provides geo-specific, trustworthy, timely, authoritative, machine-interpretable transport regulations from jurisdictional entities, aimed at non-technical readers deciding whether METR matters for their priorities.

- **Overview:** METR covers virtually all surface-transport regulations—codes, signs, and markings—for motorized and non-motorized modes, pedestrians, and facilities from roads to plazas, so user systems can receive the regulations they need as automation grows.
- **Adding trustworthiness:** Unlike map databases or camera-based sign reading that can be stale or wrong, METR focuses on a trustworthy delivery pipeline so regulations can safely support higher levels of automated driving.
- **Type of regulations covered:** While titled as traffic regulations, METR is intended to support the trustworthy delivery of rules of the road (as defined in the highway code), regulatory and advisory restrictions, and other information (e.g., warnings and guidance) as established by various regulators. Collectively these are called traffic regulations on this site.
- **Timeliness of regulations:** METR supports both pre-announced regulations available well before they are needed and emergent regulations that reflect recent changes such as flooding or other unplanned events.
- **Discussion:** Invites readers to join the online METR discussion forum at any time.

## Overview

**METR overview:** METR electronically disseminates trustworthy traffic regulations and related advisories to stakeholders and support systems as a system of systems whose reference architecture is defined in ISO 24315-3.

- **Key components of the system of systems:** Describes the regulation, distribution, consumer, and discrepancy-handling systems, how multi-layer authorities feed a collector/distributor, and how consumers obtain needed regulations, check inconsistencies, and report discrepancies under regional guidance.

## Development

**Development approach:** METR development uses systems engineering grounded in stakeholder engagement to elicit user needs.

- **Overview:** Public workshops in 2021 with 47 stakeholders from 13 countries drove Parts 1–4 (Vocabulary, ConOps, SoSR, SysR for the four component systems), with future parts planned for data, location referencing, and cybersecurity, while regional interfaces such as DATEX II continue to evolve.
- **Stakeholders:** WG 19 continues seeking input from regulators, transport users, support providers, and third parties.

## Workshops

**Workshops:** Lists twelve late-2021 public workshop sessions—with slides and chat resolutions—covering operations, structure, lifecycle, conflicts, vehicle needs, campuses, roadwork, micromobility, and deployment, with summary points tracing to the ConOps.

## Overview

**Implementation Guides:** Guides for planners and decision makers on METR deployment configurations, regional frameworks, stakeholder benefits, and usage scenarios, organized by regional framework, rule makers, and the four component systems.

## Regional Guidance

**Regional Guidance:** Introduces METR scope, reference architecture, example deployments, usage scenarios, the regional framework tier model, stakeholder benefits, and a sample regional implementation policy framework.

- **Introduction:** Introduces purpose, audience, background on the ISO 24315 series, and why regional implementation guidance is needed.
    - **Purpose of this document:** Focuses on METR scope, deployment and usage scenarios, regional frameworks, and stakeholder benefits without deep technical implementation detail.
    - **Audience:** Primary readers are planners, decision makers, and fleet managers, with secondary value for IOOs, rule makers, OEMs, service providers, navigation developers, emergency responders, policymakers, legal professionals, and public safety officials.
    - **Background:** Summarizes the ISO 24315 series—Vocabulary, ConOps, SoSR, and SysR—as a framework for trustworthy, machine-interpretable traffic regulations supporting ITS, ADS, and connected vehicles.
    - **Need for Regional Implementation Guidance:** Regional guides keep deployments interoperable across jurisdictions while allowing local customization, avoiding fragmented systems that could harm safety and enforcement.
- **Scope of METR Systems:** METR electronically disseminates authenticated, interoperable, machine-interpretable traffic regulations without dictating regulation content, enhancing standards such as DATEX II, TN-ITS, and TransModel.
- **Reference architecture:** Describes the METR system of systems lifecycle from multi-level regulation definition through regulation-system entry, distribution-system consolidation, consumer-system use, and discrepancy handling, noting that end-user application of regulations is out of scope.
- **Example Deployment Architectures:** Introduces how deployments may vary from the reference architecture, plus placeholders for centralized and distributed rule-making and management patterns.
    - **Overview:** Explains that deployments vary with rule-maker complexity, cross-border needs, and institutional arrangements, and that standardized interfaces still allow hybrid architectures.
    - **Centralized System:** Section reserved; content not yet written.
    - **Distributed Rule-Making System:** Section reserved; content not yet written.
    - **Distributed Regulation Management System:** Section reserved; content not yet written.
    - **Distributed Regulation Management System with Service Discovery:** Section reserved; content not yet written.
- **Usage Scenarios:** Introduces planned scenarios for agency regulation management, pre-announced and emergent vehicle provision, trip planning, and as-built database refinement.
    - **Management of regulations within government agencies (e.g., UK D-TRO project):** Section reserved; content not yet written.
    - **Provision of pre-announced regulations to vehicles (e.g., ISA):** Section reserved; content not yet written.
    - **Provision of emergent regulations to vehicles:** Section reserved; content not yet written.
    - **Regulations for trip planning:** Section reserved; content not yet written.
    - **As-built refinement of database:** Section reserved; content not yet written.
- **Regional Framework:** Describes METR’s three-tier model—global ISO standards, regional refinements for major travel regions, and national/local policy choices—to scale deployment across jurisdictional differences.
    - **Benefits to Various Stakeholders:** States that METR delivers ecosystem value that facilitates AV deployment, mobility efficiency, and safer roadways by bridging regulatory gaps digitally.
- **Sample Regional Implementation Policy Framework:** Introduces prerequisites, regional reference architecture choices, regulation-verification policies, and deployment policy trade-offs for a regional METR rollout.
    - **Prerequisites for Starting a Regional METR Deployment:** Regions need governance, funding, needs assessment, technical infrastructure, adapted legal frameworks, and stakeholder engagement before starting deployment.
    - **Regional Reference Architecture:** A regional blueprint adapts the ISO architecture—especially who operates distribution—weighing government, private, and partnership options for control, innovation, cost, and trust.
    - **Policies for Regulation Verification:** Independent verification increases trust and safety but adds cost and delay, so regions need clear policies that keep regulations accurate without undue disruption.
    - **Policies for Deployment:** Regional policy must balance mandated uniformity for interoperability against local autonomy over whether and which METR regulation categories to deploy.

## Regional Framework

**Sample Regional Implementation Policy Framework:** Introduces a template regional policy framework covering purpose, audience, need for guidance, and prerequisites for starting a METR deployment.

- **Introduction:** Introduces purpose, audience, and the need for regional implementation guidance.
    - **Purpose of Document:** Serves as a customizable template for regional governments to build METR implementation policies and address essential pre-deployment steps.
    - **Audience:** Aimed at regional officials, planners, and policymakers, plus IT/infrastructure implementers and legal advisors on compliance and integration.
    - **Need for Regional Implementation Guidance:** Regional guides keep deployments interoperable across jurisdictions while allowing local customization, avoiding fragmented systems that could harm safety and enforcement.
- **Prerequisites for Starting a Regional METR Deployment:** Before deployment, regions must establish governance, funding, needs assessment, technical infrastructure, adapted legal frameworks, and stakeholder buy-in, then address architecture, verification, and deployment policies.
    - **Regional Reference Architecture:** A regional blueprint adapts the ISO architecture—especially expected distribution systems—weighing government, private, and partnership options for control, availability, privacy, and cost.
    - **Policies for Regulation Verification:** Independent verification increases trust and safety but adds cost and delay, so regions need clear policies that keep regulations accurate without undue disruption.
    - **Policies for Deployment:** Regional policy must balance mandated uniformity for interoperability against local autonomy over whether and which METR regulation categories to deploy.

## Rule Makers

**Guidance for Rule Makers:** Guides public and private rule makers—especially agencies and large campuses—on digitizing regulations, dividing the work, accessing a regional regulation system, and understanding IOO responsibilities and related obligations.

- **Introduction:** Introduces the purpose and audience for rule makers who participate in a larger METR system rather than operating their own.
    - **Purpose of Document:** Helps smaller jurisdictions, campuses, and similar entities convert and integrate local regulations into a centralized METR system for accurate, interoperable representation.
    - **Audience:** Intended for localized rule makers without their own METR systems, plus supporting IT/planners/consultants and regional authorities coordinating interoperable implementation.
- **Regulation Conversion Priority:** Prioritize electronic conversion based on current format, severity, and legislative impact, reusing existing materials such as GIS to maximize benefit while limiting cost and disruption.
- **Inter-related Regulations:** Sequence conversion so foundational definitions and related categories are in place before dependent regulations, avoiding inconsistencies across interrelated regulation sets.
- **Data Quality:** Conform to regulation-system data quality standards and record certification level with the data so converted regulations remain trusted and correctly interpreted.
- **Trustworthy Regulation Sets:** A regulation category is trustworthy only when complete within a defined area, which may be a jurisdictional sub-area under regional policy for phased rollout.
- **Evolution of Regulation Sets:** Plan processes for new, temporary, and emergent regulations so electronic regulation sets stay current as conditions and infrastructure change.
- **Planning for Evolution of the METR Standards:** Anticipate METR standard evolution—such as new vehicle types—when defining regulations so electronic representations remain compatible over time.
- **Operational Impacts to My Organization:** Electronic METR representation encourages electronic regulation creation from the start and may require more structured processes so regulations map cleanly into METR formats.
- **Importance of Connectivity:** Emergent regulations must reach users by implementation time, so reliable end-to-end connectivity—possibly with beacons or redundancy—is essential for safety and efficiency.
- **Migration from Existing Data Sources:** Leverage paper, PDF, signage, GIS, and existing electronic records to migrate into METR accurately and cost-efficiently.
- **Minimum Requirements for Interoperability:** Meet key standards and align with regional policies so local regulations integrate cleanly with the broader METR ecosystem.
- **Data Quality Assurance:** Maintain continuous quality assurance aligned with METR certification levels so electronic regulations stay accurate, reliable, and trusted.
- **Tailoring the Guide and the Standards:** Customize prioritization, data quality, and operational guidance to local conditions so METR implementation remains effective and sustainable.

## Regulation System

**Guidance for METR Regulation System:** Guides larger-jurisdiction deployers on implementing, operating, and maintaining a regulation system, including policies, accounts, resources, data quality, certificates, legal duties, and sample architecture.

- **Introduction:** Introduces purpose and audience for state and local operators of METR regulation systems.
    - **Purpose of Document:** Helps sub-national governments deploy and maintain METR regulation systems that keep traffic regulations available in trustworthy electronic form.
    - **Audience:** Aimed at state/local officials, regulators, IT staff, IOOs, policymakers, and supporting consultants involved in operating electronic traffic regulations.
- **Prerequisites for Deploying a METR Regulation System:** Before deployment, set signing and certification policies, regulation-category priorities, freshness periods, provisioning agreements, optional METR features, supporting-data providers, and related operational policies.
- **Cost Factors:** Budget for connectivity, security, operations and maintenance, information entry, impacts on field services, and certification/verification/compliance without providing specific cost estimates.
- **Benefits of Optional METR Features:** Weighs optional discrepancy reporting, regulation discovery, and independent verification for greater trust and accessibility against added cost and complexity.
- **Data Collection:** Multiple rule makers can enter data into a shared regulation system if they follow Rule Maker Guide accuracy standards and record confidence in metadata.
- **Auditing Capabilities:** Robust auditing tracks changes and verifies accuracy to reduce risk and keep the regulation system secure and trustworthy.
- **Evolution of Regulation Systems:** Design regulation systems for graceful software migration and changing standards so they remain effective as METR matures.
- **Deployment Example with Project-Level Architecture:** Illustrates adapting the ISO reference architecture where a regulation system must interface with parent and peer regulation systems.
- **How to Tailor the Guide and the Standards:** Customize prioritization, data quality, and operational processes to local conditions for an effective, sustainable regulation-system deployment.

## Distribution System

**Guidance for METR Distribution System:** Guides OEMs, navigation providers, NAPs, and similar deployers on implementing and operating a distribution system, including policies, relationships, resources, quality, certificates, duties, and sample architecture.

- **Introduction:** Introduces purpose and audience for entities that distribute METR data.
    - **Purpose of Document:** Equips distribution-system operators with guidance on prerequisites, maintenance, interoperability, and optional features for reliable regulation dissemination.
    - **Audience:** Aimed at administrators, IT staff, planners, regulators, consultants, and policymakers involved in METR distribution systems.
- **What Are the Prerequisites for Deploying a METR Distribution System?:** Requires suitable infrastructure, compatibility with regulation systems, support for intended regulation and vehicle types, and a clear understanding of the target market.
- **How Much Maintenance Is Likely to Be Required for a METR Distribution System?:** Expect ongoing software and hardware upkeep—monitoring, backups, patches, and occasional major upgrades—to stay secure, performant, and aligned with evolving METR standards.
- **What Are the Minimal Requirements for Interoperability?:** Use standardized formats, protocols, and interfaces so the system can process and distribute pre-announced and emergent regulations across regulation centers, peers, and end users.
    - **What Are the Benefits of Including Optional Features?:** Optional discrepancy reporting and regulation discovery can improve accuracy and engagement but add complexity that operators must weigh carefully.
    - **Who Is the Target Market for the Distribution System?:** Serves infrastructure operators, regulators, navigation providers, and vehicle manufacturers, each with distinct needs such as real-time updates or auditing.
        - **Types of Regulations:** Must handle varied regulation types and both pre-announced and emergent regulations, each with different data needs, priorities, and update frequencies.
        - **Types of Vehicles:** Must deliver appropriate regulation sets and formats for passenger, commercial, transit, and autonomous vehicles with differing precision needs.
- **What Is Involved with Managing the Data?:** Covers collecting, storing, validating, securing, and distributing regulation data so users receive accurate, current information under applicable regulations.
    - **How Long Do the Received Regulations Remain Reliable Once They Are Received from the Regulation System?:** Reliability lasts while regulations reflect current regulations; operators should define freshness periods and refresh mechanisms by regulation type.
    - **How Often Should Regulations Be Refreshed for the User?:** Refresh frequency should match regulation dynamics—static regulations less often, dynamic restrictions more often—via clear guidelines and automated updates.
    - **Does the Distribution System Repackage the Data or Forward Data Signed by Regulators?:** Operators choose between repackaging for user needs and forwarding regulator-signed data to preserve integrity, balancing flexibility against complexity and trust.
    - **What Is the Difference Between Pre-Announced and Emergent Regulations and How Does This Affect a Distribution System?:** Pre-announced regulations can be scheduled for reliable delivery, while emergent regulations need near-real-time dissemination; the system must support both.
- **What Auditing Information Needs to Be Captured?:** Audit receipt, processing, distribution, changes, discrepancies, and user interactions to support compliance, troubleshooting, and improvement.
- **Migration from Existing Systems:** Plan data conversion, integration, and user training so migration to a METR distribution system preserves continuity with minimal disruption.
- **Deployment Example with Project-Level Architecture:** Shows interactions among regulation centers, distribution centers, emergent distributors, and end users as a practical deployment pattern.
- **How to Tailor the Guide and the Standards:** Adapt prioritization, data management, and architecture guidance to local conditions for sustainable, reliable distribution.

## Consumer System

**Guidance for METR Consumer System:** Guides developers of vehicle, smartphone, and navigation consumer systems on deployment, operation, policies, quality, certificates, legal duties, and sample architecture.

- **Introduction:** Introduces purpose and audience for entities that consume METR data.
    - **Purpose of Document:** Helps navigation systems, vehicles, and similar consumers integrate electronic regulations, covering prerequisites, regulation types, maintenance, data use, and discrepancy handling.
    - **Audience:** Aimed at developers, operators, OEMs, agencies, infrastructure managers, consultants, and legal experts integrating or supporting METR consumer systems.
- **What Are the Prerequisites for Deploying a METR Consumer System?:** Need infrastructure to receive and act on pre-announced and emergent regulations in real time, interoperability with METR, and privacy/security protections.
- **What Types of Electronic Regulations Do I Need?:** Required regulation categories depend on the use case and may include speed, right-of-way, parking, lane use, temporary controls, and vehicle-specific regulations.
- **How Do I Determine If the Electronic Regulations That I Need Are Available Within an Area?:** Use regulation discovery against local or central repositories and coordinate with authorities or distribution centers to confirm published coverage.
- **Should I Implement Any Optional Features?:** Optional discrepancy reporting, discovery, and automated updates improve responsiveness and accuracy but add complexity that must match capabilities.
- **How Stable Is the Technology? How Much Maintenance Is Likely to Be Required for a METR Consumer System?:** Technology is generally stable but needs regular software, security, and hardware maintenance, with more effort if optional real-time features are used and as standards evolve.
- **What Are the Minimal Requirements for Interoperability?:** Comply with standard formats, protocols, and APIs so regulations from multiple sources are interpreted consistently across the METR ecosystem.
- **What Are the Benefits of Including Optional Features?:** Automatic updates, discrepancy reporting, and analysis tools improve accuracy and user experience enough that benefits often outweigh added maintenance.
- **What Is Involved with Using the Data?:** Receive, parse, and apply location- and condition-relevant regulations, with caching for connectivity gaps, plus responsibilities for multi-source management, interpretation, discrepancy reporting, and use.
    - **What Are the Responsibilities for Managing Multiple Sources of Data?:** Aggregate and reconcile regulations from centralized pre-announced sources and remote/emergent sources such as beacons, prioritizing urgent updates without compliance gaps.
    - **What Are the Responsibilities for Interpreting the Data?:** Determine which regulations apply under current conditions, reconcile conflicts, prioritize emergent regulations, present actionable information, and support discrepancy reporting.
    - **What Are the Policies for Reporting Discrepancies?:** Define how discrepancies are categorized, prioritized, validated, and timed for resolution before forwarding to the appropriate regulation system.
        - **What Steps Are Required to Validate Discrepancies Prior to Reporting Them?:** Validate accuracy and novelty—via automated and/or manual review—before submitting a discrepancy to the relevant regulation system.
        - **What Are the Time Requirements for Processing Reported Discrepancies? What Happens If There Is No Connectivity?:** Process critical discrepancies quickly; if offline, cache reports and send them when connectivity returns under clear processing guidelines.
    - **What Responsibilities Exist for Using Received Data?:** Apply received regulations by location, time, and conditions; keep data available through outages; and address discrepancies promptly.
- **What Auditing Information Needs to Be Captured?:** Record receipt, processing, application, and discrepancy handling for troubleshooting, compliance, and improvement.
- **Migration from Existing Systems:** Plan mapping, integration, training, and accurate transfer of legacy regulation data so migration minimizes disruption and unresolved discrepancies.
- **Deployment Example with Project-Level Architecture:** Illustrates a consumer-system deployment interacting with pre-announced and emergent distribution sources and vehicle sensors.
- **How to tailor the guide and the standards:** Explains revising a master guide at regional, national, and local levels to fit political, regulatory, administrative, and financial realities.

## Discrepancy Handling System

**Guidance for METR Discrepancy Handling System:** Guides jurisdictions, OEMs, and map providers on deploying and operating discrepancy handling, including policies, relationships, resources, quality, certificates, duties, and sample architecture.

- **Introduction:** Introduces purpose and audience for entities that identify, report, and resolve regulatory discrepancies in METR.
    - **Purpose of Document:** Guides deployment of discrepancy handling covering prerequisites, maintenance, data management, and policies for accurate regulation implementation.
    - **Audience:** Aimed at administrators, regulators, rule makers, policymakers, legal experts, and consultants supporting discrepancy management.
- **What Are the Prerequisites for Deploying a METR Discrepancy Handling System?:** Need real-time collection infrastructure, secure links to other METR systems, clear identification/validation/reporting policies, and integration with diverse data sources.
- **How Much Maintenance Is Likely to Be Required for a METR Discrepancy Handling System?:** Plan for software updates, security patches, hardware upkeep, monitoring, testing, and eventual upgrades as data volumes grow.
- **What Are the Minimal Requirements for Interoperability?:** Use standard formats, protocols, and APIs so discrepancies can be exchanged with regulation systems and peer discrepancy handlers across jurisdictions.
    - **What Are the Benefits of Including Optional Features?:** Optional automation, notifications, and richer reporting can speed resolution and accuracy for operators, regulators, and service providers.
- **What Is Involved with Managing the Data?:** Collect, validate, store, and process reports under quality, governance, privacy, and security controls before routing issues to authorities.
    - **What Are the Policies for Handling Received Discrepancies?:** Define severity-based prioritization and review workflows so discrepancies are processed consistently and in regulatory compliance.
    - **What Steps Are Required to Validate the Discrepancies Prior to Reporting Them to a Regulation System?:** Verify accuracy, relevance, and novelty—automatically and/or manually—before submitting a discrepancy to the appropriate regulation system.
    - **What Are the Time Requirements for Processing Reported Discrepancies?:** Set severity-based timelines so safety-critical issues are handled quickly while less urgent items allow deeper review.
    - **Is There a Difference When Reporting to Another Discrepancy Handling System?:** Peer reporting may need reformatting, protocol alignment, and cross-jurisdiction coordination when issues span multiple systems.
- **What Auditing Information Needs to Be Captured?:** Track reporting, processing, resolution, responsible parties, and data changes for compliance and continuous improvement.
- **Migration from Existing Systems:** Transfer and map legacy discrepancy data, integrate with regulation systems, and train staff so management continues without disruption.
- **Deployment Example with Project-Level Architecture:** Shows scalable interactions among regulation centers, peer discrepancy handlers, and users across jurisdictions or domains.
- **How to Tailor the Guide and the Standards:** Customize architecture, discrepancy priorities, and security to local conditions for an effective, sustainable deployment.

## Documentation

**Documentation:** ISO 24315 METR materials come from an open-source requirements repository; linked items and open comments appear on the following pages.


## Introduction

**24315 METR-Intro: Intro:** Provides interactive traceability links and open discussions for the METR Intro document; full requirement text lives in the standard.

## Vocab

**24315 METR-Vocab: Vocabulary:** Provides interactive vocabulary entries with links and open discussions for METR terms defined in the standard.

## ConOps

**24315 METR-ConOps: Operational Concept (ConOps):** Provides interactive traceability for the Operational Concept (ConOps), linking user needs and discussions to the published standard text.

## SoSR

**24315 METR-SoSR: System of Systems Requirements and Architecture:** Provides interactive traceability for System of Systems Requirements and Architecture (SoSR) items defined in the standard.

## SysR

**24315 METR-SysR: System-Level Requirements:** Provides interactive traceability for System-Level Requirements (SysR) covering the four METR component systems.

## MDR

**24315 METR-MDR: METR Data Requirements:** Provides interactive traceability for METR Data Requirements (MDR) items defined in the standard.

## Workshop Points

**24315 METR-SP: Summary Points:** Provides interactive workshop summary points with links and discussions that trace to the ConOps.

## Notes

**24315 METR-N: Notes:** Provides interactive notes with links and open discussions supporting the METR requirements materials.

## Frequently Asked Questions

**Frequently Asked Questions:** Introduces FAQ topics on benefits of electronic regulations, METR costs, and stakeholder-specific challenges.

- **What are the benefits of making electronic regulations available?:** METR improves safety and compliance for road users, traffic management for IOOs, faster consistent updates for rule makers, OEM integration for ADS, and quicker adaptation for service providers and related stakeholders.
- **What are the costs associated with METR?:** Deployments must budget for regulation and distribution systems, emergent-regulation infrastructure, user devices, discrepancy handling, connectivity, security, and public awareness.
- **What challenges do different stakeholders face?:** Each group faces distinct issues—privacy, integration cost, flexibility, data burden, vehicle trustworthiness, service continuity, usability, and emergency response—plus liability considerations across the ecosystem.
