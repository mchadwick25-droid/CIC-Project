# Authoring test: key seal

The key (which letter is which author for each record, and each author's self-reported model id) is held outside the repository until the blind read is posted. Its SHA-256, taken when the blind set was assembled:

`6a3871e7b83393d19fb8f86349c382af47fc2444be2209286cd5f87e070e7392`

When the key is committed after the blind read, `sha256sum` of that file must match this value.
