---
title: JSON Web Tokens
tags:
  - protocols
  - standards
---
JSON Web Tokens (JWT) allows to transmit data between parties providing security in forms of [[authenticity]], [[confidentiality]] and [[integrity]]. 

It contains a list of claims in the shape of key-value pairs that are either encoded using [[JSON Web Signature|JSON Web Signature (JWS)]] or [[JSON Web Encryption|JSON Web Encryption (JWE)]].

JWS focuses on authenticity, which means anyone with the JWT can read the payload. JWE, on the other hand, ensures that only authorized parties can access the payload. A JWT is considered unsecured when it is not represented by either JWS or JWE.

## Structure

A JWT has three sections: a header, a payload, and a signature. Each section is a [[Base64 Encoding|Base64-encoded]] string, and the sections are separated by periods. A typical JWT looks like this, where the X’s represent the header, the Y’s represents the payload, and the Z’s represents the signature:

`xxxxxx.yyyyyy.zzzzzz`

A more explicitly written JWT would look something like this:

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkphbmUgRG9lIiwiaWF0IjoxNjk3MjM5MDIyfQ.5CerSPBCrO_3WdiyPjR7HoWBOeXsuq2AcfplJeG7erc`

### Header

The header contains information about the overall JWT, such as the main algorithm (`alg`) used for signing and encryption (required), the media type of the JWT (`typ`), and its content type (`cty`).  A decoded JWT header might look like this:

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

### Payload

The payload consists of all of the data that’s being transmitted. This data is optional. There are three primary types of claims: registered claims, private claims, and public claims.

#### Registered claims

These are optional but pre-determined claims that are defined in the JWT specification and support interoperability. There are seven types of registered claims:

- **Issuer (`iss`):** The party that issued the JWT.
- **Subject (`sub`):** The subject of the JWT or the entity this JWT carries information about.
- **Audience (`aud`):** The recipient of the JWT.
- **Expiration time (`exp`):** The time at which the JWT expires.
- **Not before (`nbf`):** The time before which the JWT is invalid.
- **Issued at (`iat`):** The time at which the JWT was issued.
- **JTW ID (`jti`):** A string that acts as the unique identifier for this JWT.

#### Private claims

Private claims, which are used to represent the data being transported, are defined by the sender or receiver of the JWT and are therefore not registered in the JWT specification. They have specific use cases and must be structured to make sure they do not collide with registered claims. For example, you can include user profile information—such as email, name, and permissions—in your JWT as private claims.

#### Public claims

Public claims are not registered with the JWT specification, but they have been registered with the IANA (Internet Assigned Number Authority). The IANA has a [JSON Web Token Claims Registry](https://www.iana.org/assignments/jwt/jwt.xhtml), where users can register their claims to prevent collisions with other claims that are used globally. In practice, however, most claims are either registered or private claims.

### Signature

The signatures in JWT are generated using a [[security/Cryptographic Algorithms|cryptographic algorithm]] like [[HS256]]. The [JWA (JSON Web Algorithm)](https://datatracker.ietf.org/doc/html/rfc7518) standard defines a list of algorithms that can be used for signing a JWT.

The signature is created using the algorithm specified in the header, as well as the encoded header, encoded payload, and a secret. The signature is a one-way hash.

The secret used in the signature is a shared secret between the party that issues the token and the party that is verifying the token. In some cases, such as when JWT is used for authorizing user login sessions by the same server, the issuer of the token is also the verifier of the token.

During verification, the recipient generates a new signature with the secret that was provided by the issuer. If this signature matches the signature that was received in the JWT, it means the JWT has not been altered.

## Benefits

- **Statelessness**: JWTs are stateless, which means that they contain all of the necessary information for authentication and authorization.
- **Efficiency:** JWTs are compact and lightweight.
- **Interoperability**: JWTs are based on widely adopted and standardized formats.
- **Cross-domain communication:** JWTs can be used for securely sharing information between different parts of a web application or between services running on different domains.

## Best practices

- **Keep payloads small:** Minimize the amount of data stored in JWT payloads.
- **Validate and verify**: Always validate and verify the JWT before relying on the information it contains.
- **Use secure libraries:** Utilize well-established libraries and frameworks for creating, parsing, and verifying JWTs.
- **Implement token expiry:** Set a reasonable expiration time for JWTs. Shorter expiration times can enhance [API security](https://www.postman.com/api-platform/api-security/) by reducing the window of opportunity for misuse if a token is compromised. If the JWT is an access token, consider pairing it with a long-lived refresh token.
- **Implement a blacklisting mechanism:** Since JWTs are stateless and self-contained, invalidating sessions or preventing misuse on leaks needs a blacklisting mechanism so that living tokens can be disregarded.
## Sources

- [JSON Web Tokens (JWT)](https://www.iana.org/assignments/jwt/jwt.xhtml), IANA
- [What is JWT?](https://blog.postman.com/what-is-jwt/), Postman Blog
