from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


def gen_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
    public_key = private_key.public_key()

    return private_key, public_key


def read_private_key(pk):

    pem = pk.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    return pem


def read_public_key(pk):

    public_key = pk.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return public_key


def save_key(private_fn, public_fn):

    if ".pub" not in public_fn or ".pem" not in private_fn:
        raise ValueError("Incorrect file formats:\npublic key must be saved as .pub\nprivate key must be saved as .pem")

    pk = gen_key_pair()
    private = pk[0]
    public = pk[1]

    pem = read_private_key(private)
    pub = read_public_key(public)

    with open(private_fn, 'wb') as pem_out:
        pem_out.write(pem)

    with open(public_fn, 'wb') as pub_out:
        pub_out.write(pub)


def load_public_key(public_fn):

    if ".pub" not in public_fn:
        raise ValueError("Incorrect file formats:\npublic key must be saved as .pub\nprivate key must be saved as .pem")

    with open(public_fn, 'rb') as pub_in:
        publines = pub_in.read()
    public_key = load_pem_public_key(publines, None)

    return public_key
