# Roadway Environment

METR distributes trustworthy electronic rules and regulations, but those regulations still have to coexist with the physical roadway. Signs, pavement markings, signals, gates, and other traffic control devices (TCDs) remain the conventional way many regulations are publicized and enforced. The roadway environment is therefore not outside METR — it is one of the main sources of truth that electronic regulations must stay aligned with, and one of the main places where conflicts are discovered.

This page summarizes the roadway-related issues that matter for METR deployments: how physical regulations are posted and perceived, how they diverge from electronic records, and how METR uses field feedback to keep both worlds consistent.

## Physical Regulations Still Matter

Before METR, the regulatory chain typically ran from a [rule maker](physical-view.md#rule-maker) through a [regulation implementation agent](physical-view.md#regulation-implementation-agent) and a [maintenance and construction management centre](physical-view.md#maintenance-construction-management-centre-mcmc) that installs and maintains TCDs. That chain does not disappear when electronic regulations are introduced.

METR adds a parallel electronic path — translate, verify, approve, distribute — but users still encounter the roadway as posted and as-built. For human drivers, conventional TCDs remain legally and practically important. For automated driving and driver-support systems, electronic METR data is intended to reduce dependence on brittle camera interpretation of signs, yet systems still need a way to detect when the roadside and the electronic catalogue disagree.

In short: METR does not replace the roadway environment; it must remain consistent with it.

## Posted regulations, unposted rules, and observability

METR practice distinguishes several ways R&R can exist for users:

- **Unposted rules** are publicized primarily through media outlets, recorded in the highway code, and taught as a part of driver's education (legislative **rules of the road**).
- **Posted regulations** are publicized with conventional TCDs — signs, markings, signals, gates, and similar devices. Posted regulations can further be subdivided into:
  - **Observable regulations** are posted and can actually be perceived by those affected.
  - **Unobservable regulations** are posted but cannot be reliably perceived — for example because a sign is damaged, faded, covered by snow or foliage, obstructed by another vehicle, vandalized, or removed.

These distinctions matter for METR because discrepancy reports often originate from what a user system *sees* or fails to see. A blocked sign can generate a false conflict report even when the electronic regulation is correct. Conversely, an electronic record that does not match a clearly posted and observable TCD is a real discrepancy that needs investigation.

## Traffic Control Devices as Field Implementation

TCDs are the physical implementation of many posted regulations. Typical categories include:

- regulatory and advisory signs
- pavement markings (lane lines, stop bars, exclusive-use markings, and similar)
- traffic signals and variable-message signs
- gates, barriers, and other devices that convey access or lane-use constraints

Implementation is not the same as activation. A school-zone speed limit may be installed weeks before it becomes active for defined hours. A sign can be installed with a cover to prevent activation of the regulation until a later date. METR electronic records need to reflect both what has been authorized and what is currently in force, including scheduled and condition-dependent activation.

The [Maintenance & Construction Management Centre (MCMC)](physical-view.md#maintenance-construction-management-centre-mcmc) is the operational actor that installs, maintains, and reports TCD status. In the METR architecture, MCMC status feeds help electronic systems know what was posted, changed, or removed so catalogues can be checked against the roadside.

## Why the Roadway and Electronic Catalogue Drift Apart

Several recurring roadway issues create or amplify METR-relevant discrepancies:

### Damage, obstruction, and degradation

Posted devices fail in ordinary ways: knock-downs, weathering, graffiti, snow accumulation, temporary visual obstruction, and power loss for powered devices. Any of these can make a posted regulation unobservable without changing the legal regulation or the electronic record. METR allows the MCMC to be alerted to situations that need their attention; although in some cases (e.g., snow accumulation) the situation can self-correct with time.

### Installation lag and transition periods

When a regulation is enacted or rescinded, there is often a transition while crews install, uncover, cover, or remove TCDs. During that window, electronic and physical representations can legitimately differ unless policies define which source governs and how METR records the transition. Regional and local policies should define which source governs and how the two worlds are reconciled in a timely manner.

### As-built location differences

Legal regulations are often defined relative to roadway features (an intersection, a school zone boundary, a distance from a landmark). Electronic systems need precise, machine-usable location references (e.g., geographic coordinates) that can be used to accurately locate the regulation in the field and across different mapping systems. However, even with an accurate representation of the location, there can be differences between the location defined in a legal regulation and the as-built position of an associated sign or marking. To overcome this issue METR allows regulations to be associated with both an official location and a as-built location. In addition, METR supports [regulation discovery](deployment-scenarios.md#regulation-discovery) to enable a level of collecting as-built locations in an automated way.

### Conflicting or incomplete physical posting

The roadway itself can be inconsistent: successive signs that disagree without an obvious reason, markings that conflict with nearby signs, temporary work-zone devices that overlay permanent posting, or intended coverings that inadvertently fall off of a sign. METR allows users to report conflicts among physical regulations, among electronic regulations, and between electronic and physical regulations as discrepancies, which can then be investigated and resolved.

### Temporary and emergent field conditions

Collisions, weather events, evacuations, infrastructure damage, and temporary work create short-notice constraints. Some are posted with temporary TCDs; some are conveyed by officers or responders in the field; some may be issued electronically as [emergent regulations](deployment-scenarios.md#emergent-regulations). Users need clarity about which categories are available electronically for a given location and how physical posting is still used for the rest. This is especially important for ADSs as it can impact decisions about whether they are within a valid operational design domain.

## Keeping Electronic METR Synchronized with the Physical Infrastructure

The regulation system should provide for independent verification of electronic regulations prior to their distribution.
However, METR allows for continued synchronization between the electronic and physical worlds through two primary mechanisms:

1. **TCD status from field operations** — MCMC and related field systems notify METR when devices are newly installed, changed, or removed, supporting verification that electronic records match what was implemented.
2. **Discrepancy reporting from users** — METR consumer and adapter systems can report suspected conflicts between electronic regulations and observed TCDs (or between TCDs themselves), typically with location, time, type, and optional supporting evidence such as imagery or sensor readings. See the [functional view](functional-view.md#detecting-and-reporting-discrepancies) and [discrepancy handling](key-components.md) descriptions.

## Supporting Conditional Regulations

Many regulations are only active under specific conditions: time of day, day of week, weather, road surface state, vehicle occupancy, or other contextual factors. Determining whether such a regulation applies is not purely a catalogue lookup — it depends on [supporting data](physical-view.md#supporting-data-provider) sensed or received from the vehicle, the roadway, other related systems, or a combination of these.

METR distributes the regulation along with its associated conditions. Interpreting current conditions — for example, whether precipitation is occurring at a rate that triggers a weather-dependent speed limit — remains a responsibility of the user environment, using vehicle sensors, infrastructure feeds, other supporting-data providers, or the user's judgement. Poor or ambiguous condition data is therefore a roadway-environment issue with direct METR impact: the electronic regulation may be correct, yet the user system may apply it incorrectly.

## Mixed Environments During Rollout

METR will not be available everywhere, for every vehicle class,for every regulation category, at the same time. Deployments are expected to be [incremental](deployment-scenarios.md). That creates mixed operating environments in which different areas can:

- publish electronic pre-announced regulations while not yet providing electronic coverage for emergent regulations;
- provide electronic emergent (e.g., work-zone) regulations while not yet providing electronic pre-announced regulations; 
- do not provide any electronic regulations; 
- offer some electronic regulations but do not offer seamless connectivity for user devices; and
- offer electronic regulations for some types (e.g., speed limits) but not others (e.g., parking restrictions).

To promote better interoperability and regional behaviour and expectations, regional policy needs to provide guidance on which regulation categories should be considered for prioritization. In addition, each defined area needs to electronically indicate which regulation categories are electronically trustworthy (and complete) for the area and the level of authority associated with the electronic regulation (i.e., is it legally binding or just informational). Without that clarity, both human drivers and automated systems can place unwarranted trust in incomplete electronic data — or discard useful electronic data because the roadside still looks primary.

