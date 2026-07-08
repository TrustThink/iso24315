# Management of Electronic Transport Regulations (METR)

!!! note
    Audience: Non-technical, unfamiliar with METR

    Purpose: inform industry, encourage deployment

    Scope: “Is it needed?”, “Why should I care?”, “How does it fit into priorities?”

!!! abstract ""
    METR provides users with geo-specific, trustworthy, timely, authoritative, machine-interpretable, transport-related rules (e.g., traffic regulations) established by jurisdictional entities

<div class="button-row" markdown="span">

[METR Vision](METRVision.pdf "A 13-page PDF describing METR"){ .md-button .md-button--primary }
[Vocabulary](documentation/Vocab.md "Definitions for key terms used in METR"){ .md-button .md-button--primary }
[Overview Presentation](METROverview.pdf "A 36-slide presentation describing METR"){ .md-button .md-button--primary }

</div>

## Overview

Traffic regulations include all of the rules related to using the surface transport infrastructure. This includes:

- Virtually all types of rules, including those:
    - Published in the vehicle code
    - Posted with signs
    - Marked on the roadway (i.e., pavement markings)
- Virtually all modes of travel, including rules for:
    - Motor vehicles (i.e., self-propelled road vehicles)
    - Non-motorized road vehicles (e.g., horse and buggy)
    - Vehicles that do not normally mix with motor vehicles (e.g., pedal cycles, public-area mobile robots)
    - Pedestrians
- Virtually all surface transport facilities, including rules for the use of:
    - Roads
    - Auxiliary lanes (e.g., cycle lanes)
    - Footpaths
    - Pedestrian plazas
    - Indoor environments

METR should be able to support virtually any rule that needs to be conveyed to virtually any transport user. The graphic depicts rules for freight vehicles, ride sharing, kerbside usage, micromobility operations, vulnerable road users (VRUs), public transport usage, lane usage, public-area mobile robots (PMRs), and road works. This information and more needs to be conveyed to all transport user systems; sample user systems include nomadic devices, PMRs, driver support systems, and ADS-equipped vehicles.

![Illustration of diverse transport rules and user systems](images/streetscape.png)

As driving automation systems become more common, the importance of providing trustworthy rules of the road to the public has become more critical.

## Adding trustworthiness

While many previous efforts have focused on information delivery, METR focuses more on the pipeline to ensure that it can deliver rules of the road in a trustworthy manner. At a very basic level, consider a navigation system that displays the speed limit to the driver. Most current generation systems rely upon GNSS information from the navigation unit coupled with a database of speed limits (stored either locally or in the cloud) to display the current sped limit to the driver. But this can result in inaccurate information as the data in the database ages (e.g., especially in the case of temporary road work speed limits). Other implementations rely on video imaging technologies to read signage, but these are also subject to errors in missing obscured signs or improperly interpreting signs. These issues can result in systems displaying erroneous speed limits (and other rules) to the driver, or worse, using them for automated driving (e.g., Level 3). While the developers of these systems acknowledge their limitations, they claim that the information is only informative and the driver is still responsible for complying with the posted rules, even when these errors occur. For a human driver, this is an annoyance that could result in the driver being liable for violating what is actually posted in the field - but to improve road safety and to enable higher levels of automated driving (e.g., Level 4 and 5), a more trustworthy mechanism is required to deliver these rules.

METR, as defined in the ISO 24315 series, aims to address this issue by providing all relevant transport-related rules to user systems in a trustworthy manner.

## Type of rules covered

While the title of the standards refers to "regulations", the intent is that it will be capable of providing trustworthy advisories, guidance, regulations, and unposted rules of the road to the user. This site uses the term **rule** to represent the aggregation of regulations, advisories, and guidance.

## Timeliness of rules

Within its scope, METR will support both pre-announced rules, which can be accessed well in advance of the location and time of need, and emergent rules, which reflect recent changes (for example, due to flooding or other unplanned activities).

## Discussion

Join the online discussion anytime.

[Discussion forum](https://github.com/ISO-TC204/iso24315/discussions){ .md-button }
