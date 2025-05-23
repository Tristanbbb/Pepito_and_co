
# Examples of messages from certstream. Used in unit_tests/test_CertstreamMessage

standard_message = {
    "data": {
        "cert_index": 487230610,
        "cert_link": "https://ct.googleapis.com/logs/eu1/xenon2025h2/ct/v1/get-entries?start=487230610&end=487230610",
        "leaf_cert": {
            "all_domains": ["mail.prophesyclothing.com"],
            "extensions": {
                "authorityInfoAccess": "URI:http://r10.i.lencr.org/, URI:http://r10.o.lencr.org",
                "authorityKeyIdentifier": "keyid:bb:bc:c3:47:a5:e4:bc:a9:c6:c3:a4:72:0c:10:8d:a2:35:e1:c8:e8",
                "basicConstraints": "CA:FALSE",
                "keyUsage": "Digital Signature, Key Encipherment",
                "subjectAltName": "DNS:mail.prophesyclothing.com",
                "subjectKeyIdentifier": "keyid:55:13:71:6b:c4:e2:68:c9:1e:25:df:e8:46:56:ec:3c:60:93:fe:31",
            },
            "fingerprint": "95:37:84:21:AA:42:0A:39:DB:56:ED:F7:EC:FB:BC:DA:43:49:38:7C",
            "sha1": "95:37:84:21:AA:42:0A:39:DB:56:ED:F7:EC:FB:BC:DA:43:49:38:7C",
            "sha256": "40:D8:EF:C8:A1:CB:9A:CF:24:82:1E:99:96:D1:44:60:E3:07:0B:FD:72:99:EE:71:40:2A:5D:D1:F4:F5:7F:6C",
            "not_after": 1753521603,
            "not_before": 1745745604,
            "serial_number": "068F4DF9666E1CA94C7EB4A7361B14F5447F",
            "signature_algorithm": "sha256, rsa",
            "subject": {
                "C": None,
                "CN": "mail.prophesyclothing.com",
                "L": None,
                "O": None,
                "OU": None,
                "ST": None,
                "aggregated": "/CN=mail.prophesyclothing.com",
                "email_address": None,
            },
            "issuer": {
                "C": "US",
                "CN": "R10",
                "L": None,
                "O": "Let's Encrypt",
                "OU": None,
                "ST": None,
                "aggregated": "/C=US/CN=R10/O=Let's Encrypt",
                "email_address": None,
            },
            "is_ca": False,
        },
        "seen": 1745749178.077,
        "source": {
            "name": "Google 'Xenon2025h2' log",
            "url": "https://ct.googleapis.com/logs/eu1/xenon2025h2",
        },
        "update_type": "PrecertLogEntry",
    },
    "message_type": "certificate_update",
}

message_without_domains = {
    "data": {
        "cert_index": 487230610,
        "cert_link": "https://ct.googleapis.com/logs/eu1/xenon2025h2/ct/v1/get-entries?start=487230610&end=487230610",
        "leaf_cert": {
            "extensions": {
                "authorityInfoAccess": "URI:http://r10.i.lencr.org/, URI:http://r10.o.lencr.org",
                "authorityKeyIdentifier": "keyid:bb:bc:c3:47:a5:e4:bc:a9:c6:c3:a4:72:0c:10:8d:a2:35:e1:c8:e8",
                "basicConstraints": "CA:FALSE",
                "keyUsage": "Digital Signature, Key Encipherment",
                "subjectAltName": "DNS:mail.prophesyclothing.com",
                "subjectKeyIdentifier": "keyid:55:13:71:6b:c4:e2:68:c9:1e:25:df:e8:46:56:ec:3c:60:93:fe:31",
            },
            "fingerprint": "95:37:84:21:AA:42:0A:39:DB:56:ED:F7:EC:FB:BC:DA:43:49:38:7C",
            "sha1": "95:37:84:21:AA:42:0A:39:DB:56:ED:F7:EC:FB:BC:DA:43:49:38:7C",
            "sha256": "40:D8:EF:C8:A1:CB:9A:CF:24:82:1E:99:96:D1:44:60:E3:07:0B:FD:72:99:EE:71:40:2A:5D:D1:F4:F5:7F:6C",
            "not_after": 1753521603,
            "not_before": 1745745604,
            "serial_number": "068F4DF9666E1CA94C7EB4A7361B14F5447F",
            "signature_algorithm": "sha256, rsa",
            "subject": {
                "C": None,
                "CN": "mail.prophesyclothing.com",
                "L": None,
                "O": None,
                "OU": None,
                "ST": None,
                "aggregated": "/CN=mail.prophesyclothing.com",
                "email_address": None,
            },
            "issuer": {
                "C": "US",
                "CN": "R10",
                "L": None,
                "O": "Let's Encrypt",
                "OU": None,
                "ST": None,
                "aggregated": "/C=US/CN=R10/O=Let's Encrypt",
                "email_address": None,
            },
            "is_ca": False,
        },
        "seen": 1745749178.077,
        "source": {
            "name": "Google 'Xenon2025h2' log",
            "url": "https://ct.googleapis.com/logs/eu1/xenon2025h2",
        },
        "update_type": "PrecertLogEntry",
    },
    "message_type": "certificate_update",
}

message_with_missing_issuer_org = {
    "data": {
        "cert_index": 487230610,
        "cert_link": "https://ct.googleapis.com/logs/eu1/xenon2025h2/ct/v1/get-entries?start=487230610&end=487230610",
        "leaf_cert": {
            "all_domains": ["mail.prophesyclothing.com"],
            "extensions": {
                "authorityInfoAccess": "URI:http://r10.i.lencr.org/, URI:http://r10.o.lencr.org",
                "authorityKeyIdentifier": "keyid:bb:bc:c3:47:a5:e4:bc:a9:c6:c3:a4:72:0c:10:8d:a2:35:e1:c8:e8",
                "basicConstraints": "CA:FALSE",
                "keyUsage": "Digital Signature, Key Encipherment",
                "subjectAltName": "DNS:mail.prophesyclothing.com",
                "subjectKeyIdentifier": "keyid:55:13:71:6b:c4:e2:68:c9:1e:25:df:e8:46:56:ec:3c:60:93:fe:31",
            },
            "fingerprint": "95:37:84:21:AA:42:0A:39:DB:56:ED:F7:EC:FB:BC:DA:43:49:38:7C",
            "sha1": "95:37:84:21:AA:42:0A:39:DB:56:ED:F7:EC:FB:BC:DA:43:49:38:7C",
            "sha256": "40:D8:EF:C8:A1:CB:9A:CF:24:82:1E:99:96:D1:44:60:E3:07:0B:FD:72:99:EE:71:40:2A:5D:D1:F4:F5:7F:6C",
            "not_after": 1753521603,
            "not_before": 1745745604,
            "serial_number": "068F4DF9666E1CA94C7EB4A7361B14F5447F",
            "signature_algorithm": "sha256, rsa",
            "subject": {
                "C": None,
                "CN": "mail.prophesyclothing.com",
                "L": None,
                "O": None,
                "OU": None,
                "ST": None,
                "aggregated": "/CN=mail.prophesyclothing.com",
                "email_address": None,
            },
            "issuer": {
                "C": "US",
                "CN": "R10",
                "L": None,
                "OU": None,
                "ST": None,
                "aggregated": "/C=US/CN=R10/O=Let's Encrypt",
                "email_address": None,
            },
            "is_ca": False,
        },
        "seen": 1745749178.077,
        "source": {
            "name": "Google 'Xenon2025h2' log",
            "url": "https://ct.googleapis.com/logs/eu1/xenon2025h2",
        },
        "update_type": "PrecertLogEntry",
    },
    "message_type": "certificate_update",
}
