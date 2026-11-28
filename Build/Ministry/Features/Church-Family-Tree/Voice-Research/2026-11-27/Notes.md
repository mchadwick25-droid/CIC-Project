# Second voice for people and stories: research notes

Candidates, measured on the first 508 characters of the published Polycarp brief, model `eleven_multilingual_v2`, `mp3_44100_64`, stability 0.95, similarity 0.68, style 0, speaker boost on. Pace is 96 words over the clip's length.

| Voice | Id | Pace (words a minute) | Speech above 8 kHz | Pause floor | Mark |
|---|---|---|---|---|---|
| Jane | `RILOU7YmBhvwJGDGjNmP` | 149 | 0.15% | −91 dBFS | ok, finalist |
| Maysie | `QPBKI85w0cdXVqMSJ6WB` | 151 | 0.24% | −67 | good, finalist |
| Sally Ford | `kBag1HOZlaVBH7ICPE8x` | 144 (148 at speed 1.04) | 1.43% | −59 to −62 | chosen at 1.04 |
| Beatrice | `kkPJzQOWz2Oz9cUaEaQd` | 138 | 0.58% | −64 | no |
| Katherine | `NtS6nEHDYMQC9QczMQuq` | 151 | 2.92% | −91 | too whispery |
| Amanda | `tKBQrlxp4oMJNdRuKqwM` | 187 | 0.38% | −73 to −85 | too fast |
| Rachel | `pjRN70TpPrZwgTVcpRGt` | 177 | 0.00% | −69 to −71 | too fast |
| Samantha | `9RpXYdocFG8u7K3pqNxi` | 144 (full brief) | 0.13% | −91 | whiny |

Neo on `eleven_v4`, from the site's published files: 30 to 37 percent above 8 kHz. Daniel on `eleven_multilingual_v2`: 0.6 percent.

What the free previews could and could not show: the share above 8 kHz screened out breathy voices (Katherine). It did not catch a whiny voice (Samantha). A syllable-beat count did not predict pace, because each preview reads a different text.

Method: ElevenLabs shared-voice library, previews downloaded, then `ffmpeg` and a short Python script for levels, pauses and the share above 8 kHz. Clips were measured, not heard.
