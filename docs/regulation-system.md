# Guidance for METR Regulation System

!!! note
    Audience: Deployer of METR regulation system (e.g., larger jurisdictions)

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

This document is designed to provide comprehensive guidance for state and local entities that operate a Management of Electronic Traffic Regulations (METR) system. Its primary purpose is to assist sub-national governments in effectively deploying, managing, and maintaining METR systems, ensuring that transport rules are accessible in trustworthy, electronic formats. By focusing on sub-national guidance, this document addresses the unique challenges and opportunities that state and local operators face, helping them to establish robust and compliant METR systems tailored to their specific needs and jurisdictions.

### Audience

This document is intended for state and local government officials, transportation regulators, IT professionals, and other stakeholders involved in the deployment and operation of METR systems. It is particularly relevant for those responsible for the oversight and management of electronic traffic regulations, including infrastructure owners and operators (IOOs), policy makers, and technical staff who ensure the system’s integrity and compliance. Additionally, this guide will be useful for consultants and service providers who support sub-national entities in implementing METR systems.

## Prerequisites for Deploying a METR Regulation System

Before deploying a METR regulation system, operators must address several key prerequisites to ensure successful implementation. These include:

1. **Rule Signing Policies:** Establish clear policies on rule signing, including the required certification levels for different rules (e.g., testing, status quo, verified, verified and proven). Additionally, determine who is authorized to sign rules, such as requiring a professional engineering license.

2. **Rule Category Prioritization:** Prioritize which categories of rules will be converted into the METR system first, such as speed limits, right of way, or parking regulations.

3. **Rule Freshness Periods:** Define how much advance notice the regulation system will provide before a rule goes into effect without needing to classify it as an emergent rule.

4. **Rule Provisioning Agreements:** Determine who the regulation system will provide rules to, including any external entities or third-party systems.

5. **METR Options to Support:** Decide which METR features to enable, such as linking to discrepancy handling systems or supporting rule discovery features.

6. **Supporting Data Providers:** Identify authorized providers of supporting data for rules that require additional datasets and determine if formal agreements with these providers are necessary.

7. **Outsourcing vs. In-House Operations:** Assess how much of the METR system will be managed in-house versus outsourced, considering factors such as cost, expertise, and control.

## Cost Factors

While specific cost estimates are beyond the scope of this document, several cost factors must be considered during the deployment, operation, and maintenance of a METR system:

1. **Connectivity Costs:** Ensure reliable and secure connectivity for all system components, which is crucial for real-time rule dissemination and compliance.

2. **Security Ecosystem:** Invest in a comprehensive security framework to protect the integrity of the regulation system, including data encryption, access controls, and threat monitoring.

3. **Operation and Maintenance Costs:** Budget for the ongoing costs associated with running the regulation system, including data storage, archiving, non-repudiation, and auditing.

4. **Information Entry Costs:** Consider the costs of entering various categories of rules into the system, with attention to the complexity and volume of data required for different rule types.

5. **Impact on Maintenance, Construction, and Emergency Services:** Plan for the operational impacts of emergent rules on field personnel, particularly during critical periods such as construction or emergency response.

6. **Certification, Verification, and Compliance Costs:** Allocate resources for the certification, verification, and ongoing compliance of rules within the METR system.

7. **Personnel Training:** Ensure that staff are adequately trained to manage and operate the METR system, including understanding the technical, legal, and operational aspects of electronic rule management.

## Benefits of Optional METR Features

This section explores the benefits and challenges of implementing optional METR features, such as:

1. **Discrepancy Reporting:** Enables the identification and resolution of conflicts or errors in the rules, improving the overall reliability and trustworthiness of the system.

2. **Rule Discovery:** Allows users to query the system for applicable rules in specific areas, enhancing transparency and accessibility.

3. **Verification Processes:** Independent verification of rules can increase confidence in their accuracy, but may also introduce additional costs and complexity.

## Data Collection

The METR regulation system can be utilized by multiple rule makers within a jurisdiction, such as campuses that input data into the parent jurisdiction’s system. This section also emphasizes the importance of data accuracy and the need to indicate confidence levels within the metadata of each rule. By following the guidelines provided in the Rule Maker Guide, operators can ensure that all data entered into the system meets the required standards of accuracy and reliability.

## Auditing Capabilities

Implementing robust auditing capabilities within the METR system is crucial for maintaining its integrity and compliance. This section explains the importance of audit systems, which allow operators to track changes, verify rule accuracy, and identify potential issues before they become critical. Effective auditing can reduce the risk and cost of operating the system, ensuring that it remains secure and trustworthy over time.

## Evolution of Regulation Systems

As METR regulation systems are relatively new, particularly outside of navigation providers, it is essential to plan for their evolution from the outset. This section discusses the need to design systems that can gracefully migrate between software versions and adapt to changing standards and requirements. By planning for evolution, operators can ensure that their METR systems remain relevant and effective in the long term.

## Deployment Example with Project-Level Architecture

This section provides a practical example of how the ISO reference architecture might be implemented in a specific location where it must interface with multiple systems of the same type, such as a parent regulation system and a peer regulation system. The example illustrates how the architecture can be adapted to meet the needs of a particular project while ensuring compatibility and interoperability with other systems.

## How to Tailor the Guide and the Standards

While this guide offers a comprehensive framework for METR implementation, it is important for deployment sites to tailor the guidance and standards to their specific contexts. This section highlights the key aspects that may require customization, including rule prioritization, data quality requirements, and operational processes. By tailoring the guide to local conditions, operators can ensure that their METR systems are both effective and sustainable, meeting the unique needs of their jurisdictions.
