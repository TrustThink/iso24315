# Functional View: How METR Works

METR defines how traffic laws and regulations can be transformed into geo-specific, trustworthy, machine-interpretable data that vehicles, apps, and other transport systems can rely on. The figure, from ISO/TR 24315-2, is the functional view of the METR reference architecture. Clicking on any link will jump to the segment of text that explains the specific function.

<div class="diagram-light-bg" markdown="0">
--8<-- "images/functional_view.svg"
</div>

A **rule maker** enacts legal regulations. Those regulations are translated, checked, approved, stored, and distributed. A **transport user** (driver, fleet manager, or automated vehicle) requests the regulations that apply, combines them with supporting data (e.g., location, time, environmental conditions), and follows what is currently relevant. If any inconsistencies are detected between the electronic regulations and physical traffic control devices, the user can report a discrepancy so the catalogue can be corrected.

---

## Creating and Publishing Regulations

### Implement regulations
Authorities publicize legal regulations to put them into force. Rules of the road, defined in the highway code, are publicized through driver's education courses and similar means. Changes to these regulations are announced using media outlets. Other regulations, i.e., as defined by regulatory bodies and other entities, are typically posted using signs or other traffic control devices. This is the source of truth outside METR and it is critical that METR data is consistent with this source of truth.

### Translate into electronic regulations
A translator turns each legal regulation into a standardized METR regulation: machine-interpretable, scoped in space and time, and ready to be signed so it can be processed and distributed electronically. The METR format is designed to minimize ambiguities.

### Verify electronic regulations
Ideally, regulations should be verified by an independent third party to ensure it reflects the original regulation — right location, right conditions, right values — so downstream systems and travelers can trust it.

### Approve electronic regulations
Verified regulations still need formal sign-off from an authority with the power to publish them. This function is the governance checkpoint: a designated approver reviews and authorizes the regulation before it's released for distribution, ensuring accountability for what enters the system.

### Distribute regulations to users
Approved regulations are packaged for a place and a need (e.g., route, vehicle class, regulation type) and sent to METR user devices. Users can request regulations; the distributor returns what applies.

## Refining to find relevant regulations

### Identify current regulations
From the downloaded catalogue, the regulations are filtered to determine which approved regulations are in force *now* (i.e., based on time, environmental conditions, and other factors).

### Monitor supporting data
The activation status of some regulations can vary based on external factors, such as time of day, environmental conditions, and other factors. These factors need to be monitored to ensure compliance to defined regulations; for electronic systems, the monitoring typically requires some sort of sensor or other data source.

### Obtain electronic supporting data
The METR system needs to obtain data from the sensor or other external data source.

### Identify relevant regulations
The METR system needs to integrate the relevant current regulations with the supporting data to determine which regulations are active and relevant to the current situation. 

### Present relevant regulations
Once the applicable regulations are identified, they need to be presented to the user of the data in an appropriate form. The could be a person, an Automated Driving System (ADS), driver support system, etc. 

## Detecting and Reporting Discrepancies

Whenever multiple records exist for a regulation, conflicts can occur, yet transport users need to maintain confidence that the data is accurate. To minimize the existence of any conflict, METR provides for the reporting of identified discrepancies so that they can be resolved as quickly as possible. For example, a sign might be knocked down, a regulation might be updated, or a two regulations from different levels of hierarchy might conflict. The discrepancy reporting process is designed to be identify, report, and resolve these issues.

### Report system-generated discrepancies
This function allows for regulation systems and distributors to automatically detected and report discrepancies prior to their distribution to users. For example, automated checks can identify invalid digital signatures, conflicting approved regulations, and other issues or ambiguities so that the can be corrected before they are distributed to users.

### Report unverified discrepancies
Even with system checks being performed prior to distribution, some discrepancies are unlikely to be identified until after their distribution. For example, signs that are knocked down or a recent regulatory change could create a conflict that needs to be reported. This function allows a user to report instances of users detecting a discrepancy in the field.

However, discrepancies reported by users can be inaccurate due to a variety of reasons (e.g., obscured signs, coding errors, bad actors, etc.) and as such should be considered suspect until they can be verified. An easy initial verification step is to see if the discrepancy is being reported by other users.

### Consolidate discrepancies
This function manages unverified discrepancy reports and groups them into a single, organized view. This allows a greater level of confidence that multiple users are detecting the issue so they can be triaged and resolved efficiently instead of handled piecemeal.

### Report discrepancies
This function flags the consolidated reports to be resolved once they satisfy  defined criteria (e.g., a number of unverified reports within a specified time period). 

## Resolving Discrepancies and Keeping Systems in Sync

### Resolve discrepancies
This function addresses teh reported problem. The first step is to verify that there is in fact an inconsistency (and not just a temporary problem) and identify the source of the error. The fix might require any of the following:

- correcting the electronic regulation (e.g., updating a regulation to more accurately define the location of a regulation)
- correcting the traffic control device (e.g., replacing a sign that is knocked down)
- clarifying the legal source (e.g., if local and national regulations are in conflict)
- notifying the developer of the METR user device that their discrepancy detection logic is incorrect and needs to be updated.

### Update external systems
If the problem is located outside of the METR system (e.g., an issue with a METR user device reporting a discrepancy when none exists), then the problem needs to be corrected in the external system. 

## Audit systems

This function allows for the system to be monitored to ensure that all components have been functioning correctly. This function is important both to maintain trustworthy operation of the system while also allowing for forensic analysis when and if any disagreements arise. For example, if an ADS driven vehicle is ticketed for exceeding a speed limit, it is important to be able to review the system's audit trail to determine if:

- the speed limit was correctly entered into the METR system
- the speed limit was correctly verified by an independent third party
- the speed limit was correctly approved by an authority with the power to publish it
- the speed limit was correctly distributed to the METR user device
- the speed limit was correctly identified as active and relevant to the current situation
- the correct speed limit was reaffirmed by traffic control devices (e.g., a speed limit sign)
- the speed limit was correctly provided to the ADS
- the ADS correctly complied with the supplied speed limit
- the enforcer properly issued the ticket
 
Identifying the root cause of the non-compliance is critical to identifying the responsible party and taking corrective action.

---

*Together, these functions form a continuous loop: regulations are created, verified, approved, and distributed; discrepancies are identified, reported, and resolved; and ongoing auditing and monitoring keep the system accurate over time.*
