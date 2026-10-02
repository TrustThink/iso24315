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

![ISO-21177 Transport Layer Security](images\iso2177-tls.jpg)

 

#### 1.1.1.1     Secure Session Lifecycle and Protected Message Exchange

METR secure transport operates as a coordinated lifecycle that begins with local message preparation and continues through secure session establishment, mutual authentication, authorization enforcement, and protected message exchange between peer systems. Application-layer content is first assembled and authorized within a METR subsystem, then transmitted over a secure channel established in accordance with ISO 21177 using TLS 1.3. 

The following sections describe (1) how a METR system generates and transmits an ALPDU within an established session, and (2) how two METR systems establish and maintain a mutually authenticated secure session prior to exchanging protected application data.

 

##### 1.1.1.1.1   ALPDU Generation

When a METR system transmits information to a peer, the METR Application shall prepare an outbound message consisting of a signed METR Digital Envelope and its associated NROT (non repudiation token). The signed METR Digital Envelope and the NROT shall be treated as distinct application-layer elements and are combined within a single METR application-layer protocol data unit (ALPDU). The NROT is cryptographically bound to the signed object through a digest computed over the complete encoded secure data structure, enabling the receiving system to verify the evidentiary relationship independently of the transport session. The completed ALPDU shall be provided to the METR Security Subsystem for evaluation against locally configured authorization policy.

Once authorized, the ISO 21177 Security Adaptor Layer shall encapsulate the encoded payload within an Iso21177AdaptorLayerPDU. The adaptor layer then submits the resulting ALPDU to the Secure Session Service associated with the active TLS session. The Secure Session Service shall apply transport-layer protection using the negotiated session keys and prepares the protected record for transmission to the peer ITS station. 

Figure 8 ALPDU Generation illustrates how application-layer content, local authorization enforcement, and transport-layer protection interact within a single METR system prior to on-the-wire transmission.

![TLS Internal Operations](images\tls-internal-sequence.jpg)

Two METR systems exchanging data operate in client and server roles. The client role is responsible for initiating a secure session with METR system acting in a server role. Both client and server implement a secure data exchange using Transport Layer Security (TLS) using ISO 21177 services.  

 

##### Session Initiation

A METR system operating in the client role shall initiate a secure session toward the peer system operating in the server role. The client-side ISO 21177 Security Adaptor Layer shall invoke the session start primitive, which causes its Secure Session Service to initiate a TLS handshake with the remote Secure Session Service. No METR application data is exchanged at this point. 

 

##### 1.1.1.1.2   Mutual TLS Authentication

During the TLS handshake, both METR systems shall perform mutual authentication at the transport layer. Each system presents its credential set and validates the credentials presented by its peer. Certificate chains shall be evaluated against configured trust anchors, and cryptographic parameters shall be negotiated to derive shared session keys. This authentication step establishes trusted endpoint identities for the duration of the session and is distinct from any object-level signature validation associated with application payloads.

The credential structure may reflect either an X.509-based public key infrastructure model or an IEEE 1609.2 certificate model containing ITS-AID, PSID, SSP, or other authorization attributes. The session architecture accommodates either approach without modification,. Regional standards development organizations may adopt trust models appropriate to their governance and deployment environments.

##### Session Establishment Indication 

Upon successful completion of the TLS handshake, the server-side Secure Session Service shall generate a session establishment indication and deliver it to the ISO 21177 Security Adaptor Layer. This indication shall convey the authenticated peer identity, the validated credential chain, negotiated session parameters, and any authorization-relevant attributes extracted from the credentials. At this stage, transport authentication has been completed and session context is available for authorization processing.

##### Local Authorization Enforcement

Following authentication, each METR system shall evaluate the authenticated peer against its locally configured Access Control Policy. Authorization decisions shall be derived from credential attributes and locally defined rules that determine whether the peer is permitted to establish the session and access specific services. These rules may rely on ITS-AID values, PSID and SSP permissions, X.509 extensions, organizational identifiers, or other recognized role attributes.

Because authorization enforcement occurs locally within each METR system, jurisdictions retain flexibility to define trust hierarchies, certificate profiles, and role semantics consistent with regional policy objectives. The secure session framework therefore provides interoperable transport security while allowing trust and authorization models to vary across implementations.

##### Active Secure Session

When authentication and authorization have both completed successfully, an active secure session exists between the two METR systems, as illustrated in Figure 9 Active TLS Secure Session. The session provides confidentiality, integrity protection, and replay resistance for all subsequent communications. All application-layer exchanges occur within the context of this established and authorized secure channel.

![TLS Server and Client Exchange](images\tls-server-client-sequence.jpg)

##### Protected APDU Exchange

With the secure session active, application data is encapsulated by the ISO 21177 Security Adaptor Layer within an Iso21177AdaptorLayerPDU. The Secure Session Service applies transport-layer protection using the negotiated TLS session keys and transmits the protected record to the peer system. Upon receipt, the peer Secure Session Service decrypts and validates the transport-layer protection before delivering the extracted APDU to its local adaptor layer and METR application.



