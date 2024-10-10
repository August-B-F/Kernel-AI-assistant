# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['DolceLaze.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/pixel.ttf', '.'), ('assets/logo.png', '.'), ('assets/pixel/folder.png', '.'), ('assets/pixel/file.png', '.'), ('assets/pixel/music.png', '.'), ('assets/pixel/film.png', '.'), ('assets/pixel/img.png', '.'), ('assets/pixel/pdf.png', '.'), ('assets/pixel/exe.png', '.'), ('assets/edit.png', '.'), ('assets/delet.png', '.'), ('UI.py', '.'), ('AI.py', '.'), ('Constants.py', '.'), ('KeyIntercept.py', '.'), ('.env', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DolceLaze',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
