# -*- mode: python -*-

block_cipher = None


a = Analysis(['mygame.py'],
             pathex=['D:\\coding\\my_code\\programing_2d_game\\2D_game_programing\\code'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mygame',
          debug=False,
          strip=False,
          upx=True,
          console=True )
