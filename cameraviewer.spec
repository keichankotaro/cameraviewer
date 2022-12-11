# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cameraviewer.py'],
    pathex=[
        'C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\cv2\\',
    	'C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\win32',
#    	'C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\win32ctypes\\pywin32'
    	'C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\pywin32_system32',
#    	'C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\win32ctypes'
    ],
    binaries=[
    	('C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\', 'cv2'),
    	('C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\pywin32_system32\\pythoncom37.dll', 'pywin32_system32'),
    	('C:\\Users\\keich\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\pywin32_system32\\pywintypes37.dll', 'pywin32_system32')
    ],
    datas=[],
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
    name='cameraviewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='camera.ico',
)
