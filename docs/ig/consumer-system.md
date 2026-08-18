# Guidance for METR Consumer System

!!! note
    Audience: Deployer of METR consumer system (e.g., consumer system developers for vehicle, smartphone app, navigation app, etc.)

    Purpose: Guidance for implementation, deployment, maintenance, and operation, including legal and cybersecurity responsibilities

    Scope: Guidance on:
    - Prerequisites and policies that need to be established/considered
    - Account management & relationships that may need to be created
    - Resources & capabilities needed
    - Data quality & consistency, certification, certificate management
    - Responsibilities of owner/operator (including any legal responsibilities)
    - Sample project-level architecture, existing systems with similar or related capabilities

## Introduction

### Purpose of Document

This document provides guidance for deploying and managing a Management of Electronic Traffic Regulations (METR) consumer system. It focuses on helping entities that consume METR data, such as navigation systems, vehicles, and infrastructure operators, to effectively utilize transportation regulations in an electronic format. The document outlines key considerations, including prerequisites for deployment, the types of rules required, maintenance expectations, data management responsibilities, and discrepancy handling. By following this guide, stakeholders will be able to integrate METR into their systems, ensuring compliance and operational efficiency.

### Audience

This document is intended for system developers, IT professionals, transportation operators, and other stakeholders responsible for deploying or managing systems that consume METR data. It is also relevant for navigation system developers, vehicle manufacturers, public transportation agencies, and infrastructure managers who need to integrate electronic transportation rules into their systems. Consultants, service providers, and legal experts involved in regulatory compliance and system design will also find this guide useful for supporting their clients' and stakeholders’ needs.

## What Are the Prerequisites for Deploying a METR Consumer System?

Before deploying a METR consumer system, several prerequisites must be met. These include establishing a reliable infrastructure capable of receiving and processing electronic rule data, ensuring the system can handle both pre-announced and emergent rules, and confirming interoperability with existing METR systems. Additionally, the system must be designed to interpret and act on rule data in real-time, requiring integration with vehicle sensors, navigation systems, or other consumer-facing technologies. Stakeholders must also ensure that data privacy and security measures are in place to protect the integrity of the received rules.

## What Types of Electronic Rules Do I Need?

The types of electronic rules required for a METR consumer system depend on the specific use case. Common types include speed limits, right-of-way regulations, parking restrictions, lane usage rules, and temporary traffic controls (e.g., road closures, detours). Additionally, systems may need access to vehicle-specific rules, such as those governing the use of autonomous vehicles or electric vehicle charging stations. Understanding the needs of the system’s users will help determine which categories of electronic rules are essential.

## How Do I Determine If the Electronic Rules That I Need Are Available Within an Area?

To determine if the necessary electronic rules are available within a given area, systems must be able to query local METR databases or centralized rule repositories. This process involves accessing a rule discovery feature, which allows consumers to identify available rules based on geographic location, rule type, or jurisdiction. Additionally, stakeholders can collaborate with local authorities or METR distribution centers to ensure that the required rules are published and accessible.

## Should I Implement Any Optional Features?

Optional features such as real-time discrepancy reporting, rule discovery, and automated updates can enhance the functionality of a METR consumer system. Implementing these features allows for more responsive systems, improves data accuracy, and helps ensure that users are always operating with the most current rules. However, adding these features may increase complexity and maintenance requirements, so stakeholders must assess their specific needs and technical capabilities before implementing optional features.

## How Stable Is the Technology? How Much Maintenance Is Likely to Be Required for a METR Consumer System?

The technology supporting METR consumer systems is generally stable but requires regular maintenance to ensure optimal performance. Maintenance activities include software updates, security patches, hardware monitoring, and system testing. Systems that include optional features such as real-time updates or discrepancy handling may require more frequent maintenance to ensure they remain responsive and secure. As METR standards evolve, periodic updates may also be needed to maintain compatibility with newer versions.

## What Are the Minimal Requirements for Interoperability?

Interoperability is crucial for METR consumer systems to function within the larger METR ecosystem. Minimal requirements include compliance with standardized data formats, communication protocols, and APIs that enable seamless interaction between rule sources, distribution centers, and end-user systems. Ensuring interoperability allows consumer systems to accurately interpret and apply rules from multiple sources while maintaining consistent performance and regulatory compliance.

## What Are the Benefits of Including Optional Features?

Including optional features such as automatic rule updates, discrepancy reporting, and advanced data analysis tools can significantly enhance the functionality of a METR consumer system. These features enable the system to proactively manage rule changes, alert users to discrepancies, and provide more accurate and timely rule information. While optional features increase complexity and may require additional maintenance, the benefits of improved data accuracy, system responsiveness, and user experience often outweigh these challenges.

## What Is Involved with Using the Data?

Using METR data involves receiving, processing, and interpreting electronic rules in real-time or near real-time. Systems must be capable of correctly parsing rule data, ensuring that it is relevant to the user’s location, and applying it in accordance with the current conditions (e.g., weather, time of day, traffic). Additionally, systems need to store or cache certain rule data to ensure continuity in the event of connectivity issues and ensure that users can access the most recent information.

### What Are the Responsibilities for Managing Multiple Sources of Data?

Managing multiple data sources requires the ability to aggregate, validate, and reconcile rule information from various distribution centers and rule systems. This may involve handling discrepancies between sources, ensuring that data from different jurisdictions is correctly interpreted, and prioritizing rule updates based on relevance and urgency. Consumer systems must be equipped with tools to manage data from centralized distribution systems, as well as remote or emergent rule sources, to ensure consistent and accurate rule delivery.

METR consumer systems are expected to be able to receive rule data from at least one centralized distribution center (for any given location), which provides pre-announced rules, and from potentially multiple remote distribution systems (e.g., local beacons), particularly for emergent rules. Centralized distribution allows for planned updates, while remote distribution is often necessary for handling emergent rules that arise from unplanned events (e.g., accidents, weather conditions, or emergency road closures). Systems must be capable of handling both types of data and ensuring that emergent rules are processed and applied promptly to avoid compliance issues or operational disruptions.

### What Are the Responsibilities for Interpreting the Data?

Consumer systems have the responsibility to correctly interpret rule data based on current conditions and ensure that users receive relevant, actionable information. This involves determining which rules are in effect at any given time, reconciling conflicting data, and ensuring that emergent rules are prioritized. The system must also be able to translate complex rule data into a format that is easily understood and acted upon by the user. Additionally, the system should include mechanisms for reporting discrepancies when rules are unclear or contradictory.

### What Are the Policies for Reporting Discrepancies?

Discrepancy reporting is a key feature that allows users to flag issues with received rule data, such as inaccuracies or conflicts between data sources. Policies for reporting discrepancies should define how discrepancies are categorized, prioritized, and resolved. Consumer systems must include tools for validating discrepancy reports before they are forwarded to the appropriate rule system for further action. Policies should also outline the timeframe for addressing discrepancies based on their severity.

#### What Steps Are Required to Validate Discrepancies Prior to Reporting Them?

Before discrepancies are reported to a rule system, they must undergo a validation process. This includes verifying the data’s accuracy, ensuring that the discrepancy is legitimate, and confirming that it has not already been addressed by the system. Validation may involve automated checks as well as manual review by system operators. Once validated, the discrepancy is submitted to the relevant rule system for resolution.

#### What Are the Time Requirements for Processing Reported Discrepancies? What Happens If There Is No Connectivity?

The time required to process reported discrepancies depends on the severity of the issue and its impact on system users. Critical discrepancies, such as those affecting public safety or compliance, should be processed as quickly as possible—often within minutes or hours. If there is no connectivity, systems should cache discrepancies and automatically report them once connectivity is restored. It is important to establish clear guidelines for processing discrepancies to ensure timely resolution.

### What Responsibilities Exist for Using Received Data?

Once data is received, the system has the responsibility to apply it in accordance with current conditions and ensure users are informed of relevant rules. This includes interpreting rules based on geographic location, time, and environmental conditions. Systems must also ensure that the data is stored securely and remains available to users even in the event of temporary connectivity disruptions. Additionally, systems must ensure that any discrepancies or issues with the data are promptly addressed.

## What Auditing Information Needs to Be Captured?

To maintain transparency and accountability, METR consumer systems must capture auditing information such as when data was received, how it was processed, and when it was applied to user systems. Auditing should also include records of any discrepancies reported and how they were resolved. This information can be used for troubleshooting, compliance verification, and system improvements.

## Migration from Existing Systems

Migrating from existing systems to a METR consumer system requires careful planning to ensure data continuity and minimal disruption to users. Migration steps include data mapping, integration with existing rule systems, and training personnel on the new system’s features. Operators must also ensure that all relevant rule data from legacy systems is accurately transferred to the new system and that any discrepancies during the migration are promptly addressed.

## Deployment Example with Project-Level Architecture

This section provides an example of how a METR consumer system can be deployed using a project-level architecture. It shows the interactions between multiple rule distribution sources (both pre-announced and emergent), vehicle sensors (e.g., cameras reading road signs or rain sensors on windscreens),

## How to tailor the guide and the standards

This section provides an explanation of how the guide can be tailored to meet the needs of the regional, national, or local agency. The concept is that there is one master guide that is constantly revised at each level of the METR system to address local political, regulatory, administrative, financial and other realities that prevent a single solution for all agencies.
