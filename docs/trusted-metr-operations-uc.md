### Trusted METR Operations

Trusted METR operation use cases specify the cybersecurity activities applicable to METR information and associated transactions during operational use. These use cases define the security requirements necessary to maintain the authenticity, integrity, authorization, provenance, confidentiality, non-repudiation, accountability, availability, and trustworthiness of METR information as it is created, approved, transformed, distributed, received, verified, and used.

The use cases define, as applicable, requirements for entity authentication, credential and trust validation, authorization, cryptographic protection, validation of security evidence, preservation of provenance, protected communications, generation and retention of non-repudiation evidence, and recording of security-relevant events.

![Trusted METR Operations](images\trusted-metr-operations-uc.jpg)

#### Verify Legal Rule

Before a Legal Rule is transformed into a METR Rule, the METR Regulation System shall authenticate the Rule Maker and verify that the Rule Maker is authorized to publish the rule.

The verification shall determine whether the Rule Maker has authority applicable to the rule, including, as relevant:

·    the defined geographic area; 

·    the applicable vehicle classes; 

·    the category of rule, such as parking restrictions or speed limits; 

·    the affected vehicle types, such as emergency vehicles; 

·    the defined times of day or operational periods; and 

·    the applicable roadway classifications, such as municipal roads or interstate highways. 

The METR Regulation System shall record the Rule Maker identity, the applicable authorization evidence, and the results of the role and scope authorization decisions.

The authentication and verification process is region-specific and may be performed manually or electronically. If the Rule Maker’s identity or authority cannot be verified, the Legal Rule shall not proceed to digitization.

 ![Verify Legal Rule](images\verify-legal-rule.png)





#### Digitize Legal Rule

After a Legal Rule has been verified, the METR Regulation System shall make the verified Legal Rule available to an authorized Rule Translation Agent for conversion into the applicable METR format.

The digitization process shall preserve the relationship between the source Legal Rule and the resulting METR information. At a minimum, the process shall:

·    identify the Legal Rule used as the source; 

·    record the Rule Translation Agent responsible for the digitization; 

·    record the transformation from the Legal Rule to the METR representation; 

·    associate applicable provenance information with the resulting METR information; 

·    protect the integrity of the digitized METR information during submission and processing; 

·    record the results of applicable format, completeness, and internal consistency checks; and 

·    record applicable digitization transaction events. 

The METR Regulation System shall restrict digitization functions to authorized Rule Translation Agents.

If the digitized information does not satisfy applicable format, completeness, consistency, or policy checks, the METR Regulation System shall return the identified issues for correction. The digitized information shall not proceed to independent verification until the applicable checks have been satisfied.

The output of this process is unverified METR information. Independent verification, approval, and digital signing are performed in subsequent processes.

![Digitize Legal Rule](images\digitize-legal-rule.png)





#### Digitally Sign and Approve METR Rule

After a digitized METR Rule has been independently verified, the METR Regulation System shall request approval and signature from an authorized Rule Signing Agent.

Before presenting the rule for approval, the METR Regulation System shall:

·    confirm that the METR Rule has successfully completed the required verification process; 

·    authenticate the Rule Signing Agent; 

·    validate the applicable signing credential and certificate chain; 

·    determine that the Rule Signing Agent is authorized to act for the applicable signing organization; and 

·    protect the integrity and provenance of the METR Rule presented for approval. 

The Rule Signing Agent shall review the verified METR Rule and either approve or reject it. The approval or rejection decision, the identity of the Rule Signing Agent, and the associated transaction event shall be recorded.

If approved, the Rule Signing Agent shall apply a digital signature that is bound to the specific version of the METR information being approved.

The signed METR Rule shall identify, directly or through an associated internal record:

·    the approving person or organization; 

·    the applicable rule record; and 

·    relevant signing and update information. 

Upon receipt of the signed METR Rule, the METR Regulation System shall validate:

·    the digital signature; 

·    the signing credential; 

·    the applicable certificate chain; and 

·    the authority of the Rule Signing Agent. 

If these validations succeed, the METR Regulation System shall preserve the signed object and associated evidence, record the transaction event and validation results, and mark the METR Rule as approved.

If the Rule Signing Agent rejects the rule, or if the signature, credential, certificate chain, or signing authority cannot be validated, the rule shall not be marked as approved or made available for distribution. The rejection or validation failure and associated evidence shall be recorded and preserved.

![Digitally Sign METR Rule](images\digitally-sign-legal-rule.png)

#### Package Rule for Distribution

After a METR Rule has been approved and digitally signed, the METR Regulation System shall prepare the rule for provisioning to an authorized METR Distribution System.

Before packaging the rule, the METR Regulation System shall verify that:

- the rule remains approved; 
- the digital signature is valid; 
- the supporting credential and applicable     certificate chain are valid; 
- the signed content has not been modified;     and 
- the associated security evidence remains     valid. 

The METR Regulation System shall authenticate the intended METR Distribution System and determine that it is authorized to receive the package.

The package shall preserve the signed METR Rule without altering the signed content. Metadata or packaging information added for distribution shall remain distinguishable from the signed content and shall be associated with the applicable signed rule.

The METR Regulation System shall record the packaging transaction event, the selected rules, the applicable criteria, the intended METR Distribution System, and the results of applicable validation and authorization decisions.

If the signature, credential, certificate chain, approval status, integrity, authorization, or other applicable security evidence cannot be validated, the affected rule shall not be included in the distribution package.

![Package Rule for Distribution](images\package-rule-for-distribution.png)



#### Distribute Rule

This use case describes how signed METR information is distributed while preserving the trust established during rule generation, verification, approval, signing, and packaging.

Distribution may be performed by a METR Distribution System or by an authorized third-party distribution service, such as an OEM cloud service or map provider, when permitted by applicable METR policy.

Before distribution, the distribution service shall verify that:

·    the METR information originated from an authorized source; 

·    the included METR Rules remain approved and digitally signed; 

·    the signatures, supporting credentials, and applicable certificate chains are valid; 

·    the signed content has not been modified; 

·    the information remains within its applicable freshness and authorization scope; and 

·    the package and associated security evidence comply with applicable METR policy. 

Before transmitting the METR information, the distribution service shall establish Transport Layer Security with the destination system using an approved secure communication protocol.

The distribution service shall record the information transmitted, the destination, the applicable selection criteria, the establishment of the secure communication session, and the results of security validation. Where required by applicable policy, the sender shall generate and retain non-repudiation-of-origin evidence for the transmitted METR information.

If the signature, credential, integrity, freshness, authorization, provenance, secure communication session, or other applicable security evidence cannot be validated, the affected information shall not be distributed.

The output of this process is signed METR information transmitted or made available to a METR Consumer System over a protected communication channel.

 ![Distribute METR Rule](images\distribute-metr-rule.png)



#### Receive Rule

This use case describes how a METR Consumer System receives signed METR information from a METR Distribution System or an authorized third-party distribution service.

The METR Consumer System shall receive the METR information over an established protected transport session and shall preserve the received signed METR object without altering its signed content.

The METR Consumer System shall record the applicable transaction event, including:

·    the source of the METR information; 

·    the receiving system; 

·    the time and status of receipt; 

·    the received METR information package; and 

·    the applicable transport and transaction evidence. 

Where required by applicable policy, the METR Consumer System shall generate and retain non-repudiation-of-delivery evidence confirming receipt of the specific METR information package.

If the protected transport session is not established or the METR information package cannot be received successfully, the METR Consumer System shall record the failure and shall not make the affected information available for further processing or use.

The output of this process is received METR information preserved for subsequent verification. Validation of the rule signature, credential, content integrity, authorization scope, freshness, provenance, and other security evidence is addressed by the separate Verify Received Rule use case.

 ![Receive METR Rule](images\receive-metr-rule.png)



#### Verify Received Rule

This use case describes how a METR Consumer System verifies received METR information before accepting it for storage or use.

The METR Consumer System shall verify that:

·    the digital signature is valid for the received METR Rule; 

·    the signing credential is valid, current, not revoked, and appropriate for use; 

·    the credential chains to an accepted trust anchor; 

·    the signed content has not been modified; 

·    the signer was authorized to act in the applicable role and scope; 

·    the METR information remains sufficiently fresh; 

·    the provenance and associated security evidence are valid; and 

·    the METR information complies with applicable METR policy. 

The METR Consumer System shall record the applicable transaction event and the results of the signature, credential, integrity, authorization, freshness, provenance, and policy validations.

If all required validations succeed, the METR Consumer System shall accept the METR Rule as verified and preserve the signed object, associated provenance, and supporting evidence for subsequent storage or use.

If any required validation fails, the affected METR Rule shall be rejected and shall not be made available for use. The METR Consumer System shall record the validation failure and reason for rejection and preserve applicable evidence for audit or investigation.

The output of this process is either a verified METR Rule accepted for subsequent processing or a rejected METR Rule retained only as required for security evidence.

![Verify Received METR Rule](images\verify-received-rule.png)



#### Report Discrepancy

This use case describes the secure submission of a METR discrepancy report from a METR Consumer System to a METR Discrepancy Handling System.

Before transmitting the discrepancy report, the METR Consumer System shall establish Transport Layer Security with the destination system. As part of establishing the protected session, the destination system shall authenticate the reporting system and validate the applicable credential and certificate chain.

The METR Discrepancy Handling System shall determine whether the reporting system is authorized to submit discrepancy reports and shall enforce the resulting access control decision.

The discrepancy report shall be protected from unauthorized disclosure or modification while in transit. The reporting and receiving systems shall record the applicable transaction event, including the source, destination, time of submission, participating systems, and results of applicable authentication and authorization checks.

Where required by applicable policy, the sender shall generate and retain non-repudiation-of-origin evidence for the submitted discrepancy report.

If the protected communication session cannot be established, or if the reporting system cannot be authenticated or authorized, the discrepancy report shall not be accepted for further processing. The failure and applicable evidence shall be recorded and preserved.

The output of this process is an authenticated and authorized discrepancy report received by the METR Discrepancy Handling System.



![Report METR Discrepancy](images\report-metr-discrepancy.png)





#### Evaluate METR Rule Provenance

This use case describes the activities performed by a METR Component to evaluate the provenance of a METR Rule and determine whether the rule’s recorded origin and history can be relied upon.

The METR Component shall retrieve the provenance information associated with the METR Rule and electronically evaluate the recorded history of the rule from its current form back to the originating Rule Maker or other authoritative source.

The evaluation shall consider, as applicable, the recorded Rule Maker identity, rule origin, source system, translation and transformation events, approval and signing events, distribution history, trust-bridge processing, and other provenance information associated with the rule.

The METR Component shall verify that the provenance information remains associated with the METR Rule being evaluated and that the recorded sequence of events provides a continuous and internally consistent history from the originating source to the current rule object.

Where provenance records or associated security evidence are cryptographically protected, the METR Component shall validate the applicable signatures, hashes, credentials, bindings, or other security evidence needed to establish confidence in the provenance information.

The METR Component shall evaluate whether the recorded actors, systems, and transformations were permitted under the applicable METR security policy and whether any transformation or trust-bridge event preserved the relationship to the preceding object and original Rule Maker.

If provenance information is incomplete, inconsistent, cannot be fully associated with the evaluated rule, cannot be fully validated, or indicates a gap or uncertainty in the recorded history, the METR Component shall determine that the provenance cannot be established with full confidence. In such cases, the component shall assign a reduced-confidence or indeterminate provenance determination in accordance with applicable METR policy. The METR Component shall record the provenance evaluation result and the basis for the determination.

The output of this use case is a determination that the METR Rule provenance is established, established with reduced confidence, or indeterminate, based on electronic evaluation of the rule’s metadata, recorded history, and associated security evidence back to its authoritative origin.

 ![Evaluate METR Rule Provenance](images\evaluate-metr-rule-provenance.jpg)