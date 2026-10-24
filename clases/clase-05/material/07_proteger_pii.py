"""
DPL1046 · Clase 5 · 07_proteger_pii.py
Proteger datos personales (PII): hashing de un RUT y masking de un email.

Córrelo con el botón ▶ o con:
    python clases/clase-05/material/07_proteger_pii.py
"""

import hashlib

SALT = "udla-dpl1046"          # texto secreto que se mezcla antes de hashear
rut = "12.345.678-9"
email = "juan@gmail.com"

# 1) Hashing: el RUT se convierte en un código que no se puede revertir
texto = (SALT + rut).encode("utf-8")
rut_hash = hashlib.sha256(texto).hexdigest()[:16]
print("RUT original:", rut)
print("RUT hasheado:", rut_hash)

# 2) Masking: del email solo se ve la primera letra
usuario, dominio = email.split("@")
email_masked = usuario[0] + "***@" + dominio
print("Email original:", email)
print("Email enmascarado:", email_masked)
