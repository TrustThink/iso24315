# Physical View

<div class="diagram-light-bg" markdown="0">
--8<-- "images/physical-view.svg"
</div>

The diagram is the **physical view** of the METR system of systems with descriptions of each component provided below. The diagram identifies the major actors within a METR deployment and the relationships between them.

---

## Traditional Regulatory Components

Prior to electronic regulations, the traditional regulatory process consisted of a rule maker, a regulation implementation agent, and a maintenance & construction management centre. These components are still present in the METR system, but are supplemented with the METR system of systems.

### Rule Maker
The rule maker is the originating actor in the METR chain of trust. Rule makers are responsible for defining the regulations that govern vehicle behaviour within a jurisdiction. Rule makers include legislative bodies, road authorities, road operators, emergency response personnel, and campus authorities. The (legal) regulations that they define are provided to the METR translation agent and to the implementation agent. 

### Regulation Implementation Agent

The regulation implementation agent is a person who takes legal regulations from the rule maker and handles the operational work of putting them into effect — for example, coordinating physical signage, infrastructure changes, or system configuration required to enforce a regulation in the real world. The implementation agent is an employee of the Maintenance & Construction Management Centre, which is a centre that installs, maintains, and reports status of traffic control devices. The implementation work is managed by the the Maintenance & Construction Management Centre.

Implementing a regulation does not necessarily mean that it is active (e.g., a speed limit for a school zone might only be `active` a few hours each day).

### Maintenance & Construction Management Centre (MCMC)
Centre that manages the installation, maintenance, and status of traffic control devices. It feeds **TCD status** into METR (what was posted, changed, or removed) so electronic data can be checked against the roadside. Also receives METR information so crews know what should be on the ground.

## METR Translation Components

The regulations issued by a rule maker need to be entered into the METR regulation system, verified and signed. The METR translation components are responsible for this process.

### METR Translation Agent

The METR translation agent a person who accepts regulations from rule makers and translates them into the structured, machine-readable format, called the **electronic regulation**, used throughout the rest of the METR system. The translation agent works closely with the METR verification agent to verify each electronic regulation. The translation agent records the electronic regulation in the METR regulation system and coordinates with the METR verification agent and METR signing agent to ensure that the regulation is verified and signed. 

### METR Verification Agent

The METR verification agent is a person who works alongside the METR translation agent to check that translated, electronic regulations accurately and completely reflect the legal regulation as issued by the rule maker. This is a quality-assurance and validation checkpoint: it catches translation errors, ambiguous encodings, or inconsistencies before a regulation is allowed to progress further into the system. The bidirectional link to the translation agent indicates that this can be an iterative review process.

### METR Signing Agent

The METR signing agent is a person who is authorized to electronically sign the electronic regulation on behalf of the regulation system. Ideally, the signing agent is a direct representative of the rule maker. This establishes a chain of authenticity: any regulation or dataset a vehicle receives can be traced back to the non-repudiable source, protecting the system against tampering or spoofed regulatory content.

## METR System of Systems

The METR system of systems is a collection of systems that work together to implement the METR regulations. It includes the METR regulation system, the METR distribution system, the METR consumer system, and the METR discrepancy handling system.

### METR Regulation System

The METR Regulation System is the authoritative core of the METR System of systems boundary. It stores the electronic regulations as entered by the METR translation agent, interacts with the METR verification and signing agents, and provides verified, signed regulations to the METR distribution system for delivery to vehicles. It also maintains a bidirectional relationship with the METR discrepancy handling system, so that conflicts, exceptions, or reported inconsistencies in electronic regulations can be fed back for correction and re-issuance. In effect, this is the control-plane component that governs what regulatory content is considered valid at any given time.

### METR Distribution System

The METR distribution system is responsible for providing vehicles with the complete relevant set of signed, verified regulations as provided by relevant METR regulation systems (often from multiple jurisdictions). When regulations are known well in advance (i.e., **pre-announced regulations**), they are distributed by a centralized METR distribution system; regulations that arise with short notice  (i.e., **emergent regulations**)can be distributed by centralized, field-based (roadside), or vehicle-based METR distribution systems. METR distribution systems communicate directly with the METR consumer system on the vehicle side, pushing regulation updates and pulling acknowledgments or status information as needed.

### METR Consumer System

The METR consumer system is the vehicle-side component that receives regulatory data provided by the METR distribution system. It lives within the METR user device as it is part of the onboard hardware/software stack rather than back-office infrastructure. It provides local storage of electronic regulations to ensure seamless operation when when their is no connectivity and passes the regulations to the METR adapter system as needed. The METR consumer system is also responsible for reporting anomalies to the METR discrepancy handling system when regulations appear to be inconsistent. The inconsistencies can be detected by the consumer system itself (e.g., two inconsistent electronic regulations) or by the adaptor system (e.g., a conflict with an observed physical sign).

### METR Discrepancy Handling System

The METR discrepancy handling system captures and manages conflicts or inconsistencies reported by METR consumer systems (e.g., mismatches between an electronic regulation and a physical sign). It maintains a two-way link with the METR Regulation System so that identified discrepancies can trigger corrections upstream, and it connects to the METR Consumer System so that field-reported issues (e.g., from a vehicle encountering an unexpected condition) can enter the resolution pipeline.

## METR User Device (container)

The METR user device is a physical host for the METR consumer system, which is a part of the METR system of systems and the METR adapter system.

### METR Adapter System

The METR adapter system sits between the METR consumer system and the end METR user, determining which electronic regulations are currently active  (e.g., based on current supporting data) and relevant to the current situation (e.g., based on the vehicle's location, speed, and parameters set by the user). It then presents these regulations to the user in a form that the user can efficiently use. 

## Supporting Data Provider

The supporting data provider supplies auxiliary field, centre, and vehicle data that determines whether a regulation is currently active. For example, some regulations are only active during defined times, road conditions, weather conditions, or other contextual conditions. Supporting data allows vehicles to correctly interpret conditions and apply METR regulations.

## METR User

The METR user represents a transport (or ancillary) user who has a need to be aware of applicable regulations. This includes a human operator of a vehicle, an automated driving system, a pedestrian mobility device, a navigation system, a fleet management system, etc. This is the point at which the entire pipeline — regulation creation, translation, verification, signing, distribution, and adaptation — culminates in a real-world action or decision.

---

## Interfaces between components

In some cases, interfaces are non-electronic or can be custom to a deployment; in other cases, they electronic components need to be able to share information in a standardized interoperable manner. The following interfaces are considered priority for standardization:

### IF 1: Regulation System -> Distribution System <a id="if-1"></a>

Distribution systems will typically need to collect regulations from multiple regulation systems. To facilitate integration, each region deploying METR should standardize the interface been regulation systems and distribution systems. 

### IF 2: Distribution System -> Consumer System <a id="if-2"></a>

Distribution systems are intended to provide regulations to many consumer systems. To properly interoperate, each consumer system will need to support the same interface definition used by the distribution system. This could be a regional standard or could be a custom interface for a defined by a distribution system (e.g., especially if the distribution system is a private service). Each region should consider whether this interface needs to be standardized.

### IF 3: Consumer System -> Discrepancy Handling System <a id="if-3"></a>

Consumer systems are responsible for reporting anomalies to the discrepancy handling system. To properly interoperate, each consumer system will need to support the interface offered by the discrepancy handling system. This could be a regional standard or could be a custom interface (e.g., a private discrepancy handling system that acts as a front end for another system). Each region should consider whether this interface needs to be standardized.

### IF 4: Discrepancy Handling System -> Regulation System <a id="if-4"></a>

The discrepancy handling system is responsible for reporting anomalies to the regulation system. To properly interoperate, the regulation system will need to support the interface offered by the discrepancy handling system. To facilitate integration, each region deploying METR should standardize the interface been regulation systems and distribution systems.