# Verification

“Verified” means the relevant claim has evidence appropriate to its risk.

| Claim type | Minimum evidence |
| --- | --- |
| Package structure | Manifest and referenced files resolve locally. |
| Script behavior | Focused automated check or reproducible command. |
| Host installation | Fresh host/version install, discovery, and uninstall record. |
| Lifecycle behavior | Host-specific exercise of the hook or gate. |
| Public quality/performance claim | Reproducible comparative evidence. |

Do not replace a missing check with a confident description. A passing local test does not prove cross-host installation, and a single example does not prove universal quality or speed.

The current release gate requires every plugin manifest to resolve, relevant focused checks to pass, and the [host support record](HOSTS.md) to be completed before broad compatibility claims are promoted.
