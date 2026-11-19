# The METR Solution

<div class="draft4-watermark" aria-hidden="true"></div>

METR defines a complete, end-to-end (i.e., from rule-maker to user) approach to managing and distributing R&amp;Rs. METR's holistic approach enables the secure electronic dissemination of trustworthy R&amp;Rs, ensuring that all stakeholders and their driving and navigation support systems have access to current R&amp;Rs. The system can be used to disseminate all [types of regulations](index.md#scope-of-rr-covered-by-metr), including regulatory, advisory, and guidance information, as well as rules of the road, as defined in the highway code. The technology will assist in both improving the quality of information provided to human drivers as well as enabling better trust of Automated Driving Systems (ADS).

Enabling the trustworthy distribution of electronic regulations results in a complex system of systems, where the components are acquired and managed by independent entities but are still interoperable. The reference architecture for METR is defined in ISO 24315-3 and summarized in the [physical view](physical-view.md).

## Characteristics of the METR Solution

### Accommodates Varied User Needs

Transport users have different needs for each trip that they take. For example, different users can have different needs based on:

1. The type of vehicle being operated (e.g., passenger car, heavy goods, or public-area mobile robot)
2. The origin and destination of a trip (e.g., local trip vs. cross-country)
3. The way in which the information is being used (e.g., pre-trip planning, driver information for speed limits, Level 4 ADS)

Each user needs access to the relevant regulations in a trustworthy manner although the agencies who sign and issue these regulations generally group them in different ways. As a result, the issued regulations will typically need to be repackaged before distribution to the end user. The METR architecture allows for this repackaging while preserving a trust chain back to the originator of the regulation.

### Supports a Complex R&R Environment

**Rules and regulations (R&R)** are defined by multiple layers of government and different departments within each layer. For example, **rules** may be enacted in legislation (highway/road code), while **regulations** may be established by a regional (multi-national) government, national government, state or provincial government, county government, city government, and even more local entities (e.g., borough, subdivision, or property/campus owner). Further, each of these entities can authorize multiple representatives to issue regulations, often with specific scopes. The following are some typical examples of how authorities can be divided within each level:

- the legislative arm can retain the authority to define rules and any regulation it wishes
- traffic engineers define permanent regulations (e.g., stop signs, speed limits)
- road operators (e.g., operators of traffic management systems) implement specific types of regulations based on schedules and current conditions (e.g., dynamic speed limits, lane closures)
- maintenance personnel approve and implement temporary regulations in relation to road works
- law enforcement personnel implement specific types of regulations based on current conditions (e.g., road closures due to flooding)

Each of these entities potentially have their own distinct data entry system yet all of these R&R need to be digitized, stored in a secure manner, and made available for sharing with other systems in a standard format. The METR [reference architecture](ig/guides.md) allows for all of these entities to enter regulations into a common network.

## Allows for Regional Tailoring

The METR standards provide a framework for providing electronic regulations, but allow flexibility to adopt this framework to the regional, national, and local context accommodate the political, legal, and financial realities across the world. It is the responsibility of regional authorities to further guide deployments to develop a consistent environment within each region. Additional details are provided in the [regional body perspective](regional-body-perspective.md).

### Enables Accurate R&R Locations

Virtually all rules and regulations are specific to a defined location. The location can be a point (e.g., a stop sign), a linear extent (e.g., a speed limit), or an area (e.g., a pedestrian zone, city, or country). Precisely defining locations so that they can be properly interpreted by multiple systems over prolonged periods of time is a major challenge. This is complicated by the fact that virtually all regulations are legally defined base on the location of "features" (e.g., an intersection, a bus stop, a distance from another feature, a city, etc.) while computer systems rely heavily on geographic coordinate systems to define locations. Aligning different systems is a challenge by itself. METR allows for various levels of location referencing data quality with an indication of the quality provided within the data to allow systems to avoid invalid inferences.

### Provides Timely Information Delivery

Within its scope, METR will support both pre-announced regulations, which can be accessed well in advance of the location and time of need, and emergent regulations, which reflect recent changes in regulations (for example, due to flooding or other unplanned activities). Pre-announced regulations can easily be distributed via any number of internet technologies; the provision of emergent regulations can be more challenging given that they can be enacted with limited notice and impact vehicles that do not currently have internet connectivity.

### Maintains a Trustworthy Environment

While many previous efforts have focused on information delivery, METR focuses more on the pipeline to ensure that it can deliver regulations in a [trustworthy](need-for-trustworthiness.md) manner. At a very basic level, consider a navigation system that displays the speed limit to the driver. Most current generation systems rely upon GNSS information from the navigation unit coupled with a database of speed limits (stored either locally or in the cloud) to display the current sped limit to the driver. But this can result in inaccurate information as the data in the database ages (e.g., especially in the case of temporary road work speed limits).

Other implementations rely on video imaging technologies to read signage, but these are also subject to errors in missing obscured signs or improperly interpreting signs. These issues can result in systems displaying erroneous speed limits (and other regulations) to the driver, or worse, using them for automated driving (e.g., Level 3). The developers of these systems acknowledge their limitations and they claim that the information is only informative and the driver is still responsible for complying with the posted regulations, even when these errors occur. For a human driver, such errors could result in the driver being liable for violating what is actually posted in the field - but to improve road safety and to enable higher levels of automated driving (e.g., Level 4 and 5), a more trustworthy mechanism is required to deliver these regulations.

METR, as defined in the ISO 24315 series, aims to enhance trustworthiness by using robust cryptographic mechanisms, authentication, feedback loops through discrepancy reports, and other security controls that ensure trustworthiness among all METR users and data providers.

## Stakeholder Benefits

| **Stakeholder**                                  | **Key Benefits**                                                                                                                                                              |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Planners and Decision Makers (Public Sector)** | Enhanced digitalization programs; improved interoperability for cross-jurisdictional planning; lower risks via international collaboration.|
| **Infrastructure Owners/Operators (IOOs)**       | Safer, better informed ADS and ADAS; efficient data sharing for traffic management systems, minimizes cost of development of electronic traffic regulation systems.|
| **Fleet Managers, Navigators, and Other Planners** | Trustworthy, real-time access to regulations for safer routing and compliance; reduced liability and operational costs; support for automated fleets in diverse environments.|
| **Vehicle Operators**                 | Trustworthy, real-time access to on-board regulations for better compliance; safer operations; and reduced liability.|
| **ADS Developers and Map Providers**             | Standardized data reduces interpretation efforts; facilitates global scalability; avoids vendor lock-in.|
| **Enforcement and Emergency Agencies**           | Better ADS and ADAS accountability; improved road safety through compliant automation; improve the safety of mixing conventional and automated vehicles.  |

As a connected system of systems, METR facilitates AV deployment, enhances mobility efficiency, and promotes safer roadways by providing all relevant trustworthy digital regulations.
