### METR Trust Management Use Cases

Trusted METR domain preparation use cases define the security activities required to establish a METR environment in which trusted operations can occur. They address the establishment and maintenance of trust relationships, security policy, identities and credentials, authorization privileges and scopes, security audit requirements, and secure METR services. Figure X illustrates the principal actors and use cases involved in preparing the METR domain for trusted operation. The subsections that follow define each of these security use cases and identify the security controls applied to support them.

![METR Trust Management Use Cases](images\metr-trust-management-uc.jpg)



#### Manage METR Trust Relationships

This use case describes the activities required to establish and maintain the trust framework used by a METR domain. Before trusted METR operations begin, the responsible METR authority shall identify the external or internal trust services on which the METR deployment will rely and determine that those services provide an appropriate level of assurance for their intended use.

For each trust service, the METR authority shall evaluate the applicable governing policies, practices, trust model, security requirements, and operating procedures. This may include certificate policies and certification practice statements for credential services, as well as equivalent policy and assurance documentation for other identity, authentication, authorization, or trust services. The METR deployment shall be configured and operated in accordance with the applicable requirements of those documents and the METR security policy.

Where a METR domain relies on an external trust service, the METR authority shall establish the organizational, contractual, or other trust relationship necessary to use that service and shall define the respective responsibilities of the METR domain and service provider.

The METR authority shall configure the trust information necessary for METR components to rely on approved trust services. Depending on the trust mechanism, this may include trust anchors, trusted issuers, trusted service identities, verification keys, service endpoints, policy identifiers, or other trust configuration. Processes shall be established for the authorized installation, distribution, update, replacement, and removal of this trust information.

The output of this use case is an established and maintained METR trust framework identifying the approved trust services and relationships, their governing policies and practices, the trust information required by METR components, and the processes necessary to maintain those relationships throughout METR operation.

![Manage METR Trust](images\manage-metr-trust.jpg)

#### Manage METR Security Policy 

 This use case describes the activities required to establish and maintain the security policy that governs the METR domain. The METR Policy Authority shall define the roles and trust relationships recognized within the domain, select the security mechanisms approved for use, and establish the authorization, information protection, non-repudiation, trust translation, audit, and evidence policies that apply to METR operations.

The METR security policy shall define the choices and constraints that METR components use when applying the cybersecurity requirements of this standard. This includes, as applicable, approved authentication and credential mechanisms, role permissions and scope restrictions, required confidentiality and integrity protections, where secure transport is required, where non-repudiation of origin or delivery is required, how trust translation may be performed, and what audit and security evidence shall be created, protected, and retained.

The METR Policy Authority shall publish and maintain the approved domain security policy and make the applicable policy available to METR system components and participating service providers.

METR system components shall be configured to operate in accordance with the applicable METR security policy.

Third-party service providers and Trust Bridges that participate in the METR domain shall be evaluated against the applicable METR security policy before being relied upon. The evaluation shall determine whether the provider’s policies, practices, security mechanisms, and trust relationships are compatible with the METR domain policy and whether any additional constraints or trust conditions are required.

Changes to the METR security policy shall be controlled and maintained so that the policy applicable to a METR operation or security decision can be determined.

The output of this use case is an approved and maintained METR domain security policy, configured METR components, and established conditions under which third-party services and Trust Bridges may participate in trusted METR operations.

![Manage METR Security Policy](images\manage-meter-security-policy.jpg)

#### Manage METR Identities and Credentials

This use case describes the activities required to establish and maintain the identities and credentials used by METR actors, systems, services, and organizations within the trusted METR domain.

The METR domain shall define the identity types that are recognized for METR operation and the credential mechanisms used to represent or assert those identities. Identity and credential mechanisms shall be consistent with the trust relationships and approved security mechanisms established by METR security policy.

An authoritative identity shall be established before a credential is provisioned for use within the METR domain. The identity record shall identify the entity to which the credential applies and, where applicable, its organization, system, service, role, or other attributes needed by system authorization processes.

Credentials shall be provisioned, activated, renewed, replaced, suspended, revoked, or otherwise withdrawn in accordance with the applicable trust framework, credential-provider policy, and METR security policy.

Where credential services are provided by an external Credential Management System or other trusted service, the METR domain shall use the credential lifecycle, validation, and status mechanisms defined by that service and accepted through the Manage METR Trust use case.

METR components shall be configured to recognize the approved credential types and trusted issuers used within the domain. Credential status information needed to determine whether a credential remains valid and suitable for use shall be made available to applicable METR components.

Changes to an identity, credential, organizational affiliation, or other security-relevant attribute that could affect METR trust or authorization decisions shall result in the applicable identity or credential information being updated, replaced, suspended, or revoked.

 ![Manage METR Identities and Credentials](images\manage-metr-identities-credentials.jpg)

#### Manage METR Roles and Permissions

This use case describes the activities required to establish and maintain the authorization privileges that determine what an authenticated METR actor is permitted to do within the METR domain.

The METR Policy Authority shall define the METR roles and the categories of authorization scope that may be assigned to each role. For a Rule Maker, authorization scope may include geographic jurisdiction, roadway classification, rule category, vehicle class or type, operational period, and other policy-defined limits on rule-making authority.

The METR Policy Authority shall determine and approve the specific role and authorization scope assigned to an identified actor. The authorization decision shall be based on authoritative evidence that the actor is permitted to exercise the approved privileges.

Before credentials asserting those privileges are issued or updated, the Credential Management System shall validate the authorization request and supporting evidence in accordance with the applicable trust framework and credential policy. Credentials shall assert only the privileges approved by the METR Policy Authority and permitted by the applicable credential framework.

Authorization privileges shall remain associated with the identity to which they apply and shall be represented in a form that METR components can evaluate during trusted operations. The authorization information may be carried within a credential or maintained separately, provided that the relationship between the authenticated identity and its approved privileges can be reliably established.

Changes to an actor’s role, jurisdiction, organizational authority, or permitted scope shall result in the applicable authorization information and, where necessary, associated credentials being updated, replaced, suspended, or revoked.

 ![Manage METR Roles and Permissions](images\manage-metr-roles-and-permissions.jpg)

#### Manage METR Accountability and Audit

This use case describes the activities required to establish and maintain the audit framework used to support accountability, traceability, security monitoring, investigation, and forensic analysis across the METR domain.

The METR Policy Authority shall define the audit policy applicable to the METR domain, including which security-relevant events and transactions shall be recorded, what information shall be captured for those events, how long audit information shall be retained, and who is authorized to access it.

The audit policy shall define, as applicable, the recording of actor identities, source and destination information, transaction times, authorization decisions, validation results, rule origin and provenance, transformation events, non-repudiation evidence, service disruptions, and other security-relevant outcomes.

The METR Policy Authority shall also define requirements for protecting audit records and supporting evidence against unauthorized access, modification, deletion, or substitution, and for correlating related records across METR components where necessary to reconstruct a METR transaction or security-relevant event.

Each METR Component shall be configured in accordance with the applicable audit policy and shall generate, protect, and retain the audit information required for the functions it performs.

Audit records shall remain available to authorized entities for routine security audit, incident investigation, dispute resolution, and forensic analysis in accordance with applicable METR security policy.

Changes to audit scope, recorded information, retention, protection, correlation, or access requirements shall be reflected in the audit configuration of affected METR Components.

The output of this use case is a METR domain in which each component is configured to locally generate, protect, retain, and make available the security audit information required by the METR audit policy.

![Manage METR Accountability and Audit](images\manage-metr-accountability-and-audit.jpg)

#### Manage METR Device Security

This use case describes the activities performed to ensure that devices used to provide METR functions are securely configured, validated, and approved before participating in trusted METR operations.

The applicable METR security policy shall define the security conditions that a device is required to satisfy before it is authorized to participate in the METR environment.

Before a device is placed into service, the device shall be identified and evaluated against applicable METR device-security requirements. The evaluation may include, as applicable, device identity, hardware and software configuration, installed software or firmware versions, security configuration, supported security functions, cryptographic capabilities, credential status, and other security evidence required by METR policy.

The device shall be configured to provide the security functions required for its assigned METR role and shall be enrolled with the applicable device-certification, credential-management, or other security support service before performing security-relevant METR operations.

The device shall be evaluated to determine whether it satisfies applicable METR security policy and whether it is suitable for its intended METR role.

A device that does not satisfy required security conditions shall not be authorized for trusted METR operation until the identified conditions have been corrected or an applicable policy permits restricted operation.

The device security evaluation result, supporting evidence, and authorization decision shall be recorded in accordance with applicable METR audit and evidence requirements.

![Manage METR Device Security](images\manage-metr-device-security.jpg)

#### Manage Trusted METR Services

This use case describes the activities required to establish METR services and service endpoints as trusted participants within the METR domain before they are used for operational exchanges.

A METR Service Provider shall identify the METR service to be offered, the service endpoint or endpoints through which it is accessed, and the functions and information made available by the service.

The service shall be associated with an established identity and with the credentials, trust relationships, authorization privileges, and security policy applicable to its operation. Where the service is provided by a third party, the service provider shall be evaluated in accordance with the applicable METR trust and security policy before the service is accepted into the METR domain.

The METR Policy Authority shall determine the security conditions under which the service may participate in the METR domain, including the permitted service role, authorized functions and information scope, approved authentication and credential mechanisms, required transport and information protections, and applicable audit and evidence requirements.

The service shall be registered in an authorized METR Service Registry or equivalent discovery mechanism with sufficient information for METR components to identify the service, determine its intended function, locate the applicable endpoint, and obtain the trust and security information needed to establish a trusted interaction.

Before the service is made available for trusted METR operations, the applicable service identity, endpoint, credential, authorization information, and security configuration shall be validated.

Changes to a registered service, including changes to its identity, endpoint, provider, credentials, authorization scope, trust relationship, or security configuration, shall be evaluated and reflected in the service registration before the changed service is relied upon.

A service whose trust relationship, credential, authorization, or security configuration is no longer valid shall be removed, disabled, or otherwise identified as unavailable for trusted METR operation.

 

![Manage Trusted METR Services](images\manage-trusted-metr-services.jpg)



