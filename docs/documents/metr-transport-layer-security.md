# METR Transport Layer Security 

METR systems exchange information across organizational, jurisdictional, and network boundaries. These exchanges require protection against unauthorized disclosure, modification, replay, and impersonation while also ensuring that communicating systems are authorized to access the requested METR services and information.

ISO 24315-10 requires METR systems to establish secure transport communications in accordance with ISO 21177, Intelligent transport systems — ITS station security services for secure session establishment and authentication. ISO 21177 provides the security services used to establish and operate authenticated secure sessions between ITS stations, including the use of TLS for protected application-layer communications.

This page provides engineering guidance for applying ISO 21177 to METR system-to-system communications. It expands on the normative requirements in ISO 24315-10 by illustrating how METR applications, security functions, the ISO 21177 Security Adaptor Layer, and Secure Session Services interact during session establishment and protected information exchange.

The material describes:

- establishment of client and server roles between communicating METR systems;
- mutual authentication and validation of peer credentials;
- use of locally configured METR security policy to authorize the authenticated peer and requested service;
- establishment and maintenance of the TLS-protected session;
- encapsulation and exchange of METR application data through the ISO 21177 Security Adaptor Layer; and
- the relationship between transport-layer security and the separate object-level security protections applied to METR information.

The examples on this page are intended to clarify one implementation of the METR secure-transport architecture. Regional profiles may further define the TLS version, credential profiles, cryptographic algorithms, authorization attributes, trust anchors, and other parameters used within an ISO 21177 deployment.

The figure below illustrates METR Transport Security Aligned with ISO 21177 and the conceptual interaction between the METR application, the METR security subsystem, and the ISO 21177 secure session services in both client and server roles.

![](C:\Users\BrianRussell\Documents\Repos\Metr_engineering\iso24315\docs\images\iso2177-tls.jpg)

