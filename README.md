# fuse-3ds
FUSE Filesystem Python scripts for Nintendo 3DS files

ARM9 bootROM required. Checked in order of:
* `boot9.bin` (full) in current working directory
* `boot9_prot.bin` (protected) in current working directory
* `~/.3ds/boot9.bin` (full)
* `~/.3ds/boot9_prot.bin` (protected)

Requires Python 3.5+, [fusepy](https://github.com/terencehonles/fusepy), and [pycryptodomex](https://github.com/Legrandin/pycryptodome).

## mount_nand.py
Mounts NAND images. Can read essentials backup by GodMode9, else OTP file/NAND CID must be provided in arguments.

```bash
python3 mount_nand.py [-h] [--otp OTP] [--cid CID] [--dev] [--ro] [--fg] nand mount_point
```

Current files:
```
mount_point
├── agbsave.bin
├── ctrnand_fat.img
├── ctrnand_full.img
├── firm0.bin
├── firm1.bin
├── nand.bin
├── nand_hdr.bin
├── nand_minsize.bin
├── sector0x96.bin
├── twlmbr.bin
├── twln.img
└── twlp.img
```

# License/Credits
`mount_nand.py` is under the MIT license.

Special thanks to @Stary2001 for help with NAND crypto (especially TWL).
