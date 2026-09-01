# What is METR?

METR is a system of systems that ensures digital rules of the road are communicated dynamically across systems, infrastructure, and end users. Importantly, METR authenticates and secures these communications in real time. This facilitates interoperability that is trustworthy, safe and effective. METR allows for customization at the regional, national, and local levels to support a connected, interoperable, and safe global transportation ecosystem.

## Scope of Regulations Covered by METR

Traffic regulations include all of the regulations related to using the surface transport infrastructure. This includes:

- Virtually all types of regulations, including those:
    - Published in the highway code
    - Posted with signs
    - Marked on the roadway (i.e., pavement markings)
    - Indicated through other traffic control devices (e.g., gates)
- Virtually all modes of travel, including regulations for:
    - Motor vehicles (i.e., self-propelled road vehicles)
    - Non-motorized road vehicles (e.g., horse and buggy)
    - Vehicles that do not normally mix with motor vehicles (e.g., pedal cycles, e-scooters, public-area mobile robots)
    - Foot traffic
- Virtually all surface transport facilities, including regulations for the use of:
    - Roads
    - Auxiliary lanes (e.g., cycle lanes)
    - Footpaths
    - Pedestrian plazas
    - Indoor environments (e.g., for PMRs)

While the title of the standards refers to "regulations", the intent is that it will be capable of providing trustworthy advisories, guidance, regulations, and unposted regulations (i.e., rules of the road) to the user. This site uses the term **rule** to represent the aggregation of regulations, advisories, and guidance.

METR is intended to support virtually any rule that needs to be conveyed to virtually any transport user. The attached graphic depicts regulations for freight vehicles, ride sharing, kerbside usage, micromobility operations, vulnerable road users (VRUs), public transport usage, lane usage, public-area mobile robots (PMRs), and road works. This information and more needs to be conveyed to all transport user systems; sample user systems include nomadic devices, PMRs, driver support systems, and ADS-equipped vehicles.

![Illustration of diverse transport regulations and user systems](images/streetscape.png)

As driving automation systems become more common, the importance of providing trustworthy regulations to the public is becoming more critical.

## Challenges Addressed by METR

### Trustworthiness

While many previous efforts have focused on information delivery, METR focuses more on the pipeline to ensure that it can deliver regulations in a trustworthy manner. At a very basic level, consider a navigation system that displays the speed limit to the driver. Most current generation systems rely upon GNSS information from the navigation unit coupled with a database of speed limits (stored either locally or in the cloud) to display the current sped limit to the driver. But this can result in inaccurate information as the data in the database ages (e.g., especially in the case of temporary road work speed limits).

Other implementations rely on video imaging technologies to read signage, but these are also subject to errors in missing obscured signs or improperly interpreting signs. These issues can result in systems displaying erroneous speed limits (and other regulations) to the driver, or worse, using them for automated driving (e.g., Level 3). The developers of these systems acknowledge their limitations and they claim that the information is only informative and the driver is still responsible for complying with the posted regulations, even when these errors occur. For a human driver, such errors could result in the driver being liable for violating what is actually posted in the field - but to improve road safety and to enable higher levels of automated driving (e.g., Level 4 and 5), a more trustworthy mechanism is required to deliver these regulations.

METR, as defined in the ISO 24315 series, aims to enhance trustworthiness by using robust cryptographic mechanisms, authentication, feedback loops through discrepancy reports, and other security controls that ensure trustworthiness among all METR users and data providers.

### Layered Regulations

Traffic regulations are defined by multiple layers of government and different departments within each layer. For example, regulations can be defined by a regional (multi-national) government, national government, state or provincial government, county government, city government, and even more local entities (e.g., borough, subdivision, or property/campus owner). Further, each of these entities can authorize multiple representatives to issue regulations, often with specific scopes. The following are some typical examples of how authorities can be divided within each level:

- the legislative arm can retain the authority to define any regulation it wishes
- traffic engineers define permanent traffic regulations (e.g., stop signs, speed limits)
- road operators (e.g., operators of traffic management systems) implement specific types of regulations based on schedules and current conditions (e.g., dynamic speed limits, lane closures)
- maintenance personnel approve and implement temporary regulations in relation to road works
- law enforcement personnel implement specific types of regulations based on current conditions (e.g., road closures due to flooding)

Each of these entities potentially have their own distinct data entry system yet all of these regulations need to be digitized, and stored in a secure manner and made available for sharing with other systems in a standard format. The METR [reference architecture](ig/guides.md) allows for all of these entities to enter regulations into a common network.

### Location Referencing

Virtually all traffic regulations are specific to a defined location. The location can be a point (e.g., a stop sign), a linear extent (e.g., a speed limit), or an area (e.g., a pedestrian zone, city, or country). Precisely defining locations so that they can be properly interpreted by multiple systems over prolonged periods of time is a major challenge. This is complicated by the fact that virtually all regulations are legally defined base on the location of "features" (e.g., an intersection, a bus stop, a distance from another feature, a city, etc.) while computer systems rely heavily on geographic coordinate systems to define locations. Aligning different systems is a challenge by itself. METR allows for various levels of location referencing data quality with an indication of the quality provided within the data to allow systems to avoid invalid inferences.

### Varied User Needs

Transport users have different needs for each trip that they take. For example, different users can have different needs based on:

1. The type of vehicle being operated (e.g., passenger car, heavy goods, or public-area mobile robot)
2. The origin and destination of a trip (e.g., local trip vs. cross-country)
3. The way in which the information is being used (e.g., pre-trip planning, driver information for speed limits, Level 4 ADS)

Each user needs access to the relevant regulations in a trustworthy manner although the agencies who sign and issue these regulations generally group them in different ways. As a result, the issued regulations will typically need to be repackaged before distribution to the end user. The METR architecture allows for this repackaging while preserving a trust chain back to the originator of the regulation.

### Timeliness

Within its scope, METR will support both pre-announced regulations, which can be accessed well in advance of the location and time of need, and emergent regulations, which reflect recent changes in regulations (for example, due to flooding or other unplanned activities). Pre-announced regulations can easily be distributed via any number of internet technologies; the provision of emergent regulations can be more challenging given that they can be enacted with limited notice and impact vehicles that do not currently have internet connectivity.

### Regional Tailoring

The METR standards provide a framework for providing electronic regulations, but as an international standard, these standards are designed to be very flexible to accommodate the political, legal, and financial realities across the world. It is the responsibility of regional framework and implementation guides to further guide deployments to develop a consistent environment within each region.
