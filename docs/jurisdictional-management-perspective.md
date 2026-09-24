# Jurisdictional Management Perspective

The jurisdictional management perspective represents the point of view of an entity that hosts — and is accountable for — one or more of the back-office METR components that make electronic regulations available within a geographic area. In practice, that often means operating a **regulation system**, a **discrepancy handling system**, all or part of a **distribution system** (e.g., it might just perform the **collection function** and serve as a single access point to multiple regulation systems), or a combination of these.

This role is more than IT system ownership. The jurisdictional manager defines who may act as a rule maker on the hosted platform, how far each rule maker’s authority extends, how credentials and signing rights are issued and revoked, and how the hosted systems stay aligned with regional interoperability policies. Smaller jurisdictions — including campuses, toll operators, business parks, and even a mom-and-pop store with a single enforceable parking regulation — typically will not run their own METR platforms. They become recognized rule makers on a parent jurisdiction’s system instead.

For the technical deployment details of each component, see the [regulation system](regulation-system-perspective.md), [discrepancy handling](discrepancy-handling-perspective.md), and [distribution system](distribution-perspective.md) guides. This page focuses on the governance and operational perspective of the host.

## Who This Perspective Is For

Typical jurisdictional managers include:

- state, provincial, county, or large municipal transportation agencies
- metropolitan or multi-jurisdiction partnerships that run a shared METR platform
- road operators that also host regulation or collection services for their network and neighbouring entities
- public–private arrangements where a public authority remains accountable while operations are contracted out

The common factor is accountability for a hosted METR service used by multiple rule makers and relied on by downstream distributors and users.

## Why Jurisdictional Hosting Matters

METR is a [system of systems](system-of-systems.md). Regulation content originates from many legal authorities, but users need a coherent, trustworthy catalogue. If every small rule maker had to build, secure, and operate its own regulation system, METR would not scale.

Jurisdictional hosting concentrates platform, security, and interface responsibilities in organizations that can sustain them, while still allowing local authorities to define the regulations that apply on facilities they control. Benefits include:

- **Lower barrier to entry** for small rule makers that only need to enter and maintain their regulations
- **Consistent data quality, signing, and audit practices** across many rule makers
- **A clearer trust chain** for distributors and consumer systems collecting regulations for a trip
- **Shared discrepancy and collection services** that would be impractical for each small entity to operate alone
- **Incremental rollout** — a jurisdiction can begin with internal regulation management and later add collection, external distribution, or discrepancy handling ([deployment scenarios](deployment-scenarios.md))

## Scope of What a Jurisdictional Manager May Host

A jurisdictional manager may host one component or several. Common patterns include:

| Hosted capability | Typical purpose |
| --- | --- |
| **Regulation system** | Store, verify, sign, version, and publish electronic regulations for the manager’s own regulations and for recognized subordinate rule makers |
| **Collection (distribution)** | Gather regulations from the local regulation system and, where required, from peer or parent systems so downstream distributors or users can obtain a more complete set of regulations in an efficient manner |
| **Discrepancy handling** | Receive field and system reports, consolidate and validate them, and route confirmed issues to the responsible regulation system or rule maker |
| **Combined platform** | Operate regulation + discrepancy handling, or regulation + collection, under one organizational umbrella with shared identity and security controls |

Not every jurisdictional manager will host everything. Regional policy can assign collection or discrepancy handling to another entity. What the jurisdictional manager should do is make those relationships explicit: which systems it operates, which it depends on, and how rule makers and users discover them.

## Recognizing Smaller Jurisdictions as Rule Makers

A core complexity of this job is deciding **who is allowed to define which regulations where**.

The jurisdictional manager defines **recognized rule makers**, each with a scoped authority: geographic extent, regulation categories, and any limits on temporary or emergent regulations.

### Nested and neighbouring authorities

METR must accommodate real geography and governance:

- smaller governmental areas contained inside a parent jurisdiction (towns within a county; campuses within a city)
- private or semi-private campuses whose transport regulations apply on facilities they manage
- non-contiguous “islands” of authority
- higher-authority roads that pass through a lower-authority area
- neighbouring jurisdictions that prefer to use a nearby parent platform rather than stand up their own

### Multiple rule makers in a single jurisdiction

A single jurisdiction can have multiple rule makers, each with a different scope. This is common in areas where different types of regulations are published by different entities. For example, a municipality can assign a road authority to define speed limits, a city manager to define parking regulations, and its emergency response teams to define emergency regulations.

In this case, the jurisdictional manager needs to record the scope of each rule maker and how they interact with each other. This can be done by recording the geographic extent of the jurisdictional entity that they represent and the types of regulations that they are allowed to issue.

### From considerable areas to mom-and-pop stores

Recognition should scale with risk and responsibility. Examples:

- A municipality within a large metropolitan area can have broad rights to publish any type of regulation.
- A university or airport can have rights to publish campus speed limits, access restrictions, and kerbside regulations.
- A shopping centre can have rights limited to its parking facilities.
- A small store can register a single accessible parking space or a private driveway restriction.

In all cases, the small entity should not need its own METR regulation system. It needs:

1. a process to become a recognized rule maker
2. credentials scoped to its authority
3. tools or services to enter, update, and retire its regulations
4. clear expectations for data quality and completeness within its defined area
5. a process that allows the migration of responsibility (e.g., in the case of the property being sold or transferred to a new owner)

The [rule makers guide](rule-maker-perspective.md) addresses how those entities prepare and enter data. The jurisdictional manager owns the onboarding, scoping, and oversight policies that make that participation safe.

### Defined areas and trustworthy completeness

Before a regulation category is advertised as electronically trustworthy in an area, the catalogue for that category must be necessary and sufficient for users. Jurisdictional managers should support **defined areas** so completeness can be claimed in phases — for example, speed limits on a corridor first, parking later — so that subordinate rule makers can declare completeness only within their scoped facilities.

## Credentials and Security Management

Because hosted systems speak with legal and safety consequence, identity and cryptographic controls are central to jurisdictional management.

### Organizational identity and onboarding

Establish a formal process to:

- verify that an applicant is a legitimate authority for the claimed facilities or regulation types
- record legal basis and contact points for escalation
- assign organizational identifiers used in audit and provenance metadata
- approve, suspend, or revoke recognition when ownership or responsibility changes

Mom-and-pop and campus onboarding will be lighter-weight than onboarding another public agency, but it must still be deliberate: an unrecognized party must not be able to publish regulations that appear authoritative to vehicles and navigation systems.

### User accounts and role separation

Within each recognized organization, separate duties such as:

- translation / data entry
- verification
- approval / signing
- administration (user and certificate management)
- read-only audit or oversight

Least privilege reduces the chance that a single compromised account can inject or alter signed regulations unnoticed.

### Certificates, signing rights, and trust

Regulation trustworthiness depends on signing and certification practices. Jurisdictional managers should define:

- which roles may sign which regulation categories and confidence levels
- how signing keys and certificates are issued, stored, rotated, and revoked
- whether subordinate rule makers sign as themselves, or whether the parent jurisdiction countersigns or co-signs under defined policies
- how certificate status is published so distributors and consumer systems can validate signatures over time

Digital signatures should ideally indicate the entity legally responsible for the regulation, even when the regulation is hosted on a parent platform.

### Scope enforcement in the platform

Credentials are not enough by themselves. The hosted regulation system should enforce authorization in software and workflow:

- geographic and categorical limits for each rule maker
- rejection or quarantine of out-of-scope submissions
- mandatory metadata for confidence / certification level
- retention of who entered, verified, and signed each change

### Discrepancy and collection credentials

If the jurisdiction also hosts discrepancy handling or collection:

- consumer systems and partner distributors need authenticated channels to submit reports or retrieve catalogues
- peer regulation systems need mutual authentication for collection and hand-off
- operators need credentials to investigate reports without gaining unnecessary rights to alter regulations

Security design should assume that partners and devices are independently operated and upgraded systems within the larger ([system of systems](system-of-systems.md)).

### Operational security responsibilities

Ongoing duties typically include access reviews, key ceremony and HSM practices where used, logging and non-repudiation, incident response for credential compromise, and alignment with regional cybersecurity profiles. Auditing must preserve enough history to reconstruct what was published, by whom, under which authority, and when.

## Responsibilities of Jurisdictional Management

In the METR context, jurisdictional managers are generally responsible for:

1. **Hosting and sustaining** the chosen back-office components at an acceptable availability and security level
2. **Rule-maker governance** — recognition, scoping, credentials, training expectations, and revocation
3. **Policy choices** that the platform must implement — signing regulations, freshness periods, regulation-category priorities, optional features such as discovery or discrepancy linkage ([regulation system prerequisites](regulation-system-perspective.md#prerequisites-for-deploying-a-metr-regulation-system))
4. **Interface commitments** to parent, peer, and distribution systems required by regional interoperability policy
5. **Completeness signalling** — ensuring defined areas correctly advertise which electronic regulation categories are trustworthy
6. **Discrepancy closure** — ensuring confirmed issues reach the responsible rule maker or field organization and that electronic or physical corrections are completed
7. **Legal and operational accountability** for the service, including records that support investigation and non-repudiation

Where operations are outsourced, the public or lead authority should still retain policy control over recognition of rule makers and over cryptographic trust decisions.

## Complexities Unique to This Role

Several issues are easy to underestimate:

- **Authority conflicts** — overlapping claims between city, campus, and private property, or between local regulations and higher-authority roads
- **Onboarding volume** — many small rule makers with narrow scopes, each needing identity proof and credential lifecycle management
- **Uneven maturity** — some rule makers digitize quickly; others lag, affecting completeness claims for shared corridors
- **Cross-border trips** — collection relationships with neighbouring jurisdictions so users are not left with gaps at boundaries
- **Emergent regulations** — rapid authorization paths that remain auditable under emergency or work-zone conditions
- **Shared liability perceptions** — hosting another entity’s regulations does not erase the need for clear provenance of legal responsibility

## Relationship to Other Perspectives

- **[Regional body](perspectives.md)** — sets interoperability policies that the jurisdictional manager implements
- **[Rule maker](perspectives.md)** — uses the hosted platform; does not necessarily operate it
- **[Road operator](perspectives.md)** — may be both rule maker and jurisdictional host, and links TCD status to electronic records
- **[System management](perspectives.md)** — day-to-day build/operate/maintain practices for whichever components are hosted

## Related Pages

- [Key components](key-components.md)
- [Physical view](physical-view.md)
- [System of systems](system-of-systems.md)
- [Regulation system guidance](regulation-system-perspective.md)
- [Rule makers guidance](rule-maker-perspective.md)
- [Discrepancy handling guidance](discrepancy-handling-perspective.md)
- [Distribution system guidance](distribution-perspective.md)
- [Deployment scenarios](deployment-scenarios.md)
