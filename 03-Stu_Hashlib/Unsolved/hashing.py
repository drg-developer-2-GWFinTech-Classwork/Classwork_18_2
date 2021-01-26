import hashlib

# output sha256 hash in hexadecimal string format
def hash(message):
    # return hashlib.md5(message).hexdigest()
    return hashlib.sha256(message).hexdigest()

# modify these messages
# note: we include the "b" before the string definition in order to represent it as bytes instead of a string
message_one = b"This is a super-secret message."

message_two = b"This is a super-secret message. The bird is in the hen-house."

# print both messages and their corresponding hashes
message_one_hash = hash(message_one)
message_two_hash = hash(message_two)
print(f"{message_one} ({message_one_hash})")
print(f"{message_two} ({message_two_hash})")

# compare the hashes in an if/else statement

hash_one = message_one_hash

hash_two = message_two_hash

if (hash_one == hash_two):
    print("The hashes are equivalent.")
else:
    print("The hashes are NOT equivalent.")

# compare the length of the hashes

print(len(hash_one))
print(len(hash_two))
